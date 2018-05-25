# 如何为元组的每个元素命名,提高程序可读性
# original priority relations
# yourself>>wife|girlfriend if you have>>your child if you have>>parents>>
# families except parents>>dear friends||relatives since you are child
# >>dear highschool classmates>>dear college mates >>friends of career
# >>workmates >>social friends
#

# real priority relations
# wife|girlfriend if you have>>your child if you have>> -->I have none of them

# >>admiring female friends -->I have no fit object or I am not that fit object currently
# no one will like weak and sloppy man, and no one will like affected and slovenly woman
# And more importantly,woman and man both need same  sense of worth

# >>dear college mates >>friends of career >>dear highschool classmates
# >>parents>>families except parents>> >>workmates >>social friends

# >>dear friends||relatives since you are child -->I have no one man who keep in touch with
from collections import namedtuple

Jim = ('Jim', 16, 'male', 'jim8721@gamil.com')
Lilei = ('Lilei', 17, 'male', 'leile@qq.com')
Lucy = ('Lucy', 16, 'female', 'lucy123@yahoo.com')

student = [Jim, Lilei, Lucy]
for i in student:
    if i[1] > 16:
        print(i[0])
        print(i[1])
        print(i[2])

# 解决方案:
'''
定义类似与其他语言的枚举类型,也就是定义一系列数值常量
使用标准库中collections.nametuple替代内置tuple
'''
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)


Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
Jim = Student('Jim', 16, 'male', 'jim8721@gamil.com')
Lilei = Student('Lilei', 17, 'male', 'leile@qq.com')
Lucy = Student('Lucy', 16, 'female', 'lucy123@yahoo.com')
print(Jim.name)
print(Jim.age)
print(Jim.sex)
print(Jim.email)

'''NAME = 0
AGE = 1
SEX = 2
EMAIL = 3'''
# 列表生成式
NAME, AGE, SEX, EMAIL = range(4)

student = ('Jim', 16, 'male', 'jim8721@gamil.com')

# name
print(student[NAME])
print(student[AGE])
print(student[EMAIL])






