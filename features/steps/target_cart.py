from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
@given('Open target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')

@when('Click on cart icon')
def click_cart(context):
   # context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()
    sleep(5)
@then('Verify my cart is empty')
def verify_cart_empty(context):
    context.driver.find_element(By.ID, 'search').click()
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']").text
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'