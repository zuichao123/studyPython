# coding:utf-8
"""
    使用数据库存储
    "localhost", "sunjian", "root", "root"
"""
import os

import pymysql
import sqlite3

class DbopMysql(object):
    def __init__(self,host,db,table,user,passwd):
        self.host = host
        self.db = db
        self.table = table
        self.user = user
        self.passwd = passwd

    def __open(self):
        """连接"""
        self.conn = pymysql.connect(host=self.host, db=self.db, user=self.user, passwd=self.passwd)
        self.cursor = self.conn.cursor()

    def __close(self):
        """关闭"""
        self.cursor.close()
        self.conn.close()

    def getXpath(self, elementName):
        sqlSelect = "select Xpath from "+ self.table + "where ElementName = '" + elementName + "';"
        print(sqlSelect)
        try:
            self.__open()
            self.cursor.execute(sqlSelect)
            results = self.cursor.fetchall()
            return results[0][0]
            self.__close()
        except Exception as e:
            print(e)

    def getCss(self, elementName):
        sqlSelect = "select Css from "+ self.table + "where ElementName = '" + elementName + "';"
        try:
            self.__open()
            self.cursor.execute(sqlSelect)
            results = self.cursor.fetchall()
            return results[0][0]
            self.__close()
        except Exception as e:
            print(e)

    def getValues(self, elementName):
        sqlSelect = "select Values from "+ self.table + "where ElementName = '" + elementName + "';"
        try:
            self.__open()
            self.cursor.execute(sqlSelect)
            results = self.cursor.fetchall()
            return results[0][0]
            self.__close()
        except Exception as e:
            print(e)

    def getComments(self, elementName):
        sqlSelect = "select comments from "+ self.table + "where ElementName = '" + elementName + "';"
        try:
            self.__open()
            self.cursor.execute(sqlSelect)
            results = self.cursor.fetchall()
            return results[0][0]
            self.__close()
        except Exception as e:
            print(e)

    def getElementName(self, elementName):
        """获取数据库中的元素名"""
        sqlSelect = "select ElementName from " + self.table + " where ElementName = '" + elementName + "';"
        try:
            self.__open()
            self.cursor.execute(sqlSelect)
            results = self.cursor.fetchall()
            return results[0][0]
            self.__close()
        except Exception as e:
            print(e)

    def getContents(self, elementName, columName):
        """获取指定的元素的指定内容"""
        sqlSelect = "select "+ columName +" from "+ self.table + " where ElementName = '" + elementName + "';"
        try:
            self.__open()
            self.cursor.execute(sqlSelect)
            results = self.cursor.fetchall()
            return results[0][0]
            self.__close()
        except Exception as e:
            print(e)
# -----------------------------------------------------------------------------------
class DbopSqlite3(object):
    def __init__(self, db, table):
        self.db = db
        self.table = table

    def __open(self):
        """连接"""
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()

    def __close(self):
        """关闭"""
        self.cursor.close()
        self.conn.close()

    def getXpath(self, elementName):
        sqlSelect = "select Xpath from "+ self.table + " where ElementName = '" + elementName + "';"
        try:
            self.__open()
            self.cursor.execute(sqlSelect)
            results = self.cursor.fetchall()
            return results[0][0]
            self.__close()
        except Exception as e:
            print(e)

    def getCss(self, elementName):
        sqlSelect = "select Css from "+ self.table + "where ElementName = '" + elementName + "';"
        try:
            self.__open()
            self.cursor.execute(sqlSelect)
            results = self.cursor.fetchall()
            return results[0][0]
            self.__close()
        except Exception as e:
            print(e)

    def getValues(self, elementName):
        sqlSelect = "select Values from "+ self.table + "where ElementName = '" + elementName + "';"
        try:
            self.__open()
            self.cursor.execute(sqlSelect)
            results = self.cursor.fetchall()
            return results[0][0]
            self.__close()
        except Exception as e:
            print(e)

    def getComments(self, elementName):
        sqlSelect = "select comments from "+ self.table + "where ElementName = '" + elementName + "';"
        try:
            self.__open()
            self.cursor.execute(sqlSelect)
            results = self.cursor.fetchall()
            return results[0][0]
            self.__close()
        except Exception as e:
            print(e)

    def getElementName(self, elementName):
        """获取数据库中的元素名"""
        sqlSelect = "select ElementName from " + self.table + " where ElementName = '" + elementName + "';"
        try:
            self.__open()
            self.cursor.execute(sqlSelect)
            results = self.cursor.fetchall()
            return results[0][0]
            self.__close()
        except Exception as e:
            print(e)

    def getContents(self, elementName, columName):
        """获取指定的元素的指定内容"""
        sqlSelect = "select "+ columName +" from "+ self.table + " where ElementName = '" + elementName + "';"
        try:
            self.__open()
            self.cursor.execute(sqlSelect)
            results = self.cursor.fetchall()
            return results[0][0]
            self.__close()
        except Exception as e:
            print(e)

if __name__ == "__main__":
    db = DbopSqlite3(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")) + "\\test\\tools\\xxx.sqlite","LoginPage")
    val = db.getXpath("phoneNum")
    print("=========="+str(val))

    val2 = db.getContents('input','Comment')
    print(val2)
