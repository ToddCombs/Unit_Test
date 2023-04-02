# 停车记录重构接口压测脚本
import random
from urllib.parse import quote

import numpy as np
import pandas as pd
from locust import task, TaskSet
from locust.contrib.fasthttp import FastHttpUser


class Parking_Record(TaskSet):
    # 获取csv文件里的所有列,存储到一个数组中
    data = np.array(pd.read_csv("exercises/Locust_demo/10000_utf8.csv"))

    def on_start(self):
        '''测试套件开始时执行'''
        print("开始停车记录重构接口压测")

    @task(7)
    def search_carin(self):
        '''查询在场车停车记录-在场'''
        # 取数据时需要在data数组里指定[0]列，且由于车牌有中文，需要经过quote方法转码
        res = self.client.get(
            "carin/searchCarin?color=&plateNumber=" + quote(str(random.choice(Parking_Record.data)[0]),
                                                            encoding='UTF-8'), name='查询在场车停车记录')
        if res.status_code != 200:
            print("请求报错了啊，错误信息：", res.text)
        else:
            pass

    @task(1)
    def search_carin_nodata(self):
        '''查询在场车停车记录-不在场'''
        res = self.client.get(
            "carin/searchCarin?color=&plateNumber=Q6QD17", name='查询不在场车停车记录')
        if res.status_code != 200:
            print("请求报错了啊，错误信息：", res.text)
        else:
            pass

    def on_stop(self):
        '''在停止时运行'''
        print("压测已结束，请记得下载report")


class Parking_Record_Test(FastHttpUser):
    tasks = [Parking_Record]
    min_wait = 1000
    max_wait = 3000
    host = "http://parking-record-webc.b.sit.etcp.net/"
