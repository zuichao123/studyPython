# -*- coding: utf-8 -*-
import os

import scrapy

from spiders.scrapy.spiderPrac.sinaSpider import SinaspiderItem


class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ["sina.com.cn"]
    start_urls = [
        "http://news.sina.com.cn/guide/",
    ]

    def currentDesktopPath(self):
        # 作用：获取当前桌面路径
        return os.path.join(os.path.expanduser("~"), 'Desktop')

    def parse(self, response):
        items = []
        # 所有大类的URL和标题
        parentUrls = response.xpath("//div[@id='tab01']/div/h3/a/@href").extract()
        parentTitle = response.xpath("//div[@id='tab01']/div/h3/a/text()").extract()

        # 所有的小类的URL和标题
        subUrls = response.xpath("//div[@id='tab01']/div/ul/li/a/@href").extract()
        subTitle = response.xpath("//div[@id='tab01']/div/ul/li/a/text()").extract()

        # 爬取所有的大类
        for i in range(0, len(parentTitle)):
            # 指定大类目录的路径和目录名
            parentFilename = self.currentDesktopPath() + "/Data/" + parentTitle[i]
            # 如果目录不存在，则创建目录
            if(not os.path.exists(parentFilename)):
                os.makedirs(parentFilename)

            # 爬取所有小类
            for j in range(0, len(subUrls)):
                item = SinaspiderItem()

                # 保存大类的title和urls
                item['parentTitle'] = parentTitle[i]
                item['parentUrls'] = parentUrls[i]

                # 检查小类的url是否是以同类别大类URL开头，如果是返回True
                if_belong = subUrls[j].startswith(item['parentUrls'])

                # 如果属于本大类，将存储目录放在本大类目录下
                if(if_belong):
                    subFilename = parentFilename + "/" + subTitle[j]
                    # 如果不存在，则创建目录
                    if (not os.path.exists(subFilename)):
                        os.makedirs(subFilename)

                    # 存储小类URL、title和filename字段数据
                    item['subUrls'] = subUrls[j]
                    item['subTitle'] = subTitle[j]
                    item['subFilename'] = subFilename

                    items.append(item)

        # 发送每个小类URL的Request请求，得到Response连同包含meta数据，一同交给回调函数处理
        for item in items:
            yield scrapy.Request(url=item['subUrls'], meta={'meta_1':item}, callback=self.second_parse)

    # 对于返回的小类请求，再进行递归请求
    def second_parse(self,response):
        # 提取每次Response的meta数据
        meta_1 = response.meta['meta_1']

        # 取出小类里所有的子链接
        sonUrls = response.xpath('//a/@href').extract()

        items = []
        for i in range(0, len(sonUrls)):
            # 检查每个链接是否以大类URL开头，以.shtml结尾，如果是返回True
            if_belong = sonUrls[i].endswith('.shtml') and sonUrls[i].startswith(meta_1['parentUrls'])

            # 如果属于本大类，获取字段值放在同一个item下便于传输
            if(if_belong):
                item = SinaspiderItem()

                item['parentTitle'] = meta_1['parentTitle']
                item['parentUrls'] = meta_1['parentUrls']
                item['subTitle'] = meta_1['subTitle']
                item['subUrls'] = meta_1['subUrls']
                item['subFilename'] = meta_1['subFilename']
                item['sonUrls'] = sonUrls[i]

                items.append(item)

        # 发送每个小类子链接URL的Request请求，得到Response后连同包含meta数据一同交给回调函数处理
        for item in items:
            yield scrapy.Request(url=item['sonUrls'], meta={'meta_2':item}, callback=self.detail_parse)

     # 数据解析方法，获取文章标题和内容
    def detail_parse(self,response):
        item = response.meta['meta_2']
        content = ""
        head = response.xpath("//h1[@class='main-title']/text()").extract()
        if len(head) == 0:
            head = response.xpath("//div[@class='clearfix']/table/tbody//a[1]/text()").extract()

        content_list = response.xpath("//div[@id='artibody']/p/text()").extract()
        if len(content_list) == 0:
            content_list = response.xpath("//div[@class='clearfix']/table/tbody/tr[10]/td[2]/text()").extract()

        # 将p标签里的文本内容合并到一起
        # for content_one in content_list:
        #     content += content_one
        head = "".join(head)
        content = "".join(content_list)
        item['head'] = head
        item['content'] = content

        yield item

