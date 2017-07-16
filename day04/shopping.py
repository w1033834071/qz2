#!/usr/bin/env python
# -*- coding -*-

'''
购物车
功能要求：
    1，要求用户输入总资产，例如2000
    2，显示商品列表，让用户根据序号选择商品，加入购物车
    3，购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功
    3，附加：可充值、某商品移除购物车
'''
goods = [
    {'name':'电脑','price':1999},
    {'name':'鼠标','price':10},
    {'name':'游艇','price':20},
    {'name':'美女','price':998}
]
count = 0
for i,dic in enumerate(goods):
    # dic 每一个列表的元素，字典
    print(i+1,dic['name'],dic['price'])
assets = int(input("请输入总资产："))

def pay():
    money = 0
    print("您购买了：")
    for num in shopping:
        good = goods[num - 1]
        name = good['name']
        price = good['price']
        money += price
        print(name,price)
    print("总价值：%d" %money)

    choose = input("要付款吗？ y/n   ")
    if choose is 'y':
        b = assets - money
        if b >= 0:
            print("付款成功，您的余额为%d" %b)
        else:
            print("您的资金不足，请充值后再付款")
    elif choose is 'n':
        shop()

shopping = []

def shop():
    while True:
        num = input("请输入商品序号：")
        if num is 'q':
            c = int(input("请选择操作  1：付款  2：移除商品  3充值  4：放弃支付"))
            if c == 1:
                pay()
            elif c == 2:
                s = {}
                for g in shopping:
                    s[g] = goods[g-1]['name']
                print(s)
                a = input("请选择您要移除的商品：    q结束")
                if a is 'q':
                    continue
                elif int(a) in s.keys():
                    a_int = int(a)
                    shopping.remove(a_int)
                else:
                    print("商品不存在")
            break
        else:
            n = int(num)
            if n > 0 and n <= len(goods):
                shopping.append(n)
                print("已添加商品：" + goods[n-1]['name'])
            else:
                print("您选择的商品不存在！")

shop()







