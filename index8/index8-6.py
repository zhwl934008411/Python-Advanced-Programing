# coding:utf8

from multiprocessing import Process
from threading import Thread
import time

# 如何使用多进程

''''''

'''
实际案例:
由于python中全局解释器锁(global interpreter lock)的存在,
在任意时刻只允许一个线程在解释器中运行,因此python的多线程
不适合处理cpu密集型的任务

想要处理cpu密集型的任务,可以使用多进程模型
'''

'''
使用标准库中multiprocessing.Process,它可以启动子进程执行任务
操作接口,进程间通信,进程间同步等都与Threading.Thread类似

'''


def isArmstrong(n):
    a, t = [], n
    while t > 0:
        a.append(t % 10)
        t = t / 10  # 只取整数位
    k = len(a)
    return sum(x * k for x in a) == n

def findArmstrong(a,b):
    print(a,b)
    res = [k for k in xrange(a,b) if isArmstrong(k)]
    print('%s ~ %s: %s' % (a,b,res))

def findByThread(*argslist):
    workers = []
    for args in argslist:
        worker = Thread(target=findArmstrong,args = args)
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()

def findByProcess(*argslist):
    workers = []
    for args in argslist:
        worker = Process(target=findArmstrong,args=args)
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()  #执行完子进程后执行主进程


if __name__ == '__main__':
    start = time.time()
    # findByProcess((200000000,250000000),(250000000,300000000))
    findByThread((200000000,250000000),(250000000,300000000))
    print(time.time()-start)








