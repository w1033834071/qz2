#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle
import time

class Teacher:

    def __init__(self,name,age,admin):
        self.name = name
        self.age = age
        self.create_time = time.strftime("%Y-%m-%d %H-%M-%S")
        self.create_admin = admin
        self.asset = 0

    def gain(self,cost):
        '''
        增加资产
        :param cost:
        :return:
        '''
        self.asset += cost

    def decrease(self,cost):
        '''
        减少资产
        :param cost:
        :return:
        '''
        self.asset += cost


class Admin:

    def __init__(self):
        self.username = None
        self.password = None

    def login(self,username,pwd):
        if self.username == username and self.password == pwd:
            return True
        else:
            return False

    def register(self,username,pwd):
        self.username = username
        self.password = pwd

        path = self.username
        pickle.dump(self, open(path, "wb"))

class Course:
    def __init__(self,course_name,teacher_name,cost,admin):
        self.course_name = course_name
        self.teacher_name = teacher_name
        self.cost = cost
        self.admin = admin



def create_teacher(admin_obj):
    import os
    '''
    创建教师
    :param admin_obj:
    :return:
    '''
    teacher_list = []

    while True:
        name = input("请输入教师姓名：")

        if name == "q":
            break
        age = input("请输入教师年龄：")
        teacher = Teacher(name, age, admin_obj)
        teacher_list.append(teacher)

    if os.path.exists("teacher_list"):
        lists = pickle.load(open("teacher_list", "rb"))
        teacher_list.extend(lists)
    pickle.dump(teacher_list,open("teacher_list","wb"))

    for teacher in pickle.load(open("teacher_list", "rb")):
        print(teacher.name,teacher.age,teacher.create_admin.username)


def create_course(admin_obj):
    '''
    创建课程
    :param admin_obj:
    :return:
    '''
    course_list = []
    import os
    if os.path.exists("teacher_list"):
        teacher_list = pickle.load(open("teacher_list", "rb"))
        for num,teacher in enumerate(teacher_list):
            print(num,teacher.name,teacher.age)

        name = input("请输入课程名称：")
        if name == "q":
            return
        num = input("请选择老师：")
        teacher = teacher_list[int(num) - 1]
        cost = input("课程费用：")
        course = Course(name,teacher.name,cost,admin_obj)
        course_list.append(course)

        if os.path.exists("course_list"):
            lists = pickle.load(open("course_list", "rb"))
            course_list.extend(lists)
        pickle.dump(course_list, open("course_list", "wb"))

        for c in pickle.load(open("course_list", "rb")):
            print(c.course_name,c.teacher_name,c.cost)


def admin_login():
    user = input("用户名：")
    pwd = input("密码：")
    import os
    if os.path.exists(user):
        admin_obj = pickle.load(open(user, "rb"))
        if admin_obj.login(user, pwd):
            inp = input("1.创建教师  2.创建课程")
            if inp == "1":
                create_teacher(admin_obj)
            elif inp == "2":
                create_course(admin_obj)
        else:
            return 1
    else:
        return 0


def main():
    inp = input("1、管理员登陆  2、管理员注册 \n >>>")
    if inp == "1":
        r = admin_login()
        if r == 1:
            print("登陆失败")
        elif r == 0:
            print("管理员不存在")

    elif inp == "2":
        user = input("注册用户名：")
        pwd = input("密码：")
        admin_obj = Admin()
        admin_obj.register(user,pwd)

if __name__ == "__main__":
    main()