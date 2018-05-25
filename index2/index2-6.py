# 如何让字典保持有序
from collections import OrderedDict
from time import time
from random import randint
# 实际案例:某编程竞赛系统,队参赛选手编程解题进心计时,
'''
选手完成题目后,把该选手解题用时时间记录到字典中,
以便赛后按选手名查询成绩
比赛结束后,需按排名顺序依次打印选手成绩,如何实现
'''

score = {
    'LiLei': (2, 43),  # 表示第2位完成比赛,用时43s
    'HanMeimei': (5, 42),
    'Jim': (1, 39),
}

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

print(od['a'])

# 解决方案:使用collections.OrderedDict
# 以OrderedDict替代Dict,依次将选手成绩存入OrderedDict

players = list('ABCDEFGH')
start = time()
od = OrderedDict()
for i in range(8):
    input()
    p = players.pop(randint(0,7-i))
    end = time()
    print(i+1,p,end-start)
    od[p] = (i+1,end-start)
print(od.keys())

