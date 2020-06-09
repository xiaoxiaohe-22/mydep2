import time
import unittest

from BeautifulReport import BeautifulReport

from utils import Utils

test_suite = unittest.TestLoader().discover(start_dir=Utils.get_path() + "/script/", pattern="test*.py")
file_name = "report-{}.html".format(time.strftime("%Y%m%d%H%M%S"))
BeautifulReport(test_suite).report(description="注册和登陆的接口测试",
                                   filename=file_name,
                                   log_path=Utils.get_path() + "/report")
