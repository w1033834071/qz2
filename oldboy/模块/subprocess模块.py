#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess

# subprocess.call("ipconfig")

ret = subprocess.check_output("ipconfig")
print(ret.decode(encoding="gb2312"))