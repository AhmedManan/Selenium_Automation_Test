from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.demoblaze.index_page import IndexPage
from utilities.get_env import username, password, base_url

page_url = base_url + '/index.html'


# ------------------------------------------------------------------
# Test Case
# ------------------------------------------------------------------

@Given('user is on the login page')
def step_impl(context):
    driver = context.driver  # Get the WebDriver from the context
    driver.get(page_url)  # Use driver.get() for Selenium navigation


@When('user enters valid username & password')
def step_impl(context):
    driver = context.driver
    index_page = IndexPage(driver)
    index_page.get_login_popup()
    index_page.enter_username(username)
    index_page.enter_password(password)


@when('user enters username "{username}" and password "{password}"')
def step_impl(context, username, password):
    driver = context.driver
    index_page = IndexPage(driver)

    index_page.get_login_popup()
    # Use the injected parameters
    index_page.enter_username(username)
    index_page.enter_password(password)


@When('click on the login button')
def step_impl(context):
    driver = context.driver
    index_page = IndexPage(driver)
    index_page.click_login()


@Then('the username should be visible in the index page')
def step_impl(context):
    driver = context.driver
    index_page = IndexPage(driver)

    logged_in_user_text = index_page.get_logged_in_user()
    expected_text = f"Welcome {username}"

    if logged_in_user_text != expected_text:
        # Save screenshot only on failure
        driver.save_screenshot('screenshots/test_admin_login.png')

    assert logged_in_user_text == expected_text, \
        f"Login failed. Expected user text: '{expected_text}', Actual: '{logged_in_user_text}'"


@then('a login failure alert with the message "{expected_message}" is displayed')
def step_impl(context, expected_message):
    driver = context.driver

    # Wait for the alert to appear (Necessary for Selenium)
    alert = WebDriverWait(driver, 10).until(expected_conditions.alert_is_present())
    actual_message = alert.text

    # Assert the alert message matches the expected message from the table
    assert actual_message == expected_message, \
        f"Alert message mismatch. Expected: '{expected_message}', Actual: '{actual_message}'"

    # Accept the alert to continue/end the scenario
    alert.accept()