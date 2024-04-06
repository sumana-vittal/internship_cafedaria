Feature: Test Scenarios for the main page.

  Scenario: User can open the main page and verify it has a map
    Given Open the main page.
    When Scroll down to the footer.
    Then Verify the title Cafedaria in the footer exists.
    And Verify the footer contains a map.

  Scenario: User can see and click on the elements in the navigation bar
    Given Open the main page.
    Then Verify the title Cafedaria exists on the navigation bar.
    And Verify there are 6 sub-titles in the navigation bar and all of them are clickable.
    And Verify the cart and search icons exists.

  Scenario: User can click on “about” option
    Given Open the main page.
    When Click on 'About' sub-title in the navigation bar.
    Then Verify the 'About' page opens.
    Then Verify the title 'A Few Words About Us' exists.







