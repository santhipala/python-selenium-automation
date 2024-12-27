from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open target main page')
def open_target_main_page(context):
    context.app.main_page.main_page()


@when('Search for {product}')
def search_for_coffee(context, product):
    context.app.header.search_product()


@when('Click on cart icon')
def click_cart(context):
    context.app.header.click_cart()
