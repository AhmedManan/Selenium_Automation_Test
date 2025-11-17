from selenium import webdriver
from selenium.webdriver.common.by import By

from ..base_pages.index_page import IndexPage


class TestIndexPage():
    page_url = "https://demoblaze.com/index.html"
    username = "admin"
    password = "admin"


    def test_title_verification(self):
        driver = webdriver.Chrome()
        driver.get(self.page_url)
        expected_title = "STORE"
        assert driver.title == expected_title
        driver.close()

    def test_valid_admin_login(self):
        driver = webdriver.Chrome()
        driver.get(self.page_url)
        self.index_page = IndexPage(driver)
        self.index_page.get_login_popup()
        self.index_page.enter_username(self.username)
        self.index_page.enter_password(self.password)
        self.index_page.click_login()
        assert self.index_page.get_logged_in_user() == f"Welcome {self.username}"
        driver.close()
