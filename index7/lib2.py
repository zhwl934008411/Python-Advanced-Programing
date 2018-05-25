# coding:utf8

# lib2.py


class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_Area(self):
        a, b, c = self.a, self.b, self.c
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) * 0.5
        return area


