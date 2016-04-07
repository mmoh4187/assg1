from behave import *
import re

@given("at the Sign-Up page")
def step_impl(context):
    context.browser.get(context.address + "/signUp")
    signUp_found = re.search("signUp", context.browser.page_source, re.IGNORECASE)
    assert signUp_found

@when("the {inputName} or {inputEmail} is already exist")
def step_impl(context, inputName, inputPassword, inputEmail):
    """
    :type context: behave.runner.Context
    :type inputName: str
    :type inputPassword: str
    :type inputEmail: str
    """
    submit_inputName_inputPassword_inputEmail(context, inputName, inputPassword, inputEmail)

@when("the {inputName} or {inputEmail} is not exist in db")
def step_impl(context, inputName, inputPassword, inputEmail):
    """
    :type context: behave.runner.Context
    :type inputName: str
    :type inputPassword: str
    :type inputEmail: str
    """
    submit_inputName_inputPassword_inputEmail(context, inputName, inputPassword, inputEmail)

def submit_inputName_inputPassword_inputEmail(context, inputName, inputPassword, inputEmail):
    inputName_field = context.browser.find_element_by_name("inputName")
    inputPassword_field = context.browser.find_element_by_name("inputPassword")
    inputEmail_field = context.browser.find_element_by_name("inputEmail")
    inputName_field.send_keys(inputName)
    inputPassword_field.send_keys(inputPassword)
    inputEmail_field.send_keys(inputEmail)
    inputName_field.submit()
    context.response = context.browser.page_source


@then('the system should return "{text}" as the registration status of the user')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    assert text in context.response