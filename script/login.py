import logging
import unittest
import sys

import app
from utils import assert_common

from api.login_api import LoginApi


class Login(unittest.TestCase):
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

    def test_login(self):
        """登录成功接口测试用例"""
        # 调用登录接口函数
        response = self.login_api.login_interface("13800000002", "123456")
        # 获取接口返回数据
        json_data = response.json()
        # print("登录接口的返回数据为", json_data)
        # 获取日志信息
        logging.info("登录接口的返回数据为:{}".format(json_data))
        # 断言
        assert_common(self, response, 200, True, 10000, "操作成功")
        # 获取令牌,并拼接成以bearer开头的令牌字符串
        token = json_data.get("data")
        # 保存令牌到全局变量
        app.HEADERS["Authorization"] = "Bearer " + token
        # 打印令牌信息
        logging.info("保存的令牌为:{}".format(app.HEADERS))


if __name__ == '__main__':
    unittest.main()
