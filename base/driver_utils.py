"""
author :Rain
Date : 2019/08/02
Description :
"""
from appium import webdriver


def get_android_driver(package='com.yunmall.lc', activity='com.yunmall.ymctoc.ui.activity.MainActivity'):
    # com.yunmall.lc/com.yunmall.ymctoc.ui.activity.MainActivity
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = 'huawei'
    # com.android.settings
    desired_caps['appPackage'] = package
    # desired_caps['appActivity'] = '.Settings'
    desired_caps['appActivity'] = activity
    desired_caps['resetKeyboard'] = True
    desired_caps['unicodeKeyboard'] = True
    desired_caps['automationName'] = 'Uiautomator2'
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
