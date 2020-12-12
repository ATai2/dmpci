#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/12/3 15:05
# software: PyCharm
import os, pytest, sys, time
import Config as config
from GetSession import DmpLogin

if __name__ == '__main__':
    arglengh = len(sys.argv)
    print(arglengh)

    if arglengh == 1:
        arg1 = None
        port = None
    elif arglengh == 2:
        arg1 = sys.argv[1]
        port = None
    elif arglengh == 3:
        arg1 = sys.argv[1]
        port = sys.argv[2]

    if port==None:
        port='8085'

    config.url = "http://localhost:" +port
    print(config.url)
    DmpLogin.cookieStr = None
    pytest.main(["-v", '--alluredir', './temp'])
    # pytest.main(["-v", "--html=./report.html"])
