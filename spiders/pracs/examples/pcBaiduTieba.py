# coding:utf-8
"""
    爬取百度贴吧的HTML内容
"""
from urllib import request,parse
import urllib
import os

def loadPage(url, filename):
    """
        作用：根据URL发送请求，获取服务器响应文件
        :param url: 需要爬取的URL地址
        :filename: 处理的文件名
    """
    print("正在下载" + filename)
    ua_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    }
    request = urllib.request.Request(url, headers=ua_headers)
    return urllib.request.urlopen(request).read()

def writePage(html, filename):
    """
        作用：将HTML内容写入到本地
        :param html: 服务器相应文件内容
    """
    print("正在保存" + filename)
    # 文件写入
    with open(filename, 'bw') as f:
        f.write(html)
    print("-" * 33)

def tiebaSpider(url, beginPage, endPage):
    """
        作用：贴吧爬虫调度器，负责组合处理每个页面的URL
        :param url: 贴吧URL前部分
        :param beginPage: 起始页
        :param endPage: 结束页
    """
    beginPage = int(beginPage)
    endPage = int(endPage)
    for page in range(beginPage, endPage+1):
        pn = (page - 1) * 50
        filename = "第" + str(page) + "页.html"
        fullurl = url + "&pn=" + str(pn)
        # print(fullurl)
        html = loadPage(fullurl, filename)
        # print(html)
        writePage(html, getDesktopPath()+ "\\" + filename)

def getDesktopPath():
    """
        作用：获取当前桌面路径
    """
    return os.path.join(os.path.expanduser("~"), 'Desktop')


if __name__ == "__main__":
    kw = input("请输入要爬取的贴吧名：")
    beginPage = input("请输入起始页：")
    endPage = input("请输入结束页：")

    url = "http://tieba.baidu.com/f?"
    key = parse.urlencode({"kw":kw})
    fullurl = url + key
    tiebaSpider(url, beginPage, endPage)
