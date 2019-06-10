# coding:utf-8
"""
    爬取糗事
"""
import json
import urllib
from urllib import request

from lxml import etree

url = "http://www.qiushibaike.com/8hr/page/2/"
headers = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

request = request.Request(url, headers=headers)

html = urllib.request.urlopen(request).read()

# 响应返回的是字符串，解析为HTML DOM模式 text = etree.HTML(html)
text = etree.HTML(html)

node_list = text.xpath('//li[contains(@class, "item typs_video")]')

items = {}
for node in node_list:
    # xpath返回的列表，这个列表就这一个参数，用索引方式取出来，用户名
    # username = node.xpath('./div/a/@title')[0]
    # 图片连接
    image = node.xpath('./a/img/@src')#[0]
    # 取出标签下的内容,段子内容
    content = node.xpath('./div[@class="recmd-right"]/a')[0].text
    # 取出标签里包含的内容，点赞
    #zan = node.xpath('./div/div/span')[0].text
    # 评论
    # comments = node.xpath('.//i')[1].text

    items = {
        #"username" : username,
        "image" : image,
        "content" : content,
        #"zan" : zan,
        # "comments" : comments
    }
    print(image,'\n',content)
    print('-'*30)
    # with open("qiushi.json", "a") as f:
    #     f.write(json.dumps(items, ensure_ascii = False).encode("utf-8") + "\n")

