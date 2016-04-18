#!/usr/bin/env python
# coding: utf-8

from wxbot import *
import pymongo

class MyWXBot(WXBot):
    # def handle_msg_all(self, msg):
    #     if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
    #         self.send_msg_by_uid('hi', msg['user']['id'])

    def schedule(self):

        while True:
            self.send_msg('filehelper', 'start sending urls...')
            conn = pymongo.MongoClient("mongodb://172.18.79.31:27017")
            db = conn['wechatdb']
            self.coll = db['wechat_article_info']

            result = self.coll.find()
            for item in result:
                url = item['url']
                self.send_msg('filehelper',url)
                print("sent [%s] to [%s]"%(url,"filehelper"))
                time.sleep(15)

            print("all sent. %d" % result.count())
            time.sleep(300)







def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()


if __name__ == '__main__':
    main()
