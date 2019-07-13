# coding:utf-8
"""python3 破解 geetest（极验）的滑块验证码

    https://www.jianshu.com/p/2c726ff42029
"""
import base64

from pygame import image
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
# import PIL.Image as image
import time,re, random
import requests
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

#爬虫模拟的浏览器头部信息
agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers = {
        'User-Agent': agent
        }

def main():
    #打开火狐浏览器
    driver = webdriver.Firefox()
    #用火狐浏览器打开网页
    driver.get("https://www.cnblogs.com/")

    # 点击登录按钮
    driver.find_element_by_xpath("//span[@id='span_userinfo']/a[1]").click()
    time.sleep(3)
    # 输入用户名、密码
    driver.find_element_by_xpath("//form[@id='loginForm']/div[1]/input").send_keys("15510211823")
    driver.find_element_by_xpath("//form[@id='loginForm']/div[2]/input").send_keys("sunjian123!@#")

    # 点击登录按钮
    driver.find_element_by_xpath("//button[@id='submitBtn']").click()
    time.sleep(2)

    #等待页面的上元素刷新出来
    WebDriverWait(driver, 30).until(lambda the_driver: the_driver.find_element_by_xpath("//div[contains(@class,'geetest_canvas_img')]/div").is_displayed())

    #下载图片
    JS = 'return document.getElementsByClassName("geetest_canvas_bg geetest_absolute")[0].toDataURL("image/png");'
    # 执行 JS 代码并拿到图片 base64 数据
    im_info = driver.execute_script(JS)  # 执行js文件得到带图片信息的图片数据
    im_base64 = im_info.split(',')[1]  # 拿到base64编码的图片信息
    im_bytes = base64.b64decode(im_base64)  # 转为bytes类型
    with open('bggg.png', 'wb') as f:  # 保存图片到本地
        f.write(im_bytes)


#主函数入口
if __name__ == '__main__':
    pass
    main()