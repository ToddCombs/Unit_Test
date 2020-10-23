# author:ToddCombs  测试套件

from demo.unit_test_openfile import *

from HTMLTestRunner import HTMLTestRunner

# 创建一个测试套件 == list
suite = unittest.TestSuite()

# 引入测试用例到测试套件，引入形式1
# suite.addTest(forTestTest('test_4'))
# suite.addTest(forTestTest('test_3'))
# suite.addTest(forTestTest('test_5'))

# 引入形式2，批量添加case
# case = [forTestTest('test_4'), forTestTest('test_3'), forTestTest('test_5')]
# suite.addTests(case)

# 引入形式3，匹配文件名为“unit_test_*.py”的正则表达式结果文件，批量执行他们所有的测试用例
# 路径可以自定义
# test_dir = './'
# discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='unit_test_*.py')

# 引入形式4，读取模块文件名来引入测试用例
# suite.addTest(unittest.TestLoader().loadTestsFromName('demo.unit_test_openfile'))  # 这里写入模块文件名而非类名

# 引入形式5，读取类名来引入测试用例
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(forTestTest))


report_path = './report/'


# 套件通过TextTestRunner对象进行运行， ≈ unittest.main()
# unittest.main()运行所有内容，而TextTestRunner仅运行选中的用例
runner = unittest.TextTestRunner()
runner.run(suite)
# 引入形式3，运行形式3
# runner.run(discover)

