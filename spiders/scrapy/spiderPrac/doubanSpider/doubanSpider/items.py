# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanspiderItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field() # 标题
    bd = scrapy.Field() # 信息
    star = scrapy.Field() # 评分
    quote = scrapy.Field() # 简介
    pass
