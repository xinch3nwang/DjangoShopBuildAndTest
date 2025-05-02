from base.base_page import BasePage

class OrderPage(BasePage):
    """
    订单页面对象类
    """
    # 页面元素定位器
    CHECKOUT_BUTTON = ("id", "checkout-btn")
    PAYMENT_METHOD = ("css selector", "input[name='payment']")
    SUBMIT_ORDER_BUTTON = ("id", "submit-order")
    ORDER_SUCCESS_MSG = ("css selector", ".order-success")

    def __init__(self, driver):
        super().__init__(driver)

    def click_checkout(self):
        """点击结算按钮"""
        self.click(self.CHECKOUT_BUTTON)

    def select_payment_method(self, index=0):
        """选择支付方式"""
        methods = self.find_elements(self.PAYMENT_METHOD)
        if index < len(methods):
            methods[index].click()

    def click_submit_order(self):
        """点击提交订单按钮"""
        self.click(self.SUBMIT_ORDER_BUTTON)

    def get_success_message(self):
        """获取订单成功提示信息"""
        return self.get_text(self.ORDER_SUCCESS_MSG)

    def submit_order(self, payment_index=0):
        """完整订单提交流程"""
        self.click_checkout()
        self.select_payment_method(payment_index)
        self.click_submit_order()