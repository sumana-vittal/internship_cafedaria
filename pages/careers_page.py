from pages.base_page import Page


class CareersPage(Page):

    def verify_careers_page_opens(self):
        self.verify_partial_url("careers")
