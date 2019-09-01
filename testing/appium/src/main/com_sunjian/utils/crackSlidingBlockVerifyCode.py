# coding:utf-8
"""
auther: sunjian
破解博客园的滑块验证码登录
"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from PIL import Image
import time

class CrackSlidingBlock(object):
    def __init__(self, bType):
        if bType == 'ie':
            self.driver = webdriver.Ie()
        elif bType == 'firefox':
            self.driver = webdriver.Firefox()
        elif bType == 'chrome':
            self.driver = webdriver.Chrome()

    def get_snap(self, driver, i):
        """保存截屏图片，返回图片对象"""
        driver.save_screenshot('snap'+str(i)+'.png')
        snap_obj = Image.open('snap'+str(i)+'.png')
        return snap_obj

    def get_image(self, driver, i):
        """获取验证码图片矩形区域"""
        img_element = driver.find_element_by_xpath(
            '//div[@class="geetest_panel_next"]//canvas[@class="geetest_canvas_slice geetest_absolute"]')
        size = img_element.size
        location = img_element.location
        left = location['x']
        top = location['y']
        right = left + size['width']
        bottom = top + size['height']
        snap_obj = self.get_snap(driver,i)
        img_obj = snap_obj.crop((left, top, right, bottom))
        return img_obj

    def get_distance(self, img1, img2):
        '''对比两张图片，获取缺口距离'''
        start_x = 60
        threhold = 60  # 阈值
        for x in range(start_x, img1.size[0]):
            for y in range(img1.size[1]):
                rgb1 = img1.load()[x, y]
                rgb2 = img2.load()[x, y]
                res1 = abs(rgb1[0] - rgb2[0])
                res2 = abs(rgb1[1] - rgb2[1])
                res3 = abs(rgb1[2] - rgb2[2])
                if not (res1 < threhold and res2 < threhold and res3 < threhold):
                    return x - 7

    def get_tracks(self, distance):
        """获取轨道滑动数值"""
        distance += 20
        v0 = 2
        s = 0
        t = 0.4
        mid = distance * 3 / 5
        forward_tracks = []
        while s < distance:
            if s < mid:
                a = 2
            else:
                a = -3
            v = v0
            tance = v * t + 0.5 * a * (t ** 2)
            tance = round(tance) # 将一个数四舍五入到十进制数中给定的精度。
            s += tance
            v0 = v + a * t
            forward_tracks.append(tance)
        back_tracks = [-1, -1, -1, -2, -2, -2, -3, -3, -2, -2, -1]  # 20
        print('forward_tracks:',forward_tracks, '\nback_tracks:', back_tracks)
        return {"forward_tracks": forward_tracks, 'back_tracks': back_tracks}

    def start_crack(self):
        '''开始破解吧'''
        # --------------获取验证码图片
        i = 0
        # 获取默认有缺口的验证码图片
        none_img = self.get_image(self.driver, i)
        i += 1
        # ClassName的值为：与背景图片的父标签div平级的下一个canvas标签的类的值
        self.driver.execute_script(
            "var x=document.getElementsByClassName('geetest_canvas_fullbg geetest_fade geetest_absolute')[0];" "x.style.display='block';" "x.style.opacity=1")
        # 获取没有缺口的验证码图片
        block_img = self.get_image(self.driver, i)
        # ---------获取缺口距离
        distance = self.get_distance(block_img, none_img)
        # ----------移动滑块
        geetest_slider_button = self.driver.find_element_by_class_name('geetest_slider_button')  # 获取滑动的按钮元素
        tracks_dic = self.get_tracks(distance)
        ActionChains(self.driver).click_and_hold(geetest_slider_button).perform()  # 按住滑块
        forword_tracks = tracks_dic['forward_tracks']
        back_tracks = tracks_dic['back_tracks']
        for forword_track in forword_tracks:
            '''向前推进'''
            ActionChains(self.driver).move_by_offset(xoffset=forword_track, yoffset=0).perform()
            time.sleep(0.2)
        for back_tracks in back_tracks:
            '''回退'''
            ActionChains(self.driver).move_by_offset(xoffset=back_tracks, yoffset=0).perform()
            time.sleep(0.2)
        ActionChains(self.driver).move_by_offset(xoffset=-3, yoffset=0).perform()  # 左右晃动
        ActionChains(self.driver).move_by_offset(xoffset=3, yoffset=0).perform()
        time.sleep(0.3)
        ActionChains(self.driver).release().perform()  # 释放滑块按钮
        time.sleep(10)

    def login(self):
        '''登录'''
        self.driver.get('https://account.cnblogs.com/signin')
        self.driver.implicitly_wait(3)
        input_username = self.driver.find_element_by_id('LoginName')
        input_password = self.driver.find_element_by_id('Password')
        input_username.send_keys('15510211823')
        input_password.send_keys('sunjian123!@#')
        time.sleep(5)
        # 点击登录按钮
        self.driver.find_element_by_xpath("//button[@id='submitBtn']").click()
        time.sleep(2)

    def close(self):
        '''关闭浏览器'''
        self.driver.close()

    def isLoginTrue(self, driver):
        '''验证是否登录成功'''
        username = driver.find_element_by_xpath("//div[@id='header_user']/h1").text
        if not (username != None):
            print('sorry, you failed!')
            return 0
        else:
            print('very good '+username+' you are made it!')
            return 1

    def main(self):
        '''主方法'''
        try:
            flag = True
            num = 1
            while flag:
                self.login()  # 登录
                self.start_crack()  # 开始破解
                val = self.isLoginTrue(self.driver)  # 验证是否登录成功
                if val == 1:  # 登录成功了
                    print('---------第' + str(num) + '次成功了')
                    flag = False
                    self.close()
                else:
                    for i in range(5): # 再尝试5次
                        if val == 1:
                            print('---------第' + str(num) + '次成功了')
                            flag = False
                            break
                        self.start_crack()
                        val = self.isLoginTrue(self.driver)
                        num += 1
                    self.close()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    csb = CrackSlidingBlock('chrome')
    csb.main()
