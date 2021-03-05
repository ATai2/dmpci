#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2021/2/7 16:51
# software: PyCharm

# from smb.SMBConnection import SMBConnection
#
# server_ip = "10.100.1.163"  # 共享目录主机IP地址
# username = "Taihe Wang"  # 本机用户名
# password = "wtH@16016"  # 本机密码
# my_name = "home.langchao.com"  # 计算机属性中域名
# remote_name = ""  # 远端共享文件夹计算机名
# conn = SMBConnection(username, password, "", "", use_ntlm_v2=True)
# # conn = SMBConnection(username, password, my_name, remote_name,
# #                      is_direct_tcp=True)  # is_direct_tcp=True,默认为当direct_tcp=True时，port需要445。当它是False时，端口应该是139
# assert conn.connect(server_ip, 445)
# # sharelist = conn.listPath("00-访问指南","/")
# # for i in sharelist:
# #     print (i.filename)


from shutil import copyfile

copyfile("//10.100.1.163/产品服务器/待测库/BI待测补丁/数据管理平台2103/单元集成测试/20210201/SAP组件问题处理","sap.zip")