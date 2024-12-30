from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from time import sleep

class SearchResultsPage(BasePage):
    SEARCH_RESULTS=(By.XPATH, "//div[@data-test='resultsHeading']")
    FIRST_PRODUCT=(By.CSS_SELECTOR,"picture[data-test='@web/ProductCard/ProductCardImage/primary']")
    ADD_TO_CART_BTN=(By.CSS_SELECTOR, "button[data-test='chooseOptionsButton']")
    ADD_TO_CART_SIDE_NAV_BTN = (By.CSS_SELECTOR, "button[data-test='orderPickupButton']")


    def search_results(self):
        actual_search=self.find_element(*self.SEARCH_RESULTS).text
        assert 'coffee' in actual_search, f'Expected coffee not in actual {actual_search}'

    # def select_product(self):
    #     first_product = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(self.ADD_TO_CART_BTN)
    #     )
    #     first_product.click()

    def add_to_cart(self,product):
        # Wait for any potential overlay (modal) to disappear
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, '.ReactModal__Overlay'))
        )

        try:
            add_to_cart_button=WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BTN)
            )
            # Scroll the button into view
            self.driver.execute_script('arguments[0].scrollIntoView(true);', add_to_cart_button)

            add_to_cart_button.click()
            print(f"Product {product} selected for the cart.")
        except Exception as e:
            print(f"Failed to add {product} selected for the cart: {e}")
            raise


        try:
            add_to_cart_side_nav_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(self.ADD_TO_CART_SIDE_NAV_BTN)
            )

            # Scroll the button into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_side_nav_button)

            add_to_cart_side_nav_button.click()
            print(f"Product {product} added to the cart.")
        except Exception as e:
            print(f"Failed to add {product} to the cart: {e}")
            raise

        sleep(2)