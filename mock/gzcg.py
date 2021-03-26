#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2021/3/22 9:30
# software: PyCharm
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/gzcg/<version>/services/<apiName>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id



if __name__ == '__main__':
    app.run(port=8000)