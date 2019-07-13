# coding:utf-8
"""https://www.cppentry.com/bencandy.php?fid=77&aid=226745&page=2"""
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from PIL import Image
import time

driver = webdriver.Firefox()


def get_snap(driver):
    driver.save_screenshot('snap.png')
    snap_obj = Image.open('snap.png')
    return snap_obj


def get_image(driver):
    img_element = driver.find_element_by_xpath(
        '//div[@class="geetest_panel_next"]//canvas[@class="geetest_canvas_slice geetest_absolute"]')
    size = img_element.size
    location = img_element.location
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']
    snap_obj = get_snap(driver)
    img_obj = snap_obj.crop((left, top, right, bottom))
    return img_obj

def get_distance(img1, img2):
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

def get_tracks(distance):
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
        tance = round(tance)
        s += tance
        v0 = v + a * t
        forward_tracks.append(tance)
    back_tracks = [-1, -1, -1, -2, -2, -2, -3, -3, -2, -2, -1]  # 20
    return {"forward_tracks": forward_tracks, 'back_tracks': back_tracks}

try:
    driver.get('https://account.cnblogs.com/signin')
    driver.implicitly_wait(3)
    input_username = driver.find_element_by_id('LoginName')
    input_password = driver.find_element_by_id('Password')
    input_username.send_keys('928480709')
    input_password.send_keys('dfcver1112223334')
    time.sleep(5)
    # 点击登录按钮
    driver.find_element_by_xpath("//button[@id='submitBtn']").click()
    time.sleep(2)
    # 等待验证码加载
    none_img = get_image(driver)
    driver.execute_script(
        "var x=document.getElementsByClassName('geetest_canvas_fullbg geetest_fade geetest_absolute')[0];" "x.style.display='block';" "x.style.opacity=1")
    block_img = get_image(driver)
    geetest_slider_button = driver.find_element_by_class_name('geetest_slider_button')
    distance = get_distance(block_img, none_img)
    tracks_dic = get_tracks(distance)
    ActionChains(driver).click_and_hold(geetest_slider_button).perform()
    forword_tracks = tracks_dic['forward_tracks']
    back_tracks = tracks_dic['back_tracks']
    for forword_track in forword_tracks:
        ActionChains(driver).move_by_offset(xoffset=forword_track, yoffset=0).perform()
        time.sleep(0.2)
    for back_tracks in back_tracks:
        ActionChains(driver).move_by_offset(xoffset=back_tracks, yoffset=0).perform()
        print(forword_tracks)
    ActionChains(driver).move_by_offset(xoffset=-3, yoffset=0).perform()
    ActionChains(driver).move_by_offset(xoffset=3, yoffset=0).perform()
    time.sleep(0.3)
    ActionChains(driver).release().perform()
    time.sleep(60)
finally:
    driver.close()
