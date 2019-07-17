#coding:utf-8
"""
    爬虫爬取指定页面的图片
"""
import re
import urllib
import urllib.request

from urllib.parse import quote

class PcImage(object):

    # 获取网页源代码
    def getHtml(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }
        request = urllib.request.Request(url, headers=headers) # 打开URL地址
        page = urllib.request.urlopen(request, timeout=10) # 请求页面返回页面对象
        html = page.read() # 读取页面源代码信息
        return html # 返回信息

    # 下载图片
    def getImg(self, html, reg, path):
        imgre = re.compile(reg) # 将正则规则编译
        imglist = re.findall(imgre,html.decode('utf-8')) # 从HTML中匹配正则
        # imglist = re.findall(imgre,str(html)) # 从HTML中匹配正则

        x = 48 # 定义变量给图片命名
        for imgurl in imglist: # 遍历匹配到的正则信息
            imgurl = quote(imgurl,safe='/:?=') # 处理URL中包含中文
            print('----------->>' + imgurl)
            urllib.request.urlretrieve(imgurl, path+'%s.jpg' %x) # py3的urlopen返回的不是string是bytes，需要将html中的html.decode('utf-8')
            x+=1

    # 练习URL中有中文
    def prac1(self):
        from urllib.parse import quote
        url='http://www.example.com/api.php?text=中文在这里'
        # 不带附加参数
        print('\n不带附加参数：\n%s'%quote(url))
        # 附带不转换字符参数
        print('\n附加不转换字符参数：\n%s'%quote(url,safe='/:?='))

    # 练习爬取指定URL的image
    def prac2(self):
        imgurl = "images/denglu/u283_state0.png"
        imgurl = "https://axhub.im/pro/84103267b2434f03/"+imgurl
        imgurl = quote(imgurl,safe='/:?=')
        print('----------->>' + imgurl)
        urllib.request.urlretrieve(imgurl, 'C:\\Users\\sunjian\\Desktop\\Zbpl\\Data\\image\\s.jpg')#py3的urlopen返回的不是string是bytes，需要将html中的html.decode('utf-8')

    # start..
    def main(self):
        url = "http://www.win4000.com/meinvtag59_1.html"
        reg = r'src="(.*?\.jpg)"'

        # url = "https://axhub.im/pro/84103267b2434f03/denglu.html"
        # reg = r'class="img " src="(.*?\.png)"'

        savePath = 'C:\\Users\\sunjian\\Desktop\\Zbpl\\Data\\image\\'

        html = self.getHtml(url)
        self.getImg(html, reg, savePath)


if __name__ == '__main__':
    pcImage = PcImage()
    pcImage.main()


