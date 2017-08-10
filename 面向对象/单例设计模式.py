#!/usr/bin/env python
# -*- coding:utf-8 -*-

class ConnectionPool:

    # 创建一个静态字段  记录是否在内存中已存在实例
    __instance = None

    def __init__(self):
        self.ip = "111.111.11.11"
        self.port = 8080
        self.username = "edward"
        self.pwd = "123456789"
        # 去连接
        self.conn_list = [1,2,3,4,5,6,7,8,9]

    @staticmethod
    def get_instance():
        if ConnectionPool.__instance:
            return ConnectionPool.__instance
        else:
            ConnectionPool.__instance = ConnectionPool()
            return ConnectionPool.__instance

    def get_connection(self):
        import random
        r = random.randrange(1,10)
        return r


for i in range(1,10):
    pool = ConnectionPool.get_instance()
    print("获取连接池：", pool)
    conn = pool.get_connection()
    print("连接到：",conn)

