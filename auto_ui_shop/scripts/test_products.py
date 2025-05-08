import pytest
from pages.products_page import ProductsPage
from base.data_utils import read_test_data
from base.logger import logger

class TestProducts:
    @pytest.fixture
    def products_page(self, browser):
        return ProductsPage(browser)

    @pytest.mark.parametrize("data", read_test_data('../data/products_test_data.json'))
    def test_cheapest_product(self, browser, base_url, products_page, data):
        """测试进入第 index 便宜的产品详情页"""
        logger.info("开始执行商品价格筛选测试")
        index = data.get('index')
        # 访问产品页面
        browser.get(base_url + "list/")
        logger.debug("已访问商品列表页面")
        products_page.the_cheapest_one(index)
        assert "detail" in browser.current_url

    @pytest.mark.parametrize("data", read_test_data('../data/products_test_data.json'))
    def test_most_sales_product(self, browser, base_url, products_page, data):
        """测试进入第 index 销量最高的产品详情页"""
        logger.info("开始执行商品销量筛选测试")
        index = data.get('index')
        # 访问产品页面
        browser.get(base_url + "list/")
        logger.debug("已访问商品列表页面")
        products_page.the_most_sales(index)
        assert "detail" in browser.current_url

    @pytest.mark.parametrize("data", read_test_data('../data/products_test_data.json'))
    def test_latest_product(self, browser, base_url, products_page, data):
        """测试进入第 index 最新的产品详情页"""
        logger.info("开始执行商品时间筛选测试")
        index = data.get('index')
        # 访问产品页面
        browser.get(base_url + "list/")
        logger.debug("已访问商品列表页面")
        products_page.the_latest_one(index)
        assert "detail" in browser.current_url