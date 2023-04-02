# 微信支付相关接口压测
import sys
import time

from locust import task, events, TaskSet
from locust.contrib.fasthttp import FastHttpUser


class UserBehavior(TaskSet):
    """Locust任务集，定义每个locust行为"""

    def on_start(self):
        print("微信接口压测准备。。。")

    def get_response(self, response):
        """
        获取返回
        :param response:请求返回对象
        :return:
        """
        start_time = int(time.time())
        if response.status_code == 200:
            events.request_success.fire(
                request_type="recv",
                name=sys._getframe().f_code.co_name,
                response_time=int(time.time() - start_time) * 1000,
                response_length=0
            )
        else:
            events.request_failure.fire(
                request_type="recv",
                name=sys._getframe().f_code.co_name,
                response_time=int(time.time() - start_time) * 1000,
                response_length=0,
                exception=f"Response Code Error! Code:{response.content}"
            )

    @task(1)
    def test_getqueryPayOrder(self):
        self.client.get(
            "/orderquery/1/queryPayOrder?innerorderid=4A7ED092-E22C-4B2D-9B1A-E2B7290D40FA",
            name='第三方订单查询接口（有结果）')

    @task(1)
    def test_getquertPayOrder_nodata(self):
        self.client.get(
            "/orderquery/1/queryPayOrder?innerorderid=4A7ED092-E22C-4B2D-9B1A-E2B7290D1111",
            name='第三方订单查询接口（无结果）')

    # 修改测试脚本发现单跑微信代扣请求接口会报status code 456的问题，查找外网信息发现是QA服务器nginx配置456限制速度的原因
    # 联系公司运维人员去掉nginx456限速配置，问题解决
    @task(1)
    def test_paymentRest(self):
        header = {
            "Content-Type": "application/json",
        }
        payload = {
            "appId": "wxcc603d9f0d54eaf0", "goodsTag": "", "innerOrderId": "C53129C6-634F-4F27-A0EA-2E9E60341CAF",
            "openId": "", "payAmount": "11.00", "payBusinessType": "PARKING_TEMP",
            "senceInfo": "{\"start_time\":\"2021-11-08T11:02:41+08:00\",\"plate_color\":\"BLUE\",\"device_id\":\"724\",\"end_time\":\"2021-11-08T14:05:53+08:00\",\"parking_id\":\"01000076482316363405638875052\",\"charging_duration\":10992,\"plate_number\":\"豫Q59M86\",\"parking_name\":\"李朗国际珠宝产业园\"}",
            "tradeBizInfo": {"parkingCmbClearing": False, "parkingDirectClearing": False, "parkingId": 724,
                             "parkingIsWanDa": False}}
        self.client.post("/paymentRest/crePayOrd4WxWithHoldRecord", json=payload, name='微信支付分代扣接口（无结果）')

    @task(1)
    def test_paymentRest_result(self):
        header = {
            "Content-Type": "application/json",
        }
        payload = {
            "appId": "wxd4a86d0d56b87fb4", "goodsTag": "", "innerOrderId": "2d5e0710-7b77-4960-9315-09ea47a13174",
            "openId": "", "payAmount": "0.01", "payBusinessType": "PARKING_TEMP",
            "senceInfo": "{\"start_time\":\"2021-11-05T10:24:21+08:00\",\"plate_color\":\"BLUE\",\"device_id\":\"1004043\",\"end_time\":\"2021-11-05T10:25:02+08:00\",\"parking_id\":\"01002442857816360790629175595\",\"charging_duration\":41,\"plate_number\":\"赣QG0000\",\"parking_name\":\"lhq测试车场1\"}",
            "tradeBizInfo": {"parkingCmbClearing": False, "parkingDirectClearing": False, "parkingId": 1004043,
                             "parkingIsWanDa": False}
        }
        self.client.post("/paymentRest/crePayOrd4WxWithHoldRecord", json=payload, name='微信支付分代扣接口（有结果）')

class WebUser(FastHttpUser):
    """性能测试配置"""

    tasks = [UserBehavior]
    min_wait = 1000
    max_wait = 3000
    # host = "http://newpay.qa.etcp.cn/service"


# 以下为内部接口调用方式
# class DubboTask(TaskSet):
#     def on_start(self):
#         print("RPC接口压测准备。。。")
#
#     @task(1)
#     def test_dubbo_createPayOrder4WXPublicID(self):
#         payload = {
#             "appId": "wxcc603d9f0d54eaf0", "goodsTag": "", "innerOrderId": "C53129C6-634F-4F27-A0EA-2E9E60341CAF",
#             "openId": "", "payAmount": "11.00", "payBusinessType": "PARKING_TEMP",
#             "senceInfo": "{\"start_time\":\"2021-11-08T11:02:41+08:00\",\"plate_color\":\"BLUE\",\"device_id\":\"724\",\"end_time\":\"2021-11-08T14:05:53+08:00\",\"parking_id\":\"01000076482316363405638875052\",\"charging_duration\":10992,\"plate_number\":\"豫Q59M86\",\"parking_name\":\"李朗国际珠宝产业园\"}",
#             "tradeBizInfo": {"parkingCmbClearing": False, "parkingDirectClearing": False, "parkingId": 724,
#                              "parkingIsWanDa": False}}
#         self.client.invoke_dubbo_api('createPayOrder4WXPublicID', 'payment', payload)
#
#
# class TelnetDubboClient:
#     def __init__(self, host, request_event):
#         self.caller = InvokeDubboApi(host)
#         self._request_event = request_event
#
#     def __getattr__(self, name):
#         func = partial(self.caller.invoke_dubbo_api, *functions[name])
#
#         def wrapper(*args, **kwargs):
#             request_meta = {
#                 "request_type": "telnet_dubbo",
#                 "name": name,
#                 "start_time": time.time(),
#                 "response_length": 0,
#                 "exception": None,
#                 "context": None,
#                 "response": None,
#             }
#             start_perf_counter = time.perf_counter()
#             try:
#                 request_meta["response"] = func(*args, **kwargs)
#             except Exception as e:
#                 request_meta["exception"] = e
#             request_meta["response_time"] = (time.perf_counter() - start_perf_counter) * 1000
#             self._request_event.fire(**request_meta)
#             return request_meta["response"]
#
#         return wrapper
#
#
# functions = {
#     'query_order_polling': ('cn.etcp.tradecenter.facade.QueryOrderFacade', 'queryOrderPolling'),
# }
#
#
# class TelnetRpcUser(User):
#     abstract = True
#
#     stub_class = None
#
#     def __init__(self, environment):
#         super().__init__(environment)
#         self.client = TelnetDubboClient("10.103.22.92:20992", request_event=environment.events.request)
#
#
# class MyUser(TelnetRpcUser):
#
#     @task
#     def query(self):
#         with self.client.query_order_polling({
#             'orderId': 'no161490847905910927254',
#             'batchNo': 'c7708dbe-7928-4cb9-8cf6-508adcde295b'
#         }) as rsp:
#             if rsp.code:
#                 rsp.failure(rsp.raw_response)
#
#
#
