Feature:

  Scenario: User can open the main page and verify it has a map
    Given Open the main page.
    When Scroll down to the footer.
    Then Verify the title Cafedaria in the footer exists.
    And Verify the footer contains a map.






