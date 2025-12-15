from behave import *
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