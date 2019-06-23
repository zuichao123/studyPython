# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianspiderItem(scrapy.Item):
    # define the fields for your item here like:
    zhiweimingcheng = scrapy.Field() # 职位名称
    xinzifanwei = scrapy.Field() # 薪资范围
    zuobiao = scrapy.Field() # 坐标
    gongzuonianxian = scrapy.Field() # 工作年限
    xueliyaoqiu = scrapy.Field() # 学历要求
    fulidaiyu = scrapy.Field() # 福利待遇
    gongsimingcheng = scrapy.Field() # 公司名称
    gongsixingzhi = scrapy.Field() # 公司性质
    gongsiguimo = scrapy.Field() # 公司规模
    gangweizhize = scrapy.Field() # 岗位职责
    jinengyaoqiu = scrapy.Field() # 技能要求
