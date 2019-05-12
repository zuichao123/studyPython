# -*- coding: utf-8 -*-
'''
    C:\Software\pycharm\workspace\sunjian\paChong>scrapy genspider jobbole blog.jobbole.com
    Created spiders 'jobbole' using template 'basic'

    C:\Software\pycharm\workspace>scrapy startproject ArticleSpider
'''
import scrapy
import re
from scrapy.http import request
from urllib import parse

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'

    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://book.zongheng.com/showchapter/697313.html']

    def parse(self, response):
        post_urls = response.xpath("//ul[contains(@class,'chapter-list')]//li/a").extract()
        re_part = 'href="([\s\S]*\.html)"'
        for post_url in post_urls:
            post_url = re.findall(re_part,post_url)
            yield scrapy.Request(url=post_url[0],callback=self.parse_detail,dont_filter=True)

    def parse_detail(self,response):
        title = response.xpath("//div[@class='title_txtbox']/text()")
        print('-------------------',title.extract())
        contents = response.xpath("//div[@class='content']//p/text()")
        for content in contents:
            print(content.extract())
        pass

