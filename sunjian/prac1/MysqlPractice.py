#coding:utf-8
"""
    练习MySQL操作
"""
import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root')#创建对象
cursor = conn.cursor()#创建游标

conn.select_db('sunjian')#选择sunjian这个数据库

sqlInsert = "insert into user(userName,password)value('sunjian99',323)"
sqlInsert2= "insert into user(userName,password)value(%s,%s)"#插入语句
#print cursor.execute(sqlInsert2,('sunjian3','3234'))#插入操作
#cursor.execute(sqlInsert2,[('3234',765),('s1',666),('k1',544)])#插入操作

#print cursor.execute("delete from user where id='18'")#删除操作

#print cursor.execute("update user set password = '33333' where userName='addUser'")#更新操作

sqlSelect = "select * from user"#查询语句
cursor.execute(sqlSelect)#执行查询操作
print (cursor.fetchone())#输出一个查询结果
print cursor.fetchmany(13)#查询输出所有
print cursor.fetchmany(cursor.execute(sqlSelect))#查询输出所有
