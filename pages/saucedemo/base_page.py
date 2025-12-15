class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def click(self, element):
        element.click()

    def enter_text(self, element, text):
        element.clear()
        element.send_keys(text)

    def get_text(self, element):
        return element.text

    def is_element_displayed(self, element):
        return element.is_displayed()
