import pytest
from pages.register_page import RegisterPage

class TestRegister:
    @pytest.fixture
    def register_page(self, browser):
        return RegisterPage(browser)

    @pytest.mark.parametrize("username,password,confirm_password,expected", [
        ("testuser", "Test8340", "Test8340", True),  # 正常注册
        ("", "Test1234", "Test1234", False),  # 用户名为空
        ("testuser", "", "", False),  # 密码为空
        ("testuser", "Test1234", "Wrong1234", False),  # 密码不匹配
    ])
    def test_register(self, browser, base_url, register_page, username, password, confirm_password, expected):
        """测试注册功能"""
        # 访问注册页面
        browser.get(base_url + "member/register/") 
        register_page.register(username, password, confirm_password)
        # 断言注册结果
        if expected:
            assert '/login' in browser.current_url
        else:
            assert '/register' in browser.current_url