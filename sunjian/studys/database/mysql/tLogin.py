# coding:utf-8
"""
    用户登录功能练习
"""
from sunjian.studys.database.mysql.mysqlHelps import MysqlHelps
from hashlib import sha1,md5

name = input("请输入用户名")
pwd = input("请输入密码")

# 对密码使用sha1加密
s = sha1()
# s = md5() # 使用md5加密
s.update(pwd)
pwd2 = s.hexdigest()

# 根据用户名查询密码
sqlhelp = MysqlHelps('localhost','sunjian','root','root')
sqlSelect = 'select passwd  from user2 where name=%s'
result = sqlhelp.select(sqlhelp,name)

# 验证
if len(result) == 0: # 如果查询结果为空
    print("用户名错误")
elif result[0][0] == pwd2: # 如果查询出来的密码等于输入的密码（加密后的）
    print('登录成功')
else:
    print('密码错误')