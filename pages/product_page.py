import selenium.webdriver.common.by
from pages.common_page import BasePage


class ProductPage (BasePage):
    URL = 'https://www.saucedemo.com/inventory.html'
    LOGOUT_MENU_BUTTON = (selenium.webdriver.common.by.By.ID, 'react-burger-menu-btn')
    LOGOUT_BUTTON = (selenium.webdriver.common.by.By.ID, 'logout_sidebar_link')
    PRODUCT_TITLE = (selenium.webdriver.common.by.By.CLASS_NAME, 'title')
    ERROR_MESSAGE = (selenium.webdriver.common.by.By.CSS_SELECTOR, '.error-message-container')


    def load(self):
        self.browser.get(self.URL)

    def is_logged_in(self):
        """WebDriverWait(self.browser, 10).until(
            ec.url_to_be("LOGGED_PAGE_URL")
        )"""
        return self.browser.find_element(*self.PRODUCT_TITLE).is_displayed()

    def logout(self):
        self.browser.find_element(*self.LOGOUT_MENU_BUTTON).click()
        self.browser.find_element(*self.LOGOUT_BUTTON).click()

    def is_logged_out(self):
        return self.browser.find_element(*self.LOGIN_BUTTON).is_displayed()

    def is_locked_out(self):
        return self.browser.find_element(*self.ERROR_MESSAGE).is_displayed()