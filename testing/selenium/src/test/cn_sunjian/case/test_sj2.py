# coding:utf-8
"""

"""
import time
import unittest

from testing.selenium.src.main.com_sunjian.launchs.Browsers import Browsers
from testing.selenium.src.main.com_sunjian.pages.LoginPage import LoginPage
from testing.selenium.src.main.com_sunjian.utils.logger import Logger

logger = Logger(logger="sj2Test").getlog()
class sj2Test(unittest.TestCase):
    def setUp(self):
        self.driver = Browsers('chrome').driver
        logger.info('打开浏览器了')
        self.driver.get('http://www.baidu.com/')
        time.sleep(5)
        self.driver.maximize_window()

    def test_baidu(self):
        login = LoginPage(self.driver, 'LoginPage')
        login.getLoc('input').send_keys(login.getElementStr('input', 'Value'))
        logger.info('输入内容了')
        time.sleep(5)

    def tearDown(self):
        self.driver.close()
        logger.info('退出浏览器了')
