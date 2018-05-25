# coding:utf8
# 如何拆分含有多种分隔符的字符串
import re

'''
我们把某个字符串依据分隔符号拆分不同的字段,
该字符包含多种不同的分隔符,例如:

s = 'ab;cd|efg|hi,jklmn\topq;rst,uvw\txyz'

其中<,>,<;>,<|>,<\t>都是分隔符号.如何处理?



解决方案:
方法一:连续使用是str.split()方法,每次处理一种分隔符号
方法二:使用正则表达式的re.split()方法,一次性拆分字符串
txt = open('relation.txt').read()
#print(txt)

#首先要做分割,将每一个单词进行分割取出来放到list中

data=re.split('\W+',txt) #W+表示非字母形式的分割
'''
'''
s = 'ab;cd|efg|hi,jklmn|topq;rst,uvw|txyz'
t = s.split(';')
print(t)
p = []
for x in t:
    print(x.split('|'))
    for x1 in x.split('|'):
        p.append(x1.split(','))
print(p)
x = []
for i in p:
    x.append(i[0])
print(x)
'''


def mySplit(s, ds):
    # res = s.split(';')
    res = [s]
    for d in ds:
        t = []
        map(lambda x:t.extend(x.split(d)),res)
        #map(lambda x: t.extend(x.split(d)), res)

        res = t
    return [x for x in res if x]


s = 'ab;;cd|efg|hi,jklmn|topq;rst,uvw|txyz'
#ds = (',', ';', '|')
print(mySplit(s, ',;|'))
#split(pattern, string, maxsplit=0, flags=0)
# pattern表示分隔符,
print(re.split(r'[,;|\t]+',s))







