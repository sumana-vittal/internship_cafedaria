Feature: Test Scenarios for the Shop Option

  Scenario: User can click on “Shop” option
      Given Open the main page.
      When Click on 'Shop' sub-title in the navigation bar.
      Then Verify the Shop page opens.
      And Verify the title 'Catalog' exists on the left side.

  Scenario: User can add two products to the cart
      Given Open the main page.
      When Click on 'Shop' sub-title in the navigation bar.
      Then Verify the Shop page opens.
      When Click on 'Add to cart' for the first two elements.
      And Click on the cart icon.
      Then Verify the cart page opens.
      Then Verify that there are two elements in the cart.
      Then Verify 'Checkout' button is clickable.
