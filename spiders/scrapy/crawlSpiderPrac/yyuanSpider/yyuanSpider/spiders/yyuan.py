# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import YouyuanspiderItem

class YyuanSpider(CrawlSpider):
    name = 'yyuan2'
    allowed_domains = ['uy99.com']
    start_urls = [
        'http://www.uy99.com/search/index.aspx?key=2_20_30_-1_0_-1_-1_-1_-1_-1_0_-1_110000_-1_-1_-1_-1_1_-1_-1_-1_-1_-1_-1_-1&p=1'
    ]

    # 第一级规则匹配
    page_links = LinkExtractor(allow=(r'p=\d+'))

    # 第二季规则匹配
    profile_links = LinkExtractor(allow=(r'www.uy99.com/u/\d+/$'))

    rules = (
        Rule(page_links),
        Rule(profile_links, callback="parse_item"),
    )


    def parse_item(self, response):
        item = YouyuanspiderItem()
        item["username"] = self.get_username(response)
        # 年龄
        item["age"] = self.get_age(response)
        # 头像图片的链接
        item["header_url"] = self.get_header_url(response)
        # 相册图片的链接
        # item["image_url"] = self.get_image_url(response)
        # 内心独白
        item["content"] = self.get_content(response)
        # 籍贯
        item["place_from"] = self.get_place_from(response)
        # 学历
        item["education"] = self.get_education(response)
        # 　兴趣爱好
        item["hobby"] = self.get_hobby(response)
        # 个人主页
        item["source_url"] = response.url
        # 数据来源网站
        # item["sourec"] = "youyuan"

        yield item

    def get_username(self, response):
        username = response.xpath("//div[@class='uname_girl']/text()").extract()
        if len(username):
            username = username[0]
        else:
            username = "NULL"
        return username.strip()

    def get_age(self, response):
        age = response.xpath("//div[@id='pbody']//div[@class='baseinfo']//div[@class='ubase']/text()").extract()
        if len(age):
            age = re.findall(u"\d+岁", age[0])[0]
        else:
            age = "NULL"
        return age.strip()

    def get_header_url(self, response):
        header_url = response.xpath("//div[@id='pbody']//div[@class='baseinfo']//img/@src").extract()
        if len(header_url):
            header_url = header_url[0]
        else:
            header_url = "NULL"
        return header_url.strip()

    def get_image_url(self, response):
        images_url = response.xpath("//div[@id='pbody']//div[@class='uinfonav']//li[2]/a/text()").extract()
        if len(images_url):
            images_url = images_url
        else:
            images_url = "NULL"
        return images_url

    def get_content(self, response):
        content = response.xpath("//div[@id='pbody']//div[@class='moreinfo'][1]/div/text()").extract()
        if len(content):
            content = content[0]
        else:
            content = "NULL"
        return content.strip()

    def get_place_from(self, response):
        place_from = response.xpath(
            "//div[@id='pbody']//div[@class='baseinfo']//div[@class='ubase']/a/text()").extract()
        if len(place_from):
            place_from = "".join(place_from)
        else:
            place_from = "NULL"
        return place_from.strip()

    def get_education(self, response):
        education = response.xpath("//div[@id='pbody']//div[@class='baseinfo']//ul/li/text()").extract()
        if len(education):
            education = "".join(education)
        else:
            education = "NULL"
        return education.strip()

    def get_hobby(self, response):
        hobby = response.xpath("//div[@id='pbody']//div[@class='moreinfo'][3]/p/text()").extract()
        if len(hobby):
            hobby = ",".join(hobby).replace(" ", "")
        else:
            hobby = "NULL"
        return hobby.strip()
