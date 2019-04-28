#coding:utf-8
'''
    生成器练习
'''
#方式1(使用小括号组的方式)
a = (x*2 for x in range(10))
print(next(a))
#--------------------------------------------------
#方式2(使用函数方式)
def createNum():
    '''使用yield关键字，可以创建一个生产器对象
        调用这个函数后，需要用一个变量接收后
        使用nexe()方法获取值'''
    a,b = 0,1
    for i in range(5):
        yield b
        a,b = b,a+b

a = createNum()
print(next(a))