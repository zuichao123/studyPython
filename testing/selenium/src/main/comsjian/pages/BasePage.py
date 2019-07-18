# coding:utf-8
"""
    basePaeg
"""
from selenium import webdriver

from Dbop import DbopSqlite3


class BasePage(object):
    def __init__(self, driver, tableName):
        self.driver = driver
        self.db = DbopSqlite3('C:/Software/pycharm/workspace/studyPython/testing/selenium/src/test/tools/sd.sqlite', tableName)

    def getLoc(self, loc):
        xpath = self.db.getXpath(loc)
        if (xpath != None) or (xpath != ''):
            try:
                we = self.driver.find_element_by_xpath(xpath)
            except Exception as e:
                if (xpath != None) or (xpath != ''):
                    we = self.driver.find_element_by_css_selector(self.db.getCss(loc))
        else:
            we = self.driver.find_element_by_css_selector(self.db.getCss(loc))
        return we

    def getLocStr(self, loc):
        if ((self.db.getXpath(loc) != None ) or (self.db.getXpath(loc) != '')):
            str = self.db.getXpath(loc)
        elif ((self.db.getCss(loc) != None) or (self.db.getCss(loc) != '')):
            str = self.db.getCss(loc)
        return str

    def getElementStr(self, elementName, columName):
        if ((self.db.getElementName(elementName) != None) or (self.db.getElementName(elementName) != '')):
            str = self.db.getContents(elementName, columName)
            return str
        return None


if __name__ == '__main__':
    b = BasePage(webdriver, 'LoginPage')
    vla = b.getElementStr('input', 'Comment')
    print(vla)
