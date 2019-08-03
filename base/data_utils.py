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


if __name__ == '__main__':
    data = DataUtils.get_login_data('login_data.yml')
    print(data)
