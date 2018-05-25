# coding:utf8
from collections import deque
import re
'''
如何去掉字符串中不需要的字符
1.过滤掉用户输入中前后多余的空白字符
'  nick2008@gmail.com  '

2.过滤某windows下编辑文本中的'\r':
'hello world\r\n'

3.去掉文本中的unicode组合符号(音调):
'uulàlà,là,māmá'

re.split()
str.strip()
'''
'''
解决方案:
方法1:字符串strip(),lstrip(),rstrip()方法去掉字符串两段字符
方法2:删除单个固定位置的字符,可以使用切片+拼接的方式
方法3:字符串的replace()方法或正则表达式re.sub()删除任意位置字符
方法4:字符串translate()方法,可以同时删除多种不同字符

'''
print('----------------')
s='  nick2008@gmail.com  '
print(s.strip(' '))
print('----------------')
s = '====+-----'
print(s.strip('-='))
print('----------------')
s='  nick2008  @gmail.com  '
print(s[2:11]+s[12:23])
print('----------------')

s = '\tabd\t124\txyz\r\n'
print(s.replace('\t',''))
print('----------------')
s = '\tabd\t124\txyz\r\n'
print(re.sub('\t|\r|\n','',s))
print('----------------')
s = '\tabd\t124\txyz\r\n'
print(s.translate(None,'\t\r\n'))

s = '\tabd\t124\txyz\r\n'
print(s.replace('\t',''))
u = u'uulàlà,là,māmá'
print u.translate(dict.fromkeys([0x0,0x0101,0x1]))







