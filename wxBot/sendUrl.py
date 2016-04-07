#!/usr/bin/env python
# coding: utf-8

from wxbot import *
import pymongo

class MyWXBot(WXBot):
    # def handle_msg_all(self, msg):
    #     if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
    #         self.send_msg_by_uid('hi', msg['user']['id'])

    def schedule(self):

        self.send_msg('gxd', 'test')
        conn = pymongo.MongoClient("mongodb://172.18.79.31:27017")
        db = conn['wechatdb']
        self.coll = db['wechat_article_info']

        result = self.coll.find()
        for item in result:
            url = item['url']
            self.send_msg('gxd',url)
            print("sent [%s] to [%s]"%(url,"gxd"))
            time.sleep(15)

        print("all sent. %d" % len(result))







def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()


if __name__ == '__main__':
    main()
