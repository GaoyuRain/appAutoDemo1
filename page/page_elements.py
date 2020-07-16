from selenium.webdriver.common.by import By


class PageElements:
    """首页"""
    # 我 com.yunmall.lc:id/tab_me com.yunmall.lc:id/tab_me
    main_my_btn_id = (By.ID, "com.yunmall.lc:id/tab_me")

    """登录选择页面"""
    # 已有账号去登录
    choice_login_exits_account_id = (By.ID, "com.yunmall.lc:id/textView1")

    """登录页面"""
    # 用户名
    login_name_id = (By.ID, "com.yunmall.lc:id/logon_account_textview")
    # 密码
    login_passwd_id = (By.ID, "com.yunmall.lc:id/logon_password_textview")
    # 登录按钮
    login_btn_id = (By.ID, "com.yunmall.lc:id/logon_button")
    # toast消息
    toast_xpath = (By.XPATH, "//*[contains(@text,'密码错误')]")
    # x 按钮
    x_btn_id = (By.ID, 'com.yunmall.lc:id/ymtitlebar_left_btn_image')

    """个人中心页面"""
    # 我的收藏 com.yunmall.lc:id/txt_my_shoppingcart
    my_shopcart_id = (By.ID, "com.yunmall.lc:id/txt_my_shoppingcart")
    # 设置按钮
    my_setting_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")

    """设置页面"""
    # 退出按钮
    setting_logout_btn_id = (By.ID, "com.yunmall.lc:id/setting_logout")
    # 确认退出按钮
    setting_acc_logout_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_right_button")
    # 取消退出按钮
    setting_dis_logout_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_left_button")
    # 地址管理
    setting_address_manage_btn_id = (By.ID, "com.yunmall.lc:id/setting_address_manage")

    """地址管理页面"""
    # 新增地址 com.yunmall.lc:id/address_add_new_btn
    address_manage_new_address_btn = (By.ID, "com.yunmall.lc:id/address_add_new_btn")
    # 编辑按钮
    address_manage_edit_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_right_btn")
    # 修改按钮
    address_manage_update_btn_xpath = (
    By.XPATH, "//*[contains(@text,'{}')]/../following-sibiling::*/*[contains(@text,'修改')]")
    # 删除按钮
    address_manage_delete_btn_xpath = (
    By.XPATH, "//*[contains(@text,'{}')]/../following-sibiling::*/*[contains(@text,'删除')]")
    # 收件人姓名 通过默认取
    address_manage_recv_name_by_default_xpath = (By.XPATH, "//*[contains(@text,'默认')]/../preceding-sibling::*")
    # 详细地址 通过默认取
    address_manage_detail_xpath = (By.XPATH, "//*[contains(@text,'默认')]/following-sibling::*")
    # 默认 通过收件人姓名
    address_manage_default__by_rec_xpath = (
        By.XPATH, "//*[contains(@text'{}')]/following-sibling::*/*[contains(@text,'默认')]")
    # 默认
    address_manage_default_id = (By.ID, "com.yunmall.lc:id/address_is_default")

    """新增地址页面"""
    # 收件人
    add_address_recv_name_id = (By.ID, "com.yunmall.lc:id/address_receipt_name")
    # 手机号
    add_address_phone_id = (By.ID, "com.yunmall.lc:id/address_add_phone")
    # 所在地区
    add_address_select_id = (By.ID, "com.yunmall.lc:id/address_province")
    # 区域标题
    add_address_area_title_xpath = (By.XPATH, "//*[contains(@text,'{}')]")
    # 详细地址
    add_address_detail_id = (By.ID, "com.yunmall.lc:id/address_detail_addr_info")
    # 邮编
    add_address_post_code_id = (By.ID, "com.yunmall.lc:id/address_post_code")
    # 设为默认地址
    add_address_default_id = (By.ID, "com.yunmall.lc:id/address_default")
    # 保存按钮
    add_address_save_id = (By.ID, "com.yunmall.lc:id/button_send")
