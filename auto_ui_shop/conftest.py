import pytest
from base.logger import setup_logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 初始化日志配置（测试启动时执行一次）
setup_logger()

@pytest.fixture(scope="session")
def browser():
    """
    初始化浏览器驱动
    """
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver_path = 'D:/DevTool/Anaconda/chromedriver134.exe'
    driver = webdriver.Chrome(service=Service(driver_path))
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def base_url():
    """
    基础URL配置
    """
    # return "http://baykeshop.proae.cn/"
    return "http://localhost:8080/"