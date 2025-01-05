from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
class HelpPage(BasePage):

    HEADER_TEXT = (By.XPATH, "//h1[text()=' {SUBSTRING}']")
    HELP_DD = (By.CSS_SELECTOR, "[id*='ViewHelpTopics']")

    # Dynamic locator
    def _get_header_locator(self, text):
        # HEADER_TXT = (By.XPATH, "//h1[text()=' {SUBSTRING}']")
        # => HEADER_TXT = (By.XPATH, "//h1[text()=' Returns']")
        return [self.HEADER_TEXT[0], self.HEADER_TEXT[1].replace('{SUBSTRING}', text)]

    # Step 1: Open Target Help page
    def click_help(self):
        self.open('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def verify_help_opened(self):
        self.verify_partial_url('/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def select_promotions(self, dd_option_value):
        dropdown = self.find_element(*self.HELP_DD)
        select = Select(dropdown)
        select.select_by_value(dd_option_value)

    def select_returns(self, dd_option_value):
        # Step 2: Locate the dropdown for Help topics
        dropdown = self.find_element(*self.HELP_DD)
        # Step 3: Select a topic (e.g., "Returns & Exchanges")
        select = Select(dropdown)
        select.select_by_value(dd_option_value)

    def verify_hep_topic_opened(self, selected_header):
        # Step 4: Verify that the correct Help page URL is opened
        locator = self._get_header_locator(selected_header)
        self.wait_for_element_visible(*locator)