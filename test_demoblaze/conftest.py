import pytest
from selenium import webdriver


@pytest.fixture()
def chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.close()

@pytest.fixture()
def edge():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.close()