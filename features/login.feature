Feature: Login Functionality
  Scenario: Successful login with valid credentials
    Given user is on the login page
    When user enters valid username & password
    And click on the login button
    Then the username should be visible in the index page