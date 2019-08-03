"""
author :Rain
Date : 2019/08/02
Description : 登录选择页面
"""
from base.base_page import BasePage
from page.page_elements import PageElements


class LoginChoicePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_login_exitis_account(self):
        self.click_element(PageElements.choice_login_exits_account_id)
