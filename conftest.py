import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# --- Headless Fixtures ---

@pytest.fixture()
def chrome():
    # Setup Headless Options
    options = ChromeOptions()
    options.add_argument("--headed")  # headless Essential for CI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")  # Default size for headless rendering

    # WebDriver Manager to install driver
    driver = webdriver.Chrome(service=webdriver.ChromeService(ChromeDriverManager().install()), options=options)

    yield driver
    driver.quit()


@pytest.fixture()
def edge():
    # Setup Headless Options
    options = EdgeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # WebDriver Manager to install driver
    driver = webdriver.Edge(service=webdriver.EdgeService(EdgeChromiumDriverManager().install()), options=options)

    yield driver
    driver.quit()