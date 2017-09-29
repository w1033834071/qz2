#!/usr/bin/env python
# -*- coding:utf-8 -*-

import queue
import threading
import contextlib
import time

StopEvent = object()

class ThreadPool(object):

    def __init__(self, max_num, max_task_num = None):
        if(max_task_num):
            self.q = queue.Queue(max_task_num)
        else:
            self.q = queue.Queue()

        self.max_num = max_num
        self.cancel = False
        self.terminal = False
        self.generate_list = []
        self.free_list = []

    def run(self,func, args, callback=None):
        if(self.cancel):
            return

        if len(self.free_list) == 0 and len(self.generate_list) < self.max_num:
            # 创建新线程
            self.generate_thread()

        w = (func, args, callback)

        self.q.put(w)

    def generate_thread(self):
        '''
        创建一个线程
        :return:
        '''
        t = threading.Thread(target=self.call)
        t.start()


    def call(self):
        '''
        循环去获取任务函数并执行任务函数
        :return:
        '''
        current_thread = threading.currentThread()
        self.generate_list.append(current_thread)

        event = self.q.get(block=True)
        while event != StopEvent:

            func,arguments, callback = event
            try:
                result = func(* arguments)
                success = True
            except Exception as e:
                success = False
                result = None

            if callback is not None:
                try:
                    callback(success,result)
                except Exception as e:
                    pass

            with self.worker_state(self.free_list, current_thread):
                if(self.terminal):
                    event = StopEvent
                else:
                    event = self.q.get()

        else:

            self.generate_list.remove(current_thread)


    def close(self):
        '''
        执行完所有的任务后  所有线程停止
        :return:
        '''
        self.cancel = True
        full_size = len(self.generate_list)
        while full_size:
            self.q.put(StopEvent)
            full_size -= 1


    def terminate(self):
        """
        无论是否还有任务，  终止线程
        :return:
        """
        self.terminal = False

        while self.generate_list:
            self.q.put(StopEvent)

        self.q.queue.clear()

    @contextlib.contextmanager
    def worker_state(self, state_list, worker_thread):
        """
        用于记录线程中正在等待的线程数
        :param state_list:
        :param worker_thread:
        :return:
        """

        state_list.append(worker_thread)
        try:
            yield
        finally:
            state_list.remove(worker_thread)


pool = ThreadPool(5)

def callback(status, result):
    pass

def action(i):
    print(i)

for i in range(30):
    ret = pool.run(action, (i,), callback)

time.sleep(5)

print(len(pool.generate_list), len(pool.free_list))

print(len(pool.generate_list), len(pool.free_list))