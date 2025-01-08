from pytest_bdd import scenario, given, when, then, parsers

from pages.cart_page import CartPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage
from pages.sauce_demo_page import SauceDemoPage
from pages.product_page import ProductPage

@when('je me connecte avec le compte standard')
def login_standard_user(browser):
    page = SauceDemoPage(browser)
    page.login('standard_user', 'secret_sauce')


@when('je trie la liste du plus cher au moins cher')
def sort_products(browser):
    page = ProductPage(browser)
    page.sort_products_by_price_desc()


@when('j\'ajoute les deux premiers produits au panier')
def add_first_two_products_to_cart(browser):
    page = ProductPage(browser)
    page.add_first_two_products_to_cart()

@when('je vais au panier')
def go_to_cart(browser):
    page = CartPage(browser)
    page.go_to_cart()


@then('je vérifie qu\'on a bien deux produits dans le panier')
def check_two_products_in_cart(browser):
    page = CartPage(browser)
    assert page.get_cart_item_count() == 2


@when(parsers.parse('je saisis les informations du client "{first_name}" "{last_name}" "{postal_code}"'))
def enter_customer_info(browser, first_name, last_name, postal_code):
    page = CheckoutPage(browser)
    page.enter_customer_info(first_name, last_name, postal_code)


@when('je finalise la commande')
def finish_order(browser):
    page = CheckoutOverviewPage(browser)
    page.finish_order()


@then('je vérifie que la commande s\'est bien réalisée')
def check_order_success(browser):
    page = ConfirmationPage(browser)
    assert page.is_order_successful()