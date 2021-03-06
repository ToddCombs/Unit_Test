# author:ToddCombs
import unittest
import time
from selenium import webdriver
from ddt import ddt, data, unpack, file_data
import yaml

def readFile():
    # 定义一个list集合
    params = []
    # 通过open打开参数文档，以读取的形式，编码格式为utf-8，兼容中文文本
    file = open('params.txt', 'r', encoding='utf-8')
    for line in file.readlines():
        # list中添加元素，("梅赛德斯","宝马")
        params.append(line.strip('\n').split(','))

    return params

@ddt
class forTestTest(unittest.TestCase):
    def setUp(self) -> None:
    #     self.b = webdriver.Chrome()
        pass

    def tearDown(self) -> None:
        # time.sleep(5)
        # self.b.quit()
        pass

    # @data(*readFile())
    # @unpack
    # def test_1(self, txt, url):
    #     self.b.get(url)
    #     self.b.find_element_by_id('kw').send_keys(txt)
    #     self.b.find_element_by_id('su').click()
    # @data(*readFile())
    # @unpack  # unpack传入两个或多个参数

    # @file_data('ppp.yml')  # 文件读取操作
    # def test_2(self, **kwargs):
    #     # 获取参数中key为name的value
    #     name = kwargs.get('name')
    #     print(name)
    #     self.assertEqual(name, 'Mercedes', msg='NotEqual')
    #     print(kwargs.get('text'))
    #     print('**************************')

    # 无条件跳过执行该条用例
    # @unittest.skip('这里输入跳过的理由')
    def test_3(self):
        print('1')

    # 有条件执行跳过操作，当判断条件为True时，执行跳过
    # @unittest.skipIf(1 < 2, '这里是if的理由')
    def test_4(self):
        print('2')

    # 有条件执行跳过操作，当判断条件为False时，执行跳过
    # @unittest.skipUnless(1 > 2, '这里是Unless的理由')
    def test_5(self):
        print('3')

    # 如果用例执行失败，则不计入失败的Case数中
    # @unittest.expectedFailure
    def test_6(self):
        print('4')
        # 基本布尔断言，验证arg1是否等于arg2，不等则输出msg
        self.assertEqual(4, 3, msg='notEqual')

    def test_7(self):
        print('5')
        # 验证arg1是否不等于arg2，相等则输出msg
        self.assertNotEqual(21, 22, msg='equal')

    def test_8(self):
        print('6')
        # 验证arg1大于arg2，否则fail
        self.assertGreater(2, 1, msg='None')

    def test_9(self):
        print('7')
        # 验证arg1大于等于arg2，否则fail
        self.assertGreaterEqual(2, 2, msg='None')

    def test_10(self):
        print('8')
        # 比较断言，验证arg1是否约等于arg2，places指精确到小数点后多少位，默认为7
        self.assertAlmostEqual(100, 101, places=7, msg='notEqual')

    def test_11(self):
        print('9')
        # 比较布尔类型是否为True，否则返回msg
        self.assertTrue(1 + 2 == 4)

    def test_12(self):
        print('10')
        # 比较布尔类型是否为False，否则返回msg
        self.assertFalse(1 + 2 == 4)



if __name__ == '__main__':
    unittest.main()