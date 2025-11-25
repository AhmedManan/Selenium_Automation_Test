import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ..base_pages.index_page import IndexPage
from ..conftest import chrome
from ..utilities.read_proparties import ReadConfig



class TestIndexPage:
    page_url = ReadConfig.get_login_page_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    invalid_login_data = ReadConfig.get_invalid_login_data()


    def test_title_verification(self, chrome):
        driver = chrome
        driver.get(self.page_url)
        expected_title = "STORE"
        assert driver.title == expected_title

    def test_valid_admin_login(self, chrome):
        driver = chrome
        driver.get(self.page_url)
        self.index_page = IndexPage(driver)
        self.index_page.get_login_popup()
        self.index_page.enter_username(self.username)
        self.index_page.enter_password(self.password)
        self.index_page.click_login()
        if self.index_page.get_logged_in_user() == f"Welcome {self.username}":
            assert True
        else:
            driver.save_screenshot('.\\test_demoblaze\\screenshots\\test_admin_login.png')
            assert False

    @pytest.mark.parametrize("username, password", invalid_login_data)
    def test_invalid_admin_login(self, edge, username, password) ->None:
        driver = edge
        driver.get(self.page_url)
        self.index_page = IndexPage(driver)
        self.index_page.get_login_popup()
        self.index_page.enter_username(username)
        self.index_page.enter_password(password)
        self.index_page.click_login()
        alert = WebDriverWait(driver,10).until(expected_conditions.alert_is_present())
        assert (alert.text == "Please fill out Username and Password."
                or alert.text == "User does not exist."
                or alert.text == "Wrong password.")
        alert.accept()
