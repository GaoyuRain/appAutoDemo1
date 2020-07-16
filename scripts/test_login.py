"""
author :Rain
Date : 2019/08/02
Description :登录模块测试
"""
import os
import time

import allure
import pytest
from selenium.common.exceptions import TimeoutException

from base.data_utils import DataUtils
from base.driver_utils import get_android_driver
from base.page_utils import PageUtils
from page.page_elements import PageElements


class TestLogin:

    def setup_class(self) -> None:
        self.driver = get_android_driver()
        self.page_utils = PageUtils(self.driver)
        self.login_page = self.page_utils.get_login_page()
        self.my_page = self.page_utils.get_my_page()
        self.settings_page = self.page_utils.get_settings_page()

    def teardown_class(self) -> None:
        self.driver.quit()

    @pytest.fixture(autouse=True)
    def goto_login(self):
        self.page_utils.get_main_page().click_my_btn()
        self.page_utils.get_login_choich_page().click_login_exitis_account()

    # def test_login_suc(self, test_case='hehe', username='17612136829', pwd='GAOYU0829', result='我的收藏1'):
    @pytest.mark.parametrize('test_case,username,pwd,result', DataUtils.get_login_data('login_data.yml')[0])
    def test_login_suc(self, test_case, username, pwd, result):
        '''测试登录正向用例'''
        try:
            print(test_case)
            self.login_page.login(username, pwd)
            data = self.my_page.get_shopcart_result()
            print('data', data)
            assert result in data
        except TimeoutException as e:
            print('TimeoutException')
            self.login_page.attach_pic(test_case)
            self.login_page.close_page()
            raise e
        except AssertionError as e:
            print('AssertionError')
            self.login_page.attach_pic(test_case)
            self.my_page.click_settings_btn()
            self.settings_page.logout()
            raise e
        self.my_page.click_settings_btn()
        self.settings_page.logout()

    @pytest.mark.parametrize('test_case,username,pwd,toast,result', DataUtils.get_login_data('login_data.yml')[1])
    def test_login_fail(self, test_case, username, pwd, toast, result):
        '''测试登录反向用例'''
        try:
            print(test_case)
            self.login_page.login(username, pwd)
            text = self.login_page.get_toast_text(toast)
            assert result in text
        except (TimeoutException, AssertionError) as e:
            print('test_login_fail exception')
            self.login_page.attach_pic(test_case)
            raise e
        finally:
            try:
                # 是否有登录按钮
                self.login_page.get_element(PageElements.login_btn_id)
                self.login_page.close_page()
            except TimeoutException as e1:
                print('TimeoutException1')
                self.login_page.attach_pic(test_case)
                self.settings_page.logout()
                raise e1


if __name__ == '__main__':
    pytest.main(['test_login'], '-s')
