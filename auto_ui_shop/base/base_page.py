from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    页面对象基类，封装常用操作方法
    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """查找单个元素"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """查找多个元素"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        """点击元素"""
        self.find_element(locator).click()

    def input_text(self, locator, text):
        """输入文本"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """获取元素文本"""
        return self.find_element(locator).text

    def get_value(self, locator):
        """获取元素值"""
        return self.find_element(locator).get_attribute("value")
    
    def upload_file(self, locator, path):
        """上传文件"""
        self.find_element(locator).send_keys(path)
    
    def select(self, locator, value):
        """选择下拉框选项"""
        self.find_element(locator).click()