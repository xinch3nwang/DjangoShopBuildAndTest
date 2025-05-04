from base.base_page import BasePage
from selenium.webdriver.common.by import By


class AddressPageLocators(object):
    """
    地址页面的定位器
    """
    self.NAME = (By.NAME, "name")  # 姓名输入框
    self.PHONE = (By.NAME, "phone")  # 手机号输入框
    self.PROVINCE = (By.NAME, "province")  # 省份选择框
    self.CITY = (By.NAME, "city")  # 城市选择框
    self.DISTRICT = (By.NAME, "district")  # 区县选择框
    self.ADDRESS = (By.NAME, "address")  # 地址输入框
    self.ISDEFAULT = (By.NAME, "is_default")  # 默认地址选择框
    self.SAVE = (By.CSS_SELECTOR, ".mdi.mdi-content-save-all-outline")  # 保存按钮


class AddressPageActions(BasePage):
    """
    地址页面的操作方法
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AddressPageLocators()

    def input_name(self, name):
        """
        输入姓名
        """
        self.input(self.locators.NAME, name)

    def input_phone(self, phone):
        """
        输入手机号
        """
        self.input(self.locators.PHONE, phone)

    def input_province(self, province):
        """
        选择省份
        """
        self.input(self.locators.PROVINCE, province)

    def input_city(self, city):
        """
        选择城市
        """
        self.input(self.locators.CITY, city)

    def input_district(self, district):
        """
        选择区县
        """
        self.input(self.locators.DISTRICT, district)

    def input_address(self, address):
        """
        输入地址
        """
        self.input(self.locators.ADDRESS, address)

    def input_is_default(self):
        """
        选择默认地址
        """
        self.click(self.locators.ISDEFAULT)

    def click_save(self):
        """
        点击保存按钮
        """
        self.click(self.locators.SAVE)


class AddressPage(BasePage):
    """
    地址页面的操作方法
    """
    def edit_address(self, name, phone, province, city, district, address, is_default):
        """
        编辑地址
        """
        self.input_name(name)
        self.input_phone(phone)
        self.input_province(province)
        self.input_city(city)
        self.input_district(district)
        self.input_address(address)
        if is_default:
            self.input_is_default()
        self.click_save()
        
