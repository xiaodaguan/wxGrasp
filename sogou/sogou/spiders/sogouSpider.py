# coding=utf-8
import scrapy
from scrapy import log
from sogou.items import SogouItem
import time
import hashlib
from selenium import webdriver
import re
import random


class sogouSpider(scrapy.Spider):
    name = 'sogou'

    search_keywords = ['青岛交通']
    start_urls = [('http://weixin.sogou.com/weixin?query=%s&type=2&page=3' % keyword) for keyword in search_keywords]

    def parse(self, response):
        # 虽然这里已经完成了scrapy的request过程,但是仍然再调用selenium获取当前页面,暂时没有更好的解决方案
        # 后续可以实现一个downloadmiddleware,使用selenium driver替换掉默认的请求
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(response.url)
        self.wnds_visited = set()
        for i in range(0, 10):
            x = "//div[@class='txt-box']/h4/a[contains(@id,'title_%d')]" % i
            self.driver.find_element_by_xpath(x).click()
            wait = 5 + random.randrange(0,6)
            log.msg("wait %d seconds to get detail page..." % wait)
            time.sleep(wait)
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
                    html = self.driver.page_source
                    brief = response.xpath("//div[@class='txt-box']/p[contains(@id,'summary_%d')]//text()" % i).extract()
                    weixin_name = response.xpath("//div[contains(@id,'box_%d')]/div[@class='txt-box']/div[@class='s-p']/a[@id='weixin_account']/@title" % i).extract()
                    str_pubtime = response.xpath("//div[contains(@id,'box_%d')]/div[@class='txt-box']/div[@class='s-p']/span[@class='time']/script" % i).re(r"'\d+'")[0].encode('utf-8')
                    str_pubtime = str_pubtime.replace("'", "")
                    pubtime = time.strftime("%Y-%m-%d %H%M%S", time.localtime(long(str_pubtime)))
                    item = SogouItem()

                    item['url'] = url
                    item['title'] = title
                    # item['page_source'] = html
                    item['brief'] = brief
                    item['weixin_name'] = weixin_name
                    item['pubtime'] = pubtime
                    item['search_keyword'] = self.keyword
                    meta = {'item': item}

                    yield scrapy.Request(url=url, callback=self.parse_item, meta=meta)
            # end for: each window
            self.driver.switch_to.window(list_page_wnd)
        # end for: each detail link
        log.msg("page %s parsed." % response.url)
        self.driver.quit()

        wait = 60 + random.randrange(0,61)
        log.msg("wait %d seconds to get next page..." % wait)
        time.sleep(wait)
        page_num = re.search("&page=\d+", response.url)
        if page_num:
            nextUrl = re.sub("&page=\d+", "&page=%d" % (int(page_num.group(0).replace("&page=")) + 1), response.url)
        else:
            nextUrl = response.url + "&page=2"

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
