import pytest
import re
import time
from base.data_utils import read_test_data
from base.logger import logger
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.address_page import AddressPage
from pages.navigation_page import NavigationPage
from pages.products_page import ProductsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.order_page import OrderPage


class TestShoppingFlow:
    """
    购物流程测试类
    """
    @pytest.fixture
    def page(self, browser):
        """获取页面实例"""
        return {
            'register': RegisterPage(browser),
            'login': LoginPage(browser),
            'address': AddressPage(browser),
            'navigation': NavigationPage(browser),
            'products': ProductsPage(browser),
            'product': ProductPage(browser),
            'cart': CartPage(browser),
            'checkout': CheckoutPage(browser),
            'payment': PaymentPage(browser),
            'order': OrderPage(browser)
        }

    @pytest.mark.parametrize("data", read_test_data('../data/shopping_flow_data.json'))
    def test_shopping_flow(self, browser, base_url, page, data):
        """测试完整购物流程"""
        logger.info("开始执行完整购物流程测试")  # 新增：测试开始日志
        # 读取测试数据
        username = data.get('username')+str(int(time.time()))
        password = data.get('password')
        logger.debug(f"读取测试数据：username={username}, password={password}") 
        name = data.get('name')
        phone = data.get('phone')
        province = data.get('province')
        city = data.get('city')
        district = data.get('district')
        address = data.get('address')
        is_default = data.get('is_default')
        logger.debug(f"读取测试数据：name={name}, phone={phone}, province={province}, city={city}, district={district}, address={address}, is_default={is_default}") 
        keyword = data.get('keyword')
        logger.debug(f"读取测试数据：keyword={keyword}") 
        index_products = data.get('index_products')
        logger.debug(f"读取测试数据：index_products={index_products}") 
        count_buy = data.get('count_buy')
        index_spu = data.get('index_spu')
        logger.debug(f"读取测试数据：count_buy={count_buy}, index_spu={index_spu}") 
        index_address = data.get('index_address')
        logger.debug(f"读取测试数据：index_address={index_address}") 
        index_payment = data.get('index_payment')
        logger.debug(f"读取测试数据：index_payment={index_payment}") 
        expected = data.get('expected')
        
        # 用户注册
        logger.info(f"执行用户注册，用户名：{username}")  
        browser.get(base_url + "member/register/")
        logger.debug(f"页面已跳转至注册页面，URL: {browser.current_url}")
        time.sleep(0.1)
        page['register'].register(username, password, password)
        logger.debug("用户注册操作完成") 
        # 用户登录
        logger.info(f"执行用户登录，用户名：{username}")  
        time.sleep(0.1)
        page['login'].login(username, password)
        logger.debug("用户登录操作完成") 
        # 添加收货地址
        logger.info(f"执行收货地址添加，姓名：{name}，电话：{phone}")  
        time.sleep(0.1)
        browser.get(base_url + "member/address/create/")
        time.sleep(0.1)
        # assert browser.current_url == base_url + "member/address/create/", f"页面未跳转，当前 URL 是 {browser.current_url}"
        page['address'].edit_address(name, phone, province, city, district, address, is_default)
        logger.debug("收货地址添加操作完成") 
        # 搜索商品进入商品详情页并加入购物车
        logger.info(f"执行商品搜索，关键词：{keyword}") 
        time.sleep(0.1)
        browser.get(base_url + "list/")
        time.sleep(0.1)
        page['navigation'].search_product(keyword)
        time.sleep(0.1)
        page['products'].the_cheapest_one(index_products)
        logger.debug("已定位到最便宜商品，进入详情页") 
        time.sleep(0.1)
        if len(index_spu)>0:
            logger.debug(f"商品有SPU属性，选择索引：{index_spu}") 
            page['product'].add_to_cart_with_spus(count_buy, index_spu)
        else:
            logger.debug("商品无SPU属性，直接加入购物车") 
            page['product'].add_to_cart_without_spus(count_buy)
        logger.debug("商品加入购物车操作完成") 
        # 进入购物车
        logger.info("进入购物车页面")  
        time.sleep(0.1)
        browser.get(base_url + "carts/")
        time.sleep(0.1)
        page['cart'].goto_checkout_default()
        logger.debug("已跳转至结算页面") 
        time.sleep(0.1)
        # 提交订单
        logger.info(f"提交订单，选择地址索引：{index_address}")  
        page['checkout'].checkout(index_address)
        time.sleep(0.1)
        logger.debug("订单提交操作完成") 
        # 支付
        logger.info(f"执行支付操作，选择支付方式索引：{index_payment}")  
        page['payment'].pay(index_payment)
        # 刷新页面
        time.sleep(2)
        browser.switch_to.window(browser.window_handles[-1])
        logger.debug("已切换到最新窗口，准备验证订单状态") 
                
        # 断言
        if expected:
            logger.info("验证支付成功场景")  # 新增：断言日志
            assert page['order'].get_order_status() != "未支付"
        else:
            logger.info("验证支付失败场景")  # 新增：断言日志
            assert page['order'].get_order_status() == "未支付"
        logger.info("完整购物流程测试结束")  # 新增：测试结束日志
        # pattern = re.compile(re.escape(base_url) + r"member/orders//\d+")
        # if expected:
        #     assert pattern.match(browser.current_url), f"跳转到订单页面, 当前 URL 是 {browser.current_url}"
        # else:
        #     assert not pattern.match(browser.current_url), f"未跳转到结算页面, 当前 URL 是 {browser.current_url}"