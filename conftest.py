"""
Root conftest that will be used for all projects
"""

import os
import sys
import pytest
from dotenv import load_dotenv

from playwright.sync_api import Page

from pages.deployment_admin_account_balance import DeploymentAdminAccountBalancePage
from pages.ontrack_login_page import OntrackLoginPage
from pages.system_admin_deployment_page import SystemAdminDeploymentsPage
from pages.system_admin_users_page import SystemAdminUsersPage
from pages.deployment_admin_items_list_page import DeploymentAdminitemsListPage
from pages.vendor_company_information_page import VendorCompanyInformationPage
from pages.deployment_admin_message_templates_page import (
    DeploymentAdminMessageTemplatesPage,
)
from pages.system_admin_vendors_page import SystemAdminVendorsPage
from pages.system_admin_items_list_page import SystemAdminItemsListPage

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
    Initialize users list page objects and methods
    :param page:
    :return:
    """
    return SystemAdminUsersPage(page)


@pytest.fixture
def system_admin_deployments_page(page: Page) -> SystemAdminDeploymentsPage:
    """
    Initialize deployments page objects and methods
    :param page:
    :return:
    """
    return SystemAdminDeploymentsPage(page)


@pytest.fixture
def deployment_admin_account_balance_page(
    page: Page,
) -> DeploymentAdminAccountBalancePage:
    """
    Initialize account balance page objects and methods
    :param page:
    :return:
    """
    return DeploymentAdminAccountBalancePage(page)


@pytest.fixture
def system_admin_items_list_page(
    page: Page,
) -> SystemAdminItemsListPage:
    """
    Initialize system admin items list page objects and methods
    :param page:
    :return:
    """
    return SystemAdminItemsListPage(page)


@pytest.fixture
def deployment_admin_message_templates_page(
    page: Page,
) -> DeploymentAdminMessageTemplatesPage:
    """
    Initialize message templates page objects and methods
    :param page:
    :return:
    """
    return DeploymentAdminMessageTemplatesPage(page)


@pytest.fixture
def deployment_admin_items_list_page(
    page: Page,
) -> DeploymentAdminitemsListPage:
    """
    Initialize items list page objects and methods
    :param page:
    :return:
    """
    return DeploymentAdminitemsListPage(page)


@pytest.fixture
def system_admin_vendors_page(
    page: Page,
) -> SystemAdminVendorsPage:
    """
    Initialize  system admin vendors list page objects and methods
    :param page:
    :return:
    """
    return SystemAdminVendorsPage(page)


@pytest.fixture
def vendor_company_information_page(
    page: Page,
) -> VendorCompanyInformationPage:
    """
    Initialize login page objects and methods
    :param page:
    :return:
    """
    return VendorCompanyInformationPage(page)


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
