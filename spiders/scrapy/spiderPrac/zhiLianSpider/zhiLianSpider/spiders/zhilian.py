# -*- coding: utf-8 -*-
"""
    今天爬取这个智联的招聘信息，遇到个大坑
        1、明明在Chrome中使用xpath可以定位到元素，但是在scrapy shell 中却返回空的列表《搞了好久，才发现问题》
        2、原来是异步Ajax请求的
        3、所以只好浏览器中进入要爬取的页面中，打开F12--network--XHR--刷新当前页
        4、观察发现有一条是Ajax请求时返回的带json数据的，复制这条请求的URL地址
        5、在网页中打开，发现返回的正是要爬取的页面数据(但是时json格式的，所以只好使用正则将需要的请求地址匹配出来)
        6、yield scrapy.Request(url, callback=self.parse_item)使用回调函数实现了
        7、OK成功了,如下：

    {
        "gangweizhize": "",
        "gongsimingcheng": "贝壳找房(北京)科技有限公司",
        "xinzifanwei": "2万-3万",
        "fulidaiyu": "绩效奖金带薪年假弹性工作补充医疗保险",
        "gongzuonianxian": "3-5年",
        "gongsixingzhi": "互联网/电子商务,房地产/建筑/建材/工程",
        "xueliyaoqiu": "本科",
        "gongsiguimo": "1000-9999人",
        "zhiweimingcheng": "测试开发工程师",
        "zuobiao": "北京",
        "jinengyaoqiu": ""
    }, {
        "gangweizhize": "",
        "gongsimingcheng": "中国科学院电子学研究所信息技术创新工程中心",
        "xinzifanwei": "1.5万-2.5万",
        "fulidaiyu": "五险一金餐补交通补助通讯补助补充医疗保险定期体检员工旅游",
        "gongzuonianxian": "3-5年",
        "gongsixingzhi": "IT服务(系统/数据/维护),计算机软件,计算机硬件,互联网/电子商务",
        "xueliyaoqiu": "本科",
        "gongsiguimo": "100-499人",
        "zhiweimingcheng": "4. ⾼高级测试开发工程师",
        "zuobiao": "北京",
        "jinengyaoqiu": ""
    }, .....

"""
import re

import scrapy
from ..items import ZhilianspiderItem

class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['jobs.zhaopin.com']
    # 只是其中一页的
    url = "https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B5%8B%E8%AF%95%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&at=051d5b568a734e1d99e4fe5e8adad171&rt=7161a116b728486ead66d2312f74ed87&_v=0.66243185&userCode=712467738&x-zp-page-request-id=16ffe1cf130b47468c188bab6fc14744-1561276964595-774936&x-zp-client-id=3ee57aab-fed5-4db0-84fa-bc8daaec87d0"

    start_urls = [
        url
    ]

    def parse(self, response):
        html_contents = str(response.body)
        r = r'positionURL":"(.*?\.htm)","companyLogo'
        urls = re.findall(r, html_contents)

        if len(urls) != 0:
            for url in urls:
                # print('开始请求------------------>>>'+url)
                yield scrapy.Request(url, callback=self.parse_item)
        else:
            print('-------<<xiongdi meiyou zhaodao url>>-------')

    def parse_item(self, response):
        # 提取列表中的每个职位的信息
        item = ZhilianspiderItem()
        # 职位名称
        item['zhiweimingcheng'] = response.xpath("//div[@class='job-summary']//h3/text()").extract()[0].strip()
        # 薪资范围
        item['xinzifanwei'] = response.xpath("//div[@class='job-summary']//div[@class='summary-plane__left']/span/text()").extract()[0].strip()
        # 坐标
        zuobiao = response.xpath("//div[@class='job-summary']//div[@class='summary-plane__left']/ul/li/a/text()").extract()[0].strip()
        zuobiao2 = ""
        try:
            zuobiao2 = response.xpath("//div[@class='job-summary']//div[@class='summary-plane__left']/ul/li/span/text()").extract()[0].strip()
        except Exception as e:
            print('-------->>sorry there is no have zuobiao2<<---------')
        if(zuobiao2 != ""):
            item['zuobiao'] = zuobiao + zuobiao2
        else:
            item['zuobiao'] = zuobiao
        # 工作年限
        item['gongzuonianxian'] = response.xpath("//div[@class='job-summary']//div[@class='summary-plane__left']/ul/li[2]/text()").extract()[0].strip()
        # 学历要求
        item['xueliyaoqiu'] = response.xpath("//div[@class='job-summary']//div[@class='summary-plane__left']/ul/li[3]/text()").extract()[0].strip()
        # 福利待遇
        fulidaiyus = response.xpath("//div[@class='a-center-layout__content']//div[@class='highlights__content']/span/text()").extract()
        item['fulidaiyu'] = "".join(fulidaiyus).strip()
        # 公司名称
        item['gongsimingcheng'] = response.xpath("//div[@class='a-center-layout__content']//div[@class='app-main__right']//div[@class='company']/a/text()").extract()[0].strip()
        # 公司性质
        item['gongsixingzhi'] = response.xpath("//div[@class='a-center-layout__content']//div[@class='app-main__right']//div[@class='company']//button[@class='company__industry']/text()").extract()[0].strip()
        # 公司规模
        item['gongsiguimo'] = response.xpath("//div[@class='a-center-layout__content']//div[@class='app-main__right']//div[@class='company']//button[@class='company__size']/text()").extract()[0].strip()
        # 岗位职责
        gangweizhize =  response.xpath("//div[@class='a-center-layout__content']//div[@class='app-main__left']//div[@class='describtion__detail-content']//p/text()").extract()
        item['gangweizhize'] = "".join(gangweizhize).strip()
        # 技能要求
        jinengyaoqiu = response.xpath("//div[@class='a-center-layout__content']//div[@class='app-main__left']//div[@class='describtion__skills']//span/text()").extract()
        item['jinengyaoqiu'] = "".join(jinengyaoqiu).strip()

        yield item
