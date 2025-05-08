from base.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderPageLocators(object):
    """
    订单页面元素定位器
    """
    def __init__(self):
        self.ORDER_NUMBER = (By.XPATH, "//*[@id='orderDetailContent']/div[1]/ul/li[1]")  # 订单号
        self.ORDER_STATUS = (By.XPATH, "//*[@id='orderDetailContent']/div[1]/ul/li[2]")  # 订单状态

class OrderPageAction(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    def get_order_number(self):
        """获取订单号"""
        return self.get_text(self.locators.ORDER_NUMBER)[5:]

    def get_order_status(self):
        """获取订单状态"""
        return self.get_text(self.locators.ORDER_STATUS)[6:]

class OrderPage(OrderPageAction):
    '''
    订单页面业务层
    '''
    def get_order_info(self):
        """获取订单信息"""
        return {
            'order_number': self.get_order_number(),
            'order_status': self.get_order_status()
        }