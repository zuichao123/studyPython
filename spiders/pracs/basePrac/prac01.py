# coding:utf-8
import urllib.request

# User-Agent 是反爬虫和爬虫的第一步
ua_headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
}

# 通过urllib.request.Request()方法构造一个请求对象
request = urllib.request.Request("http://www.baidu.com/", headers=ua_headers)

# 向指定的URL地址发送请求，并返回服务器响应的类文件对象
response = urllib.request.urlopen(request)

# 服务器返回的类文件对象支持Python文件对象的操作方法
# read()方法就是读取文件里的全部内容，返回字符串
html = response.read()

# 打印响应内容
print(html)

# 返回HTTP的响应码
print(response.getcode())

# 返回实际数据的实际URL，防止重定向问题
print(response.geturl())

# 返回服务器响应的http报头
print(response.info())

