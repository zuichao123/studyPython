#coding:utf-8
'''
    集合练习
'''
a = 'adfasdfasdfasdfjkjlkajlfkjadlsf'
b = set(a) # 无序并且元素不可重复的集合
print(b)

A = 'adfppe'
B = set(A)
print(B)
# ------------交集（都有的）
print('交集：',b&B)

# ------------并集（都没有的）
print('并集：',b|B)

# ------------差（相减剩下的）
print('差：',b-B)

# ------------对称差集（你有我没有和我有你没有的）
print('对称差集：',b^B)