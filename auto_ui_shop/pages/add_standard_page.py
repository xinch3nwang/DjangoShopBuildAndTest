from base.base_page import BasePage
from selenium.webdriver.common.by import By

class AddStandardPageLocators(object):
    """
    新增规格页面的定位器
    """
    self.STANDARD_NAME = (By.NAME, "name")  # 规格名称输入框
    self.STANDARD_ORDER = (By.NAME, "standard_order")  # 排序输入框
    self.CHILD_STANDARD = (By.CSS_SELECTOR, "tr.form-row.dynamic-baykeshopspec_set")  # 子规格下拉框
    self.CHILD_STANDARD_NAME = (By.CSS_SELECTOR, "td.field-name")  # 子规格名称输入框
    self.CHILD_STANDARD_ORDER = (By.CSS_SELECTOR, "td.field-order")  # 子规格排序输入框
    self.ADD_CHILD_STANDARD = (By.XPATH, "a[href='#']")
    self.SAVE = (By.NAME, "_save")  # 保存按钮


class AddStandardPageActions(BasePage):
    """
    新增规格页面的操作方法
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AddStandardPageLocators()
    
    def input_standard_name(self, standard_name):
        """
        输入规格名称
        """
        self.input_text(self.locators.STANDARD_NAME, standard_name)

    def input_standard_order(self, standard_order):
        """
        输入排序
        """
        self.input_text(self.locators.STANDARD_ORDER, standard_order)

    def click_add_child_standard_button(self):
        """
        点击添加子规格按钮
        """
        self.click(self.locators.ADD_CHILD_STANDARD)

    def get_children_standard(self):
        """
        获取子规格
        """
        return self.get_elements(self.locators.CHILD_STANDARD)

    def get_child_standard(self, index):
        """
        获取子规格
        """
        return self.get_element(self.locators.CHILD_STANDARD)[index]

    def input_child_standard_name(self, index, child_standard_name):
        """
        输入子规格名称
        """
        self.get_child_standard(index).find_element(self.locators.CHILD_STANDARD_NAME).send_keys(child_standard_name)

    def input_child_standard_order(self, index, child_standard_order):
        """
        输入子规格排序
        """
        self.get_child_standard(index).find_element(self.locators.CHILD_STANDARD_ORDER).send_keys(child_standard_order)

    def click_save_button(self):
        """
        点击保存按钮
        """
        self.click(self.locators.SAVE)


class AddStandardPage(AddStandardPageActions):
    """
    新增规格页面的业务流程
    """
    def add_standard(self, standard_name, standard_order, child_standard_name, child_standard_order, child_num):
        """
        新增规格
        """
        self.input_standard_name(standard_name)
        self.input_standard_order(standard_order)

        for i in range(child_num):
            self.input_child_standard_name(i, child_standard_name)
            self.input_child_standard_order(i, child_standard_order)
            self.click_add_child_standard_button()
        self.click_save_button()