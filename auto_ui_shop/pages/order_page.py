from base.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderPageLocators(object):
    """
    订单页面元素定位器
    """
    CHECKOUT_BUTTON = (By.ID, "checkout-btn")  # 结算按钮
    ADDRESS = (By.ID, "address")  # 地址输入框


class OrderPageActions(BasePage):
    """
    订单页面操作类
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    def click_checkout(self):
        """点击结算按钮"""
        self.click(self.locators.CHECKOUT_BUTTON)
    
    def get_addresses(self):
        """获取所有地址"""
        return self.find_elements(self.locators.ADDRESS)

    def get_address(self, index):
        """获取选中的地址"""
        return self.get_addresses()[index]

    def click_address(self, index):
        """点击地址"""
        self.get_address(index).click()


class OrderPage(OrderPageActions):
    """
    订单页面业务层
    """
    def checkout(self):
        """完成订单流程"""
        self.click_checkout()

    def select_address(self, index):
        """选择地址"""
        self.click_address(index)