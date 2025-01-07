from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class SauceDemoPage:
    URL = 'https://www.saucedemo.com/'
    LOGGED_PAGE_URL = 'https://www.saucedemo.com/inventory.html'
    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    LOGOUT_MENU_BUTTON = (By.ID, 'react-burger-menu-btn')
    LOGOUT_BUTTON = (By.ID, 'logout_sidebar_link')
    PRODUCT_TITLE = (By.CLASS_NAME, 'title')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def login(self, username, password):
        self.browser.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*self.LOGIN_BUTTON).click()

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
