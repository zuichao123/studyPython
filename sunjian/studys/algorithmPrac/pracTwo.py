# coding:utf-8
"""
    数据结构与算法——Python列表和字典

    Python2和Python3中range的区别：
        Python2：返回的是列表对象；xrange()返回的是可迭代对象
        Python3：返回的是可迭代对象
"""

# 列表生成
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
