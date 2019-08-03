"""
author :Rain
Date : 2019/08/02
Description : 主页
"""
from base.base_page import BasePage
from page.page_elements import PageElements


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_my_btn(self):
        self.click_element(PageElements.main_my_btn_id)
