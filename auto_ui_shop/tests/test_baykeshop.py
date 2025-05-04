import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductDetailPage
from pages.order_page import OrderPage

class TestBaykeShop:
    """
    BaykeShop网站测试类
    """
    @pytest.mark.parametrize("username,password", [("test_user", "123456")])
    def test_login(self, browser, base_url, username, password):
        """测试BaykeShop用户登录"""
        browser.get(base_url + "/login")
        login_page = LoginPage(browser)
        login_page.login(username, password)
        assert "登录成功" in browser.title

    @pytest.mark.parametrize("keyword", [("手机")])
    def test_add_to_cart(self, browser, base_url, keyword):
        """测试BaykeShop商品加购"""
        browser.get(base_url + "/products")
        product_page = ProductDetailPage(browser)
        product_page.search_product(keyword)
        product_page.add_to_cart()
        assert product_page.get_cart_count() > 0

    def test_submit_order(self, browser, base_url):
        """测试BaykeShop订单提交"""
        browser.get(base_url + "/cart")
        order_page = OrderPage(browser)
        order_page.submit_order()
        assert "订单提交成功" in order_page.get_success_message()