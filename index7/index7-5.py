# coding:utf8
from functools import total_ordering
from math import pi
from abc import ABCMeta, abstractmethod

'''
现在，假设我们要增强now()函数的功能,比如,在函数
调用前后自动打印日志,但又不希望修改now()函数的定义,
这种在代码运行期间动态增加功能的方式,称之为“装饰器”
（Decorator）

本质上，decorator就是一个返回函数的高阶函数
'''

#  如何让类支持比较操作

'''
dd
'''

'''
实际案例：
有时我们希望自定义的类,实例间可以使用<,<=,>,>=,==,!=符号进行比较,
我们自定义比较的行为,例如,有一个矩形的类,我们希望比较两个矩形的实例
时,比较的是他们的面积,

'''


@total_ordering  # 装饰器
class Shape(object):

    @abstractmethod
    def getArea(self):
        pass

    def __lt__(self, obj):
        print('in__lt__')
        if not isinstance(obj, Shape):
            raise TypeError('obj is not Shape')
        return self.getArea() < obj.getArea()

    def __eq__(self, obj):
        print('in__eq__')
        if not isinstance(obj, Shape):
            raise TypeError('obj is not Shape')
        return self.getArea() == obj.getArea()


class Rectangle(Shape):
    def __init__(self, w, h):
        self.__w = w
        self.__h = h

    def getWidth(self):
        return self.__w

    def getHeight(self):
        return self.__h

    def setWidth(self, value):
        if not isinstance(value, (int, long, float)):
            raise valueError('wrong type .')
        self.__w = float(value)

    def setHeight(self, value2):
        if not isinstance(value, (int, long, float)):
            raise valueError('wrong type .')
        self.__h = float(value2)

    def getArea(self):
        return self.__w * self.__h

    '''def __lt__(self, obj):  # < >
        print('in__lt__')
        return self.getArea() < obj.getArea()

    def __le__(self, obj):
        print('in__le__')
        return self.getArea() <= obj.getArea()

    def __eq__(self, obj):
        print('in__eq__')
        return self.getArea() == obj.getArea()

    def __le__(self, obj):
        print('in__le__')
        return self < obj or self = obj

    def __gt__(self, obj):
        return not(self < obj or self = obj)'''

    W = property(getWidth, setHeight)
    H = property(getHeight, setHeight)


rect1 = Rectangle(5, 3)
rect2 = Rectangle(4, 4)
'''print rect1 > rect2  # 实际调用的是rect1.__lt__(rect2)
print rect1 >= rect2  # 实际调用的是rect1.__le__(rect2)
print rect1 < rect2
print rect1 == rect2'''


# +rect1.__eq__(rect2)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        # return self.radius
        return round(self.radius, 2)  # 表示四舍五入后保留小数点后两位

    def setRadius(self, value):
        if not isinstance(value, (int, long, float)):
            raise valueError('wrong type .')
        self.radius = float(value)

    def getArea(self):
        return self.radius * self.radius * pi

    R = property(getRadius, setRadius)


radius1 = Circle(4)
radius2 = Circle(5)
print(radius1 == radius2)
print(radius1 < rect1)
'''
解决方案:
比较符号运算符重载,需要实现以下方法:
__lt__,__le__,__gt__,__ge__,__en__,__ne__
使用标准库下的funtools下的类装饰器total_ordering可以简化此过程
'''
