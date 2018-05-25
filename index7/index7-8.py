# coding:utf8

from lib1 import Rectangle
from lib2 import Triangle
from lib3 import Circle

# 如何通过实例方法名字的字符串调用方法

''''''
'''
实际案例:
某项目中,我们的代码使用了三个不同库中的图形类:
      Circle,Triangle,Rectangle

他们都有一个获取图形面积的接口(方法),但接口名字不同,我们可以实现
一个统一的获取面积的函数,使用每种方法名进行尝试,调用相应类的接口

'''
'''
解决方案:
方法一:使用内置函数getattr,通过名字在实例上获取方法对象,然后调用
方法二:使用标准库operator下的methodcaller函数调用
'''

def getArea(shape):
    for name in ('area','getArea','get_Area'):
        f = getattr(shape,name,None)
        if f:
            return f()


shape1 = Rectangle(4,5)
shape2 = Triangle(4,4,4)
shape3 = Circle(6)

shapes = [shape1,shape2,shape3]
print(map(getArea,shapes))


methodcaller('getArea',)()







