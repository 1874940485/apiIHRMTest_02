import logging
import unittest

import app
from api.emp_api import EmpApi
from api.login_api import LoginApi
from data.read_employee import read_add_emp_data, read_query_emp_data, read_modify_emp_data, read_delete_emp_data
from utils import assert_common, DBUtil
from parameterized import parameterized


class TestEmp(unittest.TestCase):
    """员工增删改查测试类"""

    @classmethod
    def setUpClass(cls):
        # 初始化添加员工类
        cls.emp_api = EmpApi()
        cls.login_api = LoginApi()
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_00_login(self):
        """
        登录成功接口,员工管理依赖登录
        :return:
        """
        # 调用登录接口函数
        response = self.login_api.login_interface("13800000002", "123456")
        # 获取接口返回数据
        json_data = response.json()
        # print("登录接口的返回数据为", json_data)
        # 获取日志信息
        logging.info("登录接口的返回数据为:{}".format(json_data))
        # 断言
        assert_common(self, response, 200, True, 10000, "操作成功")
        # 获取令牌,并拼接成以bearer开头的令牌字符串,以便后续使用
        token = json_data.get("data")
        # 保存令牌到全局变量,以便员工增删改查操作使用
        app.HEADERS["Authorization"] = "Bearer " + token
        # 打印令牌信息
        logging.info("保存的令牌为:{}".format(app.HEADERS))

    @parameterized.expand(read_add_emp_data)
    def test_01_add_emp(self, username, mobile, http_code, success, code, message):
        """
        添加员工测试用例
        :return: 无
        """
        # 调用emp_api()类的实例化对象emp_api来调用方法add_emp(),发送添加员工接口
        response = self.emp_api.add_emp(username, mobile)
        # 获取返回数据
        json_data = response.json()
        # 在日志输出返回数据
        logging.info("添加后返回的数据为:{}".format(json_data))
        # 获取返回数据中,员工id,并保存到全局变量(app.py)文件中
        app.EMP_ID = json_data.get("data").get("id")
        # 调用封装的断言方法,进行断言
        assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(read_query_emp_data())
    def test_02_get_emp(self, http_code, success, code, message):
        """
        查询员工测试用例
        :return:
        """
        # 调用emp_api()类的实例化对象emp_api来调用方法get_emp(),发送查询员工接口
        response = self.emp_api.get_emp()
        # 获取返回数据
        json_data = response.json()
        #
        logging.info("查询后返回数据为:{}".format(json_data))
        # 断言
        assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(read_modify_emp_data())
    def test_03__update_emp(self, username, http_code, success, code, message):
        """
        修改员工测试用例
        :return:
        """
        # 发送修改员工接口
        response = self.emp_api.update_emp(username)
        # 获取返回数据
        json_data = response.json()
        logging.info("修改后返回的数据为:{}".format(json_data))
        # 断言
        assert_common(self, response, http_code, success, code, message)
        # 数据库操作
        with DBUtil() as db_util:
            sql = "select username from bs_user where id={}".format(app.EMP_ID)
            db_util.execute(sql)
            result = db_util.fetchone()[0]
            logging.info("数据库返回数据为:{}".format(result))
            try:
                self.assertEqual(username, result)
            except AssertionError as e:
                raise e

    @parameterized.expand(read_delete_emp_data())
    def test_04_delete_emp(self, http_code, success, code, message):
        """
        删除员工测试用例
        :return:
        """
        # 发送删除员工接口
        response = self.emp_api.delete_emp()
        # 获取返回数据
        json_data = response.json()
        # 打印日志
        logging.info("删除后返回的数据为:{}".format(json_data))
        # 断言
        assert_common(self, response, http_code, success, code, message)


if __name__ == '__main__':
    unittest.main()
