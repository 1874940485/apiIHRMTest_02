# 初始化测试套件
import time
import unittest

from app import BASE_DIR
from script.emp_all import TestEmp
from script.login import Login
from script.login_script_v2 import TestLoginScript
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
# 组装测试用例
# 员工管理测试套件
suite.addTest(unittest.makeSuite(TestEmp))
# 员工登录模块测试套件
# suite.addTest(unittest.makeSuite(TestLoginScript))
# 确认测试报告路径和报告名称
report_path = BASE_DIR + "/report/{}.html".format(time.strftime("%Y-%m-%d_%H-%M-%S"))
# 运行测试用例并生成测试报告
# with open(report_path, mode="wb") as f:
#     runner = HTMLTestRunner(stream=f, verbosity=1, title="IHRM登录接口测试", description="开发语言:Python,版本:V1.0")
#     runner.run(suite)
unittest.TextTestRunner().run(suite)
