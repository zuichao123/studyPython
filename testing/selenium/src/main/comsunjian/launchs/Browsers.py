# coding:utf-8
"""

"""
import time

from selenium import webdriver


class Browsers(object):
    def __init__(self, browser):
        if browser == 'ie':
            self.driver = webdriver.Ie()
        elif browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'edge':
            self.driver = webdriver.Edge()
        elif browser == 'safari':
            self.driver = webdriver.safari()


if __name__ == "__main__":
    browser = Browsers('firefox')
    driver = browser.driver
    driver.get('http://www.baidu.com/')
    time.sleep(5)
    driver.close()

