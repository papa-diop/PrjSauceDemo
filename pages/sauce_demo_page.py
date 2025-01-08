from selenium.webdriver.common.by import By  
from pages.common_page import BasePage

class SauceDemoPage(BasePage):
    URL = 'https://www.saucedemo.com/'
    LOGOUT_MENU_BUTTON = (By.ID, 'react-burger-menu-btn')
    LOGOUT_BUTTON = (By.ID, 'logout_sidebar_link')
    PRODUCT_TITLE = (By.CLASS_NAME, 'title')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.error-message-container')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    '''def login(self, username, password):
        self.browser.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*self.LOGIN_BUTTON).click()'''

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