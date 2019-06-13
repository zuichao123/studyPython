# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from spiders.scrapy.crawlSpiderPrac.DongguanSpider.DongguanSpider.items import DongguanspiderItem


class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    rules = (
        # 每一页的请求
        Rule(LinkExtractor(allow=r'type=4&page=\d+')),
        # 每页中每个帖子的请求
        Rule(LinkExtractor(allow=r'/html/question/\d+/\d+.shtml'), callback='parse_item'),
    )
    # http://wz.sun0769.com/html/question/201906/416121.shtml
    def parse_item(self, response):
        item = DongguanspiderItem()

        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        item['title'] = response.xpath('//div[contains(@class, "wzy1")]//table[1]//span[1]/text()').extract()[0].strip()
        # 编号
        item['number'] = response.xpath('//div[contains(@class, "wzy1")]//table[1]//span[2]/text()').extract()[0].split(":")[-1]
        # 内容，先使用有图片情况下的匹配规则，如果有内容，返回所有内容的列表集合
        content = response.xpath('//div[@class="contentext"]/text()').extract()
        # 如果没有内容，则返回空列表，则使用无图片情况下的匹配规则
        if len(content) == 0:
            content = response.xpath('//div[contains(@class, "wzy1")]//table[2]//tr[1]/td/text()').extract()
            content = "".join(content).strip() # 将列表转换成字符串
        else:
            content = "".join(content).strip()
        item['content'] = content
        # 链接
        item['url'] = response.url

        yield item
