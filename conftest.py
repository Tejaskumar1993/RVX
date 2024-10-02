"""
Root conftest that will be used for all projects
"""

import os
import sys
import pytest
from dotenv import load_dotenv

from playwright.sync_api import Page

from pages.ontrack_login_page import (
    OntrackLoginPage,
)

# Handle display of output log when using xdist
sys.stdout = sys.stderr
page: Page


@pytest.fixture
def ontrack_login_page(page: Page) -> OntrackLoginPage:
    """
    Initialize login page objects and methods
    :param page:
    :return:
    """
    return OntrackLoginPage(page)


@pytest.fixture
def get_page(page: Page):
    """
    Get the page object
    :param page:
    :return:
    """
    return page


# Pytest custom add option arguments
def pytest_addoption(parser):
    """
    Pytest custom arguments
    :param parser:
    :return:
    """
    # Load the .env file
    load_dotenv()

    parser.addoption(
        "--ontrack-user",
        action="store",
        help="username",
        default=os.getenv("ONTRACK_USER"),
    )
    parser.addoption(
        "--ontrack-pw",
        action="store",
        help="password",
        default=os.getenv("ONTRACK__PASSWORD"),
    )
    parser.addoption(
        "--env",
        action="store",
        help="Environment to run the script(staging, pilot, prod)",
        default=os.getenv("ENVIRONMENT"),
    )


def dictionary_parametrize(data, **kwargs):
    """

    Dictionary parametrize

    :param data:
    :return:
    """
    args = list(list(data.values())[0].keys())
    formatted_data = [[item[a] for a in args] for item in data.values()]
    ids = list(data.keys())
    return pytest.mark.parametrize(args, formatted_data, ids=ids, **kwargs)


@pytest.fixture
def environment_to_run(request):
    """
    Argument for environment to run the scripts
    :param request: staging, test, prod, dev
    :return:
    """
    return request.config.getoption("--env")
