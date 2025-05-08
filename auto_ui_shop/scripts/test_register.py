import pytest
from pages.register_page import RegisterPage
from base.data_utils import read_test_data
from base.logger import logger


class TestRegister:
    @pytest.fixture
    def register_page(self, browser):
        return RegisterPage(browser)

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("data", read_test_data('../data/register_data.json'))
    def test_register(self, browser, base_url, register_page, data):
        """测试注册功能"""
        logger.info("开始执行注册测试")
        username = data.get('username')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        expected = data.get('expected')
        logger.debug(f"测试数据: username={username}, expected={expected}")

        # 访问注册页面
        browser.get(base_url + "member/register/")
        logger.debug("已访问注册页面")

        register_page.register(username, password, confirm_password)
        logger.debug("已执行注册操作")

        # 断言注册结果
        if expected:
            assert '/login' in browser.current_url
            logger.info("注册成功验证通过")
        else:
            assert '/register' in browser.current_url
            logger.info("注册失败验证通过")