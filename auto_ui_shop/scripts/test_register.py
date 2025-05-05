import pytest
from pages.register_page import RegisterPage
from .data_utils import read_test_data


class TestRegister:
    @pytest.fixture
    def register_page(self, browser):
        return RegisterPage(browser)

    @pytest.mark.parametrize("data", read_test_data('../data/register_data.json'))
    def test_register(self, browser, base_url, register_page, data):
        """测试注册功能"""
        username = data.get('username')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        expected = data.get('expected')
        # 访问注册页面
        browser.get(base_url + "member/register/") 
        register_page.register(username, password, confirm_password)
        # 断言注册结果
        if expected:
            assert '/login' in browser.current_url
        else:
            assert '/register' in browser.current_url