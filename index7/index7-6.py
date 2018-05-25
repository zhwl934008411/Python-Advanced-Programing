# coding:utf8
# 如何使用描述符对实例属性做类型检查

''''''
'''
实例:在某项目中,我们实现了一些类,并希望能像静态类型语言那样(
C,C++,Java)对他们的实例属性做类型检查.
p = Person()
p.name = 'Bob'
p.age = 18
p.height = 1.83

要求:
1.可以对实例变量名指定类型(int,float,string)
2.赋予不正确类型时抛出异常
'''

'''
使用描述符来实现需要类型检查的属性:
分别实现__get__,__set__,__delete__方法,在
__set__内使用isinstance函数做类型检查
'''


class Attr(object):
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

    def __get__(self, instance, cls):
        # print('in __get__', instance, cls)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('in __set__')
        if not isinstance(value,self.type_):
            raise TypeError('expected an %s' % self.type_)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        # print('in __del__')
        del instance.__dict__[self.name]


class Person(object):
    # x = Descriptor()  # x为类的属性
    name = Attr('name', str)
    age = Attr('age', int)
    heigth = Attr('height', float)

p = Person()
p.name = 'Bob'
print(p.name)
# print(Person.name)
#p.age ='17'
#print(p.age)





'''a = A()
print(a.x)  # 类的实例属性
print(A.x)  # 类的属性'''
