from pages.about_page import AboutPage
from pages.base_page import Page
from pages.main_page_footer import MainPageFooter
from pages.main_page_header import MainPageHeader


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page_footer = MainPageFooter(driver)
        self.main_page_header = MainPageHeader(driver)
        self.about_page = AboutPage(driver)
