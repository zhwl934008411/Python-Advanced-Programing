# coding:utf8
''''''

'''
现在，假设我们要增强now()函数的功能,比如,在函数
调用前后自动打印日志,但又不希望修改now()函数的定义,
这种在代码运行期间动态增加功能的方式,称之为“装饰器”
（Decorator）

本质上，decorator就是一个返回函数的高阶函数
'''


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log  # 相当于now = log(now)
def now():
    print('ddd')
