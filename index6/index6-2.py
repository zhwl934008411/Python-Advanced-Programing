# coding:utf8
import requests
import json
# 如何读写json数据

''''''

'''
实际案例:
在web应用中常用JSON(JavaScript Object Notation)格式传输
数据,例如我们利用Baidu语音识别服务做语音识别,将本地音频数据
post到Baidu语音识别服务器,服务器响应结果为json字符串


{"corpus_no":"6303355448008565863",
"err_msg":"success.","err_no":0,"result":["你好,"],
"sn":"418359718861467614305"}

在Python中如何读写json数据?
'''

'''
解决方案:
使用标准库中的json模块,其中loads,dumps函数可以完成json数据的读写
'''
'''
# 录音
from record import Record
record = Record(channels=1)
audioData = record.record(2)'''

# 获取token

l = {"corpus_no":"6303355448008565863",
"err_msg":"success.","err_no":0,"result":["你好,"],
"sn":"418359718861467614305"}

j = json.dumps(l)
print(j)

l2 = json.loads(j)
print(l2)

with open('demo2.py','wb') as f:
    l = {"a": 6, "b": null, "c": "abc"}
    f.write('l')

print(json.loads(f))

