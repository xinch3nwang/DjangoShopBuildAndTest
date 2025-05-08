from base.base_page import BasePage
from selenium.webdriver.common.by import By

class AddBrandPageLocators(object):
    """
    新增品牌页面的定位器
    """
    def __init__(self):
        self.BRAND_LOGO = (By.NAME, "image")  # 品牌logo输入框
        self.BRAND_NAME = (By.NAME, "name")  # 品牌名称输入框
        self.BRAND_DESCRIPTION = (By.NAME, "description")  # 品牌描述输入框
        self.BRAND_ORDER = (By.NAME, "order")  # 排序输入框
        self.SAVE = (By.NAME, "_save")  # 保存按钮
        self.SAVE_AND_NEXT = (By.NAME, "_addanother")
        self.SUCCESS_MESSAGE = (By.CSS_SELECTOR, "li.success")  # 成功消息

class AddBrandPageActions(BasePage):
    """
    新增品牌页面的操作方法
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AddBrandPageLocators()

    def upload_brand_logo(self, file_path):
        """
        上传品牌logo
        """
        self.upload_file(self.locators.BRAND_LOGO, file_path)
    
    def input_brand_name(self, brand_name):
        """
        输入品牌名称
        """
        self.input_text(self.locators.BRAND_NAME, brand_name)

    def input_brand_description(self, brand_description):
        """
        输入品牌描述
        """
        self.input_text(self.locators.BRAND_DESCRIPTION, brand_description)

    def input_brand_order(self, brand_order):
        """
        输入排序
        """
        self.input_text(self.locators.BRAND_ORDER, brand_order)

    def click_save_button(self):
        """
        点击保存按钮
        """
        self.click(self.locators.SAVE)

    def click_save_and_next_button(self):
        """
        点击保存并继续添加按钮
        """
        self.click(self.locators.SAVE_AND_NEXT)
    
    def get_success_message(self):
        """
        获取成功消息
        """
        return self.find_element(self.locators.SUCCESS_MESSAGE)


class AddBrandPage(AddBrandPageActions):
    """
    新增品牌页面的业务逻辑
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.actions = AddBrandPageActions(driver)

    def add_brand(self, brand_name, brand_description, brand_order, file_path):
        """
        添加品牌
        """
        self.actions.upload_brand_logo(file_path)
        self.actions.input_brand_name(brand_name)
        self.actions.input_brand_description(brand_description)
        self.actions.input_brand_order(brand_order)
        self.actions.click_save_button()

    def add_brand_and_next(self, brand_name, brand_description, brand_order, file_path):
        """
        添加品牌并继续添加
        """
        self.actions.upload_brand_logo(file_path)
        self.actions.input_brand_name(brand_name)
        self.actions.input_brand_description(brand_description)
        self.actions.input_brand_order(brand_order)
        self.actions.click_save_and_next_button()
        
        
