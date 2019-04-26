#coding:utf-8
'''
    types.MethodType方法练习
'''
import types

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

def eat(self):
    print("----eat--------")

#给类对象添加属性
duix = Person("s",2)
duixYinyong = types.MethodType(eat,duix)


duixYinyong()
duix2 = Person("j",3)

print(duix.name)

