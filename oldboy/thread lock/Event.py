#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading

def do(event):
    print("start")
    event.wait()
    if(event.isSet()):
        print("execute")
    else:
        print("do not execute")

event_obj = threading.Event()

for i in range(10):
    t = threading.Thread(target=do, args=(event_obj,))
    t.start()

event_obj.clear()

inp = input("input:")

if(inp == 'true'):
    event_obj.set()
elif(inp == 'false'):
    event_obj.clear()

