
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CELLS=(By.CSS_SELECTOR, "[data-test*='@web/slingshot-components/CellsComponent/Link']")
EXPECTED_SEARCH_RESULT=(By.CSS_SELECTOR, "[data-test='@web/CartLink']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[data-test='chooseOptionsButton']")
ADD_TO_CART_SIDE_NAV_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
CART_ITEM=(By.CSS_SELECTOR, "div[data-test='cartItem']")
CART_ICON=(By.CSS_SELECTOR, "a[href='/cart']")
FIRST_PRODUCT=(By.CSS_SELECTOR, "[data-test*='ProductCardWrapper']")
TOTAL_PRICE=(By.CSS_SELECTOR, "p[data-test='cartItem-price']")
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
LISTINGS = (By.CSS_SELECTOR, "[data-test*='@web/site-top-of-funnel/ProductCardWrapper']")
SEARCH_BTN=(By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(5)


@then('Verify search worked for {product}')
def verify_search_worked(context, product):
    actual_search=product
    expected_search_result=context.driver.find_element(*EXPECTED_SEARCH_RESULT).text
    assert expected_search_result in actual_search, f'Expected text {expected_search_result} not in actual {actual_search}'


@given('Open target circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify {expected} benefit cells')
def verify_bcells(context, expected):
    cells = context.driver.find_elements(*CELLS)
    print('\nFind Benefit Cells:')
    print(cells)
    print(f"Number of Benefit cells found: {len(cells)}")
    assert len(cells) >= len(expected), f'Expected {expected} links but got {len(cells)}'


# @when('Search for {product}')
# def search_product(context, product):
#     context.driver.find_element(By.ID, 'search').send_keys(product)

@when('Add any {product} into a cart')
def add_to_cart(context, product):
    # Step 1: Select the first product in the search results
    first_product = context.driver.find_element(*FIRST_PRODUCT)
    first_product.click()
    sleep(2)  # Wait for product page to load

    # Step 2: Wait for the "Add to Cart" button to be clickable and scroll it into view
    try:
        add_to_cart_button = WebDriverWait(context.driver, 20).until(
            EC.element_to_be_clickable(ADD_TO_CART_BTN))

        # Scroll the button into view
        context.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)

        # Wait again to make sure the element is clickable
        WebDriverWait(context.driver, 20).until(
            EC.element_to_be_clickable(ADD_TO_CART_BTN)
        )

        add_to_cart_button.click()
        print(f"Product {product} selected for the cart.")
    except Exception as e:
        print(f"Failed to add {product} selected for the cart: {e}")
        raise
    # Step 2a: Wait for the "Add to Cart navigation" button to be clickable and scroll it into view
    try:
        add_to_cart_side_nav_button = WebDriverWait(context.driver, 20).until(
            EC.element_to_be_clickable(ADD_TO_CART_SIDE_NAV_BTN)
        )

        # Scroll the button into view
        context.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_side_nav_button)

        # Wait again to make sure the element is clickable
        WebDriverWait(context.driver, 20).until(
            EC.element_to_be_clickable(ADD_TO_CART_SIDE_NAV_BTN)
        )

        add_to_cart_side_nav_button.click()
        print(f"Product {product} added to the cart.")
    except Exception as e:
        print(f"Failed to add {product} to the cart: {e}")
        raise

    sleep(2)  # Wait for the item to be added to the cart


    try:
        cart_icon = WebDriverWait(context.driver, 20).until(
            EC.element_to_be_clickable(CART_ICON)
        )
        cart_icon.click()
        print("Cart icon clicked successfully.")
    except Exception as e:
        print(f"Failed to click on cart icon: {e}")
        raise

    # Step 4: Verify the product is in the cart
@then('Verify {product} added to cart')
def verify_add_to_cart(context, product):
    try:
        cart_item = context.driver.find_element(*CART_ITEM)
        assert product in cart_item.text, f"Product {product} is not in the cart"
        print(f"Test Passed: Product {product} is in the cart.")
    except Exception as e:
        print(f"Test Failed: Product {product} is not in the cart. Error: {e}")
        raise

    # Step 5: Optionally, verify the total price or cart items count
    try:
        total_price = context.driver.find_element(*TOTAL_PRICE).text
        print(f"Total price in the cart: {total_price}")
    except Exception as e:
        print(f"Unable to retrieve total price. Error: {e}")
        raise
