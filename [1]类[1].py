class Person:
    pass
# Person是指向类这块的指针变量    <class '__main__.Person'>
print(Person)

# __name__是类属性,类名    Person
print(Person.__name__)

#Person是指向类这块的指针变量,变量是可以被修改
Person = 666

# 666
print(Person)





