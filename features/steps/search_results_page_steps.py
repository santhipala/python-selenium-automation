from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Verify search worked for {product}')
def verify_search_worked(context, product):
    context.app.search_results_page.search_results()