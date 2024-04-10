from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):

    CART_COUNTER_ITEMS = (By.CSS_SELECTOR, "h3.js-cart-items-counter")

    def verify_cart_page_opens(self):
        self.verify_partial_url("shopping-cart")

    def verify_cart_items(self):
        item_counter = self.find_element(*self.CART_COUNTER_ITEMS)
        print(item_counter)

