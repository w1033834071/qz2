#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 模拟web框架的url请求流程

url = input("请输入url:")
target_module,target_func = url.split("/")

# m = __import__("lib",fromlist=[target_module])
# module_ = m.target_module

module_ = __import__("lib." + target_module,fromlist=True)

if hasattr(module_,target_func):
    target_func = getattr(module_,target_func,None)
    ret = target_func()
    print(ret)
else:
    print("404")