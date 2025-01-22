"""
test cases for deployment admin Users & Groups page
"""

from qase.pytest import qase
from conftest import dictionary_parametrize
from data.deployment_admin_users_and_groups import (
    DeploymentAdminUsersAndGroupsParams,
)
from conftest import deployment_admin_users_and_groups_page


@dictionary_parametrize(
    {
        "Test_1": DeploymentAdminUsersAndGroupsParams.Test_1,
    }
)
@qase.title("Verify email templates page elements")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "Verify all available fields on email templates page",
    ),
)
def test_verify_users_and_groups_page_elements(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        deployment_admin_users_and_groups_page,
        tab_to_navigate,
        users_table_headers,
        select_role,
):
    """
    Regression test for users & groups page elements verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_users_and_groups_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to users & groups tab
    deployment_admin_users_and_groups_page.verify_and_click_on_account_balance_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. Verify users & groups page elements availability
    deployment_admin_users_and_groups_page.verify_users_and_groups_page_elements(
        users_table_headers=users_table_headers,
    )


@dictionary_parametrize(
    {
        "Test_2": DeploymentAdminUsersAndGroupsParams.Test_2,
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
def test_apply_filter_on_users_data(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        select_role,
        deployment_admin_users_and_groups_page,
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
    # 2. Change user role
    deployment_admin_users_and_groups_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to users & groups tab
    deployment_admin_users_and_groups_page.verify_and_click_on_account_balance_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. Apply filter on items list and verify filtered users list
    deployment_admin_users_and_groups_page.apply_filter_on_users_list_and_verify_filtered_data(
        available_filter_options=available_filter_options,
        expected_statuses=expected_statuses,
    )


@dictionary_parametrize(
    {
        "Test_3": DeploymentAdminUsersAndGroupsParams.Test_3,
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
def test_apply_batch_action_on_users_to_changes_current_status_in_bulk(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        select_role,
        deployment_admin_users_and_groups_page,
        tab_to_navigate,
):
    """
    Regression test for batch action functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role
    deployment_admin_users_and_groups_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to users & groups tab
    deployment_admin_users_and_groups_page.verify_and_click_on_account_balance_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. Apply batch action on item to change status
    deployment_admin_users_and_groups_page.apply_batch_action_to_users()


@dictionary_parametrize(
    {
        "Test_4": DeploymentAdminUsersAndGroupsParams.Test_4,
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
def test_invite_user_flow(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        select_role,
        user_email,
        available_filter_options,
        deployment_admin_users_and_groups_page,
        tab_to_navigate,
        user_name,
        success_message,
        user_type_to_select,
):
    """
    Regression test for invite user functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role
    deployment_admin_users_and_groups_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to users & groups tab
    deployment_admin_users_and_groups_page.verify_and_click_on_account_balance_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. add item to the list
    deployment_admin_users_and_groups_page.verify_and_test_invite_user_functionality(
        user_name=user_name,
        user_email=user_email,
        available_filter_options=available_filter_options,
        success_message=success_message,
        user_type_to_select=user_type_to_select,
    )


@dictionary_parametrize(
    {
        "Test_5": DeploymentAdminUsersAndGroupsParams.Test_5,
    }
)
@qase.title("Verify suspend and delete action functionality on users list")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "Verify and perform suspend and delete actions functionality on users list",
    ),
)
def test_suspend_and_delete_action_of_users_list(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        select_role,
        deployment_admin_users_and_groups_page,
        tab_to_navigate,
):
    """
    Regression test for suspend and delete action functionality on users list
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role
    deployment_admin_users_and_groups_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to users & groups tab
    deployment_admin_users_and_groups_page.verify_and_click_on_account_balance_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. Test edit status and delete activity on users list
    deployment_admin_users_and_groups_page.verify_and_perform_status_and_delete_actions_functionality_from_actions()


@dictionary_parametrize(
    {
        "Test_6": DeploymentAdminUsersAndGroupsParams.Test_6,
    }
)
@qase.title("Verify manage user group and nudge action functionality on users list")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "Verify and perform manage user group and nudge action functionality on users list",
    ),
)
def test_manage_user_group_and_nudge_action_of_users_list(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        select_role,
        headers,
        deployment_admin_users_and_groups_page,
        tab_to_navigate,
        success_message,
):
    """
    Regression test for manage user group and nudge action functionality on users list
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role
    deployment_admin_users_and_groups_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to users & groups tab
    deployment_admin_users_and_groups_page.verify_and_click_on_account_balance_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. Test manage user group and nudge activity on users list
    deployment_admin_users_and_groups_page.verify_and_perform_manage_user_group_and_nudge_actions_functionality_from_actions(
        headers=headers, success_message=success_message
    )
