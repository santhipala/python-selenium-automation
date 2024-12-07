# Created by dhaks at 12/1/2024
Feature: Verify logged-out user can navigate to the Sign In page

  Scenario: Open Target website and navigate to Sign In
    Given Open target home page
    When Click on the Sign In link
    And Click on the Sign In option from the navigation menu
    Then I should see the Sign In form