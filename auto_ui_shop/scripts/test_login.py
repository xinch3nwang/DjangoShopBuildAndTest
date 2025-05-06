import pytest
from pages.login_page import LoginPage
from data.data_utils import read_test_data


class TestLogin:
    @pytest.fixture
    def login_page(self, browser):
        return LoginPage(browser)

    @pytest.mark.parametrize("data", read_test_data('../data/login_data.json'))
    def test_login(self, browser, base_url, login_page, data):
        """测试登录功能"""
        username = data.get('username')
        password = data.get('password')
        expected = data.get('expected')

        # 访问登录页面
        browser.get(base_url + "member/login/") 

        # 执行登录操作
        login_page.login(username, password)

        # 断言登录结果
        if expected:
            assert '/list' in browser.current_url
        else:
            assert '/login' in browser.current_url