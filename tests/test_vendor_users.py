from qase.pytest import qase
from conftest import dictionary_parametrize
from conftest import vendor_users_list_page
from data.vendor_users import VendorUsersListParams


@dictionary_parametrize(
    {
        "Test_1": VendorUsersListParams.test_1,
    }
)
@qase.title("Verify vendor users list page elements")
# @qase.id(1)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "Verify all available fields on vendor users list page",
    ),
)
def test_vendor_users_list_page_elements(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        vendor_users_list_page,
        select_role, users_table_headers,
        tab_to_navigate,
):
    # Log in to the application
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to vendor
    vendor_users_list_page.click_on_dropdown_and_change_user_role(
        role_to_change=select_role
    )
    # 3. Navigate to users list tab
    vendor_users_list_page.verify_and_click_on_users_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. verify users page elements
    vendor_users_list_page.verify_users_page_elements(users_table_headers=users_table_headers)


@dictionary_parametrize(
    {
        "Test_2": VendorUsersListParams.Test_2,
    }
)
@qase.title("Apply filter on users list data and verify filtered data on users list")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "Apply filter on users list data and verify filtered data on users list",
    ),
)
def test_apply_filter_on_vendor_users_data(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        select_role,
        vendor_users_list_page,
        tab_to_navigate,
        available_filter_options,
        expected_statuses,
):
    """
    Regression test for users list filter functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to vendor
    vendor_users_list_page.click_on_dropdown_and_change_user_role(
        role_to_change=select_role
    )
    # 3. Navigate to users list tab
    vendor_users_list_page.verify_and_click_on_users_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. Apply filter on items list and verify filtered users list
    vendor_users_list_page.apply_filter_on_users_list_and_verify_filtered_data(
        available_filter_options=available_filter_options,
        expected_statuses=expected_statuses,
    )


@dictionary_parametrize(
    {
        "Test_3": VendorUsersListParams.Test_3,
    }
)
@qase.title("Apply batch action on users to change status of users")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "apply batch action on multiple users at time to change status",
    ),
)
def test_apply_batch_action_on_vendor_users_to_changes_current_status_in_bulk(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        select_role,
        vendor_users_list_page,
        tab_to_navigate,
):
    """
    Regression test for batch action functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to vendor
    vendor_users_list_page.click_on_dropdown_and_change_user_role(
        role_to_change=select_role
    )
    # 3. Navigate to users list tab
    vendor_users_list_page.verify_and_click_on_users_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. Apply batch action on item to change status
    vendor_users_list_page.apply_batch_action_to_users()


@dictionary_parametrize(
    {
        "Test_4": VendorUsersListParams.Test_4,
    }
)
@qase.title("Verify users list invite user functionality")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "using invite user functionality, invite user ",
    ),
)
def test_vendor_invite_user_flow(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        select_role,
        user_email,
        vendor_users_list_page,
        tab_to_navigate,
        user_name,
        success_message,
        user_last_name
):
    """
    Regression test for invite user functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to vendor
    vendor_users_list_page.click_on_dropdown_and_change_user_role(
        role_to_change=select_role
    )
    # 3. Navigate to users list tab
    vendor_users_list_page.verify_and_click_on_users_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. add item to the list
    vendor_users_list_page.verify_and_test_invite_user_functionality(
        user_name=user_name,
        user_email=user_email,
        user_last_name=user_last_name,
        success_message=success_message,
    )


@dictionary_parametrize(
    {
        "Test_5": VendorUsersListParams.Test_3,
    }
)
@qase.title("Verify active/inactive and delete action functionality on users list")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "Verify and perform active/inactive and delete actions functionality on users list",
    ),
)
def test_active_and_inactive_and_delete_action_of_users_list(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        select_role,
        vendor_users_list_page,
        tab_to_navigate,
):
    """
    Regression test for active/inactive and delete action functionality on users list
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to vendor
    vendor_users_list_page.click_on_dropdown_and_change_user_role(
        role_to_change=select_role
    )
    # 3. Navigate to users list tab
    vendor_users_list_page.verify_and_click_on_users_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. Test edit status and delete activity on users list
    vendor_users_list_page.verify_and_perform_status_and_delete_actions_functionality_from_actions()


@dictionary_parametrize(
    {
        "Test_5": VendorUsersListParams.Test_3,
    }
)
@qase.title("Verify user information functionality on users list")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "Verify and perform user information functionality on users list",
    ),
)
def test_user_information_of_users_list(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        select_role,
        vendor_users_list_page,
        tab_to_navigate,
):
    """
    Regression test for user information functionality on users list
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to vendor
    vendor_users_list_page.click_on_dropdown_and_change_user_role(
        role_to_change=select_role
    )
    # 3. Navigate to users list tab
    vendor_users_list_page.verify_and_click_on_users_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. Test edit status and delete activity on users list
    vendor_users_list_page.verify_user_information_content()
