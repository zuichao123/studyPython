# coding:utf-8
"""
    Mysql测试类
"""
from sunjian.studys.database.mysql.mysqlHelps import MysqlHelps

id = input("请输入编号")
# name = input("请输入姓名")
# gender = input("请输入性别")
# age = input("请输入年龄")
# email = input("请输入邮箱")
# city = input("请输入住址")

sqlhelp = MysqlHelps('localhost','sunjian','root','root')

# 更新
# sqlUpdate = 'update user set name=%s where id=%s'
# params=[name,id]
# result = sqlhelp.update(sqlUpdate,params)
# print(result)

# 插入
# sqlInsert = 'insert into user(id,name,gender,age,email,city)values(%s,%s,%s,%s,%s,%s)'
# params=[id,name,gender,age,email,city]
# result = sqlhelp.update(sqlInsert,params)
# print(result)

# 删除
sqlDelete = 'delete from user where id =%s'
params=[id]
result = sqlhelp.update(sqlDelete,params)
print(result)

# 查询
sqlSelect = 'select * from user'
results = sqlhelp.select(sqlSelect,None)
print('results-->',results)