#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 通过字符串导入模块   通过字符串使用模块中的函数


# inp = input("请输入模块：")
# cc = __import__(inp)
# print(cc, type(cc))
#
# inp_func = input("请输入函数名：")
# func = getattr(cc, inp_func,None)
# r = func()
# print(r)
#
# inp_global = input("请输入全局变量：")
# g = getattr(cc, inp_global, None)
# print(g)
#
# inp_has = input("判断全局变量是否存在：")
# r1 = hasattr(cc,inp_has)
# print(r1)


## 补充  setattr()  delattr()

temp = __import__("lib.text",fromlist=['com'])
com = temp.com
print(com)

