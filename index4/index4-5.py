# coding:utf8
# 如何对字符串进行左,右,居中的对齐
'''
某个字典存储了一系列属性值
{
    "lodDist":100.0,
    "SmallCull":0.04,
    "DistCull":500,
    "trilinear":40,
    "farclip":477
}

'''
'''
在程序中，我们希望以以下格式输出字典的内容,该如何处理
SmallCull :0.04
farclip   :477
lodDist   :100.0
DistCull  :500
trilinear :40
'''
dict = {
    "lodDist": 100.0,
    "SmallCull": 0.04,
    "DistCull": 500,
    "trilinear": 40,
    "farclip": 477
}

for k, v in dict.items():
    print k,':', v
print('------------------')
for k, v in dict.items():
    print k.ljust(9,' '),':',v
print('------------------')
for k, v in dict.items():
    print format(k,'<9'),':',v
'''
解决方案:
方法1:使用字符串的str.ljust(),str.rjust(),str.center进行左,右,居中对齐
方法2:使用format()方法,传递类似'<20','>20','^20'参数完成左对齐,右对齐,居中对齐
'''







