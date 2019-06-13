# -*- coding: utf-8 -*-
import scrapy

from spiders.scrapy.spiderPrac.dongguanSpider.dongguanSpider.items import DongguanspiderItem


class DongguanSpider(scrapy.Spider):

    name = 'dongguan'
    allowed_domains = ['wz.sun0769.com']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='

    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        # 每页的帖子集合
        links = response.xpath("//div[@class=\"greyframe\"]//table[2]//a[2]/@href").extract()
        # 迭代取出集合里的链接
        for link in links:
            # 提取列表里每个帖子的链接，发送请求放到请求队列里,并调用self.parse_item来处理
            yield scrapy.Request(link, callback=self.parse_item)

        # 页面终止条件成立前，会一直自增offset的值，并发送新的页面请求，调用parse方法处理
        if self.offset <= 71160:
            self.offset += 30
            # 发送请求放到请求队列里，调用self.parse处理response
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    # 处理每个帖子的response内容
    def parse_item(self, response):
        item = DongguanspiderItem()

        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        item['title'] = response.xpath('//div[contains(@class, "wzy1")]//table[1]//span[1]/text()').extract()[
            0].strip()
        # 编号
        item['number'] = response.xpath('//div[contains(@class, "wzy1")]//table[1]//span[2]/text()').extract()[0].split(":")[-1]
        # 内容，先使用有图片情况下的匹配规则，如果有内容，返回所有内容的列表集合
        content = response.xpath('//div[@class="contentext"]/text()').extract()
        # 如果没有内容，则返回空列表，则使用无图片情况下的匹配规则
        if len(content) == 0:
            content = response.xpath('//div[contains(@class, "wzy1")]//table[2]//tr[1]/td/text()').extract()
            content = "".join(content).strip()  # 将列表转换成字符串
        else:
            content = "".join(content).strip()
        item['content'] = content
        # 链接
        item['url'] = response.url

        yield item
