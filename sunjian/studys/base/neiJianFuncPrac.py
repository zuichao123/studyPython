#coding:utf-8
'''
    常用的内建函数

        range
            在Python2中直接返回一个列表
            在Python3中返回一个迭代值，如果想得到列表，可以通过list函数

        map
            会根据提供的函数对指定序列做映射
            格式：
                map(function, sequence[, sequence, ...])
                function：是一个函数
                sequence：是一个或多个序列，取决于function需要几个参数
            返回的是一个list
            参数序列中每一个元素分别调用function函数，返回包含每次function函数返回值的list

        filter
            会对指定序列执行过滤操作
            格式：
                filter(function or None, sequence)
                function：接受一个参数，返回布尔值True或False
                sequence：序列可以是str,tuple, list
            filter函数会对序列参数sequence中的每个元素调用function函数，最后返回的结果包含调用结果为True的元素
            返回值的类型和参数sequence的类型相同
            0表示False，非0表示True

        reduce
            会对参数序列中元素进行累积
            格式：
                reduce（function,sequence[, initial]）
                function：改函数有两个参数
                sequence：序列可以是str, tuple, list
                initial：固定初始值
            reduce依次从sequence中取一个元素，和上一次调用function的结果做参数再次调用function
            第一次调用function时，如果提供initial参数，会以sequence中的第一个元素和initial作为参数调用function
            否则会以序列sequence中的前两个元素做参数调用function
        注意：
            function函数不能为None
            在Python3中reduce已经被从全局名字空间中移除了，需要导入from functools import reduce

        sorted
            排序

'''
# -----------------------range 练习
a = range(10)
# 方法一
for i in a:
    print(i)
# 方法二
print(list(a))

# 创建列表的另一种方法
b = [x+2 for x in range(10)] # x+2的意思是，开头和结尾各加2
print(b)

# ------------------------map 练习
# 函数需要一个参数
va = map(lambda x : x*x,[1,2,3])
print(list(va))

# 函数需要两个参数
val = map(lambda x,y : x+y,[1,2,3],[4,5,6])
print(list(val))

# 混合参数
def f1(x,y):
    return (x,y)
l1 = [0,1,2,3,4,5,6]
l2 = ['Sun','M','T','W','T','F','S']
l3 = map(f1,l1,l2)
print(list(l3))

# ----------------------filter 练习
va = filter(lambda  x: x%2,[1,2,3,4])
print(list(va))

va1 = filter(None,'fafasfasdfasdfasd') # 如果function设置为None，那就是不过滤了，所有东西全取
print(list(va1))

# ------------------------reduce 练习
from functools import reduce
va = reduce(lambda x,y : x+y, [1,2,3,4])
print(va)

va2 = reduce(lambda x,y : x+y,[1,2,3,4],5)
print(va2)

va3 = reduce(lambda x,y : x+y,['aa','bb'],'cc')
print(va3)

# ------------------------sorted 练习
va4 = sorted(['a','d','b','f','c'])
print(list(va4))

va5 = sorted([6,34,65,56,77,2])
print(list(va5))