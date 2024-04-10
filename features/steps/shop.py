from behave import given, when, then


@when("Click on 'Add to cart' for the first two elements.")
def click_add_to_cart(context):
    context.app.shop_page.add_to_cart()


@when("Click on the cart icon.")
def click_cart_icon(context):
    context.app.shop_page.click_cart_icon()


@then("Verify the cart page opens.")
def verify_cart_page_opens(context):
    context.app.cart_page.verify_cart_page_opens()


@then("Verify that there are two elements in the cart.")
def verify_cart_items(context):
    context.app.cart_page.verify_cart_items()


@then("Verify 'Checkout' button is clickable.")
def verify_checkout_clickable(context):
    pass

