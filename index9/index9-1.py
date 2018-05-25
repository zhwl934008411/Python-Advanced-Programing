# coding:utf8

# 如何使用函数装饰器

''''''

'''
实际案例:
某些时候我们想为多个函数,统一添加某种功能,比如计时统计,记录日志,
缓存运算结果等等.

我们不想在每个函数内一一添加完全相同的代码,有什么好的解决方案

[题目1]斐波那契数列(Fibonacci Sequence),又称黄金分割数列,
       指的是这样一个数列:1,1,2,3,5,8,13,21,
       这个数列从第三项开始,每一项都等于前两项之和,求数列第n项
       
'''
def meomo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap
'''
def fibonacci(n,cache=None):
    if cache is None:
        cache = {}

    if n in cache:
        return cache[n]

    if n<=1:
        return 1
    cache[n] = fibonacci(n-1,cache)+fibonacci(n-2,cache)
    return cache[n]

print(fibonacci(50))
'''
# @memo == fibonacci = meomo(fibonacci2)
@meomo
def fibonacci(n):
    if n<=1:
        return 1
    cache = fibonacci(n-1)+fibonacci(n-2)
    return cache

print(fibonacci(98))
'''
[题目2]一个共有十个10个台阶的楼梯,从下面走到上面,一次只能迈1-3个台阶,
并且不能后退,走完这个楼梯共有多少种方法
'''
@meomo
def climb(n,steps):
    count = 0
    if n == 0:
        count +=1
    elif n>0:
        for step in steps:
            count += climb(n-step,steps)
    return count


print(climb(10,(1,2,3)))











