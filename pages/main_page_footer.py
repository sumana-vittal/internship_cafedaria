from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPageFooter(Page):

    FOOTER = (By.CSS_SELECTOR, "[class*='page-footer']")
    FOOTER_TITLE = (By.CSS_SELECTOR, "[class*='page-footer'] .brand")
    GOOGLE_MAP = (By.CSS_SELECTOR, "[class*='google-map-container']")

    def open_home_page(self):
        self.open("https://cafedaria.com/")

    def verify_footer_title(self):
        # self.verify_text("CAFEDARIA",*self.FOOTER_TITLE)
        self.presence_of_element_located(*self.FOOTER_TITLE)

    def verify_footer_map(self):
        self.presence_of_element_located(*self.GOOGLE_MAP)
