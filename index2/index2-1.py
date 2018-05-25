# 如何在列表\字典\集合中根据条件筛选数据

# 可以用filter函数,lambda函数,还可以使用列表生成式

print([x * x for x in range(1, 11)])

L = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(L)
print([x for x in [1. - 1, -3, -4, 3, 3, 45, 34] if x >= 0])

L2 = list(filter(lambda x: x > 0, [1. - 1, -3, -4, 3, 3, 45, 34]))
print(L2)

L3 = list(filter(lambda x: x > 0, (1. - 1, -3, -4, 3, 3, 45, 34)))
print(L3)

L4 = (0, 1. - 1, -3, -4, 3, 3, 45, 34)
L5 = []
for i in L4:
    if i >= 0:
        L5.append(i)
L5.pop(1)
print(L5)

score = {
    "LiLei": 79,
    "Jim": 88,
    "Lucy": 92
}
score2 = {}
for k, v in score.items():
    if v >= 90:
        score2[k] = v
print(score2)
#dict的列表生成式
print({k:v for k, v in score.items() if v > 90})
#集合的列表生成式
s={1,34,5,-7,6,87,-8,-9,11}
print({x for x in s if x%3==0})


#首选列表生成式,运行快,性能更佳

