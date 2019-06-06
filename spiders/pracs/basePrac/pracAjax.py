# coding:utf-8
"""
    抓取Ajax的数据
"""
from urllib import parse,request
import urllib

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

formdata = {
        "start":"0",
        "limit":"20"
    }

data = urllib.parse.urlencode(formdata).encode(encoding='utf8')

request = request.Request(url, data = data, headers = headers)

print (urllib.request.urlopen(request).read())

