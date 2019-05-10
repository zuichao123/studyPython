# -*- coding: utf-8 -*-
'''
    C:\Software\pycharm\workspace\sunjian\paChong>scrapy genspider jobbole blog.jobbole.com
    Created spiders 'jobbole' using template 'basic'

    C:\Software\pycharm\workspace>scrapy startproject ArticleSpider
'''
import scrapy

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'

    # allowed_domains = ['blog.jobbole.com']
    # start_urls = ['http://group.jobbole.com/33695/#comm-93459']
    # def parse(self, response):
    #     for i in range(1,20):
    #         re_selector = response.xpath("//li[@id='comment-93459']//div[contains(@class,'cmnt-body')]//p["+str(i)+"]/text()")
    #         re_contents = re_selector.extract()
    #         if (len(re_contents) > 0):
    #             print(re_contents[0])
    #         i+=1
    #     pass


    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://python.jobbole.com/89290/']
    def parse(self,response):
        re_selectors = response.xpath("//div[@class='entry']//p")
        for i in range(1,len(re_selectors)):
            re_selector = response.xpath("//div[@class='entry']//p["+str(i)+"]/text()")
            if(len(re_selector) > 0):
                content = re_selector.extract()[0]
                content = content.replace("。",'\n')
                print(content)
        pass