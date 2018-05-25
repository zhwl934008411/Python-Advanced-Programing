# 如何根据字典中值的大小,对字典中的项排序


score = {
    'LiLei': 79,
    'Jim': 88,
    'Lucy': 92
}


# 对学生按照成绩排序
# 解决方案:使用内置函数sorted
# 使用zip将字典数据转化为元组
# 传递sorted函数的key函数
# sorted函数默认按照ASCII码排序
#for k, v in score.items():

#k,v交换
#score2={v:k for k,v in score.items()}

#score3=dict(zip(score2.values(),score2.keys()))

score4 = tuple(zip(score.values(),score.keys()))
score5 = sorted(score4)
print(score5)

#直接用sorted,
print(sorted(score.items(),key=lambda x:x[1]))
#表示对生成的列表的元组索引第二位进行排序



#print(dict(zip(score5.values(),score5.keys())))

