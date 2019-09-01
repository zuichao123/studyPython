# coding:utf-8
"""
    登录页面
        返回所有的元素
"""
from selenium import webdriver
from .BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver, tableName):
        super().__init__(driver, tableName)


    def getUrl(self):
        return self.getElementStr('url', 'Value')



if __name__ == '__main__':
    login = LoginPage(webdriver, 'LoginPage')
    url = login.getUrl()
    print(url)

