#coding:utf-8
'''
    python函数

'''
import re

print('---------------------group()函数详解---------------------------------------------')
sj = '234234fasdf234234234asd78923faf'
r = re.match('\d',sj)

#返回字符串的位置
print(r.span())
#返回字符串
    #分组可以有多个
print(r.group())

sj2 = 'life is short, i use python. I love python'
r = re.search('life(.*)python(.*)python',sj2)
print(r.group(0,1,2))#返回每个组的完整
print(r.groups())#返回每个组的实际

