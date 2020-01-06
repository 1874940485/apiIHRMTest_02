import logging
import unittest
import sys
from utils import assert_common

from api.login_api import LoginApi


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

    def test_01_login(self):
        """登录成功接口测试用例"""
        # 调用登录接口函数
        response = self.login_api.login_interface("13800000002", "123456")
        # 获取接口返回数据
        json_data = response.json()
        print("登录接口的返回数据为", json_data)
        # 获取日志信息
        logging.info("登录接口的返回数据为:{}".format(json_data))
        # 断言
        try:
            assert_common(self, response, 200, True, 10000, "操作成功")
        except AssertionError as e:
            # 获取异常信息
            exc = sys.exc_info()
            # 打印异常信息
            print(exc)
            # 在日志输出异常信息
            logging.info(exc[1])
            # 抛出异常
            raise e

    def test_02_username_is_not_exist(self):
        """账号不存在测试用例"""
        # 调用登录接口函数
        response = self.login_api.login_interface("18625565897", "123456")
        # 获取接口返回数据
        json_data = response.json()
        print("登录接口的返回数据为", json_data)
        # 获取日志信息
        logging.info("登录接口的返回数据为:{}".format(json_data))
        # 断言
        try:
            assert_common(self, response, 200, False, 20001, "用户名或密码错误")
        except AssertionError as e:
            # 获取异常信息
            exc = sys.exc_info()
            # 打印异常信息
            print(exc)
            # 在日志输出异常信息
            logging.info(exc[1])
            # 抛出异常
            raise e

    def test_03_password_is_error(self):
        """密码错误测试用例"""
        # 调用登录接口函数
        response = self.login_api.login_interface("13800000002", "111111")
        # 获取接口返回数据
        json_data = response.json()
        print("登录接口的返回数据为", json_data)
        # 获取日志信息
        logging.info("登录接口的返回数据为:{}".format(json_data))
        # 断言
        try:
            assert_common(self, response, 200, False, 20001, "用户名或密码错误")
        except AssertionError as e:
            # 获取异常信息
            exc = sys.exc_info()
            # 打印异常信息
            print(exc)
            # 在日志输出异常信息
            logging.info(exc[1])
            # 抛出异常
            raise e

    def test_04_username_special_characters(self):
        """账号含有特殊字符测试用例"""
        # 调用登录接口函数
        response = self.login_api.login_interface("!@#$%^&*()_-+=", "111111")
        # 获取接口返回数据
        json_data = response.json()
        print("登录接口的返回数据为", json_data)
        # 获取日志信息
        logging.info("登录接口的返回数据为:{}".format(json_data))
        # 断言
        try:
            assert_common(self, response, 200, False, 20001, "用户名或密码错误")
        except AssertionError as e:
            # 获取异常信息
            exc = sys.exc_info()
            # 打印异常信息
            print(exc)
            # 在日志输出异常信息
            logging.info(exc[1])
            # 抛出异常
            raise e

    def test_05_username_is_null(self):
        """账号为空测试用例"""
        # 调用登录接口函数
        response = self.login_api.login_interface("", "111111")
        # 获取接口返回数据
        json_data = response.json()
        print("登录接口的返回数据为", json_data)
        # 获取日志信息
        logging.info("登录接口的返回数据为:{}".format(json_data))
        # 断言
        try:
            assert_common(self, response, 200, False, 20001, "用户名或密码错误")
        except AssertionError as e:
            # 获取异常信息
            exc = sys.exc_info()
            # 打印异常信息
            print(exc)
            # 在日志输出异常信息
            logging.info(exc[1])
            # 抛出异常
            raise e

    def test_06_password_is_null(self):
        """密码为空测试用例"""
        # 调用登录接口函数
        response = self.login_api.login_interface("13800000002", "")
        # 获取接口返回数据
        json_data = response.json()
        print("登录接口的返回数据为", json_data)
        # 获取日志信息
        logging.info("登录接口的返回数据为:{}".format(json_data))
        # 断言
        try:
            assert_common(self, response, 200, False, 20001, "用户名或密码错误")
        except AssertionError as e:
            # 获取异常信息
            exc = sys.exc_info()
            # 打印异常信息
            print(exc)
            # 在日志输出异常信息
            logging.info(exc[1])
            # 抛出异常
            raise e

    def test_07_username_have_chinese(self):
        """账号含有中文测试用例"""
        # 调用登录接口函数
        response = self.login_api.login_interface("1380000000中", "123456")
        # 获取接口返回数据
        json_data = response.json()
        print("登录接口的返回数据为", json_data)
        # 获取日志信息
        logging.info("登录接口的返回数据为:{}".format(json_data))
        # 断言
        try:
            assert_common(self, response, 200, False, 20001, "用户名或密码错误")
        except AssertionError as e:
            # 获取异常信息
            exc = sys.exc_info()
            # 打印异常信息
            print(exc)
            # 在日志输出异常信息
            logging.info(exc[1])
            # 抛出异常
            raise e

    def test_08_username_have_space(self):
        """账号中含有空格测试用例"""
        # 调用登录接口函数
        response = self.login_api.login_interface("13800 00002", "111111")
        # 获取接口返回数据
        json_data = response.json()
        print("登录接口的返回数据为", json_data)
        # 获取日志信息
        logging.info("登录接口的返回数据为:{}".format(json_data))
        # 断言
        try:
            assert_common(self, response, 200, False, 20001, "用户名或密码错误")
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
