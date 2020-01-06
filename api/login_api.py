# 封装登录接口
import requests
import app


class LoginApi(object):
    """登录接口类"""

    def __init__(self):
        """获取登录接口url"""
        self.login_url = app.HOST + "/api/sys/login"
        self.headers = app.HEADERS

    def login_interface(self, mobile, password):
        """
        登录接口
        :param mobile: 外部传入的手机号
        :param password: 外部传入的密码
        :return: 接口返回的数据
        """
        data = {"mobile": mobile, "password": password}
        # 发送接口请求
        response = requests.post(self.login_url, json=data, headers=self.headers)
        return response
