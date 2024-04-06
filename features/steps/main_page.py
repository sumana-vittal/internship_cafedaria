from behave import given, when, then
from selenium.webdriver.common.by import By

FOOTER_TITLE = (By.CSS_SELECTOR, "[class*='page-footer'] .brand")

@given("Open the main page.")
def open_home_page(context):
    context.app.main_page_footer.open_home_page()


@when("Scroll down to the footer.")
def scroll_footer(context):
    context.driver.execute_script("window.scrollBy(0,3000)","")


@then("Verify the title Cafedaria in the footer exists.")
def verify_footer_title(context):
    context.app.main_page_footer.verify_footer_title()
    # title = context.driver.find_element(*FOOTER_TITLE).text
    # print(title)


@then("Verify the footer contains a map.")
def verify_footer_map(context):
    context.app.main_page_footer.verify_footer_map()


@then("Verify the title Cafedaria exists on the navigation bar.")
def verify_header_title(context):
    context.app.main_page_header.verify_header_title()


@then("Verify there are {no_of_sub_titles} sub-titles in the navigation bar and all of them are clickable.")
def verify_header_sub_titles(context, no_of_sub_titles):
    context.app.main_page_header.verify_header_sub_titles(no_of_sub_titles)


@then("Verify the cart and search icons exists.")
def verify_cart_search_icon(context):
    context.app.main_page_header.verify_cart_search_icon()
