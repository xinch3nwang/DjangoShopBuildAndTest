import pytest
from pages.login_page import LoginPage
from base.data_utils import read_test_data
from base.logger import logger


class TestLogin:
    @pytest.fixture
    def login_page(self, browser):
        return LoginPage(browser)

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("data", read_test_data('../data/login_data.json'))
    def test_login(self, browser, base_url, login_page, data):
        """测试登录功能"""
        logger.info("开始执行登录测试")
        username = data.get('username')
        password = data.get('password')
        expected = data.get('expected')
        logger.debug(f"测试数据: username={username}, expected={expected}")

        # 访问登录页面
        browser.get(base_url + "member/login/")
        logger.debug("已访问登录页面")

        # 执行登录操作
        login_page.login(username, password)
        logger.debug("已执行登录操作")

        # 断言登录结果
        if expected:
            assert '/list' in browser.current_url
            logger.info("登录成功验证通过")
        else:
            assert '/login' in browser.current_url
            logger.info("登录失败验证通过")