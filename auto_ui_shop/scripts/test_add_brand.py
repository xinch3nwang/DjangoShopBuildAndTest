import pytest
from pages.add_brand_page import AddBrandPage
from pages.login_page import LoginPage
from base.data_utils import read_test_data
from base.logger import logger

class TestAddBrand:
    @pytest.fixture
    def add_brand_page(self, browser):
        return AddBrandPage(browser)

    @pytest.fixture()
    def login_page(self, browser):
        return LoginPage(browser)

    # @pytest.mark.run(order=4)
    @pytest.mark.parametrize("data", read_test_data('../data/add_brand_data.json'))
    def test_add_brand(self, browser, base_url, add_brand_page, login_page, data):
        """测试添加品牌功能"""
        logger.info("开始执行添加品牌测试")
        browser.get(base_url + "member/login/")
        login_page.login("aaa", "please158")
        logger.debug("已登录系统")

        brand_name = data.get('brand_name')
        brand_description = data.get('brand_description')
        brand_order = data.get('brand_order')
        file_path = data.get('file_path')
        expected = data.get('expected')
        logger.debug(f"测试数据: brand_name={brand_name}, brand_description={brand_description}, brand_order={brand_order}, file_path={file_path}")

        browser.get(base_url + "admin/shop/baykeshopbrand/add/")  # 假设添加品牌页面的 URL
        logger.debug("已访问添加品牌页面")
        add_brand_page.add_brand(brand_name, brand_description, brand_order, file_path)
        logger.debug("已执行添加品牌操作")

        if expected:
            # 这里需要根据实际情况替换为获取成功消息的方法
            assert add_brand_page.get_success_message() is not None
            logger.info("添加品牌验证通过")
        else:
            assert "add" in browser.current_url
            logger.info("添加品牌验证失败")