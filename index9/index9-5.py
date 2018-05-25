# coding:utf8
import logging
from functools import wraps
from time import localtime, time, strftime, sleep
from random import choice

# 如何在类中定义装饰器

''''''

'''
实例:
实现一个能将函数调用信息记录到日志的装饰器:
1.把每次函数的调用时间,执行时间,调用次数写入日志
2.可以对被装饰函数分组,调用信息记录到不同日志
3.动态修改参数,比如日志格式
4.动态打开关闭日志输出功能
'''
'''
为了让装饰器在使用上更加灵活,可以把类的实例方法作为装饰器,
此时在包裹函数中就可以持有实例对象,便与修改属性和拓展功能
'''


class CallingInfo(object):
    def __init__(self, name):
        log = logging.getLogger(name)
        log.setLevel(logging.INFO)
        fh = logging.FileHandler(name + '.log')
        log.addHandler(fh)
        log.info('start'.center(50, '.'))
        self.log = log
        self.formatter = '%(func)s -> [%(time)s - %(used)s - %(ncalls)s]'

    def info(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            lt = localtime()  # 表示函数的调用时间点
            t2 = time()
            res = func(*args, **kwargs)
            wrapper.ncalls += 1  # 表示函数调用次数
            used = time() - t2  # t3-t2 used时间
            info = {}
            info['func'] = func.__name__
            info['time'] = strftime('%x %X', lt)
            info['used'] = used
            info['ncalls'] = wrapper.ncalls
            msg = self.formatter % info
            self.log.info(msg)
            return res

        wrapper.ncalls = 0

        return wrapper

    def setFormatter(self, formatter):
        self.formatter = formatter

    def turnOn(self):
        self.log.setLevel(logging.INFO)

    def turnOff(self):
        self.log.setLevel(logging.WARN)


if __name__ == '__main__':
    cinfo1 = CallingInfo('mylog1')
    cinfo2 = CallingInfo('mylog2')

    formatter = '%(func)s -> [%(time)s - %(ncalls)s]'
    cinfo1.setFormatter(formatter)
    cinfo2.turnOff()
    @cinfo1.info
    def f():
        print('in f')


    @cinfo1.info
    def g():
        print('in g')


    @cinfo2.info
    def h():
        print('in h')


    for _ in range(50):
        choice([f, g, h])()
        sleep(choice([0.5, 1, 1.5]))
