#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/12/3 11:12
# software: PyCharm

import util as util
from GetSession import DmpLogin
import json
import pytest
import Config as config

cases, list_params = util.get_test_data("data/test_report.yml")


class TestReport:
    @pytest.mark.parametrize("case,data,expected", list(list_params), ids=cases)
    def test_save_settingdata(self, case, data, expected):
        test = DmpLogin()
        setting_data = test.getSettingData()
        try:
            setting = json.loads(setting_data)
            data['id'] = setting['data']['basicInfoMap']['id']
            post = test.post_api("/gzapi/save", json=data)
            util.info(post)
        except Exception as e:
            util.info(e)
            post = test.post_api("/gzapi/save", json=data)
            util.info(post)

        assert post['rs'] == expected['rs']

    def test_report_test(self):
        data = {"id": "cdbe81ca-2f6c-4654-9c2d-14c9a42eb8bf", "ip": None, "port": None, "reportAgency": "云南国资委",
                "socialCreditCode": "1153000075718792X1", "apiCode": "SZ01", "userName": "Seq0vAPlI4kxaO82PA+VUA==",
                "userPasswd": "Seq0vAPlI4kxaO82PA+VUA==", "preUserName": "Seq0vAPlI4kxaO82PA+VUA==",
                "preUserPasswd": "Seq0vAPlI4kxaO82PA+VUA==", "uploadPath": "mvwO1O0sV9zehtOkSNf+IQ==",
                "downLoadPath": "92FbnU6mnuHwExgtaXhj1A==",
                "uploadUrl": "http://10.72.86.255:9010/preposed-machine/api/services/fileUpload",
                "catalogUrl": "http://10.72.86.255:9010/preposed-machine/api/services/tempDownload",
                "noticeUrl": "http://10.72.86.255:9010/preposed-machine/api/services/noticeDownload",
                "keyUrl": "http://10.72.86.255:9010/preposed-machine/api/services/keyDownload",
                "taskUrl": "http://10.72.86.255:9010/preposed-machine/api/services/taskDwonload",
                "logUrl": "http://10.72.86.255:9010/preposed-machine/api/services/logDownload", "acceptDataUrl": "",
                "prePollFileUrl": "http://127.0.0.1:8099/preposed-machine/api/superior/pollUploadFile",
                "preCatalogUrl": "", "preNoticeUrl": "", "preKeyUrl": "", "preTaskUrl": "", "preDataUrl": "",
                "preStatusUrl": "", "prePointConnUrl": "",
                "sm2Key": "B3516EC7813953B0953191884DC8BF3DA8C06F0001CC0A1B881E54A16881A4C44DBA333E388FF876CE4BD105EB4A4B03A72E9BD5BD8DEA68E6058B6A62B52CB6",
                "sm4Key": "7da306cb558948dab67f287d2b8f0f8e", "superiorSM2Key": "", "sm2PrivateKey": "", "modeWay": "1",
                "gridData": "[{\"businessCaption\":\"省国资委采集目录\",\"businessLabel\":\"0037\",\"reportPath\":\"\"},{\"businessCaption\":\"反馈文件\",\"businessLabel\":\"0007\",\"reportPath\":\"\"},{\"businessCaption\":\"静态文件\",\"businessLabel\":\"0002\",\"reportPath\":\"\"}]"}
        test = DmpLogin()
        setting_data = test.getSettingData()
        try:
            setting = json.loads(setting_data)
            data['id'] = setting['data']['basicInfoMap']['id']
            post = test.post_api("/gzapi/save", json=data)
            util.info(post)
        except Exception as e:
            util.info(e)
            post = test.post_api("/gzapi/save", json=data)
            util.info(post)

        assert post['rs'] == '1'



if __name__ == '__main__':
    config.url=""
