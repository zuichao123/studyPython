# coding:utf-8
"""
    weather spider
"""
import time

from selenium import webdriver

class Tianqi(object):
    """爬取北京最近40天的天气预报"""
    def getTianqi(self, driver, url, i, num):
        driver.get(url)
        i = str(i)

        # up_riqis = driver.find_element_by_xpath("//table[@id='table']//tr[1]/th").text
        # firstWeek = driver.find_element_by_xpath("//table[@id='table']//tr[2]/th").text
        yangli = driver.find_element_by_xpath("//table[@id='table']//tr["+str(num)+"]/td["+i+"]/h2/span[2]").text
        yinli = driver.find_element_by_xpath("//table[@id='table']//tr["+str(num)+"]/td["+i+"]/h2/span[1]").text
        wd = driver.find_element_by_xpath("//table[@id='table']//tr["+str(num)+"]/td["+i+"]/div[2]/h6").text
        # wd2 = driver.find_element_by_xpath("//table[@id='table']//tr["+j+"]/td["+i+"]/div[2]/h6/b").text

        if(wd == ""):
            xpath = "//table[@id='table']//tr["+str(num)+"]/td["+i+"]/div[4]//span[1]//i"
            xpath2 = "//table[@id='table']//tr["+str(num)+"]/td["+i+"]/div[4]//span[2]//i"
            # print(xpath)
            wd1 = driver.find_element_by_xpath(xpath).text
            # print(xpath2)
            wd2 = driver.find_element_by_xpath(xpath2).text
            wd = "白天："+wd1 + " 晚上："+wd2

        jsl = driver.find_element_by_xpath("//table[@id='table']//tr["+str(num)+"]/td["+i+"]/div[2]/a/h3").text
        jiangshuiliang = "未知"
        if (jsl != ""):
            jiangshuiliang = jsl

        shijians = time.strftime("%Y-%m", time.localtime())
        shi = shijians.split("-")
        nian = shi[0]
        yue = shi[1]
        ri = yangli

        if (yue == "01" or yue == "03" or yue == "05" or yue == "07" or yue == "08" or yue == "10" or yue == "12"):
            if (ri == "31"):
                yue = int(yue) + 1
                if yue<10:
                    yue = "0"+str(yue)

        if (yue == "04" or yue == '06' or yue == '09' or yue == '11'):
            if (ri == "30"):
                yue = int(yue) + 1
                if yue<10:
                    yue = "0"+str(yue)

        if (yue == "02"):
            if (ri == "28"):
                yue = int(yue) + 1
                if yue<10:
                    yue = "0"+str(yue)

        shijian = nian+"年"+yue+"月"+ri+"日"

        print("日  期："+shijian+"  "+yinli+"\n温  度："+wd+"\n降水量："+jiangshuiliang)

    def getWeatherContents(self):
        pass

    def main(self, url):
        driver = webdriver.PhantomJS(executable_path=r"E:\Python\phantomjs-2.1.1-windows\bin\phantomjs.exe")

        day = 1
        for num in range(2, 7):
            for i in range(1, 8):
                self.getTianqi(driver, url, i, num)
                print("--" * 15+str(day))
                day = day + 1


if __name__ == '__main__':
    url = "http://www.weather.com.cn/weather40d/101010100.shtml"

    tq = Tianqi()
    tq.main(url)
