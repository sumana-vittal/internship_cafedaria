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

