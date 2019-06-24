# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os


class ZhilianspiderPipeline(object):
    def __init__(self):
        self.filename = open(self.currentDesktopPath() + "/" + "zhilian2.json", "w", encoding='utf-8')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False).encode('utf-8')
        content = content.decode(encoding='utf-8')
        self.filename.write(content + ",\n")

        return item

    def close_spider(self, spider):
        self.filename.close()

    def currentDesktopPath(self):
        # 作用：获取当前桌面路径
        return os.path.join(os.path.expanduser("~"), 'Desktop')
