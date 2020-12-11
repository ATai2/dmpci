#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/12/3 13:15
# software: PyCharm

import yaml, os, re
import logging
from logging.handlers import TimedRotatingFileHandler

from logging import handlers

datefmt = '%Y-%m-%d %H:%M:%S'
level = logging.DEBUG
filename = './logs/default.log'
format = '%(asctime)s [%(module)s] %(levelname)s [%(lineno)d] %(message)s'
log = logging.getLogger(filename)
format_str = logging.Formatter(format, datefmt)
# backupCount 保存日志的数量，过期自动删除
# when 按什么日期格式切分(这里方便测试使用的秒)
th = handlers.TimedRotatingFileHandler(filename=filename, when='D', backupCount=3, encoding='utf-8')
th.setFormatter(format_str)
th.setLevel(logging.INFO)
log.addHandler(th)
log.setLevel(level)


def info(msg):
    log.info(msg)
    print(msg)


def get_test_data(test_data_path):
    case = []  # 存储测试用例名称
    data = []  # 存储请求对象
    expected = []  # 存储预期结果
    with open(test_data_path, "r", encoding='utf-8') as f:
        dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = dat['tests']
        for td in test:
            case.append(td.get('case', ''))
            data.append(td.get('data', {}))
            expected.append(td.get('expected', {}))
    parameters = zip(case, data, expected)
    return case, parameters

# cases, parameters = get_test_data("../dmp/data/test_report.yml")
# list_params = list(parameters)
# print(list_params)
