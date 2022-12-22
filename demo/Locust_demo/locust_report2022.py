# 2022出行报告小程序压测

from icecream import ic
from locust import task, TaskSet
from locust.contrib.fasthttp import FastHttpUser


def create_connection():

class Reporter(TaskSet):

    mobile = []
    userId = []

    def on_start(self):
        ic("------ 开始压测 ------")

    def on_stop(self):
        ic("------ Test over ------")

    @task(1)
    def query_parking(self):



class Reporter_Run(FastHttpUser):
    tasks = [Reporter]
    min_wait = 1000
    max_wait = 3000
    host = ""