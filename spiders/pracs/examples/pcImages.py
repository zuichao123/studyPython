#coding:utf-8
"""
    爬虫爬取指定页面的后缀为.jpg的图片
"""
import re
import urllib
import urllib.request

#获取页面的源代码
def getHtml(url):
    page = urllib.request.urlopen(url)#打开URL地址
    html = page.read()#读取页面源代码信息
    return html#返回信息

#下载图片
def getImg(html):
    reg = r'src="(.*?\.jpg)"'#src=...jpg的链接地址正则
    imgre = re.compile(reg)#将正则规则编译
    imglist = re.findall(imgre,html.decode('utf-8'))#从HTML中匹配正则
    #遍历匹配到的正则信息
    x = 0#定义变量给图片命名
    for imgurl in imglist:
        print(imgurl)
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)#py3的urlopen返回的不是string是bytes，需要将html中的html.decode('utf-8')
        x+=1


#爬取的页面URL地址
url = "http://www.win4000.com/meinvtag59_1.html"
html = getHtml(url)#获取该地址的所有源代码
getImg(html)
#打印匹配正则的地址；并下载图片