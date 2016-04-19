import re

s = "http://weixin.sogou.com/weixin?query=%E9%9D%92%E5%B2%9B%E4%BA%A4%E9%80%9A&type=2&page=123&ie=utf8"

m = re.search("query=.+?&",s)
print m.group(0)
# if m:
#     print m.group(0).replace("&page=","")
#     new = re.sub("&page=\d+","&page=555",s)
#     print(new)