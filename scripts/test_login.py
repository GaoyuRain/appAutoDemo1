"""
author :Rain
Date : 2019/08/02
Description :登录模块测试
"""
import os
import time

import pytest
from selenium.common.exceptions import TimeoutException

from base.data_utils import DataUtils
from base.driver_utils import get_android_driver
from base.page_utils import PageUtils


class TestLogin:

    def setup_class(self) -> None:
        self.driver = get_android_driver()
        self.page_utils = PageUtils(self.driver)

    def teardown_class(self) -> None:
        self.driver.quit()

    @pytest.fixture(autouse=True)
    def goto_login(self):
        self.page_utils.get_main_page().click_my_btn()
        self.page_utils.get_login_choich_page().click_login_exitis_account()

    # def test_login_suc(self, test_case='hehe', username='17612136829', pwd='GAOYU0829', result='我的收藏1'):
    @pytest.mark.parametrize('test_case,username,pwd,result', DataUtils.get_login_data('login_data.yml')[0])
    def test_login_suc(self, test_case, username, pwd, result):
        try:
            print(test_case)
            self.page_utils.get_login_page().login(username, pwd)
            data = self.page_utils.get_my_page().get_shopcart_result()
            print('data', data)
            assert result in data
        except TimeoutException as e:
            print('TimeoutException')
            self.page_utils.get_login_page().attach_pic('test_login_suc')
            self.page_utils.get_login_page().close_page()
            raise e
        except AssertionError as e:
            print('AssertionError')
            self.page_utils.get_login_page().attach_pic('test_login_suc')
            self.page_utils.get_my_page().click_settings_btn()
            self.page_utils.get_settings_page().logout()
            raise e
        self.page_utils.get_my_page().click_settings_btn()
        self.page_utils.get_settings_page().logout()

    # def test_login_fail(self):
    #     pass


if __name__ == '__main__':
    pytest.main(['test_login'], '-s')
