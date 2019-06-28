# coding:utf-8
"""

"""
from selenium import webdriver


class Browsers(object):
    def __init__(self, browser):
        self.broser_type = browser
        self.driver = ''

    def get_driver(self):
        return self.driver

    def get_broswers(self):
        return self.broser_type

    def launch_browsers(self):
        if self.get_broswers() == 'ie':
            return webdriver.ie()
        if self.get_broswers() == 'chrome':
            return webdriver.chrome
        if self.get_broswers() == 'firefox':
            return webdriver.firefox
        if self.get_broswers() == 'edge':
            return webdriver.edge
        if self.get_broswers() == 'safari':
            return webdriver.safari


if __name__ == "__main__":
    browser = 'ie'
    browser = Browsers(browser)
    driver = browser.launch_browsers()
