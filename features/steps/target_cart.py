

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


CART_ICON=(By.XPATH, "//div[@data-test='@web/CartIcon']")
CART_EMPTY=(By.XPATH, "//div[@data-test='boxEmptyMsg']")


# @given('Open target main page')
# def open_target_main_page(context):
#     context.driver.get('https://www.target.com/')

# @when('Click on cart icon')
# def click_cart(context):
#     # context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()
#     # sleep(5)
#     WebDriverWait(context.driver, 10).until(
#     EC.presence_of_element_located(CART_ICON)).click()
#
# @then('Verify my cart is empty')
# def verify_cart_empty(context):
#     context.driver.find_element(By.ID, 'search').click()
#     expected_result = 'Your cart is empty'
#     actual_result = WebDriverWait(context.driver, 10).until(
#             EC.element_to_be_clickable(CART_EMPTY)).text
#     assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'