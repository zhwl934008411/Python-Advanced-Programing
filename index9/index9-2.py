# coding:utf8
from datetime import datetime
import functools
from time import time
# 如何为被装饰的函数保存元数据

''''''
'''
实际案例:
在函数对象中保存着一些函数的元数据,例如:
f.__name__  :  函数的名字
f.__doc__   :  函数文档字符串
f.__module__:  函数所属模块名
f.__dict__  :  属性字典
f.__defaults__: 默认参数元组

.....

我们在使用装饰器后,在使用上面这些属性访问时,看到的是内部包裹函数
的元数据,原来函数的元数据便丢失掉了,应该如何解决
'''

'''
解决方案:
使用标准库functools中的的装饰器wraps装饰内部包裹函数,可以制定
将原函数的某些属性,更新到包裹函数上面

python一切皆对象
'''
def log5(func):
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return wrapper

def log2(text):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kwargs)
        return wrapper
    return decorator

def log3(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def log4(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log4('excute')
def now():
    print(datetime.now())

#now()


#print(now.__name__)
#print(f.__name__)
# 在函数调用前后自动打印日志
# Decorator装饰器,定义一个能打印日志的decorator


def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        t0 = time()
        func(*args, **kw)
        print('%s executed in %s ms' % (func.__name__, (time() - t0) * 1000))
        return func
    return wrapper

def metric2(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('%s begin call' % func.__name__)
        func(*args, **kw)
        print('%s end call' % func.__name__)
        return func
    return wrapper

def log6(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if isinstance(text,str):
                print('%s %s():' % (text, func.__name__))
            else:
                print('%s():' % func.__name__)
            return func(*args, **kw)
        return wrapper
    if callable(text):
        return decorator(text)
    else:
        return decorator

@log6
def now():
    print(datetime.now())

now()






