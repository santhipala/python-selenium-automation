from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    CART_EMPTY = (By.XPATH, "//div[@data-test='boxEmptyMsg']")

    def verify_cart_is_empty(self):
        actual_cart=self.find_element(*self.CART_EMPTY).text
        assert 'Your cart is empty' in actual_cart, f'Expected cart not empty but actual {actual_cart}'

