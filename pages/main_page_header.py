from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPageHeader(Page):

    HEADER_TITLE = (By.CSS_SELECTOR, ".page-header .rd-navbar-brand")
    HEADER_NAV_ITEMS = (By.CSS_SELECTOR, ".rd-navbar-nav li.rd-nav-item")
    CART_ICON = (By.CSS_SELECTOR, "a.mdi-cart-outline")
    SEARCH_ICON = (By.CSS_SELECTOR, "div.rd-navbar-search")
    ABOUT_LINK = (By.CSS_SELECTOR, ".rd-navbar-nav [href*='about']")
    TEAM_OPTION = (By.XPATH, "//a[text()='Team']")
    FAQ_OPTION = (By.XPATH, "//a[text()='FAQ']")
    CAREERS_OPTION = (By.XPATH, "//a[text()='Careers']")
    SHOP_LINK = (By.XPATH, "//a[text()='Shop']")
    CONTACT_LINK = (By.XPATH, "//a[text()='Contacts']")

    def click_about(self):
        self.wait_locator_clickable_click(*self.ABOUT_LINK)

    def click_contact(self):
        self.wait_locator_clickable_click(*self.CONTACT_LINK)

    def verify_header_title(self):
        self.presence_of_element_located(*self.HEADER_TITLE)

    def verify_header_sub_titles(self, no_of_sub_titles):
        nav_items = self.find_elements(*self.HEADER_NAV_ITEMS)
        assert len(nav_items) == int(no_of_sub_titles), f"Required {no_of_sub_titles} sub titles but found {len(nav_items)}."
        for item in nav_items:
            self.wait_element_clickable(item)
            # print(item.text)

    def verify_cart_search_icon(self):
        self.presence_of_element_located(*self.CART_ICON)
        self.presence_of_element_located(*self.SEARCH_ICON)

    def hover_over_about(self):
        web_element = self.find_element(*self.ABOUT_LINK)
        self.hover_over(web_element)
        # sleep(3)

    def click_on_team(self):
        self.wait_locator_clickable_click(*self.TEAM_OPTION)

    def click_on_faq(self):
        self.wait_locator_clickable_click(*self.FAQ_OPTION)

    def click_on_career(self):
        self.wait_locator_clickable_click(*self.CAREERS_OPTION)

    def click_on_shop(self):
        self.wait_locator_clickable_click(*self.SHOP_LINK)




