Feature: Validate the login feature

  Background:
    Given Launch the browser
    When Open the router app https://qa2-platform.navigo.global/apps/router/
    Then The login portal has been opened

  @ValidLogin
  Scenario: Login with valid credentials
    And Provide valid username and password
    And Click on the Login button
    Then Login is successful and dashboard is opened

  @InvalidLogin
  Scenario Outline: Login with invalid credentials
    And Provide the username "<username>" and password "<password>"
    And Click on the Login button
    Then Login is failed and invalid credential error is displayed
    Then Close the browser
    Examples:
      | username | password |
      | abcd     | 1234     |
      | 35473    | afsdf    |

  @InvalidLogin
  Scenario: Login with empty username
    And Provide the password "admin123"
    And Click on the Login button
    Then Login is failed and empty username error is displayed
    Then Close the browser
#
#  Scenario: Login with empty password
#    And Provide the username "Admin"
#    And Click on the Login button
#    Then Login is failed and empty password error is displayed
#    Then Close the browser
