from base.base_page import BasePage

class ProductPage(BasePage):
    """
    商品页面对象类
    """
    # 页面元素定位器
    SEARCH_INPUT = ("id", "search-input")
    SEARCH_BUTTON = ("id", "search-btn")
    PRODUCT_LIST = ("css selector", ".product-list li")
    ADD_TO_CART_BUTTON = ("css selector", ".add-to-cart")
    CART_COUNT = ("id", "cart-count")

    def __init__(self, driver):
        super().__init__(driver)

    def search_product(self, keyword):
        """搜索商品"""
        self.input_text(self.SEARCH_INPUT, keyword)
        self.click(self.SEARCH_BUTTON)

    def get_product_list(self):
        """获取商品列表"""
        return self.find_elements(self.PRODUCT_LIST)

    def add_to_cart(self, index=0):
        """将指定商品加入购物车"""
        products = self.get_product_list()
        if index < len(products):
            self.click(("css selector", f".product-list li:nth-child({index+1}) .add-to-cart"))

    def get_cart_count(self):
        """获取购物车商品数量"""
        return int(self.get_text(self.CART_COUNT))