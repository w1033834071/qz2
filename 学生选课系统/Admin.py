#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Teacher:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.asset = 0

class Course:

    def __init__(self,course_name,course_cost,teacher_obj):
        self.course_name = course_name
        self.course_cost = course_cost
        self.teacher_obj = teacher_obj


t1 = Teacher("Teacher1",20)
t2 = Teacher("Teacher2",21)

c1 = Course("math",1000,t1)
c2 = Course("chinese",2000,t2)


