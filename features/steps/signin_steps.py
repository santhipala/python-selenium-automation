import selenium
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




@when('Click on the Sign In option from the navigation menu')
def click_signin_nav(context):
    context.app.header.side_nav_sign_in()

@then('Verify Sign In form opened')
def signin_form(context):
   context.app.signin_page.verify_signin_form()

