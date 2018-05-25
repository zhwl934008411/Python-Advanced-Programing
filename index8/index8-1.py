# coding:utf8
import csv
from xml.etree.ElementTree import Element, ElementTree
import requests
from StringIO import StringIO
from time import time
from xml_pretty import pretty  # 这个模块是自定义的
import threading

# 如何使用多线程

# PS：python多线程只适合处理IO型的操作,而调用cpu进行转换的工作可以用多进程

''''''
'''
实际案例,
'http://quotes.money.163.com/service/chd'
            'data.html?code=1000001&start=19910102&e'
            'nd=20180523&fields=TCLOSE;HIGH;LOW;TOPE'
            'N;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;V'
            'ATURNOVER;TCAP;MCAP'
我们通过网易财经网站获取了中国股市某支股票csv数据文件,现在要下载多只
股票的csv数据,并将其转换为xml文件.

如何使用线程来提高下载并处理的效率

'''


def download(url):
    response = requests.get(url)
    if response.ok:
        return StringIO(response.content)


def csvToXml(scsv, fxml):
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


# 多进程,多线程,串行和并行
def handle(sid):
    print('Download..(%d)' % sid)
    url = 'http://quotes.money.163.com/service/chddata.html?code=%s&start=20140810&end=20150911&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER'
    url %= str(sid).rjust(7, '0')
    rf = download(url)
    data = rf.read()
    s = data.decode('GB2312')
    f = open('pingan.csv', 'wb')
    f.write(s.encode('utf8'))
    f.close()
    f = open('pingan.csv', 'rb')
    print('Convert to XML...(%d)') % sid
    fname = str(sid).rjust(7, '0') + '.xml'
    print(fname)
    with open(fname, 'wb') as wf:
        csvToXml(f, wf)


'''t = threading.Thread(target=handle,args=(1,))
t.start()

print('main thread')'''


class Mythread(threading.Thread):
    def __init__(self, sid):
        threading.Thread.__init__(self)  # 调用父类的构造器
        self.sid = sid

    def run(self):
        handle(self.sid)


threads = []
start = time()
for i in xrange(1, 6):
    t = Mythread(i)
    threads.append(t)
    t.start()
for t in threads:
    t.join()
    # 表示等待每一个线程的退出,实测6个线程同时运行才不会报错,csv文件较大只能5个
print('main thread')
print(time()-start)
'''t = Mythread(1)
    t.start()
    t.join() #退出子线程后退出主线程
print('main thread')

def Bythread():
        threads = []
        for sid in xrange(1, 11):
            threadd = threading.Thread(target=handle, args=sid)
            threads.append(threadd)
            threadd.start()
        for threadd in threads:
            threadd.join()
if __name__ == '__main__':
        start = time()
        Bythread()
        print(time() - start)

if __name__ == '__main__':
        start = time()
        for sid in xrange(1,11):
            print('Download..(%d)' % sid)
            url = 'http://quotes.money.163.com/service/chddata.html?code=%s&start=20150810&end=20150911&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER'
            url %= str(sid).rjust(7,'0')
            rf = download(url)
            data = rf.read()
            s = data.decode('GB2312')
            f = open('pingan.csv', 'wb')
            f.write(s.encode('utf8'))
            f.close()
            f = open('pingan.csv', 'rb')
            print('Convert to XML...(%d)') % sid
            fname = str(sid).rjust(7,'0')+'.xml'
            print(fname)
            with open(fname, 'wb') as wf:
                csvToXml(f, wf)
        print(time()-start)
        url = 'http://quotes.money.163.com/service/chddata.html?code=0000001&start=20150810&end=20150911&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER'
        rf = download(url)
        data = rf.read()
        s = data.decode('GB2312')
        f = open('pingan.csv', 'wb')
        f.write(s.encode('utf8'))
        f.close()
        f = open('pingan.csv', 'rb')
        data = f.read(200)
        print data.decode('utf8')
        #print(type(f))
        with open('0000001.xml', 'wb') as wf:
                csvToXml(f, wf)'''
