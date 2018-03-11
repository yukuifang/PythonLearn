#类属性
#python里万物皆对象，类也是对象

class Person:
    name = 'fangyukui'
    pass

Person.age = 21

# fangyukui 21
print(Person.name,Person.age)

#__dict__ 可以看到类对象有内置属性，还有我们新增的类对象属性
print(Person.__dict__)


p = Person()

#name和age是类对象的属性，注意他们不属于类实例的属性，但是类实例对象可以访问到类对象属性
#  {}
print(p.__dict__)

#类实例对象查找机制：先查找自己的属性有没有，如果没有的话，会根据__class__ 找到类对象，在类对象的属性中查找
# fangyukui 21
print(p.name,p.age)


#动态修改类
class Animal:
    gender = '非人类'
    name = '旺财'
    pass
p.__class__ = Animal
# 旺财
print(p.name,p.gender)


