import pytest
from pages.address_page import AddressPage
from base.data_utils import read_test_data
from base.logger import logger


class TestAddress:
    @pytest.fixture
    def address_page(self, browser):
        return AddressPage(browser)

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("data", read_test_data('../data/address_data.json'))
    def test_address_management(self, browser, base_url, address_page, data):
        """测试地址管理功能"""
        logger.info("开始执行添加收货地址测试")
        name = data.get('name')
        phone = data.get('phone')
        province = data.get('province')
        city = data.get('city')
        district = data.get('district')
        address = data.get('address')
        is_default = data.get('is_default')
        expected = data.get('expected')
        logger.debug(f"测试数据: name={name}, phone={phone}, province={province}, city={city}, district={district}, address={address}, is_default={is_default}")

        browser.get(base_url + "member/address/create/")
        logger.debug("已访问添加收货地址页面")
        address_page.edit_address(name, phone, province, city, district, address, is_default)
        logger.debug("已执行添加收货地址操作")

        if expected:
            assert address_page.get_success_message() is not None
            logger.info("添加收货地址验证通过")
        else:
            assert "update" in browser.current_url or "create" in browser.current_url
            logger.info("添加收货地址验证失败")