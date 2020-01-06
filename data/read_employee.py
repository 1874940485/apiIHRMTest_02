import json
from app import BASE_DIR

employee_data_path = BASE_DIR + "/data/employee.json"


def read_add_emp_data():
    """添加员工接口数据"""
    data_list = list()
    with open(employee_data_path) as f:
        data = json.load(f)
        add_emp_data = data.get("add_emp")
        username = add_emp_data.get("username")
        mobile = add_emp_data.get("mobile")
        http_code = add_emp_data.get("http_code")
        success = add_emp_data.get("success")
        code = add_emp_data.get("code")
        message = add_emp_data.get("message")
        data_list.append((username, mobile, http_code, success, code, message))
    return data_list


def read_query_emp_data():
    """查询员工接口数据"""
    data_list = list()
    with open(employee_data_path) as f:
        data = json.load(f)
        query_emp_data = data.get("query_emp")
        http_code = query_emp_data.get("http_code")
        success = query_emp_data.get("success")
        code = query_emp_data.get("code")
        message = query_emp_data.get("message")
        data_list.append((http_code, success, code, message))
    return data_list


def read_modify_emp_data():
    """修改员工接口数据"""
    data_list = list()
    with open(employee_data_path) as f:
        data = json.load(f)
        modify_emp_data = data.get("modify_emp")
        username = modify_emp_data.get("username")
        http_code = modify_emp_data.get("http_code")
        success = modify_emp_data.get("success")
        code = modify_emp_data.get("code")
        message = modify_emp_data.get("message")
        data_list.append((username, http_code, success, code, message))
    return data_list


def read_delete_emp_data():
    """删除员工接口数据"""
    data_list = list()
    with open(employee_data_path) as f:
        data = json.load(f)
        delete_emp_data = data.get("delete_emp")
        http_code = delete_emp_data.get("http_code")
        success = delete_emp_data.get("success")
        code = delete_emp_data.get("code")
        message = delete_emp_data.get("message")
        data_list.append((http_code, success, code, message))
    return data_list


if __name__ == '__main__':
    print(read_add_emp_data())
    print(read_query_emp_data())
    print(read_modify_emp_data())
    print(read_delete_emp_data())
