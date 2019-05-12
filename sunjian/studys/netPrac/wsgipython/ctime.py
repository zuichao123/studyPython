#coding:utf-8
'''
    动态显示的文件
'''

import time

def application(env, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type","text/plain")
    ]
    start_response(status, headers)
    return time.ctime()