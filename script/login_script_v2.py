import logging
import unittest
import sys

from data.read_login_data import read_login_data
from utils import assert_common

from api.login_api import LoginApi
from parameterized import parameterized


class TestLoginScript(unittest.TestCase):
    """登录接口测试类"""

    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginApi()  # 初始化登录接口类

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @parameterized.expand(read_login_data())
    def test_login(self, mobile, password, http_code, success, code, message):
        """登录接口测试用例"""
        # 调用登录接口函数
        response = self.login_api.login_interface(mobile, password)
        # 获取接口返回数据
        json_data = response.json()
        # print("登录接口的返回数据为", json_data)
        # 获取日志信息
        logging.info("登录接口的返回数据为:{}".format(json_data))
        # 断言
        try:
            assert_common(self, response, http_code, success, code, message)
        except AssertionError as e:
            # 获取异常信息
            exc = sys.exc_info()
            # 打印异常信息
            print(exc)
            # 在日志输出异常信息
            logging.info(exc[1])
            # 抛出异常
            raise e


if __name__ == '__main__':
    unittest.main()
