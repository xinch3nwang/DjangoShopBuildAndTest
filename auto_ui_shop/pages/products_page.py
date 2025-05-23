from base.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductsPageLocators(object):
    """
    产品页面元素定位层
    """
    def __init__(self):
        # brand_name 是传入的参数
        self.brand_name = "示例品牌"  
        self.BRAND = (By.XPATH, f"//a[contains(text(), '{self.brand_name}')]")  # 品牌

        self.category_name = "示例分类"
        self.CATEGORY = (By.XPATH, f"//a[contains(text(), '{self.category_name}')]")

        self.ORDERBYPRICE = (By.XPATH, "//a[contains(text(), '价格')]")
        self.ORDERBYSALES = (By.XPATH, "//a[contains(text(), '销量')]")
        self.ORDERBYTIME = (By.XPATH, "//a[contains(text(), '时间')]")
        self.PRODUCTS = (By.CSS_SELECTOR, "a.bk-box")

class ProductsActions(BasePage):
    """
    产品页面操作层
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProductsPageLocators()

    def get_brand(self, brand_name):
        """获取品牌"""
        self.locators.brand_name = brand_name  # 设置品牌名称
        return self.find_element(self.locators.BRAND)

    def get_category(self, catagory_name):
        """获取分类"""
        self.locators.category_name = category_name  # 设置分类名称
        return self.find_element(self.locators.CATEGORY)

    def orderby_price(self):
        """获取价格排序"""
        # 每次操作前重新定位元素
        price_element = self.find_element(self.locators.ORDERBYPRICE)
        price_element.click()

    def orderby_sales(self):
        """获取销量排序"""
        # 每次操作前重新定位元素
        sales_element = self.find_element(self.locators.ORDERBYSALES)
        sales_element.click()

    def orderby_time(self):
        """获取时间排序"""
        # 每次操作前重新定位元素
        time_element = self.find_element(self.locators.ORDERBYTIME)
        time_element.click()

    def click_brand(self, brand_name):
        """点击品牌"""
        self.get_brand(brand_name).click()

    def click_category(self, category_name):
        """点击分类"""
        self.get_category(category_name).click()

    def get_products(self):
        """获取产品列表"""
        return self.find_elements(self.locators.PRODUCTS)

    def click_product(self, index):
        """点击产品"""
        self.get_products()[index].click()

class ProductsPage(ProductsActions):
    """
    产品页面业务层
    """
    def the_cheapest_one(self, index):
        """进入第index便宜的产品详情页"""
        self.orderby_price()
        self.click_product(index)

    def the_most_sales(self, index):
        """进入第index销量最高的产品详情页"""
        self.orderby_sales()
        self.orderby_sales()
        self.click_product(index)

    def the_latest_one(self, index):
        """进入第index最新的产品详情页"""
        self.orderby_time()
        self.orderby_time()
        self.click_product(index)