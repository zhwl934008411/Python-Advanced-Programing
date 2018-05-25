# 如何使用生成器函数实现可迭代对象
from collections import Iterable, Iterator
# 一类是generator，包括生成器和带yield的generator function。
# (将列表生成式的[]改为()就是generator)

# 实现一个可迭代对象的类,它能迭代出给定范围内所有素数:
# 把print语句换成yield语句,函数就变成了一个generator
'''pn = PrimeNumbers(1,30)
for k in pn:
    print(k)
# 解决方案:将该类的__iter__方法实现成生成器函数
# ,每次yield返回一个素数
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
'''


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
for n in f:
    print(n)


class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimeNumber(self, k):
        if k < 2:
            return False
        for i in range(2, k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in range(self.start, self.end + 1):
            if self.isPrimeNumber(k):
                yield k
print('--------------')
print(type(PrimeNumbers(1,100)))
print(isinstance(PrimeNumbers(1,100),Iterable))
print('------------------------')
for n in PrimeNumbers(1,100): #默认实例实现定义的所有方法
    print(n)

if __name__ == '__main__':
    a = PrimeNumbers(1, 100)
    f = a.__iter__()
    print(type(f))
    L=[]
    for n in f:
        L.append(n)
    print(L)


