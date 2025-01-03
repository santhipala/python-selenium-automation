from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def open(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_partial_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url in actual_url, f'Expected partial url {expected_url} not in actual {actual_url}'

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows=self.driver.window_handles
        print('All Windows',all_windows)
        self.driver.switch_to.window(all_windows[1])
        print('Current Window:',self.driver.current_window_handle)

    def switch_to_original_window_by_id(self,window_id):
        self.driver.switch_to.window(window_id)
        print('Current Window:',self.driver.current_window_handle)

    def close(self):
        self.driver.close()