# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YouyuanspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 用户名
    username = scrapy.Field()
    # 年龄
    age = scrapy.Field()
    # 头像图片的链接
    header_url = scrapy.Field()
    # 相册图片的链接
    image_url = scrapy.Field()
    # 内心独白
    content = scrapy.Field()
    # 籍贯
    place_from = scrapy.Field()
    # 学历/婚姻、身高、月薪等
    education = scrapy.Field()
    # 兴趣爱好
    hobby = scrapy.Field()
    # 个人主页
    source_url = scrapy.Field()
