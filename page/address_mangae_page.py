"""
author :Rain
Date : 2019/08/05
Description : 地址管理页面
"""
import time

import allure

from base.base_page import BasePage
from page.page_elements import PageElements


class AddressManagePage(BasePage):

    @allure.step(title='点击新增地址按钮')
    def click_new_add_address(self):
        '''新增地址'''
        self.click_element(PageElements.address_manage_new_address_btn)

    @allure.step( title='点击编辑按钮')
    def click_edite_address(self):
        '''点击编辑地址'''
        self.click_element(PageElements.address_manage_edit_btn_id)

    @allure.step(title='通过收件人姓名定位默认按钮')
    def get_default_text(self, recName):
        time.sleep(2)
        xpath = list(PageElements.address_manage_default__by_rec_xpath)[1].format(recName)
        return self.get_element(tuple(xpath)).text

    @allure.step(title='通过默认按钮定位收件人姓名和手机号')
    def get_rec_name(self):
        '''获取收件人姓名和手机号'''
        time.sleep(2)
        return self.get_element(PageElements.address_manage_recv_name_by_default_xpath).text

    @allure.step(title='修改地址')
    def update_address(self, name):
        '''
        点击修改地址
        :param name: 用户名
        :return: 
        '''''
        time.sleep(2)
        self.click_text_element(PageElements.address_manage_delete_btn_xpath, name)

    @allure.step(title='删除地址')
    def delete_address(self, name):
        '''
        点击修改地址
        :param name: 点击删除地址
        :return: 
        '''''
        self.click_text_element(PageElements.address_manage_delete_btn_xpath, name)

    @allure.step(title='获取地址详细信息')
    def get_addres_detail(self):
        """获取地址详细信息"""
        return self.get_element(PageElements.address_manage_detail_xpath).text

    @allure.step(title='获取默认按钮数量')
    def get_default_count(self):
        """获取默认数量"""
        return len(self.get_elements(PageElements.address_manage_default_id))
