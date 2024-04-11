from behave import given, when, then


@then("Verify the right page opens.")
def verify_contact_page_open(context):
    context.app.contact_page.verify_contact_page_open()


@then("Verify the title 'Contact' exists on the left side.")
def verify_contact_title(context):
    context.app.contact_page.verify_contact_title()


@then("Verify the title 'Get in touch' exists on the right side.")
def verify_title_get_in_touch(context):
    context.app.contact_page.verify_title_get_in_touch()
