from base.base_page import BasePage
from selenium.webdriver.common.by import By


class AddProductPageLocators(object):
    """
    新增商品页面的定位器
    """
    self.brand_name = "测试品牌"  # 品牌名称
    self.category_name = "测试分类"  # 分类名称
    self.standard_name = "测试规格"  # 规格名称

    self.PRODUCT_NAME = (By.NAME, "name")  # 商品XPATH名称输入框
    self.BRAND = (By.XPATH, "option[title=f'{self.brandname}')]")  # 品牌下拉框
    self.SELECT_CATEGORY = (By.XPATH, "option[title=f'{self.category_name}')]")
    self.ADD_CATEGORY = (By.XPATH, "a[title='选择']")  # 添加分类按钮
    self.PRODUCT_KEYWORDS = (By.NAME, "keywords")  # 商品关键字输入框
    self.PRODUCT_DESCRIPTION = (By.NAME, "description")  # 商品描述输入框
    self.PRODUCT_DETAIL = (By.ID, "tinymce")  # 商品详情输入框
    
    self.ADD_SKU = (By.CSS_SELECTOR, "div.add-row")  # 添加SKU按钮
    self.SKUS = (By.CSS_SELECTOR, ".inline-related.dynamic-baykeshopgoodssku_set")  # SKU输入框
    self.SELECT_STANDARD = (By.XPATH, "option[title=f'{self.standard_name}')]")  # 规格名称下拉框
    self.ADD_STANDARD = (By.XPATH, "a[title='选择']")  # 添加规格按钮
    self.PRICE = (By.ID, "f'id_baykeshopgoodssku_set-{index}-price'")  # 价格输入框
    self.LINE_PRICE = (By.ID, "f'id_baykeshopgoodssku_set-{index}-line_price'")  # 划线价格输入框
    self.STOCK = (By.ID, "f'id_baykeshopgoodssku_set-{index}-stock'")  # 库存输入框
    
    self.PRODUCT_IMAGES = (By.ID, "id_baykeshopgoodsimages_set-0-image")  # 商品图片输入框
    self.SAVE = (By.NAME, "_save")  # 保存按钮



class AddProductPageActions(BasePage):
    """
    新增商品页面的操作方法
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AddProductPageLocators()

    def input_product_name(self, product_name):
        """
        输入商品名称
        """
        self.input_text(self.locators.PRODUCT_NAME, product_name)

    def select_brand(self, brand_name):
        """
        选择品牌
        """
        self.brand_name = brand_name
        self.find_element(self.locators.BRAND).click()

    def select_category(self, category_name):
        """
        选择分类
        """
        self.category_name = category_name
        self.find_element(self.locators.SELECT_CATEGORY)
    
    def add_category(self):
        """
        添加分类
        """
        self.find_element(self.locators.ADD_CATEGORY).click()
    
    def input_product_keywords(self, keywords):
        """
        输入商品关键字
        """
        self.input_text(self.locators.PRODUCT_KEYWORDS, keywords)

    def input_product_description(self, description):
        """
        输入商品描述
        """
        self.input_text(self.locators.PRODUCT_DESCRIPTION, description)

    def input_product_detail(self, detail):
        """
        输入商品详情
        """
        self.input_text(self.locators.PRODUCT_DETAIL, detail)

    def get_sku(self, index):
        """
        获取SKU
        """
        return self.get_elements(self.locators.SKUS)[index]

    def add_sku(self):
        """
        添加SKU
        """
        self.find_element(self.locators.ADD_SKU).click()

    def select_standard(self, standard_name):
        """
        选择规格名称
        """
        self.standard_name = standard_name
        self.find_element(self.locators.SELECT_STANDARD).click()

    def add_standard(self):
        """
        添加规格名称
        """
        self.find_element(self.locators.ADD_STANDARD).click()

    def input_price(self, price):
        """
        输入价格
        """
        self.input_text(self.locators.PRICE, price)

    def input_line_price(self, line_price):
        """
        输入划线价格
        """
        self.input_text(self.locators.LINE_PRICE, line_price)

    def input_stock(self, stock):
        """
        输入库存
        """
        self.input_text(self.locators.STOCK, stock)

    def save_product(self):
        """
        保存商品
        """
        self.find_element(self.locators.SAVE).click()
          
    def upload_product_images(self, file_path):
        """
        上传商品图片
        """
        self.upload_file(self.locators.PRODUCT_IMAGES, file_path)


class AddProductPage(AddProductPageActions):
    """
    新增商品页面的业务逻辑
    """
    def add_product(self, product_name, brand_name, category_name, keywords, description, detail, sku, standard_name, price, line_price, stock, file_path):
        """
        添加商品
        """
        self.input_product_name(product_name)
        self.select_brand(brand_name)
        self.select_category(category_name)
        self.add_category()
        self.input_product_keywords(keywords)
        self.input_product_description(description)
        self.input_product_detail(detail)

        for i in range(sku):
            self.add_sku()
            self.get_sku(i).select_standard(standard_name)
            self.get_sku(i).add_standard()
            self.get_sku(i).input_price(price)
            self.get_sku(i).input_line_price(line_price)
            self.get_sku(i).input_stock(stock)

        self.upload_product_images(file_path)
        self.save_product()
