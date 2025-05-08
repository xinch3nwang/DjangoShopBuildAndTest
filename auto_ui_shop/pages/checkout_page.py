from base.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutPageLocators(object):
    """
    创建订单页面元素定位器
    """
    def __init__(self):
        self.CHECKOUT_BUTTON = (By.ID, "create-order-btn")  # 结算按钮
        self.ADDRESS = (By.CSS_SELECTOR, ".bk-is-clickable.address-box")  # 地址输入框


class CheckoutPageActions(BasePage):
    """
    创建订单页面操作类
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CheckoutPageLocators()

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


class CheckoutPage(CheckoutPageActions):
    """
    创建订单页面业务层
    """
    def checkout(self, index):
        """完成创建订单流程"""
        self.click_address(index)
        self.click_checkout()