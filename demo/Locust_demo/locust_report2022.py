# 2022出行报告小程序压测——shenyu
import random
import numpy as np
import pandas as pd
from icecream import ic
from locust import task, TaskSet
from locust.contrib.fasthttp import FastHttpUser


class Reporter(TaskSet):
    """
    :param:userId
    :return:res.text
    """
    data = np.array(pd.read_csv("demo/data/userid10000.csv"))

    def on_start(self):
        ic("------ 开始压测 ------")

    def on_stop(self):
        ic("------ Test over ------")

    @task(4)
    def query_parking_details(self):
        """2022年度账单接口1详细信息"""
        res = self.client.get("hp/2022/1/?user_id=" + str(random.choice(Reporter.data)[0]), name='年度账单详情接口1')
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    @task(4)
    def query_parking(self):
        """2022年度账单接口2"""
        res = self.client.get("hp/2022/2/?user_id=" + str(random.choice(Reporter.data)[0]), name='年度账单接口2')
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

    # @task(2)
    def no_result(self):
        """查询无结果测试"""
        res = self.client.get("hp/2022/" + str(random.choice([1, 2])) + "/?user_id=no_result", name='无查询结果')
        if res.status_code != 200:
            ic(res.text)
        else:
            pass

class Reporter_Run(FastHttpUser):
    tasks = [Reporter]
    min_wait = 1000
    max_wait = 3000
    host = "http://10.110.60.33:8081/"
