# coding:utf8
'''
# 如何进行反向迭代以及如何实现反向迭代
# xrange() 函数用法与 range 完全相同,python3已经合并了range()用法
# 所不同的是生成的不是一个数组，而是一个生成器
# 实现一个连续浮点数发生器FloatRange(和range类似
# 根据给定范围(start,end)和步进值(step)产生一些列连续浮点数,
# 如迭代FloatRange(3.0,4.0,0.2)可产生序列:

正向：3.0-->3.2-->3.4-->3.6-->3.8-->4.0
反向：4.0-->3.8-->3.6-->3.4-->3.2-->3.0

'''


# 反向迭代器
# <list_reverseiterator object at 0x7fa3007b7390>

class FloatRange():
    def __init__(self, start, end, step=0.1):
        self.start = start  # 在对象内部记录这三个参数,方便其他方法的调用,
        self.end = end
        self.step = step  # 指定每次迭代的值的循环操作

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step

# self可看做是类的实例

for t in FloatRange(1.0,4.0,0.5): #默认实现了iter()方法
    print(t)

for t in FloatRange(1.0,4.0,0.2).__reversed__():
    print(t)

for t in reversed(FloatRange(1.0,4.0,0.2)):
    print(t)

#python2运行没有问题,都是一位小数









