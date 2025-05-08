from base.base_page import BasePage
from selenium.webdriver.common.by import By


class DeliverPageLocators(object):
    """
    配送页面的定位器
    """
    def __init__(self):
        self.ORDER_ITEMS = (By.CSS_SELECTOR, "#result_list > tbody > tr")  # 订单中的商品项
        self.CHECKBOX = (By.CLASS_NAME, "action-checkbox")  # 选择框
        self.ACTION_DELIVER = (By.CSS_SELECTOR, "option[value='shipments']")  # 配送按钮
        self.ACTION_DELETE = (By.CSS_SELECTOR, "option[value='delete_selected']")  # 删除按钮
        self.ACTION_VERIFY = (By.CSS_SELECTOR, "option[value='verify']")  # 核销按钮
    

class DeliverPageActions(BasePage):
    """
    配送页面的操作方法
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = DeliverPageLocators()

    def get_order_items(self):
        """
        获取订单中的商品项
        """
        return self.find_elements(self.locators.ORDER_ITEMS)

    def get_order_item(self, index):
        """
        获取订单中的指定商品项
        """
        return self.get_order_items()[index]

    def select_item(self, index):
        """
        选择订单中的指定商品
        """
        self.get_order_item(index).find_element(self.locators.CHECKBOX).click()

    def click_deliver(self):
        """
        点击配送按钮
        """
        self.click(self.locators.ACTION_DELIVER)

    def click_delete(self):
        """
        点击删除按钮
        """
        self.click(self.locators.ACTION_DELETE)

    def click_verify(self):
        """
        点击核销按钮
        """
        self.click(self.locators.ACTION_VERIFY)



class DeliverPage(BasePage):
    """
    配送页面
    """
    def deliver_order(self, index):
        """
        配送订单
        """
        self.select_item(index)
        self.click_deliver()

    def deliver_all_orders(self):
        """
        配送所有订单
        """
        for i in range(len(self.get_order_items())):
            self.deliver_order(i)
    
    def delete_order(self, index):
        """
        删除订单
        """
        self.select_item(index)
        self.click_delete()
    
    def delete_all_orders(self):
        """
        删除所有订单
        """
        for i in range(len(self.get_order_items())):
            self.delete_order(i)

    def verify_order(self, index):
        """
        核销订单
        """
        self.select_item(index)
        self.click_verify()

    def verify_all_orders(self):
        """
        核销所有订单
        """
        for i in range(len(self.get_order_items())):
            self.verify_order(i)
            