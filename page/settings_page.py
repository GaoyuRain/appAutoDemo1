"""
author :Rain
Date : 2019/08/02
Description : 设置页面
"""
from base.base_page import BasePage
from page.page_elements import PageElements


class SettingsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def logout(self):
        '''退出'''
        self.scroll_screen()
        self.click_element(PageElements.setting_logout_btn_id)
        self.click_element(PageElements.setting_acc_logout_btn_id)
