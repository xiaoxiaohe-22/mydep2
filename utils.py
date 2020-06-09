import json
import os
import random


class Utils(object):

    # 获取项目的根目录
    @classmethod
    def get_path(cls):
        return os.path.abspath(os.path.dirname(__file__))


# 定义随机生成手机号码的方法
def get_random_phone():
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]
    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]
    # 最后八位数字
    suffix = random.randint(9999999, 100000000)
    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)


# 读取注册的数据文件register_data.json
def get_register_data(file_path):
    with open(file=file_path, encoding="utf-8") as f:
        register_list = []
        json_load = json.load(f)  # type:list
        for element in json_load:
            register_list.append(list(element.values()))
        return register_list


# 返回登陆所需的数据
def get_login_data(file_path):
    with open(file=file_path, encoding="utf-8") as f:
        register_list = []
        json_load = json.load(f)  # type:list
        for element in json_load:
            register_list.append(list(element.values()))

        # print(register_list)
        login_params = []
        for e in register_list:
            mini_list = []
            username = e[0].get("username")
            password = e[0].get("password")
            verify_code = e[0].get("verify_code")
            mini_list.append(username)
            mini_list.append(password)
            mini_list.append(verify_code)
            login_params.append(mini_list)
        return login_params



