"""
author :Rain
Date : 2019/08/02
Description : 获取各个页面对象
"""
from page.add_address_page import AddAddressPage
from page.address_mangae_page import AddressManagePage
from page.login_choice_page import LoginChoicePage
from page.login_page import LoginPage
from page.main_page import MainPage
from page.my_page import MyPage
from page.settings_page import SettingsPage


class PageUtils:
    def __init__(self, driver):
        self.driver = driver

    def get_main_page(self):
        '''主页'''
        return MainPage(self.driver)

    def get_my_page(self):
        '''我的页面'''
        return MyPage(self.driver)

    def get_login_choich_page(self):
        '''登录方式选择页面'''
        return LoginChoicePage(self.driver)

    def get_login_page(self):
        ''''登录页面'''
        return LoginPage(self.driver)

    def get_settings_page(self):
        ''''设置页面'''
        return SettingsPage(self.driver)

    def get_address_manage_page(self):
        '''地址管理页面'''
        return AddressManagePage(self.driver)

    def get_add_address_page(self):
        '''添加地址页面'''
        return AddAddressPage(self.driver)


if __name__ == '__main__':
    pass
