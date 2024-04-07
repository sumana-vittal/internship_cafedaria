from pages.about_page import AboutPage
from pages.base_page import Page
from pages.careers_page import CareersPage
from pages.faq_page import FAQPage
from pages.main_page_footer import MainPageFooter
from pages.main_page_header import MainPageHeader
from pages.team_page import TeamPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page_footer = MainPageFooter(driver)
        self.main_page_header = MainPageHeader(driver)
        self.about_page = AboutPage(driver)
        self.team_page = TeamPage(driver)
        self.faq_page = FAQPage(driver)
        self.careers_page = CareersPage(driver)
