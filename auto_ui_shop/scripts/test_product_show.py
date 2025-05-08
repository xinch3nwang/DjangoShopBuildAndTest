import pytest
from pages.product_page import ProductPage
from base.data_utils import read_test_data
from base.logger import logger
from base.db_utils import execute_sql

class TestProductShow:
    @pytest.fixture
    def product_page(self, browser):
        """初始化商品详情页操作对象"""
        return ProductPage(browser)

    # @pytest.mark.run(order=4)
    @pytest.mark.parametrize("data", read_test_data('../data/product_show_data.json'))
    def test_product_info_display(self, browser, base_url, product_page, data):
        """验证商品详情页信息与数据库一致"""
        logger.info("开始执行商品详情页信息显示测试")
        
        # 1. 从数据库获取商品信息
        product_id = data.get('product_id')
        db_path = r'd:\Code\Personal\DjangoShop\djangoshop\db.sqlite3'
        sql = "SELECT price, stock FROM shop_baykeshopgoodssku WHERE id = ?"
        result = execute_sql(db_path, sql, (product_id,))
        
        if not result:
            pytest.fail(f"数据库未找到ID为 {product_id} 的商品")
        
        row = result[0]
        db_product = {'price': row[0], 'stock': row[1]}
        logger.debug(f"数据库商品信息: {db_product}")

        # 2. 访问商品详情页
        browser.get(f"{base_url}detail/{product_id}/")
        logger.debug(f"已访问商品详情页，URL: {browser.current_url}")

        # 3. 获取页面显示的信息
        page_price = product_page.get_price()
        page_stock = product_page.get_stock()
        logger.debug(f"页面显示的价格: {page_price}, 库存: {page_stock}")

        # 4. 断言页面信息与数据库一致
        assert float(page_price) == db_product['price'], "商品价格显示不一致"
        assert int(page_stock) == db_product['stock'], "商品库存显示不一致"
        
        logger.info("商品详情页信息显示验证通过")