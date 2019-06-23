# -*- coding: utf-8 -*-
import re

import scrapy
from selenium import webdriver
from ..items import ZhilianspiderItem

class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['jobs.zhaopin.com']
    url = "https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B5%8B%E8%AF%95%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&at=051d5b568a734e1d99e4fe5e8adad171&rt=7161a116b728486ead66d2312f74ed87&_v=0.66243185&userCode=712467738&x-zp-page-request-id=16ffe1cf130b47468c188bab6fc14744-1561276964595-774936&x-zp-client-id=3ee57aab-fed5-4db0-84fa-bc8daaec87d0"

    # offset = 0
    # start_urls = [url + str(offset)]
    start_urls = [
        url
    ]

    def parse(self, response):
        html_contents = str(response.body)
        r = r'positionURL":"(.*?\.htm)","companyLogo'
        urls = re.findall(r, html_contents)

        if urls:
            for url in urls:
                print('开始请求------------------>>>'+url)
                yield scrapy.Request(url, callback=self.parse_item)
        else:
            print('xiongdi meiyou zhaodao url')

    def parse_item(self, response):
        # 提取列表中的每个职位的信息
        item = ZhilianspiderItem()
        # 职位名称
        item['zhiweimingcheng'] = response.xpath("//div[@class='job-summary']//h3/text()").extract().strip()
        # 薪资范围
        item['xinzifanwei'] = response.xpath("//div[@class='job-summary']//div[@class='summary-plane__left']/span/text()").extract().strip()
        # 坐标
        zuobiao = response.xpath("//div[@class='job-summary']//div[@class='summary-plane__left']/ul/li/a/text()").extract().strip()
        zuobiao2 = response.xpath("//div[@class='job-summary']//div[@class='summary-plane__left']/ul/li/span/text()").extract().strip()
        item['zuobiao'] = zuobiao + zuobiao2
        # 工作年限
        item['gongzuonianxian'] = response.xpath("//div[@class='job-summary']//div[@class='summary-plane__left']/ul/li[2]/text()").extract().strip()
        # 学历要求
        item['xueliyaoqiu'] = response.xpath("//div[@class='job-summary']//div[@class='summary-plane__left']/ul/li[3]/text()").extract().strip()
        # 福利待遇
        fulidaiyus = response.xpath("//div[@class='a-center-layout__content']//div[@class='highlights__content']/span/text()").extract()
        item['fulidaiyu'] = "".join(fulidaiyus).strip()
        # 公司名称
        item['gongsimingcheng'] = response.xpath("//div[@class='a-center-layout__content']//div[@class='app-main__right']//div[@class='company']/a/text()").extract().strip()
        # 公司性质
        item['gongsixingzhi'] = response.xpath("//div[@class='a-center-layout__content']//div[@class='app-main__right']//div[@class='company']//button[@class='company__industry']/text()").extract().strip()
        # 公司规模
        item['gongsiguimo'] = response.xpath("//div[@class='a-center-layout__content']//div[@class='app-main__right']//div[@class='company']//button[@class='company__size']/text()").extract().strip()
        # 岗位职责
        gangweizhize =  response.xpath("//div[@class='a-center-layout__content']//div[@class='app-main__left']//div[@class='describtion__detail-content']//p/text()").extract()
        item['gangweizhize'] = "".join(gangweizhize).strip()
        # 技能要求
        jinengyaoqiu = response.xpath("//div[@class='a-center-layout__content']//div[@class='app-main__left']//div[@class='describtion__skills']//span/text()").extract()
        item['jinengyaoqiu'] = "".join(jinengyaoqiu).strip()

        yield item


    # def parse_item(self, response):
    #     # 每页所有的职位集合
    #     links = response.xpath("//div[@id='listContent']/div").extract()
    #     # 迭代取出集合中的链接
    #     for link in links:
    #         # 提取列表中的每个职位的信息
    #         item = ZhilianspiderItem()
    #         # 职位名称
    #         item['zhiweimingcheng'] = response.xpath(".//div[contains(@class,'contentpile__content__wrapper__item__info__box__jobname jobName')]/span[1]/text()").extract().strip()
    #         # 薪资范围
    #         item['xinzifanwei'] = response.xpath(".//div[contains(@class,'contentpile__content__wrapper__item__info__box__job jobDesc')]/p/text()").extract().strip()
    #         # 坐标
    #         item['zuobiao'] = response.xpath(".//div[contains(@class,'contentpile__content__wrapper__item__info__box__job jobDesc')]/ul/li[1]/text()").extract().strip()
    #         # 工作年限
    #         item['gongzuonianxian'] = response.xpath(".//div[contains(@class,'contentpile__content__wrapper__item__info__box__job jobDesc')]/ul/li[2]/text()").extract().strip()
    #         # 学历要求
    #         item['学历要求'] = response.xpath(".//div[contains(@class,'contentpile__content__wrapper__item__info__box__job jobDesc')]/ul/li[3]/text()").extract().strip()
    #         # 福利待遇
    #         fulidaiyus = response.xpath(".//div[contains(@class,'contentpile__content__wrapper__item__info__box itemBox')]/div/div").extract()
    #         item['fulidaiyu'] = "".join(fulidaiyus).strip()
    #         # 公司名称
    #         item['gongsimingcheng'] = response.xpath(".//div[contains(@class,'commpanyName')]/a/text()").extract().strip()
    #         # 公司性质
    #         item['gongsixingzhi'] = response.xpath("//div[contains(@class,'contentpile__content__wrapper__item__info__box__job__comdec')]/span[1]/text()").extract().strip()
    #         # 公司规模
    #         item['gongsiguimo'] = response.xpath("//div[contains(@class,'contentpile__content__wrapper__item__info__box__job__comdec')]/span[2]/text()").extract().strip()
    #
    #         yield item
