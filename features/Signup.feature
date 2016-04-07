# Created by Mohamed_86 at 3/27/2016
Feature: As an executive, I want users to be able to sign up,
         so that the system can save necessary to identify and verify individual user.

  Scenario Outline: user already exist 
    Given  at the Sign-Up page
    When   the <inputName> or <inputEmail> is already exist
    Then   the system should return "fail" as the registration status of the user 
	Examples:
      | inputName | inputEmail        |
      | mohamed   | mohamed@gmail.com |
      | admin     | admin@admin.com   |
	
  Scenario Outline: new user
    Given  at the Sign-Up page
    When   the <inputName> or <inputEmail> is not exist in db
    Then   the system should return "success" as the registration status of the user
	Examples:
      | inputName | inputEmail        |
      | mike      | mike@gmail.com    |
      | ray       | ray@yahoo.com     |