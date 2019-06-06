# coding:utf-8
from urllib import request,parse
from urllib.request import urlopen

url = "http://www.baidu.com/s"
ua_headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
}

keyword = input("请输入需要查询的关键字：")
wd = {"wd":keyword}

fullurl = url + "?" + parse.urlencode(wd)

print(fullurl)
request = request.Request(url, headers=ua_headers)

response = urlopen(request)
print(response.read())