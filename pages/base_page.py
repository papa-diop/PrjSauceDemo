from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find_element(self, *locator):
        return self.browser.find_element(*locator)

    def find_elements(self, *locator):
        return self.browser.find_elements(*locator)
