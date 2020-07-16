"""
author :Rain
Date : 2019/08/02
Description : 登录页面
"""
import allure

from base.base_page import BasePage
from page.page_elements import PageElements


class LoginPage(BasePage):
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, driver):
        if not LoginPage.init_flag:
            # self.xBtn = None
            super().__init__(driver)
            LoginPage.init_flag = True

    @allure.step(title='登录')
    def login(self, username, pwd):
        '''登录'''
        allure.attach('登录信息', '用户名：{},密码：{}'.format(username, pwd))
        self.send_element(PageElements.login_name_id, username)
        self.send_element(PageElements.login_passwd_id, pwd)
        self.click_element(PageElements.login_btn_id)

    # def find_x_btn(self):
    #     if self.xBtn is None:
    #         print('init xBtn')
    #         self.xBtn = self.get_element(PageElements.x_btn_id)
    #     return self.xBtn
    @allure.step(title='关闭登录页面')
    def close_page(self):
        self.click_element(PageElements.x_btn_id)


if __name__ == '__main__':
    pass
