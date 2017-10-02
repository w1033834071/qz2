#!/usr/bin/env python
# -*- coding:utf-8 -*-


import pickle

f = open('account.db','rb')
print(pickle.loads(f.read()))