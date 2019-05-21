# coding:utf-8
"""
    MySQL
"""
import pymysql

class MysqlHelps(object):
    """我的mysql帮助类"""
    def __init__(self,host,db,user,passwd):
        self.host = host
        self.db = db
        self.user = user
        self.passwd = passwd

    def open(self):
        """连接"""
        self.conn = pymysql.connect(host=self.host,db=self.db,user=self.user,passwd=self.passwd)
        self.cursor = self.conn.cursor()

    def close(self):
        """关闭"""
        self.cursor.close()
        self.conn.close()

    def update(self,sql,params):
        """增、删、改"""
        try:
            self.open()
            self.cursor.execute(sql,params)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            print(e.args)
            return False

    def select(self,sql,params):
        """查询"""
        try:
            self.open()
            self.cursor.execute(sql,params)
            result = self.cursor.fetchall()
            self.close()
            return result
        except Exception as e:
            print(e.args)
            return None