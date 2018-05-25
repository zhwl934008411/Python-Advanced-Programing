# coding:utf8

# lib1.py


class Rectangle(object):
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

    W = property(getWidth, setHeight)
    H = property(getHeight, setHeight)

