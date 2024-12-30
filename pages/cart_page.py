from pages.base_page import BasePage
from pages.search_results_page import SearchResultsPage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    CART_EMPTY = (By.XPATH, "//div[@data-test='boxEmptyMsg']")
    CHECK_OUT=(By.CSS_SELECTOR,"a[href='/cart']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "a[data-test='cartItem-linked-title']>div>div")
    def verify_cart_is_empty(self):
        actual_cart=self.find_element(*self.CART_EMPTY).text
        assert 'Your cart is empty' in actual_cart, f'Expected cart not empty but actual {actual_cart}'

    def click_cart(self):
        self.find_element(*self.CHECK_OUT).click()

    def verify_product_added(self,product):
        actual_product_added=self.find_element(*self.PRODUCT_NAME).text
        assert product in actual_product_added, f'expected_product {product} but actual {actual_product_added}'

