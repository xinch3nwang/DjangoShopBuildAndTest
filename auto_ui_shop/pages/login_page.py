from base.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    """
    登录页面元素定位层
    """
    def __init__(self):
        self.USERNAME_INPUT = (By.ID, "id_username")
        self.PASSWORD_INPUT = (By.ID, "id_password")
        self.LOGIN_BUTTON = (By.CSS_SELECTOR, "button.bk-button.bk-is-link.bk-is-fullwidth")
        self.REGISTER_BUTTON = (By.XPATH, "//a[contains(text(), '注册账号')]")
        self.FORGET_PASSWORD_BUTTON = (By.XPATH, "//a[contains(text(), '忘记密码')]")
        self.ERROR_MSG = (By.CSS_SELECTOR, "ul.errorlist.nonfield")

class LoginPageActions(BasePage):
    """ 
    登录页面操作层
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()

    def input_username(self, username):
        """输入用户名"""
        self.input_text(self.locators.USERNAME_INPUT, username)

    def input_password(self, password):
        """输入密码"""
        self.input_text(self.locators.PASSWORD_INPUT, password)

    def click_login(self):
        """点击登录按钮"""
        self.click(self.locators.LOGIN_BUTTON)

    def click_register(self):
        """点击注册按钮"""
        self.click(self.locators.REGISTER_BUTTON)

    def click_forget_password(self):
        """点击忘记密码按钮"""
        self.click(self.locators.FORGET_PASSWORD_BUTTON)

    def get_error_message(self):
        """获取错误提示信息"""
        return self.get_text(self.locators.ERROR_MSG)

class LoginPage(LoginPageActions):
    """
    登录页面业务层
    """
    def login(self, username, password):
        """完整登录流程"""
        self.input_username(username)
        self.input_password(password)
        self.click_login()

    def go_to_register_page(self):
        """跳转到注册页面"""
        self.click_register()

    def go_to_forget_password_page(self):
        """跳转到忘记密码页面"""
        self.click_forget_password()