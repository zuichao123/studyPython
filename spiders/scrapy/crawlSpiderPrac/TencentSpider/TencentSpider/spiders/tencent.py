# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
# 导入链接规则匹配类，用来提取符合规则的链接
from scrapy.linkextractors import LinkExtractor
from spiders.scrapy.crawlSpiderPrac.TencentSpider.TencentSpider.items import TencentspiderItem

class TencentSpider(CrawlSpider):
    name = 'tencent2'
    allowed_domains = ['hr.tencent.com']
    start_urls = ["http://hr.tencent.com/position.php?&start=0#a"]

    # Response里链接的提取规则，返回的符合匹配规则的链接对象的列表
    pagelink = LinkExtractor(allow=("start=\d+"))

    rules = [
        # 获取这个列表中的链接，依次发送请求，并且继续跟进，调用指定回调函数处理
        Rule(pagelink, callback="parseTencent", follow=True)
    ]

    # 指定的回调函数
    def parseTencent(self, response):
        # evenlist = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        # oddlist = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        # fulllist = evenlist + oddlist
        # for each in fulllist:
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentspiderItem()
            # 职位名称
            item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详情连接
            item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            # 招聘人数
            item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            yield item
