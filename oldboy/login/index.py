#!/usr/bin/env python
# -*- coding:utf-8 -*-

def login(username,password):
    '''
    用于验证用户名及密码
    :param username: 用户名
    :param password: 密码
    :return: True:用户登录成功  False:用户登录失败
    '''
    with open("db",'r',encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            line_list = line.split(':')
            if username == line_list[0] and password == line_list[1]:
                return True
    return False

def register(username,password):
    with open("db",'a',encoding='utf-8') as f:
        temp = '\n' + username + ':' + password
        f.write(temp)

def user_exist(username):
    with open("db",'r',encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            line_list = line.split(':')
            if line_list[0] == username:
                return True
    return False

def main():
    print("1:登录  2：注册")
    num = input()
    if num == '1':
        username = input("请输入用户名：")
        password = input("请输入密码：")
        ret = login(username, password)
        if ret:
            print("登录成功")
        else:
            print("登录失败")
    elif num == '2':
        username = input("请输入用户名：")
        password = input("请输入密码：")
        is_exist = user_exist(username)
        if is_exist:
            print("用户名已被注册")
        else:
            register(username,password)

main()