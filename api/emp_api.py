# 封装添加员工接口
import requests
import app


class EmpApi(object):
    """添加员工接口"""

    def __init__(self):
        """添加员工接口url"""
        self.emp_url = app.HOST + "/api/sys/user"
        # 获取请求头
        self.headers = app.HEADERS

    def add_emp(self, username, mobile):
        """
        添加员工接口
        :param username: 添加员工的用户名
        :param mobile: 添加员工的手机号
        :return: 接口返回的数据
        """
        data = {"username": username,
                "mobile": mobile,
                "timeOfEntry": "2019-12-02",
                "formOfEmployment": 1,
                "workNumber": "1234",
                "departmentName": "测试",
                "departmentId": "1210411411066695680",
                "correctionTime": "2019-12-15T16:00:00.000Z"}
        # 发送添加员工请求
        response = requests.post(self.emp_url, json=data, headers=self.headers)
        return response

    def get_emp(self):
        """
        查询员工接口
        :return: 返回查询到的员工信息
        """
        url = self.emp_url + "/" + app.EMP_ID

        # 发送查询员工接口,需要加headers
        response = requests.get(url, headers=self.headers)
        return response

    def update_emp(self, username):
        """
        修改员工接口
        :param username: 修改后的用户名
        :return: 修改后返回数据
        """
        url = self.emp_url + "/" + app.EMP_ID

        data = {"username": username}
        # 发送修改员工接口,需要加headers
        response = requests.put(url, json=data, headers=self.headers)
        return response

    def delete_emp(self):
        """
        删除员工
        :return: 删除后返回数据
        """
        url = self.emp_url + "/" + app.EMP_ID
        # 发送删除员工接口,需要加headers
        response = requests.delete(url, headers=self.headers)
        return response
