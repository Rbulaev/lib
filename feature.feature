Feature: test case :)

  Scenario: Check login
    Given I open test page
    When I click to the login button
    When I write user name:"Test_test"
    When I write user password:"mazafaka_321"
    When I press enter button
    Then I see user name:"ТЕСТ"

  Scenario: Negative search
    Given I open test page
    When I click to the login button
    When I write user name:"Test_test"
    When I write user password:"mazafaka_321"
    When I press enter button
    When I search info:"какая то инфа которой нет"
    Then I see message:"Записи не найдены"

  Scenario: Check advanced search
    Given I open test page
    When I click to the login button
    When I write user name:"Test_test"
    When I write user password:"mazafaka_321"
    When I press enter button
    When I open advanced search
    When I select material type:"Ноты"
    When I select lang:"Английский"
    When I select publication date:"Последние 10 лет"
    When I write advanced text"книга"
    When I click advanced search button
