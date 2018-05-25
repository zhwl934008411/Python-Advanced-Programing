#!/usr/bin/python2.7
# coding:utf8

' a test module '

__author__ = 'Michael zhao'
from math import pi

# 如何创建可管理的对象属性
# 断点调试是一项非常重要的技能,重要性不亚于多线程和面向对象
'''
发送卡
'''
'''
在面向对象编程中,我们把方法(函数)看做对象的接口,直接访问对象的属性
是不安全的,或设计上不够灵活,但是直接调用方法在形式上不如访问属性简洁
circle.getRadius()
circle.setRadius(5.0) #繁

circle.radius
circle.radius = 5.0   #简

能否在形式上是属性访问,但实际上调用方法
'''


class Circle(object):
    def __init__(self, radius):
        self.__radius = radius  # 此时__radius为私有属性

    def getRadius(self):
        return self.__radius

    def setRadius(self, value):
        if not isinstance(value, (int, long, float)):
            raise valueError('wrong type .')
        self.__radius = float(value)

    def getArea(self):
        return self.__radius ** 2 * pi


class Circle2(object):
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
        return self.radius * 2 * pi

    R = property(getRadius, setRadius)


r = Circle2(3.2)
r.radius = 'abc'
r.setRadius(2)
print(r.getRadius())
print(r.radius)
print(r.radius * 2)

print(r.R)  # 自动调用getRadius
r.R = 5.4   # 自动调用setRadius
print(r.R)  # 自动调用getRadius

r2 = Circle2('abs')
print(r2.radius)

'''
解决方案:
使用property函数为类创建可管理属性,fget/fset/fdel对应相应属性访问

'''
# 外部不需要引用的函数全部定义成private，
# 只有外部需要引用的函数才定义为public
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数
