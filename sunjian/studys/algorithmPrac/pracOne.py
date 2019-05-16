# coding:utf-8
"""
    数据结构与算法
    练习一
"""

# 如果a+b+c=1000且a^2+b^2=c^2(a,b,c为自然数)，如果求出所有的组合？
import time

def method_1():
    """方式一"""
    start_time = time.time()
    for a in range(0, 1001):
        for b in range(0, 1001):
            for c in range(0, 1001):
                if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                    print("a,b,c:%d, %d, %d" % (a, b, c))
    end_time = time.time()
    print("times:%d" % (end_time - start_time))

# method_1()

def method_2():
    """方式二"""
    start_time = time.time()
    for a in range(0, 1001):
        for b in range(0, 1001):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print("a,b,c:%d, %d, %d" % (a, b, c))
    end_time = time.time()
    print("times:%d" % (end_time - start_time))

method_2()