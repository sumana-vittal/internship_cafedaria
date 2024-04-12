from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page


class ContactPage(Page):

    CONTACT_TITLE = (By.CSS_SELECTOR, "h1.breadcrumbs-custom-title")
    GET_IN_TOUCH_TITLE = (By.XPATH, "//h3[text()='Get in Touch']")

    FIRST_NAME_FIELD = (By.ID, "contacts-name")
    LAST_NAME_FIELD = (By.ID, "contacts-last-name")
    EMAIL_FIELD = (By.ID, "contacts-email")
    PHONE_FIELD = (By.ID, "contacts-phone")
    MESSAGE_FIELD = (By.ID, "contacts-message")
    SEND_BUTTON = (By.CSS_SELECTOR, ".js-contact-submit")

    def verify_contact_page_open(self):
        self.verify_partial_url("contacts")

    def verify_contact_title(self):
        self.presence_of_element_located(*self.CONTACT_TITLE)

    def verify_title_get_in_touch(self):
        self.presence_of_element_located(*self.GET_IN_TOUCH_TITLE)

    def enter_contact_test_data(self):
        self.input_text("abc", *self.FIRST_NAME_FIELD)
        self.input_text("test", *self.LAST_NAME_FIELD)
        self.input_text("test@test.com", *self.EMAIL_FIELD)
        self.input_text("0000000000", *self.PHONE_FIELD)
        self.input_text("contact details", *self.MESSAGE_FIELD)

    def verify_send_btn_clickable(self):
        self.wait_element_locator_clickable(*self.SEND_BUTTON)

