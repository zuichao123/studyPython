# coding:utf-8
"""
    数据结构与算法——算法引入、时间复杂度和大O表示法
    练习一

    时间复杂度：
        执行次数函数举例        阶       非正式术语
        12                      O(1)        常数阶
        2n+3                    O(n)        线性阶
        3n2+2n+1                O(n2)       平方阶
        5log2n+20               O(logn)     对数阶
        2n+3nlog2n+19           O(nlogn)    nlogn阶
        6n3+2n2+3n+4            O(n3)       立方阶
        2n                      O(2n)       指数阶

        注意，经常讲log2n（以2为底的对数）简写成logn

        O(1)<O(logn) < O(n) < O(nlogn) < O(n2) O(n3) < O(2n) < O(n!) < O(nn)
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