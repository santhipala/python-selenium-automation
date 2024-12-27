from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify my cart is empty')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_is_empty()
