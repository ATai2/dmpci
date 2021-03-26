#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2021/3/22 9:30
# software: PyCharmsf

from influxdb import InfluxDBClient

# client = InfluxDBClient('10.110.81.74', 8086, 'dmp', '123456', 'dmp')  # 初始化
client = InfluxDBClient('10.110.87.204', 8086, 'dmp','123456','dmp') # 初始化
print(client.get_list_database())  # 显示所有数据库名称




