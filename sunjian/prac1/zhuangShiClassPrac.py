#conding:utf-8
'''
    装饰器练习
        函数装饰器
        类装饰器
'''

print("----------------函数装饰器-----------------")
def w1(func):
    '''无参装饰'''
    print("===1===")
    def w1_in():
        '''闭包'''
        print("===2===")
        func()
        print("===3===")
    return w1_in

'''
    在此处使用装饰器@w1表示：ddd = w1(ddd)
    1.将ddd函数作为参数传递给w1函数，而在w1函数中又定义了一个内部函数，
      在这个内部函数中调用了负责接收传进来的ddd函数的参数变量func
    2.然后将内部函数返回给w1函数，也就是说最后在调用函数对象ddd的时候，
      其实是在调用w1函数的内部函数w1_in()
    3.由于这个内部函数中调用了当初传递的ddd()方法的引用，所有此时最终还是调用被装饰的ddd()方法
'''
@w1
def ddd():
    print("---dddd---")


ddd()
print('-----------------------------------------------')
def w2(func):
    '''有参装饰'''
    print("===========1")
    def func_in(*args,**args2):
        '''闭包'''
        print("=============2")
        func(*args,**args2)
        print('=============3')
    return func_in


@w2
def ccc(a,b,c):
    print("---------a=%d,b=%d,c=%d"%(a,b,c))


ccc(11,22,33)

print("----------------类装饰器--------------------------")

class Test(object):
    def __init__(self,func):
        print('------初始化------')
        print('------func name is %s'%func.__name__)
        self.__func = func

    def __call__(self, *args, **kwargs):
        print('------------装饰器的功能-------------')
        self.__func()

'''
1.在此处使用装饰器@Test表示：test = Test(test)
2.创建Test类对象的时候，将test方法作为一个参数传给Test类的初始化方法__init__
3.然后在方法中创建一个私有的变量__func将传入的func变量接收的test方法的引用赋值给这个私有变量__func，此时这个函数运行完成，所以负责接收的变量func消失
  所以此时，对象创建完成后，只剩下一个私有属性__func得到了test()方法的引用
4.最后调用这个被装饰的test()方法，等于在调用这个Test类的对象，这个对象中目前只有私有变量__func，但是Python中对象是不可以被直接调用的；
  由于Python规定，调用类的对象时，会自动调用这个类中的__call__方法；
  而在这个__call__方法中，引用了定义的私有变量__func()，so...
'''
@Test
def test():
    print('-----------test-------------')

test()