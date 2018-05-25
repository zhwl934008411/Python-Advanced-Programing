# 如何快速找到多个字典中的公共键(key)
from functools import reduce

N1 = {
    '苏亚雷斯': 1,
    '梅西': 2,
    '本泽马': 1,
    'C罗': 3
}

N2 = {
    '苏亚雷斯': 2,
    'C罗': 1,
    '格里子曼': 2,
    '贝尔': 1
}

N3 = {
    '苏亚雷斯': 1,
    '托雷斯': 2,
    '内马尔': 1,
    '贝尔': 1
}

# 统计出每轮比赛都有进球的球员
res = []
for k in N1:
    if k in N2 and k in N3:
        res.append(k)

print(res)
#set(list)

#解决方案:
'''
利用set集合的交集操作
1.使用dict的viewkeys()方法,返回一个dict.keys()的集合
2.使用map函数,得到所有字典的keys的集合
3.使用reduce函数,取所有字典的keys的集合的交集
'''
#python3.6不直接支持reduce,需要from functools import reduce
print(reduce(lambda x,y:x & y,list(map(dict.keys,[N1,N2,N3]))))
# 集合和集合之间可以求交集





