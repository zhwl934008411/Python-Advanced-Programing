# 如何在for语句中迭代多个可迭代对象
from random import randint
from functools import reduce
from itertools import chain

'''
1.某班学生期末考试成绩,语文数学英语分别存在3个列表中,
  同时迭代三个列表,计算每个学生的总分.(并行)

2.某年级有4个班,,某次考试每班英语成绩分别存储在4个列表中,依次迭代每个
  列表,统计全学年成绩高于90分人数.(串行)

print(reduce(lambda x,y:x & y,list(map(dict.keys,[N1,N2,N3]))))
'''
data1 = {k: randint(50, 100) for k in 'ABCD'}

data2 = {k: randint(50, 100) for k in 'ABCD'}

data3 = {k: randint(50, 100) for k in 'ABCD'}

# score2 = list(map(dict.values(),[data1,data2,data3]))
# print(score2)

score = reduce(lambda x, y: x & y, map(dict.keys, [data1, data2, data3]))
print(score)

'''
解决方案:
并行:使用内置函数zip,它能将多个可迭代对象合并.每次迭代返回一个元组

串行:使用标准库中的itertools.chain,它能将多个可迭代对象连接

# 使用zip将字典数据转化为元组
score4 = tuple(zip(score.values(),score.keys()))
'''
score = []
print(data1.values())
print(data2.values())
print(data3.values())

for e,m,l in zip(data1.values(),data2.values(),data3.values()):
    score.append(e+m+l)
print(score)

class1 = [randint(60, 100) for _ in range(40)]
class2 = [randint(60, 100) for _ in range(42)]
class3 = [randint(60, 100) for _ in range(44)]
class4 = [randint(60, 100) for _ in range(44)]
num = []
for x in chain(class1, class2, class3, class4):
    if x > 90:
        num.append(x)

print(len(num))
