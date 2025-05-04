from base.base_page import BasePage
from selenium.webdriver.common.by import By

class NavigationPageLocators(object):
    """
    导航页面元素定位层
    """
    def __init__(self):
        self.PROFILE = (By.CSS_SELECTOR, "a[href='/member/profile/']")  # 个人中心链接
        self.ORDER = (By.CSS_SELECTOR, "a[href='/member/orders/']")  # 订单链接
        self.LOGOUT = (By.CSS_SELECTOR, "form.bk-dropdown-item")  # 退出登录链接
        self.CART = (By.CSS_SELECTOR, "a[href='/carts/']")  # 购物车链接
        self.NAVTOPRODUCTS = (By.CSS_SELECTOR, "a[href='/list/']")  # 导航到产品页面链接
        self.NAVTONEWS = (By.CSS_SELECTOR, "a[href='/article/']")  # 导航到新闻页面链接
        self.SEARCH_INPUT = (By.NAME, "keyword")  # 搜索框输入框
        self.SEARCH_BUTTON = (By.XPATH, "//button[contains(text(), '搜索')]")  # 搜索按钮

class NavigationPageActions(BasePage):
    """
    首页操作层
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = NavigationPageLocators()

    def click_profile(self):
        """点击个人中心"""
        self.click(self.locators.PROFILE)

    def click_order(self):
        """点击订单"""
        self.click(self.locators.ORDER)

    def click_logout(self):
        """点击退出登录"""
        self.click(self.locators.LOGOUT)

    def click_cart(self):
        """点击购物车"""
        self.click(self.locators.CART)

    def click_navtoproducts(self):
        """点击导航到产品页面"""
        self.click(self.locators.NAVTOPRODUCTS)

    def click_navtonews(self):
        """点击导航到新闻页面"""
        self.click(self.locators.NAVTONEWS)

    def input_search(self, keyword):
        """输入搜索关键词"""
        self.input_text(self.locators.SEARCH_INPUT, keyword)

    def click_search(self):
        """点击搜索按钮"""
        self.click(self.locators.SEARCH_BUTTON)

class NavigationPage(BasePage):
    """
    导航页面操作层
    """
    def logout(self):
        """退出登录"""
        self.click_logout()

    def go_to_profile(self):
        """跳转到个人中心页面"""
        self.click_profile()

    def go_to_order(self):
        """跳转到订单页面"""
        self.click_order()

    def search_product(self, keyword):
        """搜索产品"""
        self.input_search(keyword)
        self.click_search()

    def go_to_cart_page(self):
        """跳转到购物车页面"""
        self.click_cart()

    def go_to_products_page(self):
        """跳转到产品页面"""
        self.click_navtoproducts()

    def go_to_news_page(self):
        """跳转到新闻页面"""
        self.click_navtonews()