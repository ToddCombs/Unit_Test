# 运行测试时输入不同参数代表
# -H, --host：被测系统的host，若在Terminal中不进行指定，就需要在Locust子类中通过host参数进行指定；
# -f, --locustfile：指定执行的Locust脚本文件；
# -P, --port：指定web端口，默认为8089.
# 如果采用no_web形式，则需使用——no-web参数，并会用到如下几个参数:
# -c, --clients：指定并发用户数；
# -n, --num-request：指定总执行测试；
# -r, --hatch-rate：指定并发加压速率，默认值位1。

# 多进程分布式运行方式
# 不管是单机多进程，还是多机负载模式，运行方式都是一样的，都是先运行一个master，再启动多个slave。
# 启动master时，需要使用--master参数；同样的，如果要使用8089以外的端口，还需要使用-P, --port参数。
# 如果slave与master不在同一台机器上，还需要通过--master-host参数再指定master的IP地址
# $ locust -H http://debugtalk.com
#       -f exercises.py --slave --master-host=<locust_machine_ip>
from lxml import etree
from locust import HttpUser, TaskSet, task

class WebsiteTask(TaskSet):
    """
    在某些请求中，需要携带之前从Server端返回的参数，
    因此在构造请求时需要先从之前的Response中提取所需的参数。
    """
    @staticmethod
    def get_session(html):
        tree = etree.HTML(html)
        return tree.xpath("//div[@class='btnbox']/input[@name='session']/@value")[0]

    def on_start(self):
        self.index = 0

    @task
    def test_visit(self):
        url = self.locust.share_data[self.index]
        print('visit url: %s' % url)
        self.index = (self.index + 1) % len(self.locust.share_data)
        self.client.get(url)

    @task(10)
    def test_login(self):
        html = self.client.get('/login').text
        username = 'user@compay.com'
        password = '123456'
        session = self.get_session(html)
        payload = {
            'username': username,
            'password': password,
            'session': session
        }
        self.client.post('/login', data=payload)


    # def on_start(self):
    #     self.client.post("/login", {
    #         "username": "test",
    #         "password": "123456"
    #     })

    # 请求两次/ 请求一次/about/
    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def about(self):
        self.client.get("/about/")

    @task(1)
    def test_job1(self):
        self.client.get("/job1")

    @task(2)
    def test_job2(self):
        self.client.get("/job2")

    @task(1)
    def test_post(self):
        self.client.get("/post/head-first-locust-advanced-script/")


class WebsiteUser(HttpUser):

    tasks = [WebsiteTask]

    host = "http://debugtalk.com"

    # 参数化：依次传入url地址。每个虚拟用户会循环加载这100个URL地址
    share_data = ['url1', 'url2', 'url3', 'url4', 'url5']

    # 两次请求间隔1-5秒的随机值
    min_wait = 1000
    max_wait = 5000

