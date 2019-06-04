# coding:utf-8
"""
    抓取Ajax的数据
"""
from urllib import parse,request
import urllib

# 通过fiddler抓包获取URL地址和headers和formdata信息
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
ua_headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
}
key = input("请输入需要翻译的文字：")
# 表单数据
formdata = {
    "i":key,
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":"15596310197985",
    "sign":"8661edb943d1b5234c5e7e5e9e25479a",
    "ts":"1559631019798",
    "bv":"6f8ea7d9e1022bbfea406563f58b2705",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_REALTlME"
}

data = parse.urlencode(formdata).encode(encoding='utf8')
request = request.Request(url, data = data, headers=ua_headers)
print(urllib.request.urlopen(request).read())
