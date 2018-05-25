# coding:utf8
from functools import wraps
import time
import logging
from random import randint
# 如何实现属性可修改的函数装饰器

''''''

'''
实际案例:
为了分析程序内哪些函数执行时间开销较大,我们定义一个带timeout参数
的函数装饰器,装饰功能如下:

1.统计被装饰函数单次调用运行时间
2.时间大于参数timeout的,将此次函数调用记录到Log日志中,
3.运行时可修改timeout的值

'''

def warn(timeout):
    timeout = [timeout]
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            start = time.time()
            res = func(*args,**kwargs)
            t = time.time()-start
            if t > timeout[0]:
                msg = '"%s": %s > %s' % (func.__name__,t,timeout[0])
                logging.warn(msg=msg)
            return res
        def setTimeout(k):
            #nonlocal timeout
            timeout[0] = k
        wrapper.setTimeout = setTimeout
        return wrapper
    return decorator


@warn(1.5)
def test():
    print('in test')
    while randint(0,1):
        time.sleep(0.5)

test.setTimeout(1)
for _ in range(30):
    test()



