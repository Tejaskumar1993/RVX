"""
test cases for System Admin product request page
"""

from conftest import dictionary_parametrize
from data.system_admin_product_requests import SystemAdminProductRequestParams
from conftest import system_admin_product_request_page


@dictionary_parametrize(
    {
        "Test_1": SystemAdminProductRequestParams.Test_1,
    }
)
def test_verify_system_admin_product_request_page_elements(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    system_admin_product_request_page,
    tab_to_navigate,
):
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify product request tab
    system_admin_product_request_page.verify_and_click_on_product_request_tab(
        side_navigation_item=tab_to_navigate
    )
    # 3. Verify product request page elements availability
    system_admin_product_request_page.verify_product_request_page_elements()


@dictionary_parametrize(
    {
        "Test_2": SystemAdminProductRequestParams.Test_2,
    }
)
def test_verify_system_admin_product_request_page_add_item(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    system_admin_product_request_page,
    tab_to_navigate,
):
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify product request tab
    system_admin_product_request_page.verify_and_click_on_product_request_tab(
        side_navigation_item=tab_to_navigate
    )

    # 3. Verify approve and add item functionality
    system_admin_product_request_page.verify_approve_and_add_item_functionality()


@dictionary_parametrize(
    {
        "Test_3": SystemAdminProductRequestParams.Test_3,
    }
)
def test_verify_system_admin_product_request_page_add_item(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    system_admin_product_request_page,
    tab_to_navigate,
    available_filter_options,
    expected_statuses,
):
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify product request tab
    system_admin_product_request_page.verify_and_click_on_product_request_tab(
        side_navigation_item=tab_to_navigate
    )

    # 3. Verify approve and add item functionality
    system_admin_product_request_page.apply_filter_on_product_request_and_verify_filtered_data(
        available_filter_options=available_filter_options,
        expected_statuses=expected_statuses,
    )
