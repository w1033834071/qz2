#!/usr/bin/env python
# -*- coding:utf-8 -*-


import pickle

account_file = open('account.db','rb')
account_dic = pickle.loads(account_file.read())
account_file.close()
#修改余额后写入
account_dic[1000]['balance'] -= 500
account_file = open('account.db','wb')
account_file.write(pickle.dumps(account_dic))
account_file.close()

