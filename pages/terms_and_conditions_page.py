from pages.base_page import BasePage
class TermsAndConditionsPage(BasePage):

    def verify_tc_opened(self):
        self.verify_partial_url('/c/terms-conditions/')
