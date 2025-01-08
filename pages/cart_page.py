from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class CartPage(BasePage):
    URL = 'https://www.saucedemo.com/cart.html'
    CART_ITEMS = (By.CLASS_NAME, 'cart_item')
    CART_QUANTITY = (By.CLASS_NAME, 'cart_quantity')
    CHECKOUT_BUTTON = (By.ID, 'checkout')

    def get_cart_quantity(self):
        return len(self.find_elements(*self.CART_QUANTITY))

    def proceed_to_checkout(self):
        self.find_element(*self.CHECKOUT_BUTTON).click()

    def cart_contains_two_products(self):
        return self.get_cart_quantity() == 2