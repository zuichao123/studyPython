#coding:utf-8
'''
    元类：就是用来创建class的

        类也是一个对象
        你也可以打印一个类
        你可以在运行时动态的创建它们
    eg:
        Cat = type("Cat",(Animal,),{"sleep":"night"})
            "Cat"               类名，必须使用双引号括起来
            Animal              父类
            "sleep":"night"     属性
'''
#动态的创建类
def choose_class(name):
    if name == "foo":
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar
MyClass = choose_class("foo")
print('这是类，不是类的实例',MyClass)
print('这是类的实例',MyClass())

# -----------------------------------------------------
# 使用type创建类
    # type还有一种完全不同的功能，动态的创建类

class Person:
    num = 0

#p1 = Person   # 这是创建一个类的引用赋值给变量p1
p1 = Person() # p1 = Person() 这是创建一个对象的引用赋值给p1

print(type(p1))
print(p1.num)

Person2 = type("Person2",(),{"num":0}) # () 继承的类  {}类的属性
#P2 = Person2
p2 = Person2()

print(type(p2))
print(p2.num)
# --------------------------带方法的元类
def printNum(self):
    print("----num-%d---"%self.num)

Test3 = type("Test3",(),{"printNum":printNum}) # 属性是printNum()方法
t3 = Test3()
t3.num = 300
t3.printNum()

# 上边的这个等于下边
class PrintNum2:
    def printNum(self):
        print("----num-%d---"%self.num)

t2 = PrintNum2()
t2.num = 300
t2.printNum()

#--------------------------------元类的继承、和属性
class Animal:
    def eat(self):
        print('-----------eat-----------')

class Dog(Animal):
    pass

wangcai = Dog()
print(wangcai.eat())

# 等于下边的
Cat = type("Cat",(Animal,),{"sleep":"night"})
tom = Cat()
print(tom.eat())

#--------------------------------------------------------------- 例子
def upper_attr(future_class_name, futrue_class_parents, future_class_attr):
    '''定义函数
        第一个参数是接收类名 # 相当于Foo
        第二个参数是父类名 # 相当于object
        第三个参数是接收属性名 # 相当于下边的bar
    '''

    # 遍历属性字典，把不是__开头的属性名字改为大写
    newAttr = {}
    for name, value in future_class_attr.items():
        if not name.startswith("__"):
            newAttr[name.upper()] = value

    # 调用type来创建一个类
    return type(future_class_name,futrue_class_parents,newAttr)

class Foo(object,metaclass=upper_attr): # 这是Python3 的方式
    # class Foo(object):
    #__metaclass__ = upper_attr # 指定创建类的格式；这是Python2 的方式
    bar = "bip"
# class Foo(object):

print(hasattr(Foo,'bar'))
print(hasattr(Foo,'BAR'))

f = Foo()
print("BAR属性的值=",f.BAR)
