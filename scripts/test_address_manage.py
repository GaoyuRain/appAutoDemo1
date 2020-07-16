"""
author :Rain
Date : 2019/08/05
Description : 测试地址管理
"""

import pytest

from base.data_utils import DataUtils
from base.driver_utils import get_android_driver
from base.page_utils import PageUtils


class TestAddressManger:

    def setup_class(self) -> None:
        self.driver = get_android_driver()
        self.page_utils = PageUtils(self.driver)
        self.address_manage_page = self.page_utils.get_address_manage_page()

    def teardown_class(self) -> None:
        self.driver.quit()

    @pytest.fixture(scope='class', autouse=True)
    def go_add_address(self):
        self.page_utils.get_main_page().click_my_btn()
        self.page_utils.get_login_choich_page().click_login_exitis_account()
        self.page_utils.get_login_page().login('17612136829', 'GAOYU0829')
        self.page_utils.get_my_page().click_settings_btn()
        self.page_utils.get_settings_page().click_address_btn()

    @pytest.mark.parametrize('case_num,name,phone,area,detail,post_code,isdefault,tag',
                             DataUtils.get_add_address_data('addres_data.yml'))
    def test_add_address_suc(self, case_num, name, phone, area, detail, post_code, isdefault, tag):
        '''test_add_address_suc'''
        print('test_add_address_suc')
        self.address_manage_page.click_new_add_address()
        self.page_utils.get_add_address_page().add_new_address(name, phone, area, detail, post_code, isdefault)
        name_phone = self.address_manage_page.get_rec_name()
        if tag:
            assert name in name_phone
        else:
            assert self.address_manage_page.get_default_count() == 1
            assert name not in name_phone


if __name__ == '__main__':
    pytest.main([''], '-s')
