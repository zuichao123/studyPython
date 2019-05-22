# coding:utf-8
"""
    mongodb练习
"""
import pymongo as pm

# 建立连接并创建客户端
# 无安全认证
client = pm.MongoClient('localhost',27017)
# 有安全认证
# client = MongoClient('mongodb://root:root@localhost:27017/sunjian')
# 切换数据库
db = client.sunjian
# 获取集合
stb = db.stb

# 插入数据
# stb.insert_one({'name':'sunjian2'})

# 修改
# stb.update_one({'name':'sunjian2'},{'$set':{'name':'sunjian3'}})

# 删除
# stb.delete_one({'name':'sunjian3'})

# 获取数据信息
datas = stb.find()

# 输出信息
for data in datas:
    print(data['name'])