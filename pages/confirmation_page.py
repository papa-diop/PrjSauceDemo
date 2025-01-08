from selenium.webdriver.common.by import By

from pages.common_page import BasePage


class ConfirmationPage (BasePage):

    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')