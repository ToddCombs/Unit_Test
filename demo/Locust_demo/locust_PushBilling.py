# 大数据推送账单查费接口压测

import random
from urllib.parse import quote
import numpy as np
import pandas as pd
import openpyxl

from locust import task, TaskSet
from locust.contrib.fasthttp import FastHttpUser


class pushBilling(TaskSet):

    data_w = np.array(pd.read_excel(""))

    def on_start(self):
        print("开始压测推送账单接口周月季。。。")

    def on_stop(self):
        print("推送账单接口压测停止")

    @task(1)
    def push_bill_w(self):
        self.client.get("/push_bill?user_id=23555438&plate_number=藏Q6QD177&p_t=w", name="周推送")

    @task(1)
    def push_bill_m(self):
        self.client.get("/push_bill?user_id=23555438&plate_number=藏Q6QD177&p_t=m", name="月推送")

    @task(1)
    def push_bill_q(self):
        self.client.get("/push_bill?user_id=23555438&plate_number=藏Q6QD177&p_t=q", name="季推送")


class pushUser(FastHttpUser):
    tasks = [pushBilling]
    min_wait = 1000
    max_wait = 3000
    host = "http://10.103.22.88:8090/hp"  # qa
