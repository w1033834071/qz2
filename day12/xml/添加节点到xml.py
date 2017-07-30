#!/usr/bin/env python
# -*- coding:utf-8 -*-


from xml.etree import ElementTree

tree = ElementTree.parse("food.xml")
root = tree.getroot()

# 创建节点   Element类型
food = root.makeelement("food",{})
sons = food.makeelement("name",{})
sons.text = "IceCream"

food.append(sons)
root.append(food)

tree.write("food.xml")