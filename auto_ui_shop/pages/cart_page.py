from base_page import BasePage
from selenium.webdriver.common.by import By

class CartPageLocators(object):
    """
    购物车页面的定位器
    """
    self.SELECTALL = (By.CSS_SELECTOR, ".checkbox")  # 全选按钮
    self.CART_ITEM = (By.CSS_SELECTOR, "#cartList > div > div > div > table > tbody > tr")  # 购物车中的商品项
    self.NUMS_BUY =  (By.CSS_SELECTOR, "input.bk-input.bk-is-small.bk-has-text-centered.bk-is-shadowless")
    self.PLUS = (By.CSS_SELECTOR, "i.mdi.mdi-plus")
    self.MINUS = (By.CSS_SELECTOR, "i.mdi.mdi-minus")
    self.SELECT = (By.CLASS_NAME, "bk-checkbox")  # 选择按钮
    self.DELETE = (By.CSS_SELECTOR, "i.mdi.mdi-delete-outline")  # 删除按钮
    self.CHECKOUT = (By.CSS_SELECTOR, "i.mdi.mdi-cart-check")  # 结算按钮
    self.GOTOMALL = (By.CSS_SELECTOR, "i.mdi.mdi-cart-plus")  # 继续购物按钮
    

class CartPageActions(BasePage):
    """
    购物车页面的操作方法
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CartPageLocators()

    def get_cart_items(self):
        """
        获取购物车中的商品项
        """
        return self.find_elements(self.locators.CART_ITEM)
    
    def get_cart_item(self, index):
        """
        获取购物车中的指定商品项
        """
        return self.get_cart_items()[index]

    def select_all(self):
        """
        全选购物车中的商品
        """
        self.click(self.locators.SELECTALL)

    def select_item(self, index):
        """
        选择购物车中的指定商品
        """
        self.get_cart_item(index).find_element(self.locators.SELECT).click()

    def delete_item(self, index):
        """
        删除购物车中的指定商品
        """
        self.get_cart_item(index).find_element(self.locators.DELETE).click()

    def set_input_number(self, value, index):
        """设置购买数量"""
        element = elf.get_cart_item(index).find_element(self.locators.NUMS_BUY)
        self.driver.execute_script("arguments[0].removeAttribute('readonly');", element)
        element.clear()
        element.send_keys(value)

    def get_input_number(self, index):
        """获取购买数量"""
        return self.get_cart_item(index).get_value(self.NUMS_BUY)

    def plus(self,index):
        """
        增加购买数量
        """
        self.get_cart_item(index).click(self.locators.PLUS)

    def minus(self):
        """
        减少购买数量
        """
        self.get_cart_item(index).click(self.locators.MINUS)
    
    # def get_item_price(self, index):
    #     """
    #     获取购物车中指定商品的价格
    #     """
    #     return self.get_cart_item(index).find_element(self.locators.PRICE).text
    
    def checkout(self):
        """
        结算购物车中的商品
        """
        self.click(self.locators.CHECKOUT)

    def goto_mall(self):
        """
        继续购物
        """
        self.click(self.locators.GOTOMALL)


class CartPage(CartPageActions):
    """
    购物车页面的业务逻辑
    """
    def checkout(self, indexs, nums):
        """
        结算购物车中的商品
        """
        for index in indexs:
            self.select_item(index)
            self.set_input_number(nums[index], index)
        self.checkout()