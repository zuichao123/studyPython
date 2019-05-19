#coding:utf-8
'''
    匿名函数
        lambda表达式
            不能再lambda表达式中做赋值操作

    三元表达式
        条件为真时返回的结果 if 条件判断 else 条件为假时的返回结果

    map

'''
def add(x,y):
    return x+y

#使用lambda函数实现匿名函数如下：
f = lambda x,y:x+y
#调用匿名函数时，可以使用将匿名函数赋值给一个变量

print(add(3,4))
print(f(3,4))

# ---------------------------------------------
a = 1
b = 2
r = a if a > b else b
print(r)

a = 3
b = 2
r2 = lambda a,b:a*b if a > b else lambda a,b:a/b
print(r2)

# -----------------------------------------------
# map
list_x = [1,2,3,4,5,6,7,8,9]
def square(x):
    return x*x
r = map(square,list_x)# 参数1：函数   参数2：集合or列表
# 相当于
# for x in list_x:
#     square(x)
print(list(r))
# 相当于
list_x = [1,2,3,4,5,6,7,8,9]
r = map(lambda x:x*x,list_x)
print(list(r))