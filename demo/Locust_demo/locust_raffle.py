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
    activityId = ['100001', '160001']
    drawStartTime = ["2022-06-23 00:00:00", "2022-06-24 00:00:00", "2022-06-25 00:00:00", "2022-06-26 00:00:00",
                     "2022-06-27 00:00:00", "2022-06-28 00:00:00", "2022-06-29 00:00:00", "2022-06-30 00:00:00"]
    drawEndTime = ["2022-06-23 23:59:59", "2022-06-24 23:59:59", "2022-06-25 23:59:59", "2022-06-26 23:59:59",
                   "2022-06-27 23:59:59", "2022-06-28 23:59:59", "2022-06-29 23:59:59", "2022-06-30 23:59:59"]

    def on_start(self):
        ic("开始抽奖系统接口压测。。。")

    def on_stop(self):
        ic("------ Test over ------")

    # @task(1)
    def raffle_search(self):
        """
        查询抽奖结果
        :param:入参json串
        :return:返回请求时间
        """
        data = {
            "activityId": str(random.choice(Raffle.activityId)),
            "drawStartTime": str(random.choice(Raffle.drawStartTime)),
            "drawEndTime": str(random.choice(Raffle.drawEndTime)),
            "userTag": str(random.choice(Raffle.user_tag)[0]),
            "userType": ic(random.choice([1, 2, 3]))
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/result", json=data, name="抽奖结果查询")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user1(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_1",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_1抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user2(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_2",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_2抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user3(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_3",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_3抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user4(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_4",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_4抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

class Raffle_Run(FastHttpUser):
    tasks = [Raffle]
    min_wait = 1000
    max_wait = 3000
    host = "http://marketing-raffle-client.pc.sit.etcp.net:80/"
