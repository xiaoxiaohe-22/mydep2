import logging
import requests
import unittest
from parameterized import parameterized
from api.registerApi import RegisterApi
from utils import get_random_phone, get_register_data, Utils
import pymysql


class TestRegister(unittest.TestCase):
    session = None

    @classmethod
    def setUpClass(cls):
        cls.conn = pymysql.connect(host='localhost', user='root', password='root', database='tpshop2.0', port=3306)
        cls.cursor = cls.conn.cursor()

    @classmethod
    def tearDownClass(cls):
        cls.cursor.close()
        cls.conn.close()

    def setUp(self):
        self.session = requests.Session()
        self.register_api = RegisterApi()

    def tearDown(self):
        if self.session is not None:
            self.session.close()

    @parameterized.expand(get_register_data(Utils.get_path() + "/data/register_data.json"))
    def test_register(self, info, status, status_code, msg):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        # 调用注册的验证码接口并进行断言
        self.register_api.register_code(self.session)
        # 调用注册接口并进行断言
        response_register = self.register_api.register(data=info, session=self.session, headers=headers)
        logging.info("注册后respons返回json格式的结果为:{}".format(response_register.json()))
        self.assertEqual(status, response_register.json().get("status"))
        self.assertEqual(status_code, response_register.status_code)
        self.assertIn(msg, response_register.json().get("msg"))
        # 和数据库中的数据进行比较然后断言 断言方法采取的是注册的手机号码是否在返回的结果集中
        sql = "select * from tp_users where user_id = {}".format(response_register.json().get("result").get("user_id"))
        self.cursor.execute(sql)
        self.assertIn(info.get("username"), self.cursor.fetchone())
