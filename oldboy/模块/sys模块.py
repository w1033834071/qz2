#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os
import time

# 需求1： 读写用户输入，根据用户的输入，创建一个相应的目录
# 需求2： 自己写一个简单的脚本，可以在任何路径下导入
# 需求3： 进度条   +  百分比显示

def fun1():
    val = sys.stdin.readline()[:-1]
    os.mkdir(sys.path[0] + '/' + val)


# 需求2 想不出来
def fun2():
    pass

def fun3():
    N = 31
    for i in range(N):
        sys.stdout.write('\r')    #每次打印完就清空一次
        sys.stdout.write("%s%% | %s" %(int(i/30*100), int(i/30*100) * '*'))
        sys.stdout.flush()
        time.sleep(0.3)

fun3()
