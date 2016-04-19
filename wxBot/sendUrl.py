#!/usr/bin/env python
# coding: utf-8
from pymongo.errors import CursorNotFound

from wxbot import *
import pymongo


class MyWXBot(WXBot):
    # def handle_msg_all(self, msg):
    #     if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
    #         self.send_msg_by_uid('hi', msg['user']['id'])

    def schedule(self):

        # USER_NAME = 'xiaoda'
        USER_NAME = 'filehelper'

        while True:

            conn = pymongo.MongoClient("mongodb://172.18.79.31:27017")
            db = conn['wechatdb']
            self.coll = db['wechat_article_info']

            results = list(self.coll.find())


            try:
                self.send_msg(USER_NAME, 'start sending urls...')
                time.sleep(5)
                for i in range(3, 0, -1):
                    self.send_msg(USER_NAME, "%d..." % i)
                    time.sleep(5)

                k = 0
                for item in results:
                    k += 1
                    url = item['url']
                    title = item['title']
                    msg = "%d, %s, %s" % (k, title, url)

                    if self.test_sync_check():
                        print("sync check successful")
                        if self.send_msg(USER_NAME, msg):
                            print("SENT>>: %s %s  to [%s]" % (time.strftime("%y-%m-%d %H:%M:%S"), msg, USER_NAME))
                        else:
                            print("failed>>: %s %s  to [%s]" % (time.strftime("%y-%m-%d %H:%M:%S"), msg, USER_NAME))
                    else:
                        print("sync check failed.")
                    time.sleep(10)
            except CursorNotFound:
                print("err...")
            print("all sent." )
            time.sleep(10)


def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()


if __name__ == '__main__':
    main()
