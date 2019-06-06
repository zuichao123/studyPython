#coding:utf-8
'''
正则表达式练习：
    []里边的字符是或关系。
    ()表示组，里边的字符是与关系。

    .   匹配换行符\n之外的所有字符
    \d  数字
    \D  非数字
    +   前一个字符至少出现一次（可以出现多次）
    *   前一个字符可以出现0次或多次
    $   结尾
    ^   开头
    \b  匹配一个单词的边界
    \B  匹配非单词边界
    ?   前一个字符可有可无（匹配0次或1次）【非贪婪操作符】
    []  括号中的任意字符
    {3} 前一个字符字符个数为3个
    {3,}    前一个字符个数至少为3个
    {3,4}   前一个字符出现3或4个
    \w  单词字符（不能匹配非单词字符&等）
    \W  非单词字符（如空格、&、……等）
    \s  空白字符（回车、制表、\r、\n、\t等）
    \S  非空白字符

    (ab)  将括号中字符作为一个分组
    \num    引用分组num匹配到的字符串(就是说，引用当前正则中的前边的分组结果。如：r"(.*)sf(.+)\2asdf\1" --> \2引用第二个括号)
    (?p<name>)  分组起别名
    (?P=name)   引用别名为name分组匹配到的字符串

    group() 获取匹配成后的分组【参数：0表示所有 1表示第一组 2表示第二组 ...】

    注意：字符串前边加上r表示原始字符串（如：r"\n\w\swoshiyuanshide"）可以忽略转义

    ex:
        email:
            re_p = r"(\w+)@(163|126|gmail|qq|irisking)\.(com|cn|net)$"
            str = "sunjian@irisking.com"
            result = re.match(re_p, str)
            result.group() # sunjian@irisking.com
            result.group(1) # sunjian
            result.group(2) # irisking
            result.group(3) # com


查找：
    re.findall(pattern,string,flags) # 返回所有匹配的，返回列表
        pattern:  正则模式
        string:   字符
        flags:
            re.I  忽略pattern大小写
            re.S  改变pattern中.的行为作用
        eg:
            laguage = 'PythonC#\nJavaPHP'
            result = re.findall('c#.{1}',lanuage,re.I | re.S)
            print(result)

    re.match() # 返回第一个（找到第一个就不往后找了；从起始位置开始往后查找）
        eg:
            # match匹配（字符串第一个必须是正则要求的，返回第一个搜索到的）
            laguage = '2330494'
            result2 = re.match('\d',laguage)
            print('match:',result2.span()) #span() 返回位置


    re.search() # 返回第一个（找到第一个就不往后找了；从任何位置开始往后查找；详见下边的实例）
        eg:
            # search匹配（搜索匹配，返回第一个搜索到的）
            laguage = '玩儿2330494'
            result2 = re.search('\d',laguage)
            print('match:',result2.group()) # 返回字符

替换：
    way1、
        re.sub(pattern,repl,string,count=0,flags=0)
            pattern:    正则
            repl:       替换后的字符串
            string:     原始字符串
            count:      默认参数0（0表示替换的字符串无限制的替换；1表示只替换第一个匹配正则的字符）

            eg:
                laguage = 'PythonC#\nJavaPHPC#'
                result = re.sub('C#','Go',laguage,0)
                print(result)

            eg2:把函数作为参数传递
                s = 'ABC123456789WER'
                    # 把字符串s中，大于等于5的数字替换为9；小于5的替换为0
                def convert(value):
                    matched = value.group()
                    if int(matched) >= 5:
                        return '9'
                    else:
                        return '0'

                r = re.sub('\d',convert,s)#convert函数的返回值，替换‘\d’匹配到的s字符串中的数字
                print(r)

    way2、
        lanuage.replace(old,new,count)
            old:    替换前的字符
            new:    替换后的字符
            count:  默认参数0（0表示替换的字符串无限制的替换；1表示只替换第一个匹配正则的字符）
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

#忽略大小写，并且改变换行符的行为
laguage = 'PythonC#\nJavaPHP'
result = re.findall('c#.{1}', laguage, re.I | re.S)
print(result)

#match匹配（字符串第一个必须是正则要求的，返回第一个搜索到的）
laguage = '2330494'
result2 = re.match('\d',laguage)
print('match:',result2.span())#span()返回位置

#search匹配（搜索匹配，返回第一个搜索到的）
laguage = '玩儿2330494'
result2 = re.search('\d',laguage)
print('match:',result2.group()) # 返回字符

# 替换1
laguage = "qweqweqweeeeerrrr"
result = laguage.replace("qwe",'yyyy',0)
print(result)
# 替换2
laguage = 'PythonC#\nJavaPHPC#'
result = re.sub('C#', 'Go', laguage, 0)
print(result)
# 替换3
    # 把函数作为参数传递
s = 'ABC123456789WER'
# 把字符串s中，大于等于5的数字替换为9；小于5的替换为0
def convert(value):
    matched = value.group()
    if int(matched) >= 5:
        return '9'
    else:
        return '0'

r = re.sub('\d',convert,s) # convert函数的返回值，替换‘\d’匹配到的s字符串中的数字
print(r)

print('---------------------group()函数详解---------------------------------------------')
sj = '234234fasdf234234234asd78923faf'
r = re.match('\d',sj)

# 返回字符串的位置
print(r.span())
# 返回字符串
    # 分组可以有多个
print(r.group())

sj2 = 'life is short, i use python. I love python'
r = re.search('life(.*)python(.*)python',sj2)
print(r.group(0,1,2)) # 返回每个组的完整
print(r.groups()) # 返回每个组的实际
print(r.group()) # 返回实际匹配的所有

print("----"*16,'经典例子')
s = "http://www.baidu.com/messagfin.asp?id=77"
'''将.com/后边的字符替换为空'''
# 思路：使用sub函数；先将所有的匹配出来；将较容易的部分先匹配出来；使用lambda表达式将较容易的部分返回
result = re.sub(r"(http://.+?/).*", lambda x:x.group(1), s)
print(result)