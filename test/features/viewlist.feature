Feature: Test Home Page
    As a music teacher I want tips on pieces to use.

Scenario: View List
    When I visit the web site
    Then I should see the list

Scenario: Search for Composer
    When I visit the web site
    Then I should see two items in the list
    When I fill in composer with "Bach"
    Then I should see one item in the list

Scenario: Search for Title
    When I visit the web site
    And I fill in title with "Prelude"
    Then I should see one item in the list


Scenario: Search for Instrument
    When I visit the web site
    And I fill in instrument with "Piano"
    Then I should see two items in the list

Scenario: Searching for nonexisting title
    When I visit the web site
    And I fill in title with "Waltz"
    And I fill in composer with "Bach"
    Then I should see no items in the list
    When I click on reset
    Then I should see two items in the list

Scenario: Getting JSON representation with the /json path
    When I visit json
    Then Then I should see the expected JSON encoding
