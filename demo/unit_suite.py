# author:ToddCombs  测试套件
import os
from demo import HTMLTestRunner
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
# suite.addTest(unittest.TestLoader().loadTestsFromName('exercises.unit_test_openfile'))  # 这里写入模块文件名而非类名

# 引入形式5，读取类名来引入测试用例
# suite.addTest(unittest.TestLoader().loadTestsFromTestCase(forTestTest))

report_name = '测试报告名称'
report_title = '测试报告标题'
report_desc = '测试报告描述'
report_path = './report/'
report_file = report_path + 'report3.html'
if not os.path.exists(report_path):
    os.mkdir(report_path)
else:
    pass
with open(report_file, 'wb') as report:
    suite.addTest(unittest.TestLoader().loadTestsFromName('unit_test_openfile.forTestTest'))

    # 套件通过TextTestRunner对象进行运行， ≈ unittest.main()
    # unittest.main()运行所有内容，而TextTestRunner仅运行选中的用例
    # 如果结合HTMLTestRunner使用，则需要调用HTMLTestRunner中的运行器
    runner = HTMLTestRunner.HTMLTestRunner(stream=report, title=report_title,description=report_desc)
    runner.run(suite)


# 引入形式3，运行形式3
# runner.run(discover)
report.close()