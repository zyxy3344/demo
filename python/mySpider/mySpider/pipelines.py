# -*- coding: utf-8 -*-
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class MyspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item

class ItcastPipeline(object):

    def __init__(self):
        self.filename = open('teacher.json','w')
    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.filename.write(jsontext)
        return item
    def close_spider(self, spider):
        self.filename.close()
