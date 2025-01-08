from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
#import time

class ProductPage(BasePage):
    URL = 'https://www.saucedemo.com/inventory.html'
    SORT_DROPDOWN = (By.CLASS_NAME, 'product_sort_container')
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[text()='Add to cart']")
    CART_BUTTON = (By.CLASS_NAME, 'shopping_cart_link')

    def load(self):
        self.browser.get(self.URL)

    def sort_products_by_price_desc(self):
        dropdown = self.find_element(*self.SORT_DROPDOWN)
        dropdown.click()
        option = self.find_element(By.XPATH, "//option[text()='Price (high to low)']")
        option.click()

    def add_first_two_products_to_cart(self):
        buttons = WebDriverWait(self.browser, 10).until(
            ec.presence_of_all_elements_located(self.ADD_TO_CART_BUTTONS)
        ) 
        print(f"Nombre de boutons 'Add to cart' trouvés : {len(buttons)}")
        buttons[0].click()
        #time.sleep(10)
        buttons[1].click()
        
    def go_to_cart(self):
        self.find_element(*self.CART_BUTTON).click()
