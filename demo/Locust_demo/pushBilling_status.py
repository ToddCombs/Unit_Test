# 大数据web服务纯接口无业务

from icecream import ic
from locust import task, TaskSet
from locust.contrib.fasthttp import FastHttpUser


class Web_Status(TaskSet):
    """纯Web服务，无业务"""

    @task(10)
    def Push_Privilege_Status(self):
        res = self.client.get("/privilege/status", name="纯web服务无业务")
        if res.status_code != 200:
            ic("出错了，错误信息：", res.text)
        else:
            ic(res.text)
            # pass


class Web_User(FastHttpUser):
    tasks = [Web_Status]
    min_wait = 1000
    max_wait = 3000
    host = "http://10.103.22.88:8090"  # qa
