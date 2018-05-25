# coding:utf8
# 如何读写文本文件
# 如何处理二进制文件


'''
实际案例:
某一txt文件编码格式已知(如UTF-8,GBK,BIG5),
在python2.x和python3.x中分别如何读取该文件

解决方案:
pyhton3:
f = open('py3.txt','wt',encoding='utf-8')
f.write('你好,我爱编程')
7
f.close()
f = open('py3.txt','rt',encoding='utf-8')
s = f.read()
print(s)
你好,我爱编程

python2:
s = u'你好,我爱编程'
f = open('py2.txt','w')
f.write(s.encode('utf8'))
f.close()
f = open('py2.txt','r')
s = f.read()
print s.decode('utf8')
'''

'''
实际案例:
wav是一种音频文件的格式,音频文件为二进制文件
wav文件有头部信息和音频采样数据构成,前44个字节为头部信息
包括声道数,采样频率,PCM位宽等等,后面视音频采样数据

利用python分析一个wav文件头部信息,处理音频数据
'''
'''
解决方案:
open函数想以二进制打开文件,指定mode参数为'b'
二进制数据可以用readinto,读入到提前分配好的buffer中,便于数据处理
解析二进制数据可以使用标准库中的struct Module的unpack方法

'''
print('kk')
