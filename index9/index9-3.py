# coding:utf8
import functools
from inspect import signature

# 如何定义带参数的装饰器


''''''

'''
实际案例:
实现一个装饰器,它用来检查被装饰函数的参数类型,
装饰器可以通过参数指明函数参数的类型,调用时如果
检测出类型不匹配则抛出异常.

'''
'''
解决方案:
提取函数签名:inspect.signature()
带参数的装饰器,也就是根据参数定制化一个装饰器,可以看出生产装饰器
的工厂,每次调用typeassert,返回一个特定的装饰器,然后用它去修饰其它函数
'''


# typeassert 类型断言
def typeassert(*ty_args, **ty_kwargs):
    def decorator(func):
        sig = signature(func)
        bargs = sig.bind_partial(*ty_args, **ty_kwargs)
        btypes = bargs.arguments

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for name, obj in sig.bind(*args, **kwargs).arguments.items():
                if name in btypes:
                    if not isinstance(obj, btypes[name]):
                        raise TypeError('%s must be %s' % (name, btypes[name]))

            return func(*args, **kwargs)

        return wrapper

    return decorator


@typeassert(int, str, list)
def f(a, b, c):
    print(a, b, c)


f(1,'abc',[1,3,4])

f(1,2,[1,3,4])