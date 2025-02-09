import pytest

from pytest_bdd import given
from selenium import webdriver

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


# Fixtures

@pytest.fixture
def browser():
    # For this example, we will use Firefox
    # You can change this fixture to use other browsers, too.
    # A better practice would be to get browser choice from a config file.
    b = webdriver.Chrome()
    b.implicitly_wait(10)
    yield b
    b.quit()
