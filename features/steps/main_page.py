from behave import given, when, then


@given("Open the main page.")
def open_home_page(context):
    context.app.main_page_footer.open_home_page()


@when("Scroll down to the footer.")
def scroll_footer(context):
    context.driver.execute_script("window.scrollBy(0,3000)", "")


@when("Click on 'About' sub-title in the navigation bar.")
def click_about(context):
    context.app.main_page_header.click_about()


@then("Verify the 'About' page opens.")
def verify_about_page_opens(context):
    context.app.about_page.verify_about_page_opens()


@then("Verify the title 'A Few Words About Us' exists.")
def verify_about_page_title(context):
    context.app.about_page.verify_about_page_title()


@then("Verify the title Cafedaria in the footer exists.")
def verify_footer_title(context):
    context.app.main_page_footer.verify_footer_title()


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
