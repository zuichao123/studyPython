# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

class DoubanspiderPipeline(object):
    def __init__(self):
        self.host = settings["MONGODB_HOST"]
        self.port = settings["MONGODB_PORT"]
        self.dbname = settings["MONGODB_DBNAME"]
        self.sheetname = settings["MONGODB_SHEETNAME"]
        # 创建mongo的数据库连接
        self.client = pymongo.MongoClient(host = self.host, port = self.port)
        # 指定数据库
        self.mydb = self.client[self.dbname]
        # 指定存放数据的数据库表名
        self.mysheet = self.mydb[self.sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        self.mysheet.insert(data)

        return item
