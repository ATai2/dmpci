#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/5/25 11:00
# software: PyCharm

import util as util
import json
import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from Rest import restPost
from selenium.webdriver.chrome.options import Options
import Config  as Config
from helium import *
import time, random

class EapLogin(object):
    cookieStr = None

    def __init__(self, url):
        if url is None:
            self.url = Config.url
        else:
            self.url = url

    def adminLogin(self):
        admin_user = "admin"
        admin_pwd = "admin@dmp1227"
        start_chrome(self.url)
        write(admin_user, into="输入账号")
        write(admin_pwd, into="输入密码")
        click("登录")


    # 登录系统，具体到自己系统时需要自行修改
    def login_system(self):
        # 登录用户名密码，改成目标系统用户名密码
        # username = "wangtaihe"
        # password = "admin@123"
        username = "admin"
        password = "admin@dmp1227"
        # 登录页面url，改成目标系统登录页面
        url = self.url + "/dmp-datafactory/#"
        util.info(url)

        try:
            self.browser.get(url)
        except Exception as e:
            util.info(e)
            self.browser.close()
        # 显性等待，直到用户名控件加载出来才进行下一步
        WebDriverWait(self.browser, 20, 0.5).until(lambda x: x.find_element_by_id("j_username"))
        # WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId"))
        # WebDriverWait(self.browser,20,0.5).until(EC.presence_of_element_located((By.ID,"j_username")))
        # 填写用户名
        self.browser.find_element_by_id("j_username").send_keys(username)
        # 填写密码
        self.browser.find_element_by_id("j_password").send_keys(password)
        # 点击登录
        self.browser.find_element_by_class_name("login-btn").click()
        # 强制等待5秒，待session和token都成功返回并存到浏览器中
        # restful隐性等待不太好用？self.browser.implicitly_wait(5)
        # time.sleep(5)

    def get_welcome(self):
        self.browser.get(self.url + "/dmp-datafactory/welcome")

    # 获取sessionid
    def get_sessionid(self):
        # 是要从localStorage中获取还是要从sessionStorage中获取，具体看目标系统存到哪个中
        # window.sessionStorage和直接写sessionStorage是等效的
        # 一定要使用return，不然获取到的一直是None
        # get的Item不一定就叫sessionId，得具体看目标系统把sessionid存到哪个变量中
        sessionid = self.browser.execute_script('return sessionStorage.getItem("sessionId");')

        # 另外sessionid一般都直接通过返回Set-Cookies头设置到Cookie中，所以也可以从Cookie读取
        # 获取浏览器所有Set-Cookie，返回对象是字典列表
        # cookies = self.browser.get_cookies()
        # 获取单项Cookie，是不是叫sessionId取决于系统存成什么变量，单项Cookie是字典
        # cookie = self.browser.get_cookie("sessionId")
        # cookie = cookie["value"]
        # print(f"{cookies}")
        # print(cookies)
        return sessionid

    def get_cookies(self):
        return self.browser.get_cookies()

    # 获取token
    def get_token(self):
        # 是要从localStorage中获取还是要从sessionStorage中获取，具体看目标系统存到哪个中
        # window.sessionStorage和直接写sessionStorage是等效的
        # 一定要使用return，不然获取到的一直是None
        # get的Item不一定就叫token，得具体看目标系统把token存到哪个变量中
        token = self.browser.execute_script('return sessionStorage.getItem("token");')
        # print(f"{token}")
        return token

    def getSettingData(self):
        url = self.url + '/dmp-datafactory/gzapi/getSettingData'
        post = restPost(url, headers=self.headers)
        return post

    def post_api(self, path, json=None, data=None):
        print("参数path" + path)
        print("参数json" + str(json))
        print("参数data" + str(data))

        url = self.url + '/dmp-datafactory' + path

        return restPost(url, headers=self.headers, json=json, data=data)

    def get_api(self, path, params=None):
        print("参数path" + path)
        print("参数params" + str(params))
        url = self.url + '/dmp-datafactory' + path
        post = requests.get(url, params=params, headers=self.headers)
        if post.status_code == 200:
            print(post.text)
            return json.loads(post.text)
        else:
            print("post error")


    def close(self):
        # 退出程序时关闭浏览器
        # self.browser.close()
        self.browser.quit()

if __name__ == "__main__":
    obj = EapLogin(None)
    try:
        obj.adminLogin()
    except Exception as e:
        print(e)
    finally:
        obj.close()

