#conding:utf-8
'''
爬虫前奏：
    1.明确目的
    2.找到数据对应的网页
    3.分析网页的结构找到数据所在的标签位置

    4.模拟HTTP请求，向服务器发送这个请求，获取服务器返回给我们的HTML
    5.用正则表达式提取我们要的数据...

    Beautiful Soup
'''
from urllib import request
import re

class Spider():
    __url = "https://www.huya.com/l"
    root_pattern = '<li class="game-live-item"([\s\S]*?)</li>'
    name_pattern = '<i class="nick" ([\s\S]*?)</i>'
    number_pattern = '<i class="js-num">([\s\S]*?)</i>'

    real_name_pattern = '="([\s\S]*)">'

    def __fetch_content(self):
        r = request.urlopen(Spider.__url)
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        # print(htmls)
        return htmls


    def analyze(self,html):
        anchors = []
        root_html = re.findall(Spider.root_pattern,html)
        for html in root_html:
            names = re.findall(Spider.name_pattern,html)
            numbers = re.findall(Spider.number_pattern,html)
            anchor = {'name':names,'number':numbers}
            anchors.append(anchor)
        return anchors

    def __refine(self,anchors):
        l = lambda anchor:{
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0]
        }
        return map(l,anchors)

    def __sort(self,anchors):
        anchors = sorted(anchors,key=self.__sort_seed,reverse=True)
        return anchors

    def __sort_seed(self,anchor):
        r = re.findall('\d*',anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __show(self,anchors):
        for rank in range(0,len(anchors)):
            real_name = str(anchors[rank]['name'])
            real_names = re.findall(Spider.real_name_pattern,real_name)

            name = real_names[0]
            number = anchors[rank]['number']
            print(str(rank + 1)+ ' : '+name+ '    '+number)

    def go(self):
        html = self.__fetch_content()
        anchors = self.analyze(html)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)


spider = Spider()
spider.go()
