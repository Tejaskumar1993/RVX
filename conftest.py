"""
Root conftest that will be used for all projects
"""

import os
import sys
import pytest
from dotenv import load_dotenv

from playwright.sync_api import Page

from pages.ontrack_login_page import (
    OntrackLoginPage
)
from pages.system_admin_deployment_page import SystemAdminDeploymentsPage
from pages.system_admin_users_page import SystemAdminUsersPage

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
def system_admin_users_page(page: Page) -> SystemAdminUsersPage:
    """
    Initialize login page objects and methods
    :param page:
    :return:
    """
    return SystemAdminUsersPage(page)

@pytest.fixture
def system_admin_deployments_page(page: Page) -> SystemAdminDeploymentsPage:
    """
    Initialize login page objects and methods
    :param page:
    :return:
    """
    return SystemAdminDeploymentsPage(page)


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
        "--ontrack-password",
        action="store",
        help="password",
        default=os.getenv("ONTRACK_PASSWORD"),
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

@pytest.fixture
def ontrack_username(request):
    """
    Argument for ontrack user name
    :param request:
    :return:
    """
    return request.config.getoption("--ontrack-user")


@pytest.fixture
def ontrack_password(request):
    """
    Argument for ontrack user password
    :param request:
    :return:
    """
    return request.config.getoption("--ontrack-password")
