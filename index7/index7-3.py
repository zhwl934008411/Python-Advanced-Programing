# coding:utf8
# 如何让对象支持上下文管理
from telnetlib import Telnet
from sys import stdin, stdout
from collections import deque

with open('demo.txt', 'w') as f:
    f.write('abcdef')
    f.writelines('xyz\n')
# f.close()

'''
实际案例:
我们实现了一个telnet客户端的类TelnetClient,
调用实例的start()方法启动客户端与服务端交互
交互完毕后需调用cleanup()方法,关闭已连接的socket,
以及将操作历史记录写入文件并关闭

能否让TelnetClient的实例支持上下文管理协议
从而替代手工调用cleanup方法
'''


class TelnetClient(object):
    def __init__(self, addr, port=23):
        self.addr = addr
        self.port = port
        self.tn = None

    def start(self):
        raise Exception('Test')
        self.tn = Telnet(self.addr, self.port)
        self.history = deque()

        # user
        t = self.tn.read_until('login: ')
        stdout.write(t)
        user = stdin.readline()
        self.tn.write(user)

        # password
        t = self.tn.read_until('Password: ')
        if t.startswith(user[:-1]): t = t[len(user) + 1:]
        stdout.write(t)
        self.tn.write(stdin.readline())

        t = self.tn.read_until('$ ')
        stdout.write(t)
        while True:
            uinput = stdin.readline()
            if not uinput:
                break
            self.history.append(uinput)
            self.tn.write(uinput)
            t = self.tn.read_until('$ ')
            stdout.write(t[len(uinput) + 1:])

    def cleanup(self):
        pass
        '''self.tn.close()
        self.tn = None
        with open(self.addr + '_history.txt', 'w') as f:
            f.writelines(self.history)'''

    def __enter__(self):
        self.tn = Telnet(self.addr, self.port)
        self.history = deque()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('In __exit__')
        self.tn.close()
        self.tn = None
        with open(self.addr + '_history.txt', 'w') as f:
            f.writelines(self.history)
        #return True


# TelnetClient('127.0.0.1')在调用enter方法后才会创建client实例

with TelnetClient('127.0.0.1') as client:
    client.start()
print('END')
'''
client = TelnetClient('127.0.0.1')
print('\nstart...')
client.start()
print('\ncleanup')
client.cleanup()
'''
'''
自动完成cleanup
解决方案:实现上下文管理协议,需定义实例的__enter__,__exit__方法,
它们分别在with开始和结束时被调用

'''
