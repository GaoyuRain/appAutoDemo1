"""
author :Rain
Date : 2019/08/05
Description : 新增地址页面
"""
import allure
from django.core import mail

from base.base_page import BasePage
from page.page_elements import PageElements


class AddAddressPage(BasePage):

    @allure.step(title='输入新地址信息')
    def add_new_address(self, recname=None, tel=None, areas: list = None, detailAdd=None, post_code=None,
                        isDefault=None):
        '''添加新地址'''
        allure.attach('地址信息', '收件人:{},电话号码:{},区域:{},详细地址:{},邮编:{},是否默认:{}'
                      .format(recname, tel, areas, detailAdd, mail, isDefault))
        if recname:
            self.send_element(PageElements.add_address_recv_name_id, recname)
        if tel:
            self.send_element(PageElements.add_address_phone_id, tel)

        if areas:
            self.click_element(PageElements.add_address_select_id)
            for are in areas:
                self.click_text_element(PageElements.add_address_area_title_xpath, are)
        if detailAdd:
            self.send_element(PageElements.add_address_detail_id, detailAdd)
        if mail:
            self.send_element(PageElements.add_address_post_code_id, post_code)
        if isDefault:
            self.click_element(PageElements.add_address_default_id)

        self.click_element(PageElements.add_address_save_id)
