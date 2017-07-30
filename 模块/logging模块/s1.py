#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging


#  多文件日志

file_1_1 = logging.FileHandler("log_1", 'a', encoding="utf-8")
fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
file_1_1.setFormatter(fmt)

file_1_2 = logging.FileHandler('l1_2.log', 'a', encoding='utf-8')
fmt = logging.Formatter()
file_1_2.setFormatter(fmt)

# 定义日志

logger1 = logging.Logger("s1", level=logging.ERROR)
logger1.addHandler(file_1_1)
logger1.addHandler(file_1_2)


# 写日志  > Error等级才能写入文件

logger1.critical("我的level等级大于Error!")
