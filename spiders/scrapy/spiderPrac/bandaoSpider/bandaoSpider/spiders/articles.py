# -*- coding: utf-8 -*-
"""
    "dongmankatong":"",
    "qingchunweimei":"",
    "meituisiwa":"//div[@id='menu']//dl[3]/dd[3]/a[1]",
    "wangyouzipai":"",
    "oumeisetu":"",
    "yazhoutupian":"",
"""
import os
import random
import re
import time
import urllib.request

import scrapy
from selenium import webdriver


class BandaoSpider(scrapy.Spider):
    name = 'articles'
    allowed_domains = ['www.bandao456.com']
    url = "http://www.bandao456.com"

    start_urls = [url]
    ac = [
        # "//div[@id='menu']//dl[4]/dd[1]/a[1]",
        "//div[@id='menu']//dl[4]/dd[2]/a[1]",
        "//div[@id='menu']//dl[4]/dd[3]/a[1]",
    ]

    def parse(self, response):
        """操作"""
        for acticle in self.ac:
            try:
                driver = self.into_page(acticle)
                self.download_details(driver)
                self.next_page(driver)
            except Exception as e:
                print(e)
                break
        print('*'*20+'come over'+'*'*20)

    def into_page(self, acticle):
        """进入目标页面"""
        driver = webdriver.PhantomJS(executable_path=r"C:\Software\python\phantomjs\bin\phantomjs.exe")
        # driver = webdriver.Chrome()
        driver.get(self.start_urls[0])
        time.sleep(5)
        print('---------首页------------' + driver.current_url)
        driver.find_element_by_xpath(acticle).click()
        time.sleep(5)
        print('---------目标------------' + driver.current_url)
        return driver

    def next_page(self, driver):
        """点击下一页"""
        next_page = "//div[preceding::div[@id='bottomBox'] and descendant::div[@class='pagination']]/div/a[3]"
        next = driver.find_element_by_xpath(next_page)
        if (next.is_displayed() and next.is_enabled()):
            next.click()
            time.sleep(5)
            self.download_details(driver)
        else:
            print('come over...')
            driver.quit()

    def currentDesktopPath(self):
        """作用：获取当前桌面路径"""
        return os.path.join(os.path.expanduser("~"), 'Desktop')

    def download_details(self, driver):
        """下载每一页"""
        all_windows = driver.window_handles  # 所有的句柄
        driver.switch_to.window(all_windows[-1])  # 进入最近打开的链接页面

        # 请求头
        agents = [
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5',
            'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
            'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1'
        ]

        # 获取页面中所以的文件页面链接
        htmls = driver.page_source
        articles_links = re.findall(r'href="(/xiaoshuo.*?\d+\.html?)', str(htmls))
        # 遍历请求
        j = 1
        for link in articles_links:
            if str(link).__contains__('href'):
                link = re.findall(r'href="(.*?\d+\.html?)', str(link))[0]
            # 请求链接地址
            link = self.url+str(link)
            print('----start downloading-->>>>' + link)
            request = urllib.request.Request(link)
            request.add_header('User-Agent', random.choice(agents))
            response = urllib.request.urlopen(request, timeout=60)

            page_contents = str(response.read().decode('gbk'))
            titles = re.findall('<h1 class="h1-title">(.*?)</h1>', page_contents)
            title = "".join(titles).strip()
            contnets = re.findall(r'main-content">(.*)</td>', page_contents)
            contnet = "".join(contnets).strip()
            contnet = contnet.replace('<a', '').replace('<br', '').replace('/>', '').replace('<div', '').replace('>','\n')

            article_dirs = re.findall('.*/(\D+?)/.*', link)
            article_names = re.findall('.*?/(\d+|\d+_\d+)\.html', link)
            article_dir = article_dirs[0]  # 目录名
            article_name = article_names[0]  # 文件名
            # 文件存放路径
            save_path = self.currentDesktopPath() + "\\articles\\" + article_dir
            if not os.path.exists(save_path):
                os.makedirs(save_path)

            # 保存
            f = open(save_path + '\\' + article_name + '.txt', 'w', encoding='utf-8')
            f.write(title + '\n' + contnet)
            f.close()
        print('---------------第' + str(j) + '个链接的所有文本全部下载完成了...')
        j += 1
        next_page = "//div[preceding::div[@id='bottomBox'] and descendant::div[@class='pagination']]/div/a[3]"
        next = driver.find_element_by_xpath(next_page)
        if (next.is_enabled() and next.is_displayed()):
            next.click()
            time.sleep(5)
            self.download_details(driver)
        else:
            print('------没有下一页了------')
