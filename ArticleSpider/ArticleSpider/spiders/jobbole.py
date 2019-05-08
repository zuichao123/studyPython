# -*- coding: utf-8 -*-
'''
C:\Software\pycharm\workspace\sunjian\paChong>scrapy genspider jobbole blog.jobbole.com
Created spider 'jobbole' using template 'basic'

C:\Software\pycharm\workspace>scrapy startproject ArticleSpider
'''
import scrapy

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    # allowed_domains = ['blog.jobbole.com']
    allowed_domains = ['http://group.jobbole.com/33695/#comm-93459']
    start_urls = ['http://blog.jobbole.com/']

    def parse(self, response):
        re_selector = response.xpath("//li[@id='comment-93459']//div[contains(@class,'cmnt-body')]//p[3]")
        print(re_selector)

t = JobboleSpider()

t.parse()