# 2022出行报告小程序压测
import random

from icecream import ic
from locust import task, TaskSet
from locust.contrib.fasthttp import FastHttpUser


class Reporter(TaskSet):
    """
    :param:userId
    :return:res.text
    """
    userId = [1001]

    def on_start(self):
        ic("------ 开始压测 ------")

    def on_stop(self):
        ic("------ Test over ------")

    @task(1)
    def query_parking(self):
        """2022年度账单接口1"""
        data = {
            "user_id": str(random.choice(Reporter.userId[0]))
        }
        res = self.client.post("hp/2022/1", json=data, name='年度账单接口1')

        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(1)
    def query_parking(self):
        """2022年度账单接口2"""
        data = {
            "user_id": str(random.choice(Reporter.userId[0]))
        }
        res = self.client.post("hp/2022/2", json=data, name='年度账单接口2')

        if res.status_code != 200:
            ic(res.text)
        else:
            pass

class Reporter_Run(FastHttpUser):
    tasks = [Reporter]
    min_wait = 1000
    max_wait = 3000
    host = "http://10.110.60.33:8081/"
