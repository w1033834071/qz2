#!/usr/bin/env python
# -*- coding:utf-8 -*-

#  判断传入的对象是否是[字符串，元组，列表] 如果是 且其长度大于2 返回True  else False
def obj_len(arg):
    if isinstance(arg,str) or isinstance(arg,tuple) or isinstance(arg,list):
        if len(arg) > 2:
            return True
        else:
            return False
    return None


temp = 'alex'
ret = obj_len(temp)
print(ret)