from base.base_page import BasePage
from selenium.webdriver.common.by import By


class PaymentPageLocators(object):
    """
    支付页面元素定位器
    """
    def __init__(self):
        self.PAYMENT_METHOD = (By.CSS_SELECTOR, "div.bk-column.bk-is-4-desktop.bk-is-6-tablet")  # 支付方式
        self.BACK = (By.CSS_SELECTOR, "a[href='/member/orders/']")  # 返回
        self.SUBMIT = (By.ID, "pay-button")  # 提交
        self.MSG = (By.CSS_SELECTOR, ".qmsg.qmsg-wrapper.qmsg-is-initialized")  # 信息


class PaymentPageAction(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PaymentPageLocators()

    def get_payment_methods(self):
        """获取所有支付方式"""
        return self.find_elements(self.locators.PAYMENT_METHOD)

    def get_payment_method(self, index):
        """获取选中的支付方式"""
        return self.get_payment_methods()[index]
    
    def select_payment_method(self, index):
        """选择支付方式"""
        self.get_payment_method(index).click()

    def click_back(self):
        """点击返回按钮"""
        self.click(self.locators.BACK)

    def click_submit(self):
        """点击提交按钮"""
        self.click(self.locators.SUBMIT)

    def get_message(self):
        """获取提示信息"""
        return self.get_text(self.MSG)


class PaymentPage(PaymentPageAction):
    '''
    支付页面业务层
    '''
    def pay(self, index):
        """支付"""
        self.select_payment_method(index)
        self.click_submit()

    def back(self):
        """返回"""
        self.click_back()