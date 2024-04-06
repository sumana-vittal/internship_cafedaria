from pages.base_page import Page


class FAQPage(Page):

    def verify_faq_page_opens(self):
        self.verify_partial_url("faq")
