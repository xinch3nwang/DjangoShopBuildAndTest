import pytest
from urllib.parse import quote_plus
from pages.navigation_page import NavigationPage
from base.data_utils import read_test_data
from base.logger import logger

class TestNavigation:
    @pytest.fixture
    def navigation_page(self, browser):
        return NavigationPage(browser)

    @pytest.mark.parametrize("data", read_test_data('../data/navigation_test_data.json'))
    def test_search_function(self, browser, base_url, navigation_page, data):
        """测试导航页面的搜索功能"""
        logger.info("开始执行导航链接测试")
        keyword = data.get('keyword')
        # 对关键词进行 URL 编码
        encoded_keyword = quote_plus(keyword)

        # 访问导航页面
        browser.get(base_url)
        logger.debug("已访问主页")
        # 执行搜索操作
        navigation_page.search_product(keyword)
        logger.debug(f"已搜索: {keyword}")
        # 断言搜索结果页面的 URL 包含预期内容
        assert f'search/?keyword={encoded_keyword}' in browser.current_url
        logger.info(f"导航链接跳转验证通过，预期 URL: {expected_url}，实际 URL: {browser.current_url}")