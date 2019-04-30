# Created by olgacornovan at 2019-04-25
Feature: Test scenario to ensure the form opened
  # Enter feature description here

  Scenario: User can verify form opened
    Given Open Amazon1 page
    When Click on Ad feedback link
    Then Verify popup window is opened
