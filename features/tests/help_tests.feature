# Created by dhaks at 1/4/2025
Feature: Tests for help pages
  # Enter feature description here

  Scenario: User can select Help topic Returns
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Returns & Exchanges
    Then Verify help Returns page opened