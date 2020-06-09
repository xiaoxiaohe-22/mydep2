from requests import Session


class LoginApi(object):

    def __init__(self):
        self.login_code_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    def login_code(self, session):
        """
        :type session:Session
        """
        return session.get(url=self.login_code_url)

    def login(self, data, session):
        """
        :type session:Session
        """
        return session.post(url=self.login_url, data=data)
