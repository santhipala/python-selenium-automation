# Created by dhaks at 12/1/2024
Feature: Verify logged-out user can navigate to the Sign In page

  Scenario: Open Target website and navigate to Sign In
    Given Open target main page
    When Click on the Sign In link
    And Click on the Sign In option from the navigation menu
    Then Verify Sign In form opened