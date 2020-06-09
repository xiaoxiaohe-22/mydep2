import requests
import unittest
from parameterized import parameterized
from api.loginApi import LoginApi
from utils import get_login_data, Utils


class TestLogin(unittest.TestCase):
    session = None

    def setUp(self):
        self.session = requests.Session()
        self.login_api = LoginApi()

    def tearDown(self):
        if self.session is not None:
            self.session.close()

    @parameterized.expand(get_login_data(Utils.get_path() + "/data/register_data.json"))
    def test_login(self, username,password,verify_code):
        data = {"username": username, "password": password, "verify_code": verify_code}
        self.login_api.login_code(self.session)
        response = self.login_api.login(data=data, session=self.session)
        self.assertIn("登陆成功", response.json().get("msg"))
        self.assertEqual(200, response.status_code)
