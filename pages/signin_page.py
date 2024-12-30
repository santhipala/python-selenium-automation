from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

LOGIN_BTN=(By.ID,'login')

class SigninPage(BasePage):
    def verify_signin_form(self):
        # Wait for the sign-in form button to be visible
        sign_in_form = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LOGIN_BTN)
        )
        # Assert the element is displayed
        assert sign_in_form.is_displayed(), "Sign In form is not displayed"