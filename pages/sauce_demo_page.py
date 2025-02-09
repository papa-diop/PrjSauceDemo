from selenium.webdriver.common.by import By  
from pages.base_page import BasePage
class SauceDemoPage(BasePage):
    URL = 'https://www.saucedemo.com/'
    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    LOGOUT_MENU_BUTTON = (By.ID, 'react-burger-menu-btn')
    LOGOUT_BUTTON = (By.ID, 'logout_sidebar_link')
    PRODUCT_TITLE = (By.CLASS_NAME, 'title')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.error-message-container')

    def load(self):
        self.browser.get(self.URL)

    def login(self, username, password):
        self.browser.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*self.LOGIN_BUTTON).click()

    def is_logged_in(self):
        return self.browser.find_element(*self.PRODUCT_TITLE).is_displayed()

    def logout(self):
        self.browser.find_element(*self.LOGOUT_MENU_BUTTON).click()
        self.browser.find_element(*self.LOGOUT_BUTTON).click()

    def is_logged_out(self):
        return self.browser.find_element(*self.LOGIN_BUTTON).is_displayed()
    
    def is_locked_out(self):
        return self.browser.find_element(*self.ERROR_MESSAGE).is_displayed()