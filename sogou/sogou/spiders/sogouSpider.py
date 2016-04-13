# coding=utf-8
import scrapy
from scrapy import log
from sogou.items import SogouItem
import time
import datetime
import hashlib
from selenium import webdriver
import re
import random


class sogouSpider(scrapy.Spider):
    name = 'sogou'

    search_keywords = ['青岛交通']
    start_urls = [('http://weixin.sogou.com/weixin?query=%s&type=2' % keyword) for keyword in search_keywords]

    def __init__(self, **kwargs):
        # proxies
        super(sogouSpider, self).__init__(**kwargs)
        self.proxy_list = "proxys.txt"
        fin = open(self.proxy_list)

        self.proxies = {}
        for line in fin.readlines():
            parts = re.match('(\w+://)(\w+:\w+@)?(.+)', line)

            # Cut trailing @
            if parts.group(2):
                user_pass = parts.group(2)[:-1]
            else:
                user_pass = ''

            self.proxies[parts.group(1) + parts.group(3)] = user_pass

        fin.close()

    def start_requests(self):
        for start_url in self.start_urls:

            # print os.getcwd()
            # random proxy

            if self.settings['WEBDRIVER_USE_PROXY']:
                self.getProxyDriver()
            else:
                self.getDriver()

            # # test
            # self.driver.get("http://guanxiaoda.cn")
            # print(self.driver.page_source)
            # #

            self.driver.get(start_url)
            self.wnds_visited = set()
            for i in range(0, 10):

                brief = self.driver.find_element_by_xpath("//div[@class='txt-box']/p[contains(@id,'summary_%d')]" % i).text
                weixin_name = self.driver.find_element_by_xpath("//div[contains(@id,'box_%d')]/div[@class='txt-box']/div[@class='s-p']/a[@id='weixin_account']" % i).get_attribute("title")
                str_pubtime = self.driver.find_element_by_xpath("//div[contains(@id,'box_%d')]/div[@class='txt-box']/div[@class='s-p']/span[@class='time']" % i).text.encode('utf-8')
                pubtime = self.switch_time(str_pubtime)

                item = SogouItem()

                # item['page_source'] = html
                item['brief'] = brief
                item['weixin_name'] = weixin_name
                item['pubtime'] = pubtime
                item['search_keyword'] = self.keyword

                x = "//div[@class='txt-box']/h4/a[contains(@id,'title_%d')]" % i
                self.driver.find_element_by_xpath(x).click()
                # wait = 15 + random.randrange(0,16)
                # log.msg("wait %d seconds to get detail page..." % wait)
                # time.sleep(wait)
                list_page_wnd = self.driver.current_window_handle
                wnds = self.driver.window_handles
                for wnd in wnds:
                    if list_page_wnd == wnd:
                        continue
                    elif wnd in self.wnds_visited:
                        # print("visited! [%s]" % wnd)
                        continue
                    else:
                        self.driver.switch_to.window(wnd)  # switch to detail page window
                        self.wnds_visited.add(wnd)
                        print("visiting... [%d] [%s]" % (i, self.driver.title))
                        # visiting detail page


                        url = self.driver.current_url
                        title = self.driver.title
                        # html = self.driver.page_source
                        item['url'] = url
                        item['title'] = title

                        meta = {'item': item}

                        yield scrapy.Request(url=url, callback=self.parse_item, meta=meta)
                # end for: each window
                self.driver.switch_to.window(list_page_wnd)
            # end for: each detail link
            log.msg("page %s parsed." % start_url)
            self.driver.quit()

            wait = 60 + random.randrange(0, 61)
            log.msg("wait %d seconds to get next page..." % wait)
            time.sleep(wait)
            page_num = re.search("&page=\d+", start_url)
            if page_num:
                nextUrl = re.sub("&page=\d+", "&page=%d" % (int(page_num.group(0).replace("&page=", "")) + 1), start_url)
            else:
                nextUrl = start_url + "&page=2"

            yield scrapy.Request(url=nextUrl, callback=self.parse)

    def parse_item(self, response):
        if response.body.find("当前请求已过期") > -1:
            log.msg("当前请求已过期 %s " % response.url)
            return
        item = response.meta['item']
        print("parsing detail page %s ... " % item['title'])

        content = response.xpath("//div[@id='page-content']//text()").extract()
        img_url = response.xpath("//div[@id='page-content']//img/@src").extract()
        # nQrcode = response.xpath("//img[@id='js_pc_qr_code_img']/@src").extract()
        # if nQrcode:
        #     qrcode = "http://mp.weixin.qq.com%s" % response.xpath("//img[@id='js_pc_qr_code_img']/@src").extract()[0].encode('utf-8')
        md5 = hashlib.md5(item['url']).hexdigest()
        inserttime = time.strftime("%Y-%m-%d %H%M%S")

        item['url'] = response.url
        item['content'] = content
        item['img_url'] = img_url
        item['md5'] = md5
        item['inserttime'] = inserttime

        yield item

    def switch_time(self, time_str):
        '''
        :param time_str: 时间字符串: n小时前,n分钟前,n秒前
        :return: str formated time
        '''
        m = re.match("\d+[小]*时前", time_str)
        if m:
            t = m.group()[0]
            return (datetime.datetime.now() - datetime.timedelta(hours=int(t))).strftime("%Y-%m-%d %H:%M:%S")
        m = re.match("\d+分[钟]*前", time_str)
        if m:
            t = m.group()[0]
            return (datetime.datetime.now() - datetime.timedelta(minutes=int(t))).strftime("%Y-%m-%d %H:%M:%S")
        m = re.match("\d+秒前", time_str)
        if m:
            t = m.group()[0]
            return (datetime.datetime.now() - datetime.timedelta(seconds=int(t))).strftime("%Y-%m-%d %H:%M:%S")

        return None

    def getDriver(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def getProxyDriver(self):

        PROXY_ADDRESS = random.choice(self.proxies.keys())

        address = PROXY_ADDRESS.replace("http://", "").replace("https://", "")

        host = address.split(':')[0]
        port = int(address.split(':')[1])
        profile = webdriver.FirefoxProfile()
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", host)
        profile.set_preference("network.proxy.http_port", port)
        profile.update_preferences()

        self.driver = webdriver.Firefox(firefox_profile=profile)
        log.msg("creating driver: [%s] using proxy [%s]" % (self.driver.name, PROXY_ADDRESS))
        self.driver.maximize_window()

