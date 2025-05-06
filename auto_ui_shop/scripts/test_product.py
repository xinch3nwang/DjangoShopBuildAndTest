import pytest
from pages.product_page import ProductPage
from data.data_utils import read_test_data

class TestProductPage:
    @pytest.fixture
    def product_page(self, browser):
        return ProductPage(browser)
    
    @pytest.mark.parametrize("data", read_test_data("../data/product_data.json"))
    def test_add_to_cart(self, browser, base_url, product_page, data):
        """测试商品加入购物车功能"""
        product_id = data.get('product_id')
        count = data.get('count')
        index = data.get('index')
        expected = data.get('expected')

        browser.get(base_url + f"detail/{product_id}/") 
        if len(index)>0:
            product_page.add_to_cart_with_spus(count, index)
        else:
            product_page.add_to_cart_without_spus(count)

        assert product_page.get_cart_success() == expected