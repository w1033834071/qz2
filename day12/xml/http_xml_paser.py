#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 从服务器读取xml并解析

import requests

url = "http://www.w3school.com.cn/example/xmle/simple.xml"
response = requests.get(url)
result = response.text


from xml.etree import ElementTree as ET


# 仅 读取 xml  全部在内存中完成
# root = ET.XML(result)
# for node in root.iter("food"):
#     print(node.find("price").text)


#  写入xml文件
# food = open("food.xml","w",encoding="utf-8")
# food.write(result)


#  解析并修改xml
parser_result = ET.parse("food.xml")
root = parser_result.getroot()
for node in root.iter("food"):
    name = node.find("name").text
    if name == "French Toast":
        node.find("name").text = "French Fries"
        break

parser_result.write("food.xml")

# tree.write("food.xml")