#coding:utf-8
'''
    json练习
'''
import json

json_str = '[{"name":"sunjian","age":31},{"name2":"sunjian","age2":31}]'

print('-------反序列化（由字符串到某一种数据格式）-----------------------')
student = json.loads(json_str)
print(type(student))
print(student)
print(student[0]['name'])
print(student[1])

print('--------序列化（由数据格式到字符串）---------')
student = [
            {'name':'sunjian','age':30,'flag':False},
            {'name':'zhibo','age':7}
          ]


json_str = json.dumps(student)
print(type(json_str))
print(json_str)