# coding:utf-8
"""
    练习多线程爬虫
"""
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path=r"E:\selenium\selenium\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe")

driver.get("http://www.baidu.com/")
driver.save_screenshot("baidu.png")


from selenium.webdriver.common.keys import Keys

driver.find_element_by_id("kw").send_keys("美女")
driver.find_element_by_id("su").click()
driver.save_screenshot("baidu2.png")