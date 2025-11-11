import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def setup_driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)

    request.cls.driver = driver  # gives driver to test class
    yield
    driver.quit()
