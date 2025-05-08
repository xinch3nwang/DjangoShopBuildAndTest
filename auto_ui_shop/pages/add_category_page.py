from base.base_page import BasePage
from selenium.webdriver.common.by import By

class AddCategoryPageLocators(object):
    """
    新增分类页面的定位器
    """
    def __init__(self):
        self.CATEGORY_NAME = (By.NAME, "name")  # 分类名称输入框
        self.CATEGORY_ORDER = (By.NAME, "order")  # 排序输入框
        self.IS_FLOOR = (By.NAME, "is_floor")  # 是否是楼层分类复选框
        self.IS_NAV = (By.NAME, "is_nav")  # 是否在导航栏显示复选框
        self.CHILD_CATEGORY = (By.CSS_SELECTOR, "tr.form-row.dynamic-baykeshopcategory_set")  # 子分类下拉框
        self.CHILD_CATEGORY_NAME = (By.CSS_SELECTOR, "td.field-name")  # 子分类名称输入框
        self.CHILD_CATEGORY_ORDER = (By.CSS_SELECTOR, "td.field-order")  # 子分类排序输入框
        self.CHILD_CATEGORY_IS_FLOOR = (By.CSS_SELECTOR, "td.field-is_floor")  # 子分类是否是楼层分类复选框
        self.CHILD_CATEGORY_IS_NAV = (By.CSS_SELECTOR, "td.field-is_nav")  # 子分类是否在导航栏显示复选框
        self.ADD_CHILD_CATEGORY = (By.XPATH, "a[href='#']")
        self.SAVE = (By.NAME, "_save")  # 保存按钮


class AddCategoryPageActions(BasePage):
    """
    新增分类页面的操作方法
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AddCategoryPageLocators()
    
    def input_category_name(self, category_name):
        """
        输入分类名称
        """
        self.input_text(self.locators.CATEGORY_NAME, category_name)

    def input_category_order(self, category_order):
        """
        输入排序
        """
        self.input_text(self.locators.CATEGORY_ORDER, category_order)

    def click_is_floor_checkbox(self):
        """
        点击是否是楼层分类复选框
        """
        self.click(self.locators.IS_FLOOR)

    def click_is_nav_checkbox(self):
        """
        点击是否在导航栏显示复选框
        """
        self.click(self.locators.IS_NAV)

    def click_add_child_category_button(self):
        """
        点击添加子分类按钮
        """
        self.click(self.locators.ADD_CHILD_CATEGORY)

    def get_children_category(self):
        """
        获取子分类
        """
        return self.get_elements(self.locators.CHILD_CATEGORY)

    def get_child_category(self, index):
        """
        获取子分类
        """
        return self.get_element(self.locators.CHILD_CATEGORY)[index]

    def input_child_category_name(self, index, child_category_name):
        """
        输入子分类名称
        """
        self.get_child_category(index).find_element(self.locators.CHILD_CATEGORY_NAME).send_keys(child_category_name)
         

    def input_child_category_order(self, index, child_category_order):
        """
        输入子分类排序
        """
        self.get_child_category(index).find_element(self.locators.CHILD_CATEGORY_ORDER).send_keys(child_category_order)

    def click_child_category_is_floor_checkbox(self, index):
        """
        点击子分类是否是楼层分类复选框
        """
        self.get_child_category(index).find_element(self.locators.CHILD_CATEGORY_IS_FLOOR).click()

    def click_child_category_is_nav_checkbox(self, index):
        """
        点击子分类是否在导航栏显示复选框
        """
        self.get_child_category(index).find_element(self.locators.CHILD_CATEGORY_IS_NAV).click()

    def click_save_button(self):
        """
        点击保存按钮
        """
        self.click(self.locators.SAVE)


class AddCategoryPage(AddCategoryPageActions):
    """
    新增分类页面的业务流程
    """
    def add_category(self, category_name, category_order, is_floor, is_nav, child_category_name, child_category_order, child_category_is_floor, child_category_is_nav, child_num):
        """
        新增分类
        """
        self.input_category_name(category_name)
        self.input_category_order(category_order)
        if is_floor:
            self.click_is_floor_checkbox()
        if is_nav:
            self.click_is_nav_checkbox()

        for i in range(child_num):
            self.input_child_category_name(i, child_category_name)
            self.input_child_category_order(i, child_category_order)
            if child_category_is_floor[i]:
                self.click_child_category_is_floor_checkbox()
            if child_category_is_nav[i]:
                self.click_child_category_is_nav_checkbox()
            self.click_add_child_category_button()
        self.click_save_button()

