# coding:utf8

# lib3.py
from math import pi

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        # return self.radius
        return round(self.radius, 2)  # 表示四舍五入后保留小数点后两位

    def setRadius(self, value):
        if not isinstance(value, (int, long, float)):
            raise valueError('wrong type .')
        self.radius = float(value)

    def area(self):
        return self.radius * self.radius * pi

    R = property(getRadius, setRadius)
