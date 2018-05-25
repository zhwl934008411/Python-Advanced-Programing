# 如何实现用户的历史记录功能(最多n条)
from random import randint
from collections import deque
import pickle
# 实际案例
'''
很多应用程序都有浏览用户的历史记录的功能
例如:
浏览器可以查看最近访问过的网页
视频播放器可以查看最近播放过视频文件
Shell可以查看用户输入过的命令
-------------------------
现在我们只做了一个简单的猜数字的小游戏
添加历史记录功能,显示用户猜过的数字
如何实现
'''
N = randint(0, 100)
history=deque([],5)

def guess(k):
    if k == N:
        print('right')
        return True
    if k < N:
        print('%s is less than N' % k)
    else:
        print('%s is more than N' % k)
    return False

while True:
    line = input('please input a number:')
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == 'history' or line =='h?':
        #print(history)
        print(list(history))
    pickle.dump(list(history), open('index', 'wb+'))



#pickle.load('index')
#q2 = pickle.load(open('history'))



#解决方案:
'''
使用容量为n的队列存储历史记录
使用标准库collections的deque,他是一个双端循环队列
程序退出前,可以使用pickle将队列对象存入文件,再次运行程序时将其导入

deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：


'''
q=deque([],5)  #定义一个长度为5的队列,并deque化


