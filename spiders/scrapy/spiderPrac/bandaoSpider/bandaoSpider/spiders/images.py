# -*- coding: utf-8 -*-
"""
    dl[2]:videos
    dl[3]:tupian
    dl[4]:xiaoshuo
    "yazhoutupian":"",
    "oumeisetu":"",
    "wangyouzipai":"//div[@id='menu']//dl[3]/dd[3]/a[1]",
    "meituisiwa":"",
    "qingchunweimei":"",
    "dongmankatong":"",
"""
import os
import random
import re
import time
import urllib.request

import scrapy
from selenium import webdriver


class BandaoSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['www.bandao456.com']
    url = "http://www.bandao456.com"
    first_window = None


    start_urls = [url]
    tp = [
        "//div[@id='menu']//dl[3]/dd[1]/a[1]",
        "//div[@id='menu']//dl[3]/dd[2]/a[1]",
        # "//div[@id='menu']//dl[3]/dd[3]/a[1]",
        # "//div[@id='menu']//dl[3]/dd[4]/a[1]",
        # "//div[@id='menu']//dl[3]/dd[5]/a[1]",
        # "//div[@id='menu']//dl[3]/dd[6]/a[1]",
    ]

    def parse(self, response):
        """操作"""
        for tupian in self.tp:
            try:
                driver = self.into_page(tupian)
                self.download_details(driver)
            except Exception as e:
                print(e)
                break
        print('*'*20+'come over'+'*'*20)

    def into_page(self, tupian):
        """进入目标页面"""
        driver = webdriver.PhantomJS(executable_path=r"C:\Software\python\phantomjs\bin\phantomjs.exe")
        # driver = webdriver.Chrome()
        driver.get(self.start_urls[0])
        time.sleep(5)
        # print('---------首页------------' + driver.current_url)
        driver.find_element_by_xpath(tupian).click()
        time.sleep(5)
        # print('---------目标------------' + driver.current_url)
        self.first_window = driver.current_window_handle
        return driver

    def next_page(self, driver):
        """点击下一页"""
        next_page = "//div[preceding::div[@id='bottomBox'] and descendant::div[@class='pagination']]/div/a[3]"
        next = driver.find_element_by_xpath(next_page)
        print('----------click next page--------------1')
        if (next.is_displayed() and next.is_enabled()):
            next.click()
            print('----------click next page--------------2')
            time.sleep(5)
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

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"
        }

        # 获取页面中所以的图片页面链接
        htmls = driver.page_source
        images_links = re.findall(r'href="(/tupian.*?\d+\.html?)', str(htmls))
        # 遍历请求
        j = 1
        for link in images_links:
            if str(link).__contains__('href'):
                link = re.findall(r'href="(.*?\d+\.html?)', str(link))[0]
            # 请求链接地址
            link = self.url+str(link)
            request = urllib.request.Request(link, headers=headers)
            page = urllib.request.urlopen(request, timeout=60)
            # 获取当前页中所有的图片链接
            all_images = re.findall(r'src="(.*?\d+\.jpg)', str(page.read()))

            if len(all_images) > 0:
                # print('--start downloading-->>' + link)
                for i in range(1, len(all_images)):
                    img = all_images[i]

                    # print('--------start downloading-->>>>' + img)
                    if (str(img).__contains__("gif") or str(img).__contains__("png")):
                        break
                    image_dirs = re.findall('.*?/(\d+)/.*', img)
                    image_names = re.findall('.*?/(\d+|\d+_\d+)\.jpg', img)
                    image_dir = image_dirs[0]  # 目录名
                    image_name = image_names[0]  # 图片名
                    # 图片存放路径
                    save_path = self.currentDesktopPath() + "\\images\\" + image_dir
                    if not os.path.exists(save_path):
                        os.makedirs(save_path)
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
                    # 请求具体的图片链接地址
                    req = urllib.request.Request(img)
                    req.add_header('User-Agent', random.choice(agents))
                    pic = urllib.request.urlopen(req, timeout=60)
                    # 保存
                    f = open(save_path + '\\' + image_name + '.jpg', 'wb')
                    f.write(pic.read())
                    f.close()
                    print('第-------' + str(i) + '个图片--------下载完成')
            print('---------------第' + str(j) + '个链接的所有图片全部下载完成了...')
            j += 1
        # 返回上一页，点击下一页
        driver.switch_to.window(self.first_window)
        print(driver.current_url)
        time.sleep(2)
        next_page = "//div[preceding::div[@id='bottomBox'] and descendant::div[@class='pagination']]/div/a[3]"
        next = driver.find_element_by_xpath(next_page)
        if (next.is_enabled() and next.is_displayed()):
            next.click()
            time.sleep(5)
            self.download_details(driver)
        else:
            print('------没有下一页了------')

    def download_details2(self, driver):
        """下载每一页，这个方法有点墨迹"""
        all_links_xpath = "//div[@id='colList']//ul//li//a"  # 每页的
        all_links = driver.find_elements_by_xpath(all_links_xpath)

        j = 1
        for link in all_links:
            current_window = driver.current_window_handle  # 当前句柄
            link.click()  # 点击链接
            time.sleep(5)
            print('---------开始下载第' + str(j) + '个链接的图片-------' + driver.current_url)

            all_windows = driver.window_handles  # 所有的句柄
            driver.switch_to.window(all_windows[-1])  # 进入链接页面

            # print(driver.page_source)
            current_htmls = driver.page_source  # 获取当前页面的所有HTML元素
            all_images = re.findall(r'src="(.*?\d+\.jpg)', current_htmls)  # 获取当前页中所有的图片链接

            if len(all_images) > 0:
                for i in range(1, len(all_images)):
                    img = all_images[i]

                    if str(img).__contains__("gif"):
                        break

                    print('start download---------' + img)
                    image_dirs = re.findall('.*?/(\d+)/.*', img)
                    image_names = re.findall('.*?/(\d+|\d+_\d+)\.jpg', img)
                    image_dir = image_dirs[0]  # 目录名
                    image_name = image_names[0]  # 图片名

                    if not os.path.exists(self.currentDesktopPath() + "\\" + image_dir):
                        os.mkdir(self.currentDesktopPath() + "\\" + image_dir)
                    # urllib.request.urlretrieve(img, self.currentDesktopPath()+ "\\" + image_dir + '\\'+ image_name +'.jpg')

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

                    req = urllib.request.Request(img)
                    req.add_header('User-Agent', random.choice(agents))
                    pic = urllib.request.urlopen(req, timeout=60)
                    # 保存
                    f = open(self.currentDesktopPath() + "\\" + image_dir + '\\' + image_name + '.jpg', 'wb')
                    f.write(pic.read())
                    f.close()
                    print('第-------' + str(i) + '个图片--------下载完成')

                print('---------------第' + str(j) + '个链接的所有图片全部下载完成了...')
                j += 1
                driver.switch_to.window(current_window)
                print('----------back first page...')
                time.sleep(5)
            else:
                print('sorry this page not images...')
