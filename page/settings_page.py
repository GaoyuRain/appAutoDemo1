"""
author :Rain
Date : 2019/08/02
Description : 设置页面
"""
import allure

from base.base_page import BasePage
from page.page_elements import PageElements


class SettingsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step(title='设置页面，退出操作')
    def logout(self):
        '''退出'''
        self.scroll_screen()
        self.click_element(PageElements.setting_logout_btn_id)
        self.click_element(PageElements.setting_acc_logout_btn_id)

    @allure.step(title='点击地址管理按钮')
    def click_address_btn(self):
        self.click_element(PageElements.setting_address_manage_btn_id)
