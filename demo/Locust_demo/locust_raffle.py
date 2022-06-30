# 抽奖接口压测
import random

import numpy as np
import pandas as pd
from icecream import ic
from locust import task, TaskSet
from locust.contrib.fasthttp import FastHttpUser


class Raffle(TaskSet):
    """抽奖执行申请、抽奖结果查询压测"""
    user_tag = np.array(pd.read_csv("demo/data/user_tag.csv"))

    def on_start(self):
        ic("开始抽奖系统接口压测。。。")

    def on_stop(self):
        ic("------ Test over ------")

    @task(1)
    def raffle_search(self):
        """
        查询抽奖结果
        :param:入参json串
        :return:返回请求时间
        """
        data = {
            "activityId": "160001",
            "drawStartTime": "2022-06-29 00:00:00",
            "drawEndTime": "2022-06-29 23:59:59",
            "userTag": str(random.choice(Raffle.user_tag)),
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/result", json=data, name="抽奖结果查询")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass


class Raffle_Run(FastHttpUser):
    tasks = [Raffle]
    min_wait = 1000
    max_wait = 3000
    host = "http://marketing-raffle-client.pc.sit.etcp.net:80/"
