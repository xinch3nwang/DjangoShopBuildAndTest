from base.base_page import BasePage

class LoginPage(BasePage):
    """
    登录页面对象类
    """
    # 页面元素定位器
    USERNAME_INPUT = ("id", "id_username")
    PASSWORD_INPUT = ("id", "id_password")
    LOGIN_BUTTON = ("xpath", '//button[contains(., "登录")]')
    ERROR_MSG = ("css selector", ".error-message")

    def __init__(self, driver):
        super().__init__(driver)

    def input_username(self, username):
        """输入用户名"""
        self.input_text(self.USERNAME_INPUT, username)

    def input_password(self, password):
        """输入密码"""
        self.input_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        """点击登录按钮"""
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        """获取错误提示信息"""
        return self.get_text(self.ERROR_MSG)

    def login(self, username, password):
        """完整登录流程"""
        self.input_username(username)
        self.input_password(password)
        self.click_login()