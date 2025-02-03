"""
test cases for system admin send order list page
"""

from conftest import dictionary_parametrize
from data.system_admin_send_order_list import SystemAdminSendOrderListParams
from conftest import system_admin_send_order_list_page


@dictionary_parametrize(
    {
        "Test_1": SystemAdminSendOrderListParams.Test_1,
    }
)
def test_verify_system_admin_send_order_list_page_elements(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    system_admin_send_order_list_page,
    tab_to_navigate,
):
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify send order list tab
    system_admin_send_order_list_page.verify_and_click_on_send_order_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 3. Verify send order list page elements availability
    system_admin_send_order_list_page.verify_send_order_list_page_elements()
    # 4. Verify send order list summary page elements availability
    system_admin_send_order_list_page.verify_send_order_list_summary_page_elements()


@dictionary_parametrize(
    {
        "Test_2": SystemAdminSendOrderListParams.Test_2,
    }
)
def test_apply_filter_on_system_admin_send_order_list_page(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    system_admin_send_order_list_page,
    tab_to_navigate,
    available_filter_options,
    expected_statuses,
):
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify send order list tab
    system_admin_send_order_list_page.verify_and_click_on_send_order_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. Apply filter on send order list and verify filtered item list
    system_admin_send_order_list_page.apply_filter_on_system_admin_send_order_list_and_verify_filtered_data(
        available_filter_options=available_filter_options,
        expected_statuses=expected_statuses,
    )
