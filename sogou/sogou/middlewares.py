# Copyright (C) 2013 by Aivars Kalvans <aivars.kalvans@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import re
import random
import base64
from scrapy import log


class RandomProxy(object):
    def __init__(self, settings):
        # proxies
        self.proxy_list = settings.get('PROXY_LIST')
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
        # user_agents
        self.ua_list = settings.get('UA_LIST')
        fin = open(self.ua_list)
        self.uas = []
        for line in fin.readlines():
            self.uas.append(line)
        fin.close()

        # cookies
        self.cookie_list = settings.get('COOKIE_LIST')
        fin = open(self.cookie_list)
        self.cookies = []
        for line in fin.readlines():
            self.cookies.append(line)
        fin.close()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_request(self, request, spider):
        # Don't overwrite with a random one (server-side state for IP)

        # random proxy
        if 'proxy' not in request.meta:
            # return
            if len(self.proxies) > 0:
                proxy_address = random.choice(self.proxies.keys())
                proxy_user_pass = self.proxies[proxy_address]

                request.meta['proxy'] = proxy_address
                log.msg("[%s]using proxy %s " % (request.url, proxy_address), level=log.DEBUG)
                if proxy_user_pass:
                    basic_auth = 'Basic ' + base64.encodestring(proxy_user_pass)
                    request.headers['Proxy-Authorization'] = basic_auth
        else:
            log.msg("[%s]proxy %s " % (request.url, request.meta['proxy']), level=log.DEBUG)

        # random user-agent
        if "User-Agent" not in request.headers:
            if len(self.uas) > 0:
                ua = random.choice(self.uas)
                if ua:
                    request.headers.setdefault('User-Agent', ua)
                    log.msg("[%s]using user-agent %s " % (request.url, ua), level=log.DEBUG)
        else:
            log.msg("[%s]user-agent %s " % (request.url, request.headers['User-Agent']), level=log.DEBUG)

        # random cookie
        if len(request.cookies) == 0:
            if len(self.cookies) > 0:
                cookie = random.choice(self.cookies)
                if cookie:
                    for kv in cookie.split(';'):
                        request.cookies[kv.split('=')[0]] = kv.split('=')[1]
                    # request.headers.setdefault('Cookie', cookie)
                    log.msg("[%s]using Cookie %s " % (request.url, cookie), level=log.DEBUG)
        else:
            # log.msg("cookie %s [%s]" % (request.headers['Cookie'], request.url))
            log.msg("[%s]cookie %s " % (request.url, request.cookies), level=log.DEBUG)

            # log.msg(request.headers)

    def process_exception(self, request, exception, spider):
        proxy = request.meta['proxy']
        log.msg('failed proxy <%s>, %d proxies left' % (
            proxy, len(self.proxies)))
        # log.msg('Removing failed proxy <%s>, %d proxies left' % (
        # proxy, len(self.proxies)))
        # try:
        #     del self.proxies[proxy]
        # except ValueError:
        #     pass
