class Person:
    pass

# p 为Person实例对象
p = Person()

# p.__class__ 可以访问类  <class '__meain__.Person'>
print(p.__class__)


# 属性:类属性和对象属性

#新增对象属性
p.name = 'fangyukui'

#访问对象属性
print(p.name)

#AttributeError: 'Person' object has no attribute 'age'
# print(p.age)

#查看对象所有属性的内置属性
print(p.__dict__)


p.pets = ['小黄','小花']

#['小黄', '小花'] 4344692104
print(p.pets,id(p.pets))

p.pets.append('小白')

#['小黄', '小花', '小白'] 4344692104
print(p.pets,id(p.pets))

p.pets = [1,2,3]

# [1, 2, 3] 4539553544
print(p.pets,id(p.pets))


p.gender = 'female'

#删除属性
del p.gender

# AttributeError: 'Person' object has no attribute 'gender'
# print(p.gender)









