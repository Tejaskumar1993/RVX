"""
test cases for users list page
"""

from qase.pytest import qase
from conftest import dictionary_parametrize
from data.system_admin_users import SystemAdminUsersParams
from conftest import system_admin_users_page


@dictionary_parametrize(
    {
        "Test_1": SystemAdminUsersParams.Test_1,
    }
)
@qase.title("User should be able to see all available fields on users list page")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all available fields on users list page",
    ),
)
def test_verify_users_page_fields(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    system_admin_users_page,
    tab_to_navigate,
    headers_text,
):
    """
    Regression test for users page fields verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify users tab
    system_admin_users_page.verify_and_click_on_users_tab(
        side_navigation_item=tab_to_navigate
    )
    # 3. Verify users page elements availability
    system_admin_users_page.verify_user_page_elements(headers_text=headers_text)


@dictionary_parametrize(
    {
        "Test_2": SystemAdminUsersParams.Test_2,
    }
)
@qase.title("system admin should be able filter users list data")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "system admin should be able filter users list data",
    ),
)
def test_users_list_filters(
    environment_to_run,
    system_admin_users_page,
    available_filter_options,
    expected_statuses,
    ontrack_login_page,
    ontrack_password,
    ontrack_username,
    tab_to_navigate,
):
    """
    Regression test for users lists filters
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify users tab
    system_admin_users_page.verify_and_click_on_users_tab(
        side_navigation_item=tab_to_navigate
    )
    # 3. Verify filter title and options
    system_admin_users_page.verify_filters_field_and_filter_options(
        available_filter_options=available_filter_options
    )
    # 4. Apply all available filters and verify filtered data
    system_admin_users_page.apply_filters_and_verify_filtered_data(
        available_filter_options, expected_statuses
    )


@dictionary_parametrize(
    {
        "Test_3": SystemAdminUsersParams.Test_3,
    }
)
@qase.title("system admin should be able performe batch action on users list")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "system admin should be able apply batch actions to users list(suspended, activate)",
    ),
)
def test_batch_action(
    environment_to_run,
    system_admin_users_page,
    ontrack_login_page,
    ontrack_password,
    ontrack_username,
    tab_to_navigate,
):
    """
    Regression test for users lists Batch action
    """
    # 1. Navigate to ontrack log, in page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify users tab
    system_admin_users_page.verify_and_click_on_users_tab(
        side_navigation_item=tab_to_navigate
    )
    # 3. Verify Batch action functionality
    system_admin_users_page.apply_batch_actions_to_users_list()


@dictionary_parametrize(
    {
        "Test_4": SystemAdminUsersParams.Test_4,
    }
)
@qase.title("system admin should be able invite other users via invite button")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "system admin should be able to invite other users(vendor, deployment admin, sender, system admin) ",
    ),
)
def test_invite_system_admin_and_sender(
    environment_to_run,
    system_admin_users_page,
    first_name,
    last_name,
    email,
    user_type_select,
    ontrack_login_page,
    ontrack_password,
    ontrack_username,
    tab_to_navigate,
):
    """
    Regression test for invite users functionality
    """
    # 1. Navigate to ontrack log, in page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify users tab
    system_admin_users_page.verify_and_click_on_users_tab(
        side_navigation_item=tab_to_navigate
    )
    # 3. Verify invite user functionality
    system_admin_users_page.verify_and_invite_system_admin_and_sender_functionality(
        first_name, last_name, email, user_types=user_type_select
    )


@dictionary_parametrize(
    {
        "Test_5": SystemAdminUsersParams.Test_5,
    }
)
@qase.title("system admin should be able invite deployment admin via invite button")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "system admin should be able to invite other users deployment admin",
    ),
)
def test_invite_deployment_admin(
    environment_to_run,
    system_admin_users_page,
    first_name,
    last_name,
    email,
    user_type_select,
    ontrack_login_page,
    ontrack_password,
    ontrack_username,
    tab_to_navigate,
    deployment_name,
):
    """
    Regression test for invite users functionality
    """
    # 1. Navigate to ontrack log, in page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify users tab
    system_admin_users_page.verify_and_click_on_users_tab(
        side_navigation_item=tab_to_navigate
    )
    # 3. Verify invite user functionality
    system_admin_users_page.invite_deployment_admin(
        first_name,
        last_name,
        email,
        user_type=user_type_select,
        deployment_name=deployment_name,
    )


@dictionary_parametrize(
    {
        "Test_6": SystemAdminUsersParams.Test_6,
    }
)
@qase.title("system admin should be able invite vendor via invite button")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "system admin should be able to invite vendor ",
    ),
)
def test_invite_vendor(
    environment_to_run,
    system_admin_users_page,
    first_name,
    last_name,
    email,
    user_type_select,
    ontrack_login_page,
    ontrack_password,
    ontrack_username,
    tab_to_navigate,
    vendor_to_select,
):
    """
    Regression test for invite users functionality
    """
    # 1. Navigate to ontrack log, in page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify users tab
    system_admin_users_page.verify_and_click_on_users_tab(
        side_navigation_item=tab_to_navigate
    )
    # 3. Verify invite user functionality
    system_admin_users_page.invite_vendor(
        first_name,
        last_name,
        email,
        user_type_select=user_type_select,
        vendor=vendor_to_select,
    )


@dictionary_parametrize(
    {
        "Test_3": SystemAdminUsersParams.Test_3,
    }
)
@qase.title(
    "system admin should be able to active and suspend single user from actions"
)
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "system admin should be able make single user suspend and active from active",
    ),
)
def test_active_and_suspend_single_user(
    environment_to_run,
    system_admin_users_page,
    ontrack_login_page,
    ontrack_password,
    ontrack_username,
    tab_to_navigate,
):
    """
    Regression test for users lists Batch action
    """
    # 1. Navigate to ontrack log, in page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify users tab
    system_admin_users_page.verify_and_click_on_users_tab(
        side_navigation_item=tab_to_navigate
    )
    # 3. Verify Batch action functionality
    system_admin_users_page.suspend_and_active_user_from_actions()


@dictionary_parametrize(
    {
        "Test_3": SystemAdminUsersParams.Test_3,
    }
)
@qase.title("system admin should be able to delete users")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "system admin should be able delete any users",
    ),
)
def test_delete_user_from_list(
    environment_to_run,
    system_admin_users_page,
    ontrack_login_page,
    ontrack_password,
    ontrack_username,
    tab_to_navigate,
):
    """
    Regression test for users lists Batch action
    """
    # 1. Navigate to ontrack log, in page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify users tab
    system_admin_users_page.verify_and_click_on_users_tab(
        side_navigation_item=tab_to_navigate
    )
    # 3. Verify Batch action functionality
    system_admin_users_page.delete_user_from_list()
