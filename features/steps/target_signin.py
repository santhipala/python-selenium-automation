#from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


#from selenium.webdriver.support.wait import WebDriverWait


# @given('Open target home page')
# def open_target(context):
#     context.driver = webdriver.Chrome()
#     context.driver.get('https://www.target.com/')

@when('Click on the Sign In link')
def click_signin_link(context):
    sign_in_link = context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']")
    sign_in_link.click()

@when('Click on the Sign In option from the navigation menu')
def click_signin_nav(context):
    sign_in_button = context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']")
    sign_in_button.click()
# sleep(3)
# @then('I should see the Sign In form')
# def signin_form(context):
#     sign_in_form = context.driver.find_element(By.XPATH,"//button[@type='submit']")
#     assert sign_in_form.is_displayed(), "Sign In form is not displayed"
#     context.driver.quit()
@then('I should see the Sign In form')
def signin_form(context):
    # Wait for the sign-in form button to be visible
    sign_in_form = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))
    )
    # Assert the element is displayed
    assert sign_in_form.is_displayed(), "Sign In form is not displayed"

