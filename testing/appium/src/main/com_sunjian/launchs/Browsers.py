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
