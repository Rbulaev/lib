Feature: Check login

  Scenario: Check login
    Given I open test page
    When I click to the login button
    When I write user name:"Test_test"
    When I write user password:"mazafaka_321"
    When I press enter button
    Then I see user name:"ТЕСТ"
