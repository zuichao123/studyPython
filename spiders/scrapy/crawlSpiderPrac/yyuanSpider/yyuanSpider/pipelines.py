# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import re

import pymongo
import pymysql


class YyuanspiderPipeline(object):
    def __init__(self):
        self.filename = open(self.currentDesktopPath() + "/" + "yyuan.json", "w", encoding='utf-8')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False).encode('utf-8')
        content = content.decode(encoding='utf-8')
        self.filename.write(content + ",\n")

        # self.saveToMongo(content)
        return item

    def close_spider(self, spider):
        self.filename.close()

    def currentDesktopPath(self):
        # 作用：获取当前桌面路径
        return os.path.join(os.path.expanduser("~"), 'Desktop')

    def saveToMongo(self,data):
        # 创建MongoDB数据库连接
        mongoli = pymongo.MongoClient(host="127.0.0.1", port=27017)

        # 创建数据库名称
        dbname = mongoli["youyuan"]
        # 创建mongo数据库的表名称
        sheetname = dbname["beijing_18_25_mm"]
        offset = 0

        while True:
            offset += 1
            # 将json对象转换为Python对象
            data = json.loads(str(data))
            # 将数据插入到sheetname表里
            sheetname.insert(data)
            print ('insert '+str(offset)+' successful..')

    def saveToMysql(self,data):
        """首先要：创建好mysql数据库（youyuan）和表(beijing_18_25_mm)"""

        # 创建mysql数据库连接
        mysqlcli = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="root", db="youyuan")
        offset = 0

        while True:
            item = json.loads(data)
            try:
                # 创建mysql 操作游标对象，可以执行mysql语句
                cursor = mysqlcli.cursor()

                cursor.execute(
                    "insert into beijing_18_25_mm (username, age, header_url, images_url, content, place_from, education, hobby, source_url, source, time, spidername) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    [item['username'], item['age'], item['header_url'], item['images_url'], item['content'],
                     item['place_from'], item['education'], item['hobby'], item['source_url'], item['sourec'],
                     item['time'], item['spidername']])
                # 提交事务
                mysqlcli.commit()
                # 关闭游标
                cursor.close()
                offset += 1
                print('insert ' + str(offset) + ' successful..')
            except:
                pass
