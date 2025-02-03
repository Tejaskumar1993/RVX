"""
Root conftest that will be used for all projects
"""

import os
import sys

import pytest
from dotenv import load_dotenv

from playwright.sync_api import Page

from pages.deployment_admin_account_balance_page import (
    DeploymentAdminAccountBalancePage,
)
from pages.deployment_admin_dashboard_page import DeploymentAdminDashboardPage
from pages.deployment_admin_send_order_list_page import DeploymentAdminSendOrderList
from pages.ontrack_login_page import OntrackLoginPage
from pages.sender_connection_list_page import SenderConnectionListPage
from pages.system_admin_deployment_page import SystemAdminDeploymentsPage
from pages.system_admin_notification_settings_page import (
    SystemAdminNotificationSettingsPage,
)
from pages.system_admin_product_requests_page import SystemAdminProductRequest
from pages.system_admin_users_page import SystemAdminUsersPage
from pages.deployment_admin_items_list_page import DeploymentAdminItemsListPage
from pages.vendor_company_information_page import VendorCompanyInformationPage
from pages.deployment_admin_message_templates_page import (
    DeploymentAdminMessageTemplatesPage,
)
from pages.vendor_dashboard_page import VendorDashboardPage
from pages.sender_connects_page import SenderConnectsPage
from pages.vendor_notification_settings_page import VendorNotificationPage
from pages.deployment_admin_users_and_groups_page import (
    DeploymentAdminUsersAndGroupsPage,
)
from pages.deployment_admin_send_order_list_page import DeploymentAdminSendOrderList
from pages.sender_account_balance_page import SenderAccountBalancePage
from pages.deployment_admin_token_control_page import DeploymentAdminTokenControlPage
from pages.system_admin_vendors_page import SystemAdminVendorsPage
from pages.deployment_admin_dashboard_page import DeploymentAdminDashboardPage
from pages.system_admin_items_list_page import SystemAdminItemsListPage
from pages.deployment_admin_notification_settings_page import (
    DeploymentAdminNotificationSettingsPage,
)
from pages.vendor_orders_list_page import VendorOrdersListPage
from pages.system_admin_notification_settings_page import (
    SystemAdminNotificationSettingsPage,
)
from pages.system_admin_dashboard_page import SystemAdminDashboardPage
from pages.vendor_users_page import VendorUsersListPage
from pages.system_admin_product_requests_page import SystemAdminProductRequest
from pages.vendor_dashboard_page import VendorDashboardPage


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
def deployment_admin_notification_settings_page(
    page: Page,
) -> DeploymentAdminNotificationSettingsPage:
    """
    Initialize notification settings page objects and methods
    :param page:
    :return:
    """
    return DeploymentAdminNotificationSettingsPage(page)


@pytest.fixture
def deployment_admin_send_order_list_page(
    page: Page,
) -> DeploymentAdminSendOrderList:
    """
    Initialize send order list page objects and methods
    :param page:
    :return:
    """
    return DeploymentAdminSendOrderList(page)


@pytest.fixture
def vendor_orders_list_page(
    page: Page,
) -> VendorOrdersListPage:
    """
    Initialize order list page objects and methods
    :param page:
    :return:
    """
    return VendorOrdersListPage(page)


@pytest.fixture
def vendor_users_list_page(
    page: Page,
) -> VendorUsersListPage:
    """
    Initialize users list page objects and methods
    :param page:
    :return:
    """
    return VendorUsersListPage(page)


@pytest.fixture
def system_admin_deployments_page(page: Page) -> SystemAdminDeploymentsPage:
    """
    Initialize deployments page objects and methods
    :param page:
    :return:
    """
    return SystemAdminDeploymentsPage(page)


@pytest.fixture
def system_admin_notification_settings_page(
        page: Page,
) -> SystemAdminNotificationSettingsPage:
    """
    Initialize deployments page objects and methods
    :param page:
    :return:
    """
    return SystemAdminNotificationSettingsPage(page)


@pytest.fixture
def system_admin_product_request_page(
    page: Page,
) -> SystemAdminProductRequest:
    """
    Initialize system admin request page objects and methods
    :param page:
    :return:
    """
    return SystemAdminProductRequest(page)


