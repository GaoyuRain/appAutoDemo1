"""
author :Rain
Date : 2019/08/02
Description : 个人中心页面
"""
import allure

from base.base_page import BasePage
from page.page_elements import PageElements


class MyPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_shopcart_result(self):
        result = self.get_element(PageElements.my_shopcart_id).text
        allure.attach('定位收藏按钮：', result)
        return result

    @allure.step(title='点击设置按钮')
    def click_settings_btn(self):
        self.click_element(PageElements.my_setting_btn_id)
