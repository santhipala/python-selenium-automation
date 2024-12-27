from time import sleep

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class Header(BasePage):
    SEARCH_PRODUCT = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.XPATH, "//div[@data-test='@web/CartIcon']")

    def search_product(self):
        self.input_text('coffee',*self.SEARCH_PRODUCT)
        self.click(*self.SEARCH_BTN)
        sleep(10)

    def click_cart(self):
            self.click(*self.CART_ICON)