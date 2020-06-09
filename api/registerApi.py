from requests import Session


class RegisterApi(object):
    def __init__(self):
        self.code_url = "http://localhost/index.php/Home/User/verify/type/user_reg.html"
        self.register_url = "http://localhost/index.php/Home/User/reg.html"

    # 调用获取注册页面验证码接口
    def register_code(self, session):
        """
        :type session:Session
        """
        return session.get(url=self.code_url)

    # 调用注册接口
    def register(self, data, session, headers):
        """
        :type session:Session
        """
        return session.post(url=self.register_url, data=data, headers=headers)
