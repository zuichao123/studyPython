#coding:utf-8
from functools import reduce
import sys
"""
    python 基础语法练习
"""
print("----------------------------------------#定义一个函数，传入3个参数")
"""
*args与**kwargs的区别，两者都是python中的可变参数。
　　　　*args表示任何多个无名参数，它本质是一个tuple；
　　　　**kwargs表示关键字参数，它本质上是一个dict；
　　如果同时使用*args和**kwargs时，必须*args参数列要在**kwargs前。
"""
def f(x,*args,**args2):
    print ("x=" "%s" % x)#输出第一个传入的参数
    print ("args=",args)#输出*args的剩余参数
    print ("args2=",args2)

t=(2,3,5,6)
tt={'a':3,'b':4,'c':5}
f(*t,**tt)
print("----------------------------------------#定义一个函数，返回两个参数的乘积")
def ff(x,y):
    return x*y
x=12
y=12
print(ff(x,y))
print("----------------------------------------#lambda函数：x,y作为参数，返回的是x*y的结果")
v = lambda x,y:x*y
print(v(5,6))
print("----------------------------------------#python3中range函数返回的是一个整数序列的对象，而不是列表，可以使用list函数返回列表")
ll = range(10)
print(list(ll))
#reduce()函数作用是：把结果继续和序列的下一个元素做累积计算(在 Python3 中，reduce() 函数已经被从全局名字空间里移除了，它现在被放置在 functools 模块里，如果想要使用它，则需要通过引入 functools 模块来调用 reduce() )
print("----------------------------------------")
print(abs(-10))#abs() 函数返回数字的绝对值
print(divmod(7,3))#divmod(a,b)方法返回的是a/b（商）以及a%b(余数)，返回结果类型为tuple元组
print(pow(3,4))#pow(x,y)方法返回的是x的y次方
print("----------------------------------------")
w = 'runoob'
sys.stdout.write(w+'\n')
print("----------------------------------------")
print("----------------------------------------")
print("----------------------------------------")
print("----------------------------------------")
