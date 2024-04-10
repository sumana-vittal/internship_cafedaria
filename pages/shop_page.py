from selenium.webdriver.common.by import By

from pages.base_page import Page


class ShopPage(Page):

    SHOP_PAGE_TITLE = (By.CSS_SELECTOR, "div.breadcrumb-modern-body h1")
    SHOP_PRODUCTS = (By.CSS_SELECTOR, "div.product a.button")
    CART_ICON = (By.CSS_SELECTOR, "a.mdi-cart-outline")

    def verify_shop_page_open(self):
        self.verify_partial_url("catalog")

    def verify_shop_title_catalog(self):
        self.presence_of_element_located(*self.SHOP_PAGE_TITLE)

    def add_to_cart(self):
        products = self.find_elements(*self.SHOP_PRODUCTS)
        for i in range(0, 2):
            self.wait_element_clickable_click(products[i])

    def click_cart_icon(self):
        self.wait_locator_clickable_click(*self.CART_ICON)





