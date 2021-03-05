#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/12/3 11:12
# software: PyCharm

from GetSession import DmpLogin


# cases, list_params = util.get_test_data("data/test_setting.yml")


# 系统管理

class TestReport:

    # 创建信息资源

    def test_create_res_dir(self):
        test = DmpLogin("http://10.110.87.233:8081")
        post = test.post_api("/catalogController/getCatalogListData",
                             data={"page": 1, "rows": 20, "searchContent": "citestresdir"})
        if post['total'] < 1:
            add_res_dir = test.post_api("/catalogController/addCatalogInfo",
                                        json={"classifyCode": "citestresdircode", "classifyName": "citestresdir",
                                              "descriptions": "",
                                              "pid": "-1", "pName": "", "contactPerson": "", "phone": "",
                                              "mobilePhone": "",
                                              "email": "", "orderid": ""})
            if add_res_dir["code"] == "200":
                return True
            else:
                return False
        return True

    def test_create_res(self):
        test = DmpLogin("http://10.110.87.233:8081")
        post = test.post_api(
            "/DataCatalogManagementController/getDataCatalogList?searchContent=citestres&page=1&rows=20",
            data={})
        if post['total'] < 1:
            add_res_dir = test.post_api("/DataCatalogManagementController/saveDataCatalog",
                                        json={"id": "", "resourceCode": "citestrescode", "resourceName": "citestres",
                                              "resourceTypeId": "6dff9677-e6bb-4f02-b501-7661359cb30b",
                                              "resourceTypeName": "", "resourceProviderSub": "",
                                              "resourceProviderCode": "citestres", "resourceProvider": "citestres",
                                              "resourceAbstract": "", "resourceFormat": "OFD", "dataitemInfo": "",
                                              "shareType": "1", "shareCondition": "", "shareMode": "接口",
                                              "shareModeType": "1", "openSociety": "0", "openCodition": "",
                                              "renewalCycle": "每日", "releaseDate": "2021-02-04",
                                              "relatedResourceCode": "", "isApproval": "9", "dataSourceRange": "",
                                              "dataCollectRange": "", "catalogDataItems": [
                                                {"id": "", "catalogId": "", "indxId": "", "dataitemName": "id",
                                                 "dataitemCode": "id", "dataitemType": "2", "dataitemLength": "",
                                                 "dataitemPrecision": "", "sortNumber": 0, "isUnstructured": "0",
                                                 "shareType": "1", "shareCondition": "", "shareMode": "接口",
                                                 "shareModeType": "1", "openSociety": "0", "openCodition": "",
                                                 "renewalCycle": "每日", "datasourceId": "", "entableId": "",
                                                 "fieldId": "", "dataStand": "", "createtime": "", "updateTime": "",
                                                 "dataitemAbstract": "", "dataitemInstruction": ""},
                                                {"id": "", "catalogId": "", "indxId": "", "dataitemName": "text",
                                                 "dataitemCode": "text", "dataitemType": "0", "dataitemLength": "1111",
                                                 "dataitemPrecision": "", "sortNumber": 1, "isUnstructured": "0",
                                                 "shareType": "1", "shareCondition": "", "shareMode": "接口",
                                                 "shareModeType": "1", "openSociety": "0", "openCodition": "",
                                                 "renewalCycle": "每日", "datasourceId": "", "entableId": "",
                                                 "fieldId": "", "dataStand": "", "createtime": "", "updateTime": "",
                                                 "dataitemAbstract": "", "dataitemInstruction": ""},
                                                {"id": "", "catalogId": "", "indxId": "", "dataitemName": "double",
                                                 "dataitemCode": "double", "dataitemType": "1", "dataitemLength": "5",
                                                 "dataitemPrecision": "2", "sortNumber": 2, "isUnstructured": "0",
                                                 "shareType": "1", "shareCondition": "", "shareMode": "接口",
                                                 "shareModeType": "1", "openSociety": "0", "openCodition": "",
                                                 "renewalCycle": "每日", "datasourceId": "", "entableId": "",
                                                 "fieldId": "", "dataStand": "", "createtime": "", "updateTime": "",
                                                 "dataitemAbstract": "", "dataitemInstruction": ""},
                                                {"id": "", "catalogId": "", "indxId": "", "dataitemName": "date",
                                                 "dataitemCode": "date", "dataitemType": "3", "dataitemLength": "",
                                                 "dataitemPrecision": "", "sortNumber": 3, "isUnstructured": "0",
                                                 "shareType": "1", "shareCondition": "", "shareMode": "接口",
                                                 "shareModeType": "1", "openSociety": "0", "openCodition": "",
                                                 "renewalCycle": "每日", "datasourceId": "", "entableId": "",
                                                 "fieldId": "", "dataStand": "", "createtime": "", "updateTime": "",
                                                 "dataitemAbstract": "", "dataitemInstruction": ""},
                                                {"id": "", "catalogId": "", "indxId": "", "dataitemName": "b",
                                                 "dataitemCode": "b", "dataitemType": "6", "dataitemLength": "",
                                                 "dataitemPrecision": "", "sortNumber": 4, "isUnstructured": "0",
                                                 "shareType": "1", "shareCondition": "", "shareMode": "接口",
                                                 "shareModeType": "1", "openSociety": "0", "openCodition": "",
                                                 "renewalCycle": "每日", "datasourceId": "", "entableId": "",
                                                 "fieldId": "", "dataStand": "", "createtime": "", "updateTime": "",
                                                 "dataitemAbstract": "", "dataitemInstruction": ""},
                                                {"id": "", "catalogId": "", "indxId": "", "dataitemName": "datetime",
                                                 "dataitemCode": "datetime", "dataitemType": "7", "dataitemLength": "",
                                                 "dataitemPrecision": "", "sortNumber": 5, "isUnstructured": "0",
                                                 "shareType": "1", "shareCondition": "", "shareMode": "接口",
                                                 "shareModeType": "1", "openSociety": "0", "openCodition": "",
                                                 "renewalCycle": "每日", "datasourceId": "", "entableId": "",
                                                 "fieldId": "", "dataStand": "", "createtime": "", "updateTime": "",
                                                 "dataitemAbstract": "", "dataitemInstruction": ""},
                                                {"id": "", "catalogId": "", "indxId": "", "dataitemName": "c",
                                                 "dataitemCode": "c", "dataitemType": "8", "dataitemLength": "",
                                                 "dataitemPrecision": "", "sortNumber": 6, "isUnstructured": "0",
                                                 "shareType": "1", "shareCondition": "", "shareMode": "接口",
                                                 "shareModeType": "1", "openSociety": "0", "openCodition": "",
                                                 "renewalCycle": "每日", "datasourceId": "", "entableId": "",
                                                 "fieldId": "", "dataStand": "", "createtime": "", "updateTime": "",
                                                 "dataitemAbstract": "", "dataitemInstruction": ""}], "insertedInfo": [
                                                {"id": "", "catalogId": "", "indxId": "", "dataitemName": "id",
                                                 "dataitemCode": "id", "dataitemType": "2", "dataitemLength": "",
                                                 "dataitemPrecision": "", "sortNumber": 0, "isUnstructured": "0",
                                                 "shareType": "1", "shareCondition": "", "shareMode": "接口",
                                                 "shareModeType": "1", "openSociety": "0", "openCodition": "",
                                                 "renewalCycle": "每日", "datasourceId": "", "entableId": "",
                                                 "fieldId": "", "dataStand": "", "createtime": "", "updateTime": "",
                                                 "dataitemAbstract": "", "dataitemInstruction": ""},
                                                {"id": "", "catalogId": "", "indxId": "", "dataitemName": "text",
                                                 "dataitemCode": "text", "dataitemType": "0", "dataitemLength": "1111",
                                                 "dataitemPrecision": "", "sortNumber": 1, "isUnstructured": "0",
                                                 "shareType": "1", "shareCondition": "", "shareMode": "接口",
                                                 "shareModeType": "1", "openSociety": "0", "openCodition": "",
                                                 "renewalCycle": "每日", "datasourceId": "", "entableId": "",
                                                 "fieldId": "", "dataStand": "", "createtime": "", "updateTime": "",
                                                 "dataitemAbstract": "", "dataitemInstruction": ""},
                                                {"id": "", "catalogId": "", "indxId": "", "dataitemName": "double",
                                                 "dataitemCode": "double", "dataitemType": "1", "dataitemLength": "5",
                                                 "dataitemPrecision": "2", "sortNumber": 2, "isUnstructured": "0",
                                                 "shareType": "1", "shareCondition": "", "shareMode": "接口",
                                                 "shareModeType": "1", "openSociety": "0", "openCodition": "",
                                                 "renewalCycle": "每日", "datasourceId": "", "entableId": "",
                                                 "fieldId": "", "dataStand": "", "createtime": "", "updateTime": "",
                                                 "dataitemAbstract": "", "dataitemInstruction": ""},
                                                {"id": "", "catalogId": "", "indxId": "", "dataitemName": "date",
                                                 "dataitemCode": "date", "dataitemType": "3", "dataitemLength": "",
                                                 "dataitemPrecision": "", "sortNumber": 3, "isUnstructured": "0",
                                                 "shareType": "1", "shareCondition": "", "shareMode": "接口",
                                                 "shareModeType": "1", "openSociety": "0", "openCodition": "",
                                                 "renewalCycle": "每日", "datasourceId": "", "entableId": "",
                                                 "fieldId": "", "dataStand": "", "createtime": "", "updateTime": "",
                                                 "dataitemAbstract": "", "dataitemInstruction": ""},
                                                {"id": "", "catalogId": "", "indxId": "", "dataitemName": "b",
                                                 "dataitemCode": "b", "dataitemType": "6", "dataitemLength": "",
                                                 "dataitemPrecision": "", "sortNumber": 4, "isUnstructured": "0",
                                                 "shareType": "1", "shareCondition": "", "shareMode": "接口",
                                                 "shareModeType": "1", "openSociety": "0", "openCodition": "",
                                                 "renewalCycle": "每日", "datasourceId": "", "entableId": "",
                                                 "fieldId": "", "dataStand": "", "createtime": "", "updateTime": "",
                                                 "dataitemAbstract": "", "dataitemInstruction": ""},
                                                {"id": "", "catalogId": "", "indxId": "", "dataitemName": "datetime",
                                                 "dataitemCode": "datetime", "dataitemType": "7", "dataitemLength": "",
                                                 "dataitemPrecision": "", "sortNumber": 5, "isUnstructured": "0",
                                                 "shareType": "1", "shareCondition": "", "shareMode": "接口",
                                                 "shareModeType": "1", "openSociety": "0", "openCodition": "",
                                                 "renewalCycle": "每日", "datasourceId": "", "entableId": "",
                                                 "fieldId": "", "dataStand": "", "createtime": "", "updateTime": "",
                                                 "dataitemAbstract": "", "dataitemInstruction": ""},
                                                {"id": "", "catalogId": "", "indxId": "", "dataitemName": "c",
                                                 "dataitemCode": "c", "dataitemType": "8", "dataitemLength": "",
                                                 "dataitemPrecision": "", "sortNumber": 6, "isUnstructured": "0",
                                                 "shareType": "1", "shareCondition": "", "shareMode": "接口",
                                                 "shareModeType": "1", "openSociety": "0", "openCodition": "",
                                                 "renewalCycle": "每日", "datasourceId": "", "entableId": "",
                                                 "fieldId": "", "dataStand": "", "createtime": "", "updateTime": "",
                                                 "dataitemAbstract": "", "dataitemInstruction": ""}], "updatedInfo": [],
                                              "deletedInfo": [], "resourceTagIds": []})
            if add_res_dir["state"] == "1":
                return True
            else:
                return False
        return True

    def test_apply_res(self):
        test = DmpLogin("http://10.110.87.233:8081")
        post = test.post_api(
            "/DataCatalogManagementController/getDataCatalogList?searchContent=citestres&page=1&rows=20",
            data={})
        if post['total'] > 0:
            add_res_dir = test.post_api("/DataCatalogManagementController/updateCatalogApprovalList?newIsApproval=4",
                                        json=[{"ID": post['rows'][0]}])
            if add_res_dir["state"] == "1":
                return True, post['rows'][0]
            else:
                return False, post['rows'][0]
        return True, post['rows'][0]

    def test_applypass_res(self, catalogId='815510e4-2d9c-46ff-9c4e-6bdfff6803c9'):
        test = DmpLogin("http://10.110.87.233:8081")

        post = test.post_api(
            "/DataCatalogManagementController/getDataCatalogList?searchContent=citestres&page=1&rows=20",
            data={})
        if len(post['rows']) == 1 and post['rows'][0]['ISAPPROVAL'] != 1:
            applypass = test.post_api(
                "/dataCatalogCheck/saveDataCatalogCheck?catalogId=" + catalogId,
                json={"isApproval": "1", "approvalOpinion": ""})

    def test_collect_task(self):
        test = DmpLogin("http://10.110.87.233:8081")
        post = test.post_api("/collectTask/getCollectTaskList", data={"page": 1, "rows": 20, "searchContent": "citest"})
        if post['total'] < 1:
            #     create
            addcollection = test.post_api("/collectTask/getCollectTaskList",
                                          data={"page": 1, "rows": 20, "searchContent": "citest"})
            respost = test.post_api(
                "/DataCatalogManagementController/getDataCatalogList?searchContent=citestres&page=1&rows=20",
                data={})
            if respost['total'] > 0:
                itempost = test.post_api(
                    "/collectTask/getDataCatalogItemList?catalogIds%5B%5D=" + post['rows'][0],
                    data={})
                itemlist = []
                for i in itempost['rows']:
                    itemlist.append({"resourceId": i['CATALOGID'],
                                     "resourceItemId": i['ID']})
                addcollection = test.post_api("/collectTask/saveCollectTask",
                                              json={"collectTaskItem": itemlist,
                                                    "id": None,
                                                    "code": "cicollect", "caption": "cicollect", "enabled": "1",
                                                    "collectTaskTimeModel": {"repeatCheck": "1", "cycleType": "3",
                                                                             "minuteSetting": "", "daySetting": "01:00",
                                                                             "weekSetting": "", "monthSetting": "",
                                                                             "yearSetting": ""},
                                                    "datacatalogIds": [post['rows'][0]]})




if __name__ == '__main__':
    b = TestReport()
    b.test_collect_task()
