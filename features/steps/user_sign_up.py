from behave import *
import re

@given("at the Sign-Up page")
def step_impl(context):
    context.browser.get(context.address + "/signup")
    signup_found = re.search("signup", context.browser.page_source, re.IGNORECASE)
    assert signup_found

@when("the {username} or {email} is already exist. it does not matter if {password} is exist or not.")
def step_impl(context, username, email, password):
    """
    :type context: behave.runner.Context
    :type username: str
    :type email: str
    :type password: str
    """
    submit_username_email(context, username, email, password)

@when("the {username} or {email} is not exist in db. it does not matter if {password} is exist or not.")
def step_impl(context, username, email, password):
    """
    :type context: behave.runner.Context
    :type username: str
    :type email: str
    :type password: str
    """
    submit_username_email(context, username, email, password)

def submit_username_email(context, username, email, password):
    username_field = context.browser.find_element_by_name("username")
    email_field = context.browser.find_element_by_name("email")
    password_field = context.browser.find_element_by_name("password")
    username_field.send_keys(username)
    email_field.send_keys(email)
    password_field.send_keys(password)
    username_field.submit()
    context.response = context.browser.page_source


@then('the system should return "{text}" as the registration status of the user')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    assert text in context.response

