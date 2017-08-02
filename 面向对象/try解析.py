#!/usr/bin/env python
# -*- coding:utf-8 -*-

inp = input("请输入内容:")

try:
    li = []
    li.append(inp)
    num = li[int(inp) - 1]
    print(num)
    # raise Exception("我主动触发了异常！")   # 主动触发异常并赋值给e

except ValueError as e:
    print("类型转换异常")
except IndexError as e:
    print("索引异常")
except Exception as e:
    print(e)
else: # 主代码执行完  执行else
    print("主代码正常执行完毕！")

finally:
    print("finally")
