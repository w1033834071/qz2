#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def compute_mul_div(arg):
    '''
    处理加减运算
    :param arg:
    :return:
    '''

    pass

def compute_add_sub(arg):
    '''
    处理乘除
    :param arg:
    :return:
    '''
    pass

def compute(expression):
    '''
    操作加减乘除
    :param expression: 表达式
    :return: 计算结果
    '''
    inp = [expression,0]
    # 处理表达式中的乘除
    compute_add_sub(inp)
    # 处理表达式中的加减
    compute_add_sub(inp)

    if divmod(inp[1],2) == 1:  # 如果表达式开头为 负数  -40  结果应该是负数
        result = float(inp[0]) * -1
    else:
        result = float(inp[0])
    return result




def exec_bracket(expression):
    while True:
        result = re.split('\(([^()]+)\)', expression, 1)
        print(result)
        if len(result) == 3:  # 得到的result列表 长度为三
            before = result[0]
            content = result[1]
            after = result[2]
            r = compute(content)
            expression = before + str(r) + after
        else:
            break
    pass

# origin = "1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"






if __name__ == "__main__":
    inpp = "1-2*-30/-12*(-20+200*-3/-200*-300-100)"
    inpp = re.sub('\s','',inpp)   # 去除占位符  空格  制表符等
    result = exec_bracket(inpp)
    print(result)