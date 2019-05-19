# coding:utf-8
"""
    数据结构与算法——Python列表和字典

    Python2和Python3中range的区别：
        Python2：返回的是列表对象；xrange()返回的是可迭代对象
        Python3：返回的是可迭代对象

    list内置操作的时间复杂度
        Operation               Big-O Efficiency
        indexx[]                O(1)
        index assignment        O(1)
        append                  O(1)
        pop()                   O(1)
        pop(i)                  O(n)
        insert(i,item)          O(n)
        del operator            O(n)
        iteration               O(n)
        contains(in)            O(n)
        get slice[x:y]          O(k)
        del slice               O(n)
        set slice               O(n+k)
        reverse                 O(n)
        concatenate             O(k)
        sort                    O(n log n)
        multiply                O(nk)

    dict内置操作的时间复杂度
        Operation           Big-O Efficiency
        copy                O(n)
        get item            O(1)
        set item            O(1)
        delete item         O(1)
        contains(in)        O(1)
        iteration           O(n)
"""

# 列表生成
from timeit import Timer

li1 = [1,2]
li2 = [23,4]

# 以下4种
li3 = li1 + li2
li4 = [i for i in range(1000)] # 列表生成器
li5 = list(range(1000))
li = []
for i in range(1000):
    li.append(i)

# 测试
def test1():
    li=[]
    for i in range(10000):
        li.append(i)

def test2():
    li=[]
    for i in range(10000):
        li+=[i]

def test3():
    li = [i for i in range(10000)]

def test4():
    li = list(range(10000))

def test5():
    li = []
    for i in range(10000):
        li.extend([i])

def test6():
    li=[]
    for i in range(10000):
        li = li + [i]

timer1 = Timer("test1()", "from __main__ import test1") # 从当前启动文件中导入函数
print("append:", timer1.timeit(1000)) # 运行起来，并测算1000次---返回花费的时间单位秒
timer2 = Timer("test2()", "from __main__ import test2") # 从当前启动文件中导入函数
print("+=:", timer2.timeit(1000)) # 运行起来，并测算1000次---返回花费的时间单位秒
timer3 = Timer("test3()", "from __main__ import test3") # 从当前启动文件中导入函数
print("迭代器:", timer3.timeit(1000)) # 运行起来，并测算1000次---返回花费的时间单位秒
timer4 = Timer("test4()", "from __main__ import test4") # 从当前启动文件中导入函数
print("list:", timer4.timeit(1000)) # 运行起来，并测算1000次---返回花费的时间单位秒
timer5 = Timer("test5()", "from __main__ import test5") # 从当前启动文件中导入函数
print("extend:", timer5.timeit(1000)) # 运行起来，并测算1000次---返回花费的时间单位秒
timer6 = Timer("test6()", "from __main__ import test6") # 从当前启动文件中导入函数
print("=+:", timer6.timeit(1000)) # 运行起来，并测算1000次---返回花费的时间单位秒
