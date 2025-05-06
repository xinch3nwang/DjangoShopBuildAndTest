from base.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPageLocators(object):
    """
    商品页元素定位器
    """
    def __init__(self):
        self.PRICE = (By.CSS_SELECTOR, "#skuApp > section > div > div > p.bk-is-size-3.bk-has-text-weight-bold")
        self.NUMS_BUY =  (By.CSS_SELECTOR, "input.bk-input.bk-is-small.bk-has-text-centered.bk-is-shadowless")
        self.PLUS = (By.CSS_SELECTOR, "i.mdi.mdi-plus")
        self.MINUS = (By.CSS_SELECTOR, "i.mdi.mdi-minus")
        self.SPUS = (By.CSS_SELECTOR, "p.bk-control > button.bk-button.bk-is-small")
        self.SPU_COUNT = (By.CSS_SELECTOR, "#skuApp > div:nth-child(2) > div > div:nth-child(3) > p > button")
        self.ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.bk-button.bk-is-link.px-6.bk-is-shadowless")
        self.BUY_BUTTON = (By.XPATH, "//*[@id='skuApp']/div[2]/div/p[2]/button")
        self.CART_SUCCESS = (By.CSS_SELECTOR, "div.qmsg-item")


class ProductPageAction(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProductPageLocators()

    def get_spus(self):
        """获取所有规格"""
        return self.find_elements(self.locators.SPUS)
    
    def get_spu(self, index):
        """获取选中的规格"""
        return self.get_spus()[index]

    def get_price(self):
        """获取商品价格"""
        return self.get_text(self.locators.PRICE)

    def add_to_cart(self):
        """将商品加入购物车"""
        self.click(self.locators.ADD_TO_CART_BUTTON)

    def buy(self):
        """立即购买商品"""
        self.click(self.locators.BUY_BUTTON)

    def get_spu_count(self):
        """获取库存数量"""
        return int(self.get_text(self.CART_COUNT)[3:])

    def set_input_number(self, value):
        """设置购买数量"""
        element = self.find_element(self.locators.NUMS_BUY)
        self.driver.execute_script("arguments[0].removeAttribute('readonly');", element)
        element.clear()
        element.send_keys(value)

    def get_input_number(self):
        """获取购买数量"""
        return self.get_value(self.NUMS_BUY)

    def click_plus(self):
        """点击增加按钮"""
        self.click(self.PLUS)

    def click_minus(self):
        """点击减少按钮"""
        self.click(self.MINUS)
    
    def get_cart_success(self):
        """获取购物车成功提示"""
        if self.get_text(self.locators.CART_SUCCESS)=='添加购物车成功':
            return True
        else:
            return False


class ProductPage(ProductPageAction):
    '''
    商品页业务层
    '''
    def add_to_cart_with_spus(self, count, index):
        """将商品加入购物车"""
        for i in index:
            self.get_spu(i).click()
        self.set_input_number(count)
        self.add_to_cart()

    def buy_with_spus(self, count, index):
        """立即购买商品"""
        for i in index:
            self.get_spu(i).click()
        self.set_input_number(count)
        self.buy()

    def add_to_cart_without_spus(self, count):
        """将商品加入购物车"""
        self.set_input_number(count)
        self.add_to_cart()

    def buy_without_spus(self, count):
        """立即购买商品"""
        self.set_input_number(count)
        self.buy()

