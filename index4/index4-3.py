# coding:utf8
import re

# 如何调整字符串中文本的格式

'''
某软件的log文件,其中的日期格式为'yyyy-mm-dd':
......
2016-5-23 10:59:26 status unpacked python3-pip:all
2016-5-23 10:59:26 status half-configured python3-pip:all
2016-5-23 10:59:26 status installed python3-pip:all
2016-5-23 10:59:26 status configure python3-wheel:all 0.24.0-1
......

我们想把其中日期改为美国日期的格式 'mm/dd/yyyy'.
'2016-5-23'-->'5/23/2016',应如何处理


'''

# 正则表达式找到所有的日期,进行替换


# 使用正则表达式re.sub()方法做字符串替换,利用正则表达式的捕获组
# 捕获每个部分内容,在替换字符串中调整各个捕获组的顺序

log = open('/var/log/dpkg.log').read()
x = re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', log)
# print(x)
help(re.sub)
# print re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',r'\g<month>/\g<day>/\g<year>',log)
print('dfasdfasds' + 'dfasdfa')
