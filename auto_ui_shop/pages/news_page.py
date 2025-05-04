from base.base_page import BasePage
from selenium.webdriver.common.by import By


class NewsPageLocators(object):
    """
    新闻页面元素定位器
    """
    self.NEWS = (By.CSS_SELECTOR, ".bk-media-content")  # 新闻标题
    self.PAGES = (By.CSS_SELECTOR, ".bk-pagination-link")  # 分页


class NewsPageAction(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = NewsPageLocators()

    def get_news_list(self):
        """获取新闻"""
        return self.find_elements(self.locators.NEWS)

    def get_news(self, index):
        """获取选中的新闻"""
        return self.get_news_list()[index]

    def get_pages(self):
        """获取所有分页"""
        return self.find_elements(self.locators.PAGES)

    def get_page(self, index):
        """获取选中的分页"""
        return self.get_pages()[index]

    def get_current_page(self):
        """获取当前页码"""
        pages = self.get_pages()


class NewsPage(NewsPageAction):
    '''
    新闻页面业务层
    '''
    def read_news(self, index):
        """点击新闻"""
        self.click_news(index)

    def goto_page(self, index):
        """点击分页"""
        self.click_page(index)