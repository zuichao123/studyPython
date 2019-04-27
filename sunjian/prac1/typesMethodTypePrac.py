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

#声明一个对象
duix = Person("s",2)
#给类对象添加属性方法
duixYinyong = types.MethodType(eat,duix)

#调用添加属性方法后的对象引用
duixYinyong()

#再声明一个对象
duix2 = Person("j",3)
#打印添加的对象属性
print(duix2.name,duix2.age)

