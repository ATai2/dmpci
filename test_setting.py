#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/12/3 11:12
# software: PyCharm

import util as util
from GetSession import DmpLogin
import allure, pytest, os


# 系统管理

class TestReport:
    # @pytest.mark.parametrize("case,data,expected", list(list_params), ids=cases)
    @allure.feature('报错slaveServer信息')
    def test_save_slaveServer(self):
        test = DmpLogin()
        post = test.post_api(
            "/slaveServer/saveSlaveServer?name=kettle&hostName=127.0.0.1&port=8080&webAppName=&username=CeNTILgC6rOizgrFBjPCQQ%3D%3D&password=CeNTILgC6rOizgrFBjPCQQ%3D%3D&idSlave=&master=0",
            data=None)
        util.info(post)
        assert (post['rtCode'] == '1' or post['rtCode'] == '2')


if __name__ == '__main__':
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(["test_setting.py", '--alluredir', './temp'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ./temp -o ./report --clean')
