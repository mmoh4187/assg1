# Created by Mohamed_86 at 3/27/2016
Feature: As an executive, I want users to be able to sign up,
         so that the system can save necessary to identify and verify individual user.

  Scenario Outline: user already exist 
    Given  at the Sign-Up page
    When   the <username> or <email> is already exist. it does not matter if <password> is exist or not. 
    Then   the system should return "Fail" as the registration status of the user 
	Examples:
      | username  | email             | password |
      | mohamed   | mohamed@gmail.com | 123456   |
      | admin     | ray@yahoo.com     | 123456   |
      | ray       | admin@admin.com   | 123456   |
  Scenario Outline: new user
    Given  at the Sign-Up page
    When   the <username> or <email> is not exist in db. it does not matter if <password> is exist or not. 
    Then   the system should return "Success" as the registration status of the user
	Examples:
      | username  | email             | password |
      | mike      | mike@gmail.com    | 123456   |
      | ray       | ray@yahoo.com     | 123456   |
