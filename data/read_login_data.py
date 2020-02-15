from app import BASE_DIR
import json

login_data_path = BASE_DIR + "/data/login_data.json"


def read_login_data():
    """读取登录接口数据"""
    with open(login_data_path, mode='r', encoding="utf8") as f:
        data = json.load(f)
        data_my_list = list()
        for data in data:
            data_my_list.append((data.get("mobile"),
                                 data.get("password"),
                                 data.get('http_code'),
                                 data.get("success"),
                                 data.get("code"),
                             data.get("message")))

    print(data_my_list)
    return data_my_list


if __name__ == '__main__':
    read_login_data()