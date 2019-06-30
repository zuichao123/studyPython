# coding:utf-8
"""
    练习多线程爬虫

        下载selenium离线安装包https://pypi.org/project/selenium/#files
            selenium-3.141.0.tar.gz  SHA256
            解压后，进入该目录执行：python setup.py install命令即可安装完成

        下载PhantomJs
            http://phantomjs.org/download.html

"""
from time import sleep

from selenium import webdriver

driver = webdriver.PhantomJS(executable_path=r"C:\Software\python\phantomjs\bin\phantomjs.exe")
# driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.maximize_window()
# driver.save_screenshot("1.png") # 截/屏
# data = driver.page_source # 获取网页源代码
# print(data)

print(driver.current_url)
# jiqingxiaosh
jiqingxiaoshuo = "//div[@id='menu']//dl[4]/dd[1]/a[1]"
driver.find_element_by_xpath(jiqingxiaoshuo).click()
sleep(5)
print(driver.current_url)

current_window = driver.current_window_handle # 当前句柄

# 每页的第一个
xiaoshu = "//div[@id='colList']//ul//li[1]//a[contains(@href,'html')]"
driver.find_element_by_xpath(xiaoshu).click()
sleep(15)

all_windows = driver.window_handles # 所有的句柄
driver.switch_to.window(all_windows[-1])
print(driver.current_url)

# 也可以
# for window in all_windows:
#     if window != current_window:
#         driver.switch_to.window(window)

title = "//div[@class='area']/h1"
titles = driver.find_element_by_xpath("//div[@class='mod']//h1").text
print(titles)

# contents
content = "//div[@class='area']/div"
contents = driver.find_element_by_xpath(content).text
print(contents)
driver.quit()
# # 下一页
# nextpage = "//div[preceding::div[@id='bottomBox'] and descendant::div[contains(@class,'pagination')]]/div/a[3]"
