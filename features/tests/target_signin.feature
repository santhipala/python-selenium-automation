# Created by dhaks at 12/1/2024
Feature: Verify logged-out user can navigate to the Sign In page

  Scenario: Open Target website and navigate to Sign In
    Given Open target main page
    When Click on the Sign In link
    And Click on the Sign In option from the navigation menu
    Then Verify Sign In form opened

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open sign in page
    When Store original window
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original
