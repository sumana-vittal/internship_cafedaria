Feature: Test Scenarios for the Contact page.

  Scenario: User can click on “Contact” option and user can fill out the form
      Given Open the main page.
      When Click on 'Contact' sub-title in the navigation bar.
      And Enter some test data in the form
      Then Verify the 'Send' button is clickable.
