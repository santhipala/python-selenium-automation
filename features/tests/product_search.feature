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
    Given Open target product A-91511634 page
    Then Select each color and verify that it has been selected
#    When Search for coffee
#    When Add any coffee into a cart
#    And Click on cart icon
#Then Verify coffee added to cart
    # Enter steps here
#  Scenario: User can Search for a product colors
#    Given Search for a shoes on the Target website
#    When Open the first shoes from the search results
#    Then Select each color and verify that it has been selected