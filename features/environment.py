from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os  # For environment variables


def before_scenario(context, scenario):
    """Initializes the Selenium WebDriver and attaches it to the context."""
    # Set up options (optional: run headless)
    chrome_options = webdriver.ChromeOptions()
    # if os.environ.get('HEADLESS', 'true').lower() == 'true':
    #     chrome_options.add_argument("--headless")
    #     chrome_options.add_argument("--disable-gpu")

    # Initialize driver (using WebDriver Manager for easy setup)
    service = ChromeService(ChromeDriverManager().install())

    # Attach the driver to the context object
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver.implicitly_wait(10)  # Set implicit wait


def after_scenario(context, scenario):
    """Quits the WebDriver after each scenario."""
    if hasattr(context, 'driver'):
        context.driver.quit()