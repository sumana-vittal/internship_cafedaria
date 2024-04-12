from behave import given, when, then


@when("Enter some test data in the form")
def enter_contact_test_data(context):
    context.app.contact_page.enter_contact_test_data()


@then("Verify the 'Send' button is clickable.")
def verify_send_btn_clickable(context):
    context.app.contact_page.verify_send_btn_clickable()


@then("Verify the right page opens.")
def verify_contact_page_open(context):
    context.app.contact_page.verify_contact_page_open()


@then("Verify the title 'Contact' exists on the left side.")
def verify_contact_title(context):
    context.app.contact_page.verify_contact_title()


@then("Verify the title 'Get in touch' exists on the right side.")
def verify_title_get_in_touch(context):
    context.app.contact_page.verify_title_get_in_touch()




