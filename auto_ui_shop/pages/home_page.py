from base.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePageLocators(object):
    """
    首页元素定位层
    """
    def __init__(self):
        self.PRODUCT_RECOM = (By.CSS_SELECTOR, "a.bk_box")  # 推荐产品列表
        self.PRODUCTS_MORE = (By.XPATH, "//a[contains(text(), '更多')]")  # 更多产品按钮

class HomePageActions(BasePage):
    """
    首页操作层
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocators()

    def get_products_recom(self):
        """获取推荐产品列表"""
        return self.get_elements(self.locators.PRODUCT_RECOM)

    def goto_product_detail(self, index):
        """点击推荐产品进入详情页"""
        self.get_products_recom()[index].click()

    def get_mores(self):
        """获取更多产品按钮"""
        return self.get_elements(self.locators.PRODUCTS_MORE)

    def click_more(self,index):
        """点击更多产品按钮"""
        self.get_mores()[index].click()


class HomePage(HomePageActions):
    """
    首页业务层
    """
    def go_to_product_detail(self, index):
        """点击推荐产品进入详情页"""
        self.goto_product_detail(index)

    def go_to_more_page(self,index):
        """点击更多产品按钮"""
        self.click_more(index)