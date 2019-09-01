#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
setUp() 和 tearDown() 这两个方法在每个测试方法执行前以及执行后执行一次，setUp用来为测试准备环境，tearDown用来清理环境，已备之后的测试。
setUpClass() 与 tearDownClass() 如果想要在所有case执行之前准备一次环境，并在所有case执行结束之后再清理环境.
如果我们临时想要跳过某个case不执行怎么办？unittest也提供了几种方法：
    skip装饰器
        @unittest.skip("I don't want to run this case.")
        def test_divide(self):
'''
import os
import time
import unittest
import sys
sys.path.append('../')
from testing.selenium.src.main.com_sunjian.utils.HTMLTestRunner3 import HTMLTestRunner

class Run(object):
    def create_suite(self, test_cases):
        TestSuite = unittest.TestSuite()  # 测试集
        test_dir = './case'
        # print(test_dir)a

        discover = unittest.defaultTestLoader.discover(
            start_dir=test_dir,
            pattern=test_cases,
            top_level_dir=None
        )

        for test_case in discover:
            TestSuite.addTests(test_case)
            # print(test_case)
        return TestSuite

    def report(self):
        if len(sys.argv) > 1: # 如果运行此run.py文件时参数大于1
            report_name = os.path.dirname(os.getcwd()) + '\\report\\' + sys.argv[1] + '_result.html'
            # print(report_name)
        else: # 没有其他参数（只有python run.py  此时len(sys.argv)=1）
            now = time.strftime("%Y-%m-%d_%H_%M_%S_")
            # 需要查看每段时间的测试报告，可以这样写：
            #report_name = os.getcwd() + '\\report\\'+now+'result.html'
            report_name = '../report/'+now+'result.html'
            # print(report_name)
        return report_name

    def main(self):
        test_cases = 'test_*.py'
        TestSuite = self.create_suite(test_cases)
        fp = open(self.report(), 'wb')
        Runner = HTMLTestRunner(
            stream=fp,
            title='测试报告',
            description='测试用例执行情况'
        )
        Runner.run(TestSuite)
        fp.close()


if __name__ == '__main__':
    run = Run()
    run.main()
