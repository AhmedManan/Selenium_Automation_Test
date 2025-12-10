import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ..base_pages.product_page import ProductPage
from ..conftest import chrome
from ..utilities.read_proparties import ReadConfig
from ..utilities.custom_logger import LogMaker
from ..utilities.get_env import username, password, base_url



class TestProductPage:
    page_url = base_url+'/prod.html?idp_=1'
    username = username
    password = password
    logger = LogMaker.generate_log()

    # -------------------------------------------------
    # test cases
    # -------------------------------------------------

    def test_product_name_verification(self, chrome):
        driver = chrome
        driver.get(self.page_url)
        self.product_page = ProductPage(driver)
        expected_product_name = "Samsung galaxy s6"
        assert self.product_page.get_product_name() == expected_product_name
