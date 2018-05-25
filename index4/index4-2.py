# coding:utf8
import os, stat

# 如何判断字符串a是否以字符串b开头或结尾
# 就是先判断b是否a的一部分,b是a的开头和结尾
'''
某文件系统目录下有一系列文件:
quicksort.c
graph.py
heap.java
install.sh
stack.cpp
...

编写程序给其中所有.sh文件和.py文件加上用户可执行权限
'''
'''
使用字符串的str.startswith()和str.endswitch()方法.
注意:多个匹配时参数使用元组
'''

L = os.listdir('/home/jesee/Documents/test/')
print(L)

# 进制间的转换
# bin('Num',8) -->bin 0b
# oct,002('Num',2) -->bin  hex(0x) int

S = [name for name in L if name.endswith(('.py', '.sh'))]
print(S)
print(stat.S_IXUSR)
os.chmod('/home/jesee/Documents/test/a.sh', os.stat('/home/jesee/Documents/test/a.sh').st_mode | stat.S_IXUSR)
