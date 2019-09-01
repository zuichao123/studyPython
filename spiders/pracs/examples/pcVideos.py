# -*- coding:utf-8 -*-
"""
    爬取视频练习
"""
import os
import urllib
import urllib.request
import re

def get_video(url):
    """下载视频"""
    ua_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    }
    req = urllib.request.Request(url, headers=ua_headers)
    html = urllib.request.urlopen(req).read()
    print(html)
    req = r'src="(.*?)"' # r代表原生字符串，不会转义

    for i in re.findall(req, str(html)):
        if re.findall("/sv/\d+",i):
            i = 'http:'+i
            print(i)
            filename = i.split("/")[-1]
            print('正在下载%s'%filename)
            # urllib.request.urlretrieve(i, currentDesktopPath() + '\\vedios\\%s.mp4'%filename)
            urllib.request.urlretrieve(i, currentDesktopPath() + "\\video\\" + filename + ".swf")

def currentDesktopPath():
    # 作用：获取当前桌面路径
    return os.path.join(os.path.expanduser("~"), 'Desktop')

if __name__ == "__main__":
    if not os.path.exists(currentDesktopPath()+"\\video"):
        os.mkdir(currentDesktopPath()+ "\\video")

    # get_video('http://www.yy.com/sv/')
    get_video('https://www.bilibili.com/video/av63220537/?p=3')

    src = "blob:https://www.bilibili.com/9cfee07e-9d8b-4464-b2f6-036f19ac06de"