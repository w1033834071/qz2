#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Pool, TimeoutError

import time
import os

def f(x):
    return x*x

if __name__ == '__main__':
    #创建4个线程
    with Pool(processes=4) as pool:

        # 打印 "[0,1,2,3,4,5.......81]"
        print(pool.map(f,range(10)))

        # 使用任意顺序输出相同的数字
        for i in pool.imap_unordered(f,range(10)):
            print(i)

        #异步执行“f(20)”
        res = pool.apply_async(f,args=(20,))  #只运行一个进程
        print(res.get(timeout=1))  # 输出400

        # 异步执行"os.getpid()"
        res = pool.apply_async(os.getpid,()) #只运行一个进程
        print(res.get(timeout=1))  #输出进程的pid

        #运行多个异步执行可能会使用多个进程
        multiple_results = [pool.apply_async(os.getpid,()) for i in range(4)]
        print([res.get(timeout=1) for res in multiple_results])

        #是一个进程睡10秒
        res = pool.apply_async(time.sleep,(10,))
        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print("发现一个multiprocessing.TimeoutError异常")

        print("目前，池中还有其他的工作")

        #退出with块中已经停止的池
        print("Now the pool is closed and no longer is available")