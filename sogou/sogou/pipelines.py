# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy import log
from scrapy.exceptions import DropItem

class SogouPipeline(object):


    def __init__(self):
        # connection = pymongo.MongoClient("mongodb://guanxiaoda.cn:27017")
        connection = pymongo.MongoClient("mongodb://172.18.79.31:27017")
        db = connection['wechatdb']
        self.collection = db['wechat_article_info']
        # item crawled before
        log.msg("loading crawled items before...")
        self.url_crawled = set()
        pipeline = [
            {
                "$group":{
                    "_id":"$url","count":{"$sum":1}
                }
            }
        ]

        result = list(self.collection.aggregate(pipeline))
        for i,item in enumerate(result):
            self.url_crawled.add(item['_id'])
            if i % 1000 == 0 : print(i)
        log.msg("read %d crawled items" % len(result))

    def process_item(self, item, spider):

        valid = True

        if item['url'].find("antispider") > -1:
            valid = False
            DropItem("ip or cookie blocked %s " % item['title'])
        if item['url'].find("websearch") > -1:
            valid = False
            DropItem("bad item: request parameters incorrect, redirect failed. %s" % item['title'])
        if item['url'] in self.url_crawled:
            valid = False
            DropItem("item crawled before %s " % item['title'])
        else:
            valid = True

        if valid:
            self.collection.insert(dict(item))
            self.url_crawled.add(item['url'])
            log.msg("item wrote to mongodb %s / %s" % ('wechatdb', 'wechat_article_info'))
        else:
            log.msg("item droped %s " % item['title'])
        return item