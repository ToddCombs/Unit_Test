# 这是一个unittest应用的测试实例，地址和cookie仅仅是举例，实际情况需要具体分析开发
import time

from selenium import webdriver

from demo.common.my_unit import MyUnit

class TestInstance(MyUnit):

    def test_01_add_user(self):
        global driver
        # 打开浏览器
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        # 加载网页(这里的网址只是举例，实际情况需要具体分析)
        driver.get("https://www.baidu.com")
        # 通过cookie绕过登陆验证码，先手动登录，通过driver.get_cookies()函数获取登录前后的cookie，
        # 然后复制登录后的cookie信息，通过cookie绕过（解决所有的不需要第三方验证的验证码登录）
        driver.add_cookie({'name': 'xxxxxxx', 'value': 'xxxxxxx'})
        driver.add_cookie({'name': 'xxxxxxx', 'value': 'xxxxxxx'})
        driver.add_cookie({'name': 'xxxxxxx', 'value': 'xxxxxxx'})
        driver.add_cookie({'name': 'xxxxxxx', 'value': 'xxxxxxx'})
        # 睡两秒之后加载登录之后的网页
        time.sleep(2)
        # 登录之后的路径
        driver.get("https://www.baidu.com/my/index")
        driver.find_element_by_id('kw').send_keys("梅赛德斯")
        # 断言判断当前路径中是否包含后台主页的路径
        self.assertIn("my/index", driver.current_url)
