from pytest_bdd import scenario, given, when, then, parsers
from pages.sauce_demo_page import SauceDemoPage

@scenario('../features/login_logout.feature', 'Login et Logout sur Sauce Demo')
def test_login_logout_app():
    """Vérifie que l'application permet de se connecter et de se déconnecter"""

@scenario('../features/login_logout.feature', 'Login et Logout sur Sauce Demo')
def test_locked_out_login_app():
    """Vérifie que l'application affiche un message d'erreur pour un compte verrouillé"""

@given('je suis sur la page de login de Sauce Demo')
def iam_on_sauce_demo_page(browser):
    page = SauceDemoPage(browser)
    page.load()
    browser.implicitly_wait(10)

@when(parsers.parse('je me connecte avec "{username}" et "{password}"'))
def login(browser, username, password):
    page = SauceDemoPage(browser)
    page.login(username, password)

@then('je suis connecte à Sauce Demo')
def check_login_success(browser):
    page = SauceDemoPage(browser)
    assert page.is_logged_in()

@when('je me deconnecte')
def logout(browser):
    page = SauceDemoPage(browser)
    page.logout()

@then('je suis deconnecte de Sauce Demo')
def check_logout_success(browser):
    page = SauceDemoPage(browser)
    assert page.is_logged_out()

@then('je vois un message derreur indiquant que lutilisateur est verrouille')
def check_locked_out_error(browser):
    page = SauceDemoPage(browser)
    assert page.is_locked_out()