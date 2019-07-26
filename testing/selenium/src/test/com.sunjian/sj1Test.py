# coding:utf-8
"""

"""
import time

from testing.selenium.src.main.comsjian.launchs.Browsers import Browsers
from testing.selenium.src.main.comsjian.pages.LoginPage import LoginPage
from testing.selenium.src.main.comsjian.utils.logger import Logger

logger = Logger(logger="sj1Test").getlog()
class sj1Test(object):
    def start(self):
        driver = Browsers('chrome').driver
        logger.info('打开浏览器了')
        driver.get('http://www.baidu.com/')
        time.sleep(5)
        driver.maximize_window()
        login = LoginPage(driver, 'LoginPage')
        login.getLoc('input').send_keys(login.getElementStr('input', 'Value'))
        logger.info('输入内容了')
        time.sleep(5)

        driver.close()
        logger.info('退出浏览器了')


if __name__ == '__main__':
    sj = sj1Test()
    sj.start()


