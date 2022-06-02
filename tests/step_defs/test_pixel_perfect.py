import logging

from pytest_bdd import (
    scenarios,
    given,
    then
)

from helpers.images import ImageAnalysis

scenarios('../features/pixel_perfect.feature')
LOGGER = logging.getLogger(__name__)


@given('../features/common_steps.feature', 'The Customer visits Home Page')
def import_step():
    pass


@then('The Home Page is displayed correctly')
def validate_home(context):
    LOGGER.info("> Executing pixel-perfect validations")
    home_page = context['browser']
    file_path = home_page.take_screenshot_to_compare("test_home.png")
    found_differences = ImageAnalysis.differences(file_path, './test_data/design/home/home.jpg')
    assert not found_differences, "The Image Analysis found differences, please check the [ results ] folder"
