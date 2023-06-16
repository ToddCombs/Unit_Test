# 简单的unittest实例
import unittest
from demo.common.my_unit import MyUnit

class TestUnittest(MyUnit):

    def test_01_todd(self):
        """测试第1条"""
        print("测试todd")

    def test_02_combs(self):
        print("测试combs")
        self.assertEqual(1, 2)

    def test_03_fraulen(self):
        print("测试fraulen")
        raise Exception("粗……粗错啦！")

    a = 18
    # 跳过用例
    @unittest.skip('这里可以输入跳过原因')
    def test_04_shen(self):
        print("测试shen")
    # 有条件跳过用例
    @unittest.skipIf(a >= 16, "条件为True跳过用例")
    def test_05_ash(self):
        print("测试ash")

    # 条件为False跳过用例
    @unittest.skipUnless(a >= 19, "条件为False跳过用例")
    def test_06_edd(self):
        print("测试edd")


if __name__ == '__main__':
    print("*********************")
    unittest.main()