import pytest
import re
from pages.cart_page import CartPage
from base.data_utils import read_test_data
from base.logger import logger

class TestCart:
    @pytest.fixture
    def cart_page(self, browser):
        return CartPage(browser)

    @pytest.mark.run(order=5)
    @pytest.mark.parametrize("data", read_test_data('../data/cart_data.json'))
    def test_cart_operations(self, browser, base_url, cart_page, data):
        """测试购物车操作"""
        logger.info("开始执行购物车测试")
        browser.get(base_url + "carts/")
        logger.debug("已访问购物车页面")
        index = data.get("index")
        quantity = data.get("quantity")
        price = data.get("price")
        expected = data.get("expected")

        # assert cart_page.get_price() > 0, "购物车中应该有商品"
        cart_page.goto_checkout(index, quantity)
        logger.debug("已执行去结算操作")

        if expected:
            # 使用正则表达式进行断言
            pattern = re.compile(re.escape(base_url) + r"carts/.*")
            assert pattern.match(browser.current_url)
            logger.info("跳转到结算页面")
        else:
            assert browser.current_url == base_url + "carts/"
            logger.info("未跳转到结算页面")