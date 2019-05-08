# coding:utf-8
'''
    生成器练习
        将生成器的方式保存，需要的时候在生成
'''
# 方式1(使用小括号组的方式)
a = (x * 2 for x in range(10))
#print(next(a))


# --------------------------------------------------
# 方式2(使用函数方式)
def createNum():
    '''使用yield关键字，可以创建一个生产器对象
        程序遇到yield关键字，就会停止运行
        可以使用send方法，给此时的yield赋值
        调用这个函数后，需要用一个变量接收后
        使用nexe()方法获取值'''
    a, b = 0, 1
    for i in range(5):
        yield b
        a, b = b, a + b


# 创建一个生成器对象
a = createNum()
#print(next(a))
'''next(a)和a.__next__()是一样的'''
#print(a.__next__())


# -------------------------------------------------------
# 协程
def test1():
    while True:
        print("------1------")
        yield None


def test2():
    while True:
        print("-----2-----")
        yield None


# 创建两个对象
t1 = test1()
t2 = test2()


while True:
 	t1.__next__()
 	t2.__next__()