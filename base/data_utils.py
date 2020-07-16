"""
author :Rain
Date : 2019/08/02
Description : 获取数据工具类
"""
import os

import yaml

from config import BASE_DIR


class DataUtils:

    @staticmethod
    def get_yml_data(file_name):
        file_path = BASE_DIR + os.sep + 'data' + os.sep + file_name
        with open(file_path, 'rb') as f:
            return yaml.safe_load(f)

    @staticmethod
    def get_login_data(file_name):
        '''解析登录测试数据'''
        data = DataUtils.get_yml_data(file_name)
        keys = list(data.keys())
        suc_data = []
        fail_data = []
        for key in keys:
            value = data.get(key)
            if value.get('toast'):
                fail_data.append((key, *list(value.values())))
            else:
                suc_data.append((key, *list(value.values())))
        return [suc_data, fail_data]

    @staticmethod
    def get_add_address_data(file_name):
        data = DataUtils.get_yml_data(file_name)
        keys = data.keys()
        data_list = []
        for key in keys:
            values: dict = data.get(key)
            data_list.append((key, values.get('name'), values.get('phone'), eval(values.get('area'))
                              , values.get('detail'), values.get('post_code'), values.get('isdefault')
                              , values.get('tag')))
        return data_list


if __name__ == '__main__':
    data = DataUtils.get_add_address_data('addres_data.yml')
    print(data)
