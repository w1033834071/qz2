#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import datetime

# 打印从1970年到现在的时间戳
print(time.time())

# 换算一个time  可以选择填入一个时间
print(time.ctime(time.time() - (60*60*24)))

# 格林威治‘时间对象’
time_obj = time.gmtime()
print("%s-%s-%s %s:%s" % (time_obj.tm_year,time_obj.tm_mon,time_obj.tm_mday,time_obj.tm_hour,time_obj.tm_min))


# 10天以前
new_time = datetime.datetime.now() - datetime.timedelta(days=10)
print(new_time)