# coding:utf-8
"""
    redis学习
"""
import redis

r = redis.StrictRedis(host='127.0.0.1', port=6379)
r.set('foo', 'hello')
r.rpush('mylist', 'one')
print (r.get('foo'))
print (r.rpop('mylist'))