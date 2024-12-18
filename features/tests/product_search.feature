# Created by dhaks at 12/7/2024
Feature: Tests for search product
  # Enter feature description here
  Scenario: User can search for a product
    Given Open target main page
    When Search for coffee
    Then Verify search worked for coffee

Scenario: User can search for benefit_cells
    Given Open target circle page
    Then Verify there are at least 10 benefit cells

Scenario: User can add any product into a cart
    Given Open target main page
    When Search for coffee
    When Add any coffee into a cart
    And Click on cart icon
Then Verify coffee added to cart
    # Enter steps here