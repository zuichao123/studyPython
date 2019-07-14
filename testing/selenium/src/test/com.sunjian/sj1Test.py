# coding:utf-8
"""

"""
import time

from LoginPage import LoginPage
from testing.selenium.src.main.comsunjian.launchs.Browsers import Browsers


class sj1Test(object):
    def start(self):
        driver = Browsers('firefox').driver
        driver.get('http://www.baidu.com/')
        time.sleep(5)

        login = LoginPage(driver, 'LoginPage')
        login.getLoc('input').send_keys(login.getElementStr('input', 'Value'))
        time.sleep(5)

        driver.close()


if __name__ == '__main__':
    sj = sj1Test()
    sj.start()


