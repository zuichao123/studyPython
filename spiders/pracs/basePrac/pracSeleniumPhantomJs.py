# coding:utf-8
"""
    练习多线程爬虫

        下载selenium离线安装包https://pypi.org/project/selenium/#files
            selenium-3.141.0.tar.gz  SHA256
            解压后，进入该目录执行：python setup.py install命令即可安装完成

        下载PhantomJs
            http://phantomjs.org/download.html

"""
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path=r"C:\Software\python\phantomjs\bin\phantomjs.exe")

driver.get("https://sou.zhaopin.com/?jl=530&sf=0&st=0&kw=%E6%B5%8B%E8%AF%95%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3")
driver.save_screenshot("1.png") # 截/屏


from selenium.webdriver.common.keys import Keys

# aa = driver.find_element_by_xpath("//div[@id='listContent']//div[@class='contentpile__content__wrapper__item clearfix']/a/@href")
# print(driver.find_element_by_xpath("https://sou.zhaopin.com/?jl=530&sf=0&st=0&kw=%E6%B5%8B%E8%AF%95%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3").is_displayed())


