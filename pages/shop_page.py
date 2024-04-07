from selenium.webdriver.common.by import By

from pages.base_page import Page


class ShopPage(Page):

    SHOP_PAGE_TITLE = (By.CSS_SELECTOR, "div.breadcrumb-modern-body h1")

    def verify_shop_page_open(self):
        self.verify_partial_url("catalog")

    def verify_shop_title_catalog(self):
        self.presence_of_element_located(*self.SHOP_PAGE_TITLE)


