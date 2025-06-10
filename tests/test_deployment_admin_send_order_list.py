"""
test cases for deployment admin send order list page
"""

from conftest import dictionary_parametrize
from data.deployment_admin_send_order_list import DeploymentAdminSendOrderListParams
from conftest import deployment_admin_send_order_list_page


@dictionary_parametrize(
    {
        "Test_1": DeploymentAdminSendOrderListParams.Test_1,
    }
)
def test_verify_send_order_list_page_elements(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        deployment_admin_send_order_list_page,
        tab_to_navigate,
        headers_text,
        prospact_header,
        #role_to_change,
):
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role
    # deployment_admin_send_order_list_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=role_to_change
    # )
    # 3. Click and Verify send order list tab
    deployment_admin_send_order_list_page.verify_and_click_on_send_order_list_tab(
        side_navigation_item = tab_to_navigate
    )
    deployment_admin_send_order_list_page.verify_send_order_list_page_elements(
        headers_text = headers_text
    )
    deployment_admin_send_order_list_page.verify_click_on_send_order_summary(
        prospact_header =prospact_header
    )


@dictionary_parametrize(
    {
        "Test_2": DeploymentAdminSendOrderListParams.Test_2,
    }
)
def test_apply_filter_on_send_order_list_data(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        #role_to_change,
        deployment_admin_send_order_list_page,
        tab_to_navigate,
        available_filter_options,
        expected_statuses,
):
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role
    # deployment_admin_send_order_list_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=role_to_change
    # )
    # 3. Click and Verify send order list tab
    deployment_admin_send_order_list_page.verify_and_click_on_send_order_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. Apply filter on send order list and verify filtered item list
    deployment_admin_send_order_list_page.apply_filter_on_send_order_list_and_verify_filtered_data(
        available_filter_options=available_filter_options, expected_statuses=expected_statuses
    )
