#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/12/3 11:12
# software: PyCharm

import util as util
from GetSession import DmpLogin
import allure, pytest, os, time
import datetime

# 系统管理

class TestReport:
    # @pytest.mark.parametrize("case,data,expected", list(list_params), ids=cases)
    @allure.feature('报错slaveServer信息')
    def test_save_slaveServer(self):
        test = DmpLogin()
        post = test.get_api(
            "/subscribemanagement/subscribelist",
            params={"size": 10, "page": 0})
        util.info(post)
        assert (post['rtCode'] == '1' or post['rtCode'] == '2')

    @allure.feature('订阅')
    def test_save_sub(self):
        test = DmpLogin()
        post = test.post_api(
            "/subscribemanagement/subscribe",
            json={"pubType": '10', "targetId": "s", "condition": ""})
        util.info(post)
        # assert (post['rtCode'] == '1' or post['rtCode'] == '2')

    @allure.feature('批量订阅')
    def test_subscribe_batch(self):
        test = DmpLogin()
        # 获得当前时间
        now = datetime.datetime.now()
        # 转换为指定的格式:
        otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
        for i in range(50):
            data = {
                'pubType': "11",
                'targetId': "12345678901234567"+otherStyleTime,
                'condition': "12345678901234567"+otherStyleTime,
                'remark': ""
            }

            post = test.post_api(
                "/subscribemanagement/subscribe",
                json=data)
            util.info(post)


if __name__ == '__main__':
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(["test_setting.py", '--alluredir', './temp'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ./temp -o ./report --clean')
