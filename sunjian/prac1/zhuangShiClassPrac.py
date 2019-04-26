#conding:utf-8
'''
    装饰类练习
'''

def w1(func):
    '''无参装饰'''
    print("===1===")
    def w1_in():
        '''闭包'''
        print("===2===")
        func()
        print("===3===")
    return w1_in

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