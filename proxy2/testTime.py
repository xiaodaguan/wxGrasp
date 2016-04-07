# # coding=utf-8
# import datetime  # 调用事件模块
#
# today = datetime.datetime.today()  # 获取今天日期
# deltadays = datetime.timedelta(days=1)  # 确定日期差额，如前天 days=2
# yesterday = today - deltadays  # 获取差额日期，昨天
# tomorrow = today + deltadays  # 获取差额日期，明天
# # 格式化输出
# ISOFORMAT = '%Y-%m-%d %H:%M:%S'  # 设置输出格式
# print today.strftime(ISOFORMAT)


import time

print time.strftime("%Y-%m-%d %H:%M:%S")
