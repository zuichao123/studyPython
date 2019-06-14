# -*- coding: utf-8 -*-
import scrapy

from spiders.scrapy.spiderPrac.doubanSpider.doubanSpider.items import DoubanspiderItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    url = "https://movie.douban.com/top250?start="

    offset = 0
    start_urls = [
        url + str(offset),
    ]

    def parse(self, response):
        item = DoubanspiderItem()
        movies = response.xpath("//div[@class='info']")

        for each in movies:
            # 标题
            item['title'] = each.xpath(".//span[@class='title'][1]/text()").extract()[0]
            # 信息
            item['bd'] = each.xpath(".//div[@class='bd']/p/text()").extract()[0]
            # 评分
            item['star'] = each.xpath(".//div[@class='star']/span[@class='rating_num']/text()").extract()[0]
            # 简介
            quote = each.xpath(".//p[@class='quote']/span/text()").extract()
            if len(quote) != 0:
                item['quote'] = quote[0]
            yield item

        if self.offset < 225:
            self.offset += 25
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
