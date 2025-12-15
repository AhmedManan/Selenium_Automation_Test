Feature: Login Functionality

  Scenario: Successful login with valid credentials
    Given user is on the login page
    When user enters valid username & password
    And click on the login button
    Then the username should be visible in the index page

  Scenario Outline: Unsuccessful login with invalid credentials should show alert
    Given user is on the login page
    When user enters username "<username>" and password "<password>"
    And click on the login button
    Then a login failure alert with the message "<expected_message>" is displayed

    Examples: Invalid Login Data
      | username | password |expected_message|
      |          |          |Please fill out Username and Password.|
      | testuser |admin     |Wrong password.|
      | admin    | wrongpwd |Wrong password.|