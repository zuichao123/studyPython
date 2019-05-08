#coding:utf-8
'''
    内建属性

    常用专有属性        说明                        触发方式
    __init__            构造初始化函数              创建实例后，赋值时使用，在__new__后
    __new__             生成实例所需属性            创建实例时
    __class__           实例所在的类                实例.__class__
    __str__             实例字符串表示，可读性      print(类实例)，如没实现，使用repr结果
    __repr__            实例字符串表示，准确性      类实例 回车 或者print(repr(类实例))
    __del__             析构                        del删除实例
    __dict__            实例自定义属性              vars(实例.__dict__)
    __doc__             类文档，子类不继承          help(类或实例)
    __getattribute__    属性访问拦截器              访问实例属性时
    __bases__           类的所有父类构成元素        类名.__bases__

    访问属性时：会先调用__getattribute__这个内建属性

    注意：在__getattribute__这个方法中禁止再使用self.xxx，因为有可能会造成死循环
'''
import sys
a = "hello world"
print(a)

class Sjian(object):
    def __init__(self,subject1):
        self.subject1 = subject1
        self.subject2 = 'cpp'

    # 属性访问拦截器，打log
    def __getattribute__(self, item):
        if item == 'subject1':
            print('log subject1')
            return 'redirect python'
        else:
            return object.__getattribute__(self,item) # 否则，调用父类的去处理

    def show(self):
        print('0707 this is 01')

sj = Sjian('subject1')

print(sj.subject1)
print(sj.subject2)
print(sj.show())