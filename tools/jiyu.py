#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2021/3/3 18:02
# software: PyCharm
#
# from paho.mqtt import client as mqtt_client
# import random
#
# class Test(object):
#
#     def send(self):
#         broker = 'broker.emqx.io'
#         port = 1883
#         topic = "/python/mqtt"
#         client_id = f'python-mqtt-{random.randint(0, 1000)}'


import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('10.110.87.202', 1883, 600)  # 600为keepalive的时间间隔
# client.connect('10.110.87.202', 21883, 600)  # 600为keepalive的时间间隔
pay = '{"Device gg":[{"ts":%s,"values":{"temperature":"39488"}},{"ts":%s,"values":{"humidity":"1728"}}]}'% (int(time.time() * 1000), int(time.time() * 1000))
print(pay)
print(client.publish('gateway/5330/gg/report', payload=pay , qos=0))
# client.loop_forever() # 保持连接