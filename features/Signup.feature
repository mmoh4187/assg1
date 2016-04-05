# Created by Mohamed_86 at 3/27/2016
Feature: As an executive, I want users to be able to sign up,
         so that the system can save necessary to identify and verify individual user.

  Scenario: user already exist 
    Given  at the Sign-Up page
    When   the username or email is already exist
    Then   the system should return "user already exist" as the registration status of the user 
	Examples:
      | InputName | inputEmail        |
      | mohamed   | mohamed@gmail.com |
      | admin     | admin@admin.com   |
	
  Scenario: new user
    Given  at the Sign-Up page
    When   the username or email is not exist in db
    Then   the system should return "registered" as the registration status of the user
	Examples:
      | InputName | inputEmail        |
      | mike      | mike@gmail.com    |
      | ray       | ray@yahoo.com     |