import selenium
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open sign in page')
def open_signin_page(context):
    context.app.main_page.main_page()
    context.app.header.sign_in()
    context.app.header.side_nav_sign_in()
    sleep(3)

@when('Store original window')
def store_original_window(context):
        context.original_window = context.app.base_page.get_current_window_handle()
        print(context.original_window)

@when('Click on Target terms and conditions link')
def click_terms_and_conditions(context):
    context.app.signin_page.terms_and_conditions()
    sleep(3)

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    # sleep(3)
    # print('All windows: ', context.driver.window_handles)
    # context.driver.switch_to.window(context.driver.window_handles[1])
    context.app.base_page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.terms_and_conditions_page.verify_tc_opened()

@then('User can close new window and switch back to original')
def close_tc_window(context):
    context.app.base_page.close()
    context.app.base_page.switch_to_original_window_by_id(context.original_window)




@when('Click on the Sign In option from the navigation menu')
def click_signin_nav(context):
    context.app.header.side_nav_sign_in()

@then('Verify Sign In form opened')
def signin_form(context):
   context.app.signin_page.verify_signin_form()

