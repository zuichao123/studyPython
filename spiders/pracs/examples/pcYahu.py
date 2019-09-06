#conding:utf-8
'''
    爬取虎牙直播网站的主播排行

    爬虫前奏：
        1.明确目的
        2.找到数据对应的网页
        3.分析网页的结构找到数据所在的标签位置

        4.模拟HTTP请求，向服务器发送这个请求，获取服务器返回给我们的HTML
        5.用正则表达式提取我们要的数据...

        Beautiful Soup
        Scrapy 爬虫框架
'''
from urllib import request
import re

class Spider():
    '''定义爬虫类'''
    __url = "https://www.huya.com/l"#定义一个私有的变量，存放爬取的URL地址
    root_pattern = '<li class="game-live-item"([\s\S]*?)</li>'#爬取的内容HTML正则
    name_pattern = '<i class="nick" ([\s\S]*?)</i>'#爬取的具体匹配正则1（主播名字）
    number_pattern = '<i class="js-num">([\s\S]*?)</i>'#爬取的具体匹配正则2（粉丝数量）

    real_name_pattern = '="([\s\S]*)">'#主播名字截取正则

    def __fetch_content(self):
        '''定义一个获取内容的私有函数'''
        r = request.urlopen(Spider.__url)#获取URL页面的内容
        htmls = r.read()#读取内容，存放到变量htmls
        htmls = str(htmls, encoding='utf-8').encode("utf-8")#将内容转换为字符串，并设置编码格式
        #print(htmls)
        return htmls#返回转换后的内容

    def analyze(self, html):
        '''定义一个公有的分析函数'''
        anchors = []#定义一个列表存放字典
        root_html = re.findall(Spider.root_pattern,html.decode("utf-8"))#获取爬取的正则匹配后的内容
        for html in root_html:#遍历内容
            names = re.findall(Spider.name_pattern,html)#获取主播名字
            numbers = re.findall(Spider.number_pattern,html)#获取粉丝量
            anchor = {'name':names,'number':numbers}#将获取的内容以字典的形式存入变量anchor
            anchors.append(anchor)#将变量添加到列表中
        return anchors#返回存放主播名、粉丝量的字典

    def __refine(self,anchors):
        '''
            定义一个私有函数
            作用是：将获取的内容提纯
        '''
        #使用lambda函数，获取字典中name和number
        l = lambda anchor:{
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0]
        }
        return map(l,anchors)#返回

    def __sort(self,anchors):
        '''定义一个私有的排序函数，将爬取的内容排序'''

        #使用python内置的函数sorted
        anchors = sorted(anchors,key=self.__sort_seed,reverse=True)#使用种子排序法；反转排序
        return anchors#返回排序后的内容

    def __sort_seed(self,anchor):
        '''定义一个私有的种子排序法'''
        r = re.findall('\d*',anchor['number'])#对number精准正则
        number = float(r[0])#将精准后的正则转换为float型
        if '万' in anchor['number']:#判断如果包含万
            number *= 10000#转换为数字
        return number#返回转换后的数字

    def __show(self,anchors):
        '''定义一个私有的显示函数'''
        for rank in range(0,len(anchors)):#使用python内置的range排列函数对列表遍历
            real_name = str(anchors[rank]['name'])#获取列表中的name
            real_names = re.findall(Spider.real_name_pattern,real_name)#再次精准匹配
            #由于返回的是列表形式，所以获取0
            name = real_names[0]
            number = anchors[rank]['number']#获取number
            print(str(rank + 1)+ ' : '+name+ '    '+number)#控制台输出

    def go(self):
        '''定义一个公有的函数：相当于主运行函数'''
        html = self.__fetch_content()
        # print(html)
        anchors = self.analyze(html)
        # print(anchors)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)

#定义一个类对象
spider = Spider()
#调用喽
spider.go()