from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Verify my cart is empty')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_is_empty()

@when('Click on check out')
def click_cart_icon(context):
    context.app.cart_page.click_cart()

@then('Verify {product} added to cart')
def verify_product_added(context, product):
    context.app.cart_page.verify_product_added(product)