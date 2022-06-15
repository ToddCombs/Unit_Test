# 大数据web服务纯接口无业务

from icecream import ic
from locust import task, TaskSet
from locust.contrib.fasthttp import FastHttpUser

class web_status