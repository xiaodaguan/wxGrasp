# -*- coding: utf-8 -*-

# Scrapy settings for sogou project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

DOWNLOAD_DELAY = 5
RETRY_TIMES = 3
BOT_NAME = 'sogou'

SPIDER_MODULES = ['sogou.spiders']
NEWSPIDER_MODULE = 'sogou.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sogou (+http://www.yourdomain.com)'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 90,
    # Fix path to this module
     'sogou.middlewares.RandomProxy': 100,
     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
}

ITEM_PIPELINES = {
    'sogou.pipelines.SogouPipeline': 123,
}

PROXY_LIST = 'proxys.txt'
UA_LIST = 'uas.txt'
COOKIE_LIST = 'cookies.txt'