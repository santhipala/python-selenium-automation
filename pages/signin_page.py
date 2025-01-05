from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from time import sleep
USER_NAME=(By.ID,'username')
PASSWORD=(By.ID,'password')
LOGIN_BTN=(By.ID,'login')
TERMS_AND_CONDITIONS=(By.CSS_SELECTOR,"a[href='/c/terms-conditions/-/N-4sr7l'][aria-label='terms & conditions - opens in a new window']")
# LOGIN_ERROR=(By.CSS_SELECTOR,"div[data-test='authAlertDisplay']>div")
LOGIN_ERROR=(By.XPATH, "//div[@data-test='authAlertDisplay']/div")
class SigninPage(BasePage):

    def verify_signin_form(self):
        # Wait for the sign-in form button to be visible
        sign_in_form=self.wait_for_element_visible(*LOGIN_BTN)
        # Assert the element is displayed
        assert sign_in_form.is_displayed(), "Sign In form is not displayed"

    def terms_and_conditions(self):
        self.find_element(*TERMS_AND_CONDITIONS).click()

    def enter_username(self,username):
        self.input_text(username,*USER_NAME)

    def enter_password(self,password):
        self.input_text(password,*PASSWORD)

    def click_signin(self):
        self.click(*LOGIN_BTN)

    def verify_login_message(self):
        login_message=self.wait_for_element_visible(*LOGIN_ERROR).text
        print("Login message",login_message)
