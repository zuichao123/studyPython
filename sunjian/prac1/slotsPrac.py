#coding:utf-8
'''
    __slots__特殊变量练习

    Python允许定义类的时候，定义一个特殊的__slots__变量，来限制class实例能添加的属性
    注意：
        使用__slots__定义的属性对当前类实例起作用，对继承的子类是不起作用的

'''

class Person(object):
    pass
    # __slots__ = ("name","age")

p = Person()

p.name = "孙健"
p.age = 30
p.aa = 23

print(p.name,p.age,p.aa)

'''
    放开上边注释的__slots__那一行后，
    执行上边的打印语句会报错，因为：__slots__限制了Person类的属性只能是name和age
'''