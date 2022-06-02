import sys
import pytest
import logging
import json
import validators
import selenium.webdriver
from helpers.constants import SUPPORTED_BROWSERS

sys.path.append('./')
LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope='function')
def context():
    return {}


@pytest.fixture
def config(scope="session"):
    with open('config.json') as configFile:
        config = json.load(configFile)

    assert isinstance(config['config']['useGrid'], bool), \
        "{} Must be a Boolean".format(config['config']['useGrid'])
    assert validators.url(config['config']['grid']), \
        "{} Must be a valid url".format(config['config']['grid'])
    assert config['config']['browser']['name'].lower() in SUPPORTED_BROWSERS, \
        "{} Must be one of '{}'".format(config['config']['browser']['name'], SUPPORTED_BROWSERS)
    assert isinstance(config['config']['implicitWait'], int), \
        "{} Must be a number".format(config['config']['implicitWait'])
    assert validators.url(config['config']['environment']['url']), \
        "{} Must be a valid url".format(config['config']['environment']['url'])

    return config


@pytest.fixture
def web_browser(config, scope="function"):
    global _driver
    try:
        browser_name = config['config']['browser']['name'].lower()
        if config['config']['useGrid']:
            _driver = initialize_remote_driver(browser_name, config['config']['grid'])
        else:
            _driver = initialize_local_driver(browser_name, config['config']['browser']['executablePath'])

        _driver.implicitly_wait(config['config']['implicitWait'])
        _driver.maximize_window()
        _driver.delete_all_cookies()
        yield _driver
        _driver.quit()
    except Exception as err:
        LOGGER.error(err)


def initialize_remote_driver(browser_name, grid_url):
    LOGGER.info("Web Driver [ {} ] using [ Selenium Grid ]".format(browser_name))
    if browser_name == 'chrome':
        options = selenium.webdriver.ChromeOptions()
        options.headless = True
        driver = selenium.webdriver.Remote(
            command_executor=grid_url,
            options=options,
            desired_capabilities={
                'browserName': 'chrome',
                'acceptInsecureCerts': True
            })
    elif browser_name == 'firefox':
        driver = selenium.webdriver.Remote(
            command_executor=grid_url,
            desired_capabilities={
                'browserName': 'firefox',
                'acceptInsecureCerts': True
            })
    elif browser_name == 'safari':
        driver = selenium.webdriver.Remote(
            command_executor=grid_url,
            desired_capabilities={
                'browserName': 'operablink',
                'acceptInsecureCerts': True
            })
    elif browser_name == 'edge':
        driver = selenium.webdriver.Remote(
            command_executor=grid_url,
            desired_capabilities={
                'browserName': 'MicrosoftEdge',
                'acceptInsecureCerts': True
            })
    return driver


def initialize_local_driver(browser_name, executable_path):
    LOGGER.info("Web Driver [ {} ] using [ Local Environment ]".format(browser_name))
    if browser_name == 'chrome':
        options = selenium.webdriver.ChromeOptions()
        options.headless = True
        driver = selenium.webdriver.Chrome(
            options=options,
            executable_path=executable_path)
    elif browser_name == 'firefox':
        driver = selenium.webdriver.Firefox(
            executable_path=executable_path)
    elif browser_name == 'safari':
        driver = selenium.webdriver.Safari(
            executable_path=executable_path)
    elif browser_name == 'edge':
        driver = selenium.webdriver.Edge(
            executable_path=executable_path)
    return driver


## COMMON STEPS

from pytest_bdd import (
    given
)

from pages.home import HomePage


@given('The Customer visits Home Page')
def visit_home(config, web_browser, context):
    LOGGER.info("> Loading Home page")
    home_page = HomePage(web_browser, config)
    home_page.load()

    context['browser'] = home_page
    assert "508 Resource Limit Is Reached" not in home_page.title(), "Seems the page is not available"
