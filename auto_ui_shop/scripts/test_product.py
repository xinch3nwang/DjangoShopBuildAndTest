import pytest
from pages.product_page import ProductPage
from base.data_utils import read_test_data
from base.logger import logger

class TestProductPage:
    @pytest.fixture
    def product_page(self, browser):
        return ProductPage(browser)
    
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("data", read_test_data("../data/product_data.json"))
    def test_add_to_cart(self, browser, base_url, product_page, data):
        """测试商品加入购物车功能"""
        logger.info("开始执行商品详情测试")
        product_id = data.get('product_id')
        count = data.get('count')
        index = data.get('index')
        expected = data.get('expected')
        logger.debug(f"测试数据: product_id={product_id}")

        browser.get(base_url + f"detail/{product_id}/") 
        logger.debug("已访问商品详情页面")
        if len(index)>0:
            product_page.add_to_cart_with_spus(count, index)
        else:
            product_page.add_to_cart_without_spus(count)

        if expected:
            assert product_page.get_cart_success()
            logger.info("加入购物车验证通过")
        else:
            assert not product_page.get_cart_success()
            logger.info("加入购物车验证失败")