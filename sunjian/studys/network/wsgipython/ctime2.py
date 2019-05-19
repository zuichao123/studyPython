#coding:utf-8
'''
    动态显示的文件
'''

import time

def application(env, start_response):
    status = "404 Not Found"
    headers = [ ]
    start_response(status, headers)
    return "file not found!!!"