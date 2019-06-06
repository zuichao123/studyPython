# coding:utf-8
from urllib import request

import ssl
import urllib

context = ssl._create_unverified_context()

url = "https://www.12306.cn/mormhweb/"
#url = "https://www.baidu.com/"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    }
request = request.Request(url, headers = headers)

# 添加到context参数里
response = urllib.request.urlopen(request, context = context)

print (response.read())