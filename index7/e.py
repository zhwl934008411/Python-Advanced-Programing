# coding:utf8
# 如何派生内置不可变类型并修改实例化行为
''''''

'''
实例:我们想自定义一种新类型的元组,对于传入的可迭代对象,
我们只保留做其中int类型且值大于零的元素,例如
intTuple((1,-1,'abc',6,['x','y'],3)=>(1,6,3))

要求intTuple是内置tuple的子类,如何实现
'''
'''
解决方案:
定义类intTuple继承tuple,并实现__new__,修改实例化行为
python一切皆对象
'''


class intTuple(tuple):
    def __new__(cls, iterable):
        # g = generator
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(intTuple, cls).__new__(cls, g)

    def __init__(self, iterable):
        # before
        print(self)
        # super(intTuple,self).__init__(iterable)
        super(intTuple, self).__init__((1, 6, 3))
        # after


# 实例self是由__new__方法创建,名副其实的构造器方法
tuple1 = (1, -1, 'abc', 6, ['x', 'y'], 3)
t = intTuple(tuple1)
print(t)

# 如何为创建大量实例节省内存

'''
案例:
某网络游戏中,定义了玩家类Player(id,name,status,...)
每有一个在线玩家,在服务器程序内则有一个Player的实例,当在线人数
很多时,将产生大量实例(如百万级)

如何降低这些大量实例的内存开销
'''

'''
解决方案:
定义类的__slots__属性,它是用来声明实例属性名字的列表
'''


class Player(object):
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level


class Player2(object):
    # 声明实例的属性,就没有了__dict__方法
    __slots__ = ['uid', 'name', 'stat', 'level']

    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level


'''
sys.getsizeof(p1)
1088
sys.getsizeof(p2)
80
'''






