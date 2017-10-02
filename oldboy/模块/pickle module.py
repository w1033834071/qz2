#!/usr/bin/env python
# -*- coding:utf-8 -*-


import pickle

account = {
    1000:{
        'name':'linkwang',
        'email':'100333@qq.com',
        'passwd':'123456',
        'balance':10000,
        'phone':'1333388888',
        'bank_acc':{
            'ICBC':'2327329837289327',
            'CBC':'231323213123213'
        }
    },
    1001:{
        'name':'wang',
        'email':'100222@qq.com',
        'passwd':'123456',
        'balance':20000,
        'phone':'1888888888',
        'bank_acc':{
            'ICBC':'1127329837289327',
            'CBC':'221323213123213'
        }
    }
}

f = open('account.db','wb')
f.write(pickle.dumps(account))
f.close()

