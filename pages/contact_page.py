from selenium.webdriver.common.by import By

from pages.base_page import Page


class ContactPage(Page):

    CONTACT_TITLE = (By.CSS_SELECTOR, "h1.breadcrumbs-custom-title")
    GET_IN_TOUCH_TITLE = (By.XPATH, "//h3[text()='Get in Touch']")

    def verify_contact_page_open(self):
        self.verify_partial_url("contacts")

    def verify_contact_title(self):
        self.presence_of_element_located(*self.CONTACT_TITLE)

    def verify_title_get_in_touch(self):
        self.presence_of_element_located(*self.GET_IN_TOUCH_TITLE)
