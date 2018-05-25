# 如何统计序列中元素的出现频度
# 随机序列出现次数最高的3个元素和对应的次数和
# 英文文章出现次数最高的单词和对应的次数
# 使用Counter

from collections import Counter, OrderedDict
from random import randint
import re

L = [12, 3, 4, 5, 3, 4, 5, 6]
c = Counter()  # 创建实例

for ch in L:
    c[ch] = c[ch] + 1
print(c)  # 返回的c是一个字典
# Counter.most_common(n)方法得到频度最高的n个元素的列表
print(c.most_common(n=3))

data = [randint(0, 20) for _ in range(30)]
print(Counter(data))
print(Counter(data).most_common(3))
data2 = Counter(data).most_common(3)
print(type(data2))
for i in data2:
    print(i[0])

print('--------------------------')

print([x[0] for x in data2])

# 以data作为字典的key,0作为value

print('--------------------------')
c = dict.fromkeys(data, 0)

for x in data:
    c[x] = c[x] + 1  # 表示每遇到一个相同c[x]值就加1
print(c)

# print([v for v in sorted(c.values(),key=f1)])
# print(sorted(c.items(), lambda x, y: cmp(x[1], y[1]), reverse=True))

txt = open('relation.txt').read()
#print(txt)

#首先要做分割,将每一个单词进行分割取出来放到list中

data=re.split('\W+',txt) #W+表示非字母形式的分割
print(data)
data.pop(0)
data.pop(-1)
print(Counter(data))
print(Counter(data).most_common(n=3))








