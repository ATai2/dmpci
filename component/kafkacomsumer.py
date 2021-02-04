#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2021/1/19 12:19
# software: PyCharm
import json
from kafka import KafkaProducer
from kafka import KafkaConsumer


class KafkaComponent(object):

    def produce(self):
        producer = KafkaProducer(bootstrap_servers='10.110.87.202:9092')
        msg_dict = {
            "sleep_time": 10,
            "db_config": {
                "database": "test_1",
                "host": "xxxx",
                "user": "root",
                "password": "root"
            },
            "table": "msg",
            "msg": "Hello World"
        }
        msg = json.dumps(msg_dict)
        producer.send('test_rhj', msg, partition=0)
        producer.close()


if __name__ == '__main__':
    # bean=KafkaComponent()
    # bean.produce()

    # producer = KafkaProducer(bootstrap_servers=['10.110.87.202:9092'])
    # future = producer.send('my_topic', key=b'my_key', value=b'my_value', partition=0)
    # result = future.get(timeout=10)
    # print(result)

    consumer = KafkaConsumer('my_topic', bootstrap_servers=['10.110.87.202:9092'])
    # consumer = KafkaConsumer('my_topic', group_id='group2', bootstrap_servers=['10.110.87.202:9092'])
    for msg in consumer:
        print(msg)
