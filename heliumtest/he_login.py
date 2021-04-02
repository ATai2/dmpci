#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2021/4/2 11:09
# software: PyCharm


from helium import *

import time,random


class Test(object):

    def __init__(self):
        self.randomtrans=random.random(0,1000)

    def login(self):
        start_chrome("http://10.110.87.200:8912/")
        write("d", into="输入账号")
        write("asdf@1234", into="输入密码")
        click("登录")

    def mongoinout(self):
        hover("数据中台")
        click("数据加工厂")
        click("设计区")
        click("工厂分层")
        rightclick("ODS操作数据")

        click("新建ETL")
        click("ETL转换")

        click("添加")















if __name__ == '__main__':
    bean = Test()
    bean.login()
    time.sleep(100)
    kill_browser()
