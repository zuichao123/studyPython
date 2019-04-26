#coding:utf-8
'''
    正则表达式练习
'''

import re

s='abc'
s=r'ab[ce]d'
print (re.findall(s,'aaabcaaaaaabedaaabcdaaa'))

s='hello world,hello boy'
r=r'^hello'#开头
r2=r'boy$'#结尾
print (re.findall(r2,s))

r='t[ab$]'#结尾
print (re.findall(r,'asdfsdtaatb'))

r='x[a-zA-Z0-9]e'
print (re.findall(r,'afadxEefeafdaxdesdfx3eadfdex'))

r=r"^010-\d{8}"
print (re.findall(r,"010-333333444338"))

r=r"ab*"
#b出现0-多次

r=r"ab+"
#b出现至少一次

r=r"^010-?\d{8}$"
#表示010-开头，其中-可有可无；结尾8个数字

r=r"^010-*\d{8}$"
#表示010-开头，其中-出现0或多次；结尾8个数字
print (re.findall(r,"010-12312456"))

r=r"^\d{3,4}-?\d{8}"#正则电话号码(开头3或4个数字，-可有可无；8个数字)
print (re.findall(r,"2034-324234234"))

p_tel=re.compile(r)#将电话正则编译
p_tel.match("3423")

rs=r's..s'#正则替换
print (re.sub(rs,'jack','swers s323423s sks sssss'))#根据定义的rs正则替换)

#正则切割
rr=r'[\+\-\*/]'
print (re.split(rr,'123+32-234*sdf/sfe'))