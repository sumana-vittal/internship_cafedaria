from pages.base_page import Page
from pages.main_page_footer import MainPageFooter


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page_footer = MainPageFooter(driver)
