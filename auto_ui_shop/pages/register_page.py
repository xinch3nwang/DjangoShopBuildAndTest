from base.base_page import BasePage
from selenium.webdriver.common.by import By

class RegisterPageLocators(object):
    """
    注册页面元素定位层
    """
    def __init__(self):
        self.USERNAME_INPUT = (By.ID, "id_username")
        self.PASSWORD_INPUT = (By.NAME, "password1")
        self.CONFIRM_PASSWORD_INPUT = (By.NAME, "password2")
        self.REGISTER_BUTTON = (By.CSS_SELECTOR, "button.bk-button.bk-is-link.bk-is-fullwidth")


class RegisterPageActions(BasePage):
    """ 
    注册页面操作层
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RegisterPageLocators()

    def input_username(self, username):
        """输入用户名"""
        self.input_text(self.locators.USERNAME_INPUT, username)

    def input_password(self, password):
        """输入密码"""
        self.input_text(self.locators.PASSWORD_INPUT, password)

    def input_confirm_password(self, password):
        """输入确认密码"""
        self.input_text(self.locators.CONFIRM_PASSWORD_INPUT, password)

    def click_register(self):
        """点击注册按钮"""
        self.click(self.locators.REGISTER_BUTTON)


class RegisterPage(RegisterPageActions):
    """
    注册页面业务层
    """
    def register(self, username, password, confirm_password):
        """完整注册流程"""
        self.input_username(username)
        self.input_password(password)
        self.input_confirm_password(confirm_password)
        self.click_register()