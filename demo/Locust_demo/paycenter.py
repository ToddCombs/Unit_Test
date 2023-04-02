import time
from functools import partial

from locust import User
from locust.user import task

from demo import InvokeDubboApi

functions = {
    'query_order_polling': ('cn.etcp.tradecenter.facade.QueryOrderFacade', 'queryOrderPolling'),
}


class TelnetDubboClient:
    def __init__(self, host, request_event):
        self.caller = InvokeDubboApi(host)
        self._request_event = request_event

    def __getattr__(self, name):
        func = partial(self.caller.invoke_dubbo_api, *functions[name])

        def wrapper(*args, **kwargs):
            request_meta = {
                "request_type": "telnet_dubbo",
                "name": name,
                "start_time": time.time(),
                "response_length": 0,
                "exception": None,
                "context": None,
                "response": None,
            }
            start_perf_counter = time.perf_counter()
            try:
                request_meta["response"] = func(*args, **kwargs)
            except Exception as e:
                request_meta["exception"] = e
            request_meta["response_time"] = (time.perf_counter() - start_perf_counter) * 1000
            self._request_event.fire(**request_meta)
            return request_meta["response"]

        return wrapper


class TelnetRpcUser(User):
    abstract = True

    stub_class = None

    def __init__(self, environment):
        super().__init__(environment)
        self.client = TelnetDubboClient("10.103.22.92:20992", request_event=environment.events.request)


class MyUser(TelnetRpcUser):

    @task
    def query(self):
        with self.client.query_order_polling({
            'orderId': 'no161490847905910927254',
            'batchNo': 'c7708dbe-7928-4cb9-8cf6-508adcde295b'
        }) as rsp:
            if rsp.code:
                rsp.failure(rsp.raw_response)
