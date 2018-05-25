# -*- coding:utf-8 -*-
# 如何实现可迭代对象和迭代器对象
import requests
from collections import Iterable, Iterator

# 实际案例:某软件要求,从网络抓取各个城市气温信息,并依次显示
'''
北京:15~20
天津:17~22
长春:12~18

如果一次抓取所有城市天气再显示,显示第一个城市气温时,有很高
的延时,并且浪费存储空间,我们期望以'用时访问'的策略,并且能把
所有城市气温封装到一个对象里,可以用for语句进行迭代,如果解决

一类是集合数据类型，如list、tuple、dict、set、str等；

一类是generator，包括生成器和带yield的generator function。
(将列表生成式的[]改为()就是generator)
这些可以直接作用于for循环的对象统称为可迭代对象：Iterable

>> > l = [1, 2, 3, 4]
>> > iter(l)
< list_iterator
object
at
0x7ff035d8b668 > 迭代器: iterator

L = (x * x for x in [1, 2, 4, 5])

for n in L:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(6)
print(f)
print(next(f))
print('-------------------')
for n in f:
    print(n)

# 解决方案:1,实现一个迭代器Weatheriterator,
# next方法每次返回一个城市气温
# 2.实现一个可迭代对象
# Weatheriterable,_iter_方法返回一个迭代器对象

def getWeather(city):
    r = requests.get(url=u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
    data = r.json()['data']['forecast'][0]
    return '%s:%s , %s' % (city, data['low'], data['high'])

# [u'北京',u'上海',u'广州',u'长春']

# print(getWeather(u'北京'))
# print(getWeather(u'长春'))

r = requests.get('http://www.weather.com.cn/data/sk/101020100.html')
r.encoding = 'utf-8'
print(r.json()['weatherinfo']['city'], r.json()['weatherinfo']['WD'], r.json()['weatherinfo']['temp'])
'''


class WeatherIterator(Iterator):
    # cities表示城市名字的字符串列表
    # 函数构造器
    def __init__(self, cities, ):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = requests.get(url=u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s:%s , %s' % (city, data['low'], data['high'])

    def next(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)


class WeatherIterable(Iterable):
    def __init__(self, citiets):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


r = WeatherIterable([u'北京', u'上海', u'广州', u'长春'])
for x in r:
    print(x)