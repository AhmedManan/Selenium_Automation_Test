from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://mananacademy.com/")
driver.maximize_window()
expected_title="Home - Manan Academy"
if driver.title == expected_title:
    print("Test Case Passed")
    driver.quit()
else:
    print("Test Case Failed")
    driver.quit()