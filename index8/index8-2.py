# coding:utf8
import csv
from xml.etree.ElementTree import Element, ElementTree
import requests
from StringIO import StringIO
from time import time
from xml_pretty import pretty  # 这个模块是自定义的
from threading import Thread

# from collections import deque
from Queue import Queue

# 如何进行线程间通信
start = time()
''''''

'''
实际案例:
我们通过网易财经获取股票csv数据文件,启动多线程的方式,并行下载
多个股票的数据并将其转换为xml文件

由于全局解释器锁的存在,多线程进行CPU密集型操作并不能提高执行效率,
我们修改程序构架:
1.使用多个DownloadThread线程进行下载(I/O操作)
2.使用一个ConvertThread线程进行转换(CPU密集型操作)
3.下载线程把下载数据安全地传递给转换线程

解决方案:
使用标准库中Queue.Queue,它是一个线程安全的队列,Download
线程把下载数据放入队列,Convert线程从队列里提取数据
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
    def __init__(self, queue):
        Thread.__init__(self)  # 调用父类的构造器
        self.queue = queue

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
        while True:
            sid, data = self.queue.get()
            print(sid)
            if sid == -1:
                break
            fname = str(sid).rjust(7, '0') + '.xml'
            print('Convert to XML...(%d)') % sid
            with open(fname, 'wb') as wf:
                self.csvToXml(data, wf)
            # print(fname)


q = Queue()

dThreads = []
for i in xrange(1, 11):
    t = DownloadThread(i, q)
    t.start()
    dThreads.append(t)

for t in dThreads:
    t.join()
# dThreads = [DownloadThread((i, q) for i in xrange(1, 11)]
cThread = ConvertThread(q)
cThread.start()
q.put((-1, None))
cThread.join() #等待子线程执行完后退出主线程
print(time() - start)
#　time = 18.1110730171