@pytest.fixture
def system_admin_dashboard_page(
        page: Page,
) -> SystemAdminDashboardPage:
    """
    Initialize deployments page objects and methods
    :param page:
    :return:
    """
    return SystemAdminDashboardPage(page)


@pytest.fixture
def sender_connects_page(page: Page) -> SenderConnectsPage:
    """
    Initialize connects page objects and methods
    :param page:
    :return:
    """
    return SenderConnectsPage(page)


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
def deployment_admin_dashboard_page(
    page: Page,
) -> DeploymentAdminDashboardPage:
    """
    Initialize dashboard page objects and methods
    :param page:
    :return:
    """
    return DeploymentAdminDashboardPage(page)


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
) -> DeploymentAdminItemsListPage:
    """
    Initialize items list page objects and methods
    :param page:
    :return:
    """
    return DeploymentAdminItemsListPage(page)


@pytest.fixture
def deployment_admin_send_order_list_page(
    page: Page,
) -> DeploymentAdminSendOrderList:
    """
    Initialize items list page objects and methods
    :param page:
    :return:
    """
    return DeploymentAdminSendOrderList(page)


@pytest.fixture
def system_admin_notification_settings_page(
    page: Page,
) -> SystemAdminNotificationSettingsPage:
    """
    Initialize notification settings page objects and methods
    :param page:
    :return:
    """
    return SystemAdminNotificationSettingsPage(page)


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
def system_admin_send_order_list_page(
    page: Page,
) -> SystemAdminSendOrderList:
    """
    Initialize  system admin vendors list page objects and methods
    :param page:
    :return:
    """
    return SystemAdminSendOrderList(page)


@pytest.fixture
def vendor_notification_settings_page(
    page: Page,
) -> VendorNotificationPage:
    """
    Initialize vendor notification page objects and methods
    :param page:
    :return:
    """
    return VendorNotificationPage(page)


@pytest.fixture
def sender_account_balance_page(
    page: Page,
) -> SenderAccountBalancePage:
    """
    Initialize vendor notification page objects and methods
    :param page:
    :return:
    """
    return SenderAccountBalancePage(page)


@pytest.fixture
def sender_connection_list_page(
    page: Page,
) -> SenderConnectionListPage:
    """
    Initialize Sender Connection List page objects and methods
    :param page:
    :return:
    """
    return SenderConnectionListPage(page)


@pytest.fixture
def system_admin_dashboard_page(
    page: Page,
) -> SystemAdminDashboardPage:
    """
    Initialize system admin dashboard page objects and methods
    :param page:
    :return:
    """
    return SystemAdminDashboardPage(page)


@pytest.fixture
def vendor_dashboard_page(
    page: Page,
) -> VendorDashboardPage:
    """
    Initialize vendor dashboard page objects and methods
    :param page:
    :return:
    """
    return VendorDashboardPage(page)


# @pytest.fixture
# def vendor_product_list_page(
#     page: Page,
# ) -> VendorProductListPage:
#     """
#     Initialize vendor product list page objects and methods
#     :param page:
#     :return:
#     """
#     return VendorProductListPage(page)


@pytest.fixture
def vendor_product_list_page(
        page: Page,
) -> VendorProductListPage:
    """
    Initialize vendor product list page objects and methods
    :param page:
    :return:
    """
    return VendorProductListPage(page)


@pytest.fixture
def vendor_product_list_page(
        page: Page,
) -> VendorProductListPage:
    """
    Initialize vendor product list page objects and methods
    :param page:
    :return:
    """
    return VendorProductListPage(page)


@pytest.fixture
def deployment_admin_users_and_groups_page(
    page: Page,
) -> DeploymentAdminUsersAndGroupsPage:
    """
    Initialize system admin items list page objects and methods
    :param page:
    :return:
    """
    return DeploymentAdminUsersAndGroupsPage(page)


@pytest.fixture
def deployment_admin_token_control(
    page: Page,
) -> DeploymentAdminTokenControlPage:
    """
    Initialize token control page objects and methods
    :param page:
    :return:
    """
    return DeploymentAdminTokenControlPage(page)


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
    """Dictionary parametrize    :param data:    :return:"""
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
