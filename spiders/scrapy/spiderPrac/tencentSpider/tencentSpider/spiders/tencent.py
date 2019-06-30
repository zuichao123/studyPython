# coding:utf-8
"""

"""
import scrapy

from spiders.scrapy.spiderPrac.tencentSpider import TencentspiderItem


class TencentpositionSpider(scrapy.Spider):
    name = "tencent"
    # allowed_domains = ["tencent.com"]
    allowed_domains = ["tencent.com"]

    url = "http://hr.tencent.com/search.html?index="
    offset = 2

    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath("//a[@class='recruit-list-link']"):
            # 初始化模型对象
            item = TencentspiderItem()

            item['positionname'] = each.xpath("./h4/text()").extract()[0]
            print('--'*33)
            print(each.xpath("./h4/text()").extract()[0])
            # 详情连接
            # item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            item['positionType'] = each.xpath(".//p[1]/span[3]/text()").extract()[0]
            # 招聘人数
            # item['peopleNum'] =  each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['workLocation'] = each.xpath(".//p[1]/span[2]/text()").extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath(".//p[1]/span[4]/text()").extract()[0]

            yield item

        if self.offset < 168:
            self.offset += 10

        # 每次处理完一页的数据之后，重新发送下一页页面请求
        # self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
        yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
