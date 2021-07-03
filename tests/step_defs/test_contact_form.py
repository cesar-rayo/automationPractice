import logging
import os

from pytest_bdd import (
    scenarios,
    given,
    when,
    then
)

from pages.contact import ContactPage
from helpers.constants import EXPECTED_RESULTS

scenarios('../features/contact_form.feature')
LOGGER = logging.getLogger(__name__)

@given('../features/common_steps.feature', 'The Customer visits Home Page')
def import_step():
    pass

@when('The Customer goes to the Contact Page')
def go_to_contact_page(context):
    home_page = context['browser']
    contact_page = ContactPage(*home_page.click_contact())
    contact_page.take_screenshot()
    context['browser'] = contact_page

@when('The Customer selects the subject "<subject>"')
def fill_contact_form(context,subject):
    LOGGER.info("> Using subject [ {} ]".format(subject))
    contact_page = context['browser']
    if subject:
        contact_page.select_subject_by_text(subject)

@when('The Customer fills the email "<email>"')
def fill_contact_form(context,email):
    LOGGER.info("> Using email [ {} ]".format(email))
    contact_page = context['browser']
    if email:
        contact_page.type_email(email)

@when('The Customer fills the order "<order>"')
def fill_contact_form(context,order):
    LOGGER.info("> Using order [ {} ]".format(order))
    contact_page = context['browser']
    if order:
        contact_page.type_order(order)

@when('The Customer uploads the file "<input_file>"')
def fill_contact_form(context,input_file):
    file_path = "{}/test_data/files/{}".format(os.path.abspath(os.getcwd()), input_file)
    LOGGER.info("> Using input_file [ {} ]".format(file_path))
    contact_page = context['browser']
    if input_file:
        contact_page.load_input_file(file_path)

@when('The Customer fills the message "<content>"')
def fill_contact_form(context,content):
    LOGGER.info("> Using content [ {} ]".format(content))
    contact_page = context['browser']
    if content:
        contact_page.type_message(content)

@then('The Customer submits the form')
def submit_contact_form(context):
    contact_page = context['browser']
    contact_page.click_submit()

@then('The Contact page responses "<result>"')
def validate_contact_form(context,result):
    LOGGER.info("> Validating results")
    contact_page = context['browser']
    if result == "suceess":
        success_msg = contact_page.get_success_msg()
        assert EXPECTED_RESULTS[result] in success_msg, "Seems there is an issue with the success message"
    else:
        errors = contact_page.get_error_msgs()
        assert EXPECTED_RESULTS[result] in errors, "The error messege is not the expected one"
