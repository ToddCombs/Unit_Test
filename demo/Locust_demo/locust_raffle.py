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
    activityId = ['100001', '160001', '160005', '100012', '130010', '130007', '100011', '130008']
    drawStartTime = ["2022-06-23 00:00:00", "2022-06-24 00:00:00", "2022-06-25 00:00:00", "2022-06-26 00:00:00",
                     "2022-06-27 00:00:00", "2022-06-28 00:00:00", "2022-06-29 00:00:00", "2022-06-30 00:00:00",
                     "2022-07-01 00:00:00", "2022-07-02 00:00:00", "2022-07-03 00:00:00", "2022-07-04 00:00:00"]
    drawEndTime = ["2022-06-23 23:59:59", "2022-06-24 23:59:59", "2022-06-25 23:59:59", "2022-06-26 23:59:59",
                   "2022-06-27 23:59:59", "2022-06-28 23:59:59", "2022-06-29 23:59:59", "2022-06-30 23:59:59",
                   "2022-07-01 23:59:59", "2022-07-02 23:59:59", "2022-07-03 23:59:59", "2022-07-04 23:59:59"]

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
            "userType": str(random.choice([1, 2, 3]))
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

    @task(1)
    def raffle_submit_user5(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_5",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_5抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user6(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_6",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_6抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user7(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_7",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_7抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user8(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_8",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_8抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user9(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_9",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_9抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user10(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_10",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_10抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user11(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_11",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_11抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user12(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_12",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_12抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user13(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_13",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_13抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user14(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_14",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_14抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user15(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_15",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_15抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user16(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_16",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_16抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user17(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_17",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_17抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user18(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_18",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_18抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user19(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_19",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_19抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user20(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_20",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_20抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user21(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_21",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_21抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user22(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_22",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_22抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user23(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_23",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_23抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user24(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_24",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_24抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user25(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_25",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_25抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user26(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_26",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_26抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user27(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_27",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_27抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user28(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_28",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_28抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user29(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_29",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_29抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def raffle_submit_user30(self):
        """
        :param:
        :return:执行抽奖
        """
        data = {
            "activityId": "160005",
            "userTag": "user_30",
            "userType": 2
        }
        res = self.client.post("marketing/open/raffle/v1/mock/draw/perform", json=data, name="user_30抽奖")
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

class Raffle_Run(FastHttpUser):
    tasks = [Raffle]
    min_wait = 1000
    max_wait = 3000
    host = "http://marketing-raffle-client.pc.sit.etcp.net:80/"
