from selenium.webdriver.common.by import By

from pages.base_page import Page


class AboutPage(Page):

    ABOUT_TITLE = (By.XPATH, "//h3[text()='A Few Words About Us']")

    def verify_about_page_opens(self):
        self.verify_partial_url("about")

    def verify_about_page_title(self):
        self.presence_of_element_located(*self.ABOUT_TITLE)
