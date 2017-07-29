#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys,os


dirname = os.path.dirname(__file__)
dirname2 = os.path.dirname(dirname)

s = "lib"

module_path = os.path.join(dirname2,s)

sys.path.append(module_path)

import my_module
