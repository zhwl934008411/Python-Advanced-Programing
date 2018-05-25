# coding:utf8
import csv
from xml.etree.ElementTree import Element, ElementTree
import requests
from StringIO import StringIO
from time import time
from xml_pretty import pretty  # 这个模块是自定义的
from threading import Thread, Event
import tarfile, os

# from collections import deque
from Queue import Queue

# 如何在线程间进行事件通知
start = time()

''''''

'''
实际案例:
我们通过网易财经获取股票csv数据文件,启动多线程的方式,并行下载
多个股票的数据并将其转换为xml文件

额外需求:
实现一个线程,将转换出的xml文件压缩打包,比如转换线程每生产出100个xml
文件,就通过打包线程将它们打包成一个xxx.tgz文件,并删除xml文件,打包完成后,
打包线程反过来通知转换线程,转换线程继续转换

'''


class DownloadThread(Thread):
    def __init__(self, sid, queue):
        Thread.__init__(self)  # 调用父类的构造器
        self.sid = sid
        self.queue = queue
        # 类属性
        self.url = 'http://quotes.money.163.com/service/chddata.html?code=%s&start=20140810&end=20150911&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER'
        self.url %= str(self.sid).rjust(7, '0')

    def download(self):
        response = requests.get(self.url)
        if response.ok:
            return StringIO(response.content)

    def run(self):
        print('Download...', self.sid)
        rf = self.download()
        data1 = rf.read()
        s = data1.decode('GB2312')
        f = open('pingan.csv', 'wb')
        f.write(s.encode('utf8'))
        f.close()
        data = open('pingan.csv', 'rb')
        # print('Convert to XML...(%d)') % sid
        # DownloadThread线程下载的数据传递给ConvertThread线程
        # lock
        self.queue.put((self.sid, data))


class ConvertThread(Thread):
    def __init__(self, queue,cEvent, tEvent):
        Thread.__init__(self)  # 调用父类的构造器
        self.queue = queue
        self.cEvent = cEvent
        self.tEvent = tEvent

    def csvToXml(self, scsv, fxml):
        reader = csv.reader(scsv)
        headers = reader.next()
        headers = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']
        # headers = map(lambda h: h.replace(' ', ''), headers)

        root = Element('Data')
        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag, text in zip(headers, row[:2] + row[3:]):
                e = Element(tag)
                e.text = text
                eRow.append(e)

            # pretty(root)
            et = ElementTree(root)
            et.write(fxml)

    def run(self):
        count = 0
        while True:
            sid, data = self.queue.get()
            print(sid)
            if sid == -1:
                self.cEvent.set()
                self.tEvent.wait()
                break
            fname = str(sid).rjust(7, '0') + '.xml'
            print('Convert to XML...(%d)') % sid
            with open(fname, 'wb') as wf:
                self.csvToXml(data, wf)
                count +=1
            if count == 5:
                self.cEvent.set()

                self.tEvent.wait()
                self.tEvent.clear()
                count = 0


                # print(fname)


'''
额外需求:
实现一个线程,将转换出的xml文件压缩打包,比如转换线程每生产出100个xml
文件,就通过打包线程将它们打包成一个xxx.tgz文件,并删除xml文件,打包完成后,
打包线程反过来通知转换线程,转换线程继续转换
'''
'''
解决方案:
线程间的时间通知,可以使用标准库中Threading.Event:
1.等待事件一端调用wait,等待事件
2.通知事件一端调用set,通知事件

'''


class TarThread(Thread):
    def __init__(self,cEvent, tEvent):
        Thread.__init__(self)  # 调用父类的构造器
        self.count = 0
        self.cEvent = cEvent
        self.tEvent = tEvent
        self.setDaemon(True) # 设置TarThread为守护线程,其他线程退出后干掉该线程

    def tarXML(self):
        self.count += 1
        tfname = "%d.tgz" % self.count
        tf = tarfile.open(tfname, 'w:gz')
        for fname in os.listdir('.'):
            if fname.endswith('.xml'):
                tf.add(fname)
                os.remove(fname)
        tf.close()
        if not tf.members:
            os.remove(tfname)

    def run(self):
        # 1.监听转换线程

        # 2.数量满100就进行打包,并删除.xml文件,
        while True:
            self.cEvent.wait()
            self.tarXML()
            self.cEvent.clear()

            self.tEvent.set()

        # 3.打包完成后,打包线程反过来通知转换线程,
        # 转换线程继续转换

if __name__ == '__main__':
    q = Queue()
    cEvent = Event()
    tEvent = Event()
    tThread = TarThread(cEvent,tEvent)

    dThreads = []
    for i in xrange(1, 19):
        t = DownloadThread(i, q)
        t.start()
        dThreads.append(t)

    for t in dThreads:
        t.join()
    # dThreads = [DownloadThread((i, q) for i in xrange(1, 11)]
    cThread = ConvertThread(q,cEvent,tEvent)
    cThread.start()
    tThread.start()
    q.put((-1, None))
    cThread.join()  # 等待子线程执行完后退出主线程
    #tThread.join()
    print(time() - start)

