from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    SEARCH_RESULTS=(By.XPATH, "//div[@data-test='resultsHeading']")

    def search_results(self):
        actual_search=self.find_element(*self.SEARCH_RESULTS).text
        assert 'coffee' in actual_search, f'Expected coffee not in actual {actual_search}'