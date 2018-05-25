# 如何对迭代器做切片操作,
import os
from itertools import islice
#　有某个文本文件,我们想读取其中某范围的内容如100行~300行的内容
# python中txt文件属于可迭代对象,我们是否可以使用类似列表切片的方式得到
# 一个100~300行文件内容的生成器

# step 步径值
f = open('/var/log/bootstrap.log')
#print(f[100:300]) #可以么

#答案是不可以,提示文件无索引,故无法进行切片操作

# 传统方法
f = open('/var/log/bootstrap.log')
lines = f.readlines()
print(lines[100:301])
print(f.tell())
f.seek(0,os.SEEK_SET)
print(f.tell())

# 解决方案:
# 使用标准库的itertools.islice,它能返回一个迭代对象切片的生成器
t1 =iter(f)
t = islice(t1,100,300)
print(t)
for n in t:
    print(n)
f.seek(0,os.SEEK_SET)
print(f.tell())
# 在生成器被迭代后,文件指针会顺序移动到迭代的最后一位






