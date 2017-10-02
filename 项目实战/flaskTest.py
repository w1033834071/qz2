#!/usr/bin/env python
# -*- coding:utf-8 -*-

# it can work!
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run()