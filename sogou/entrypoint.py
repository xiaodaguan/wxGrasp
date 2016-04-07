#!/usr/bin/env python


from scrapy.cmdline import execute
import os

os.chdir('./sogou')
execute(['scrapy', 'crawl', 'sogou'])
