# Created by dhaks at 12/1/2024
Feature: Tests for my cart

  Scenario: User can check their cart
    Given Open target main page
    When Click on cart icon
    Then Verify my cart is empty


