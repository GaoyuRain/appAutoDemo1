"""
author :Rain
Date : 2019/08/02
Description : 登录选择页面
"""
import allure

from base.base_page import BasePage
from page.page_elements import PageElements


class LoginChoicePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step(title='点击以有账户去登陆按钮')
    def click_login_exitis_account(self):
        self.click_element(PageElements.choice_login_exits_account_id)
