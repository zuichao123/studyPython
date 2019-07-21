# coding:utf-8
"""

"""
import time

from testing.selenium.src.main.comsjian.launchs.Browsers import Browsers
from testing.selenium.src.main.comsjian.pages.LoginPage import LoginPage


class sj1Test(object):
    def start(self):
        driver = Browsers('chrome').driver
        driver.get('http://www.baidu.com/')
        time.sleep(5)

        login = LoginPage(driver, 'LoginPage')
        login.getLoc('input').send_keys(login.getElementStr('input', 'Value'))
        time.sleep(5)

        driver.close()


if __name__ == '__main__':
    sj = sj1Test()
    sj.start()


