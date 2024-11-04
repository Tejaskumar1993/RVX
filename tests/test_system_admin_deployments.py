"""
test cases for users list page
"""
from qase.pytest import qase
from conftest import dictionary_parametrize
from data.system_admin_deployments import SystemAdminDeploymentsParams
from conftest import system_admin_deployments_page

@dictionary_parametrize(
    {
        "Test_1": SystemAdminDeploymentsParams.Test_1,
    }
)
@qase.title("User should be able to see all available fields on deployments page")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all available fields on deployments list page",
    ),
)
def test_verify_deployments_page_elements(environment_to_run, ontrack_username, ontrack_password, ontrack_login_page,
                                  system_admin_deployments_page, tab_to_navigate, headers_text):
    """
        Regression test for users page fields verification
        """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(environment_to_run, ontrack_username, ontrack_password)
    # 2. Click and Verify users tab
    system_admin_deployments_page.verify_and_click_on_deployments_tab(side_navigation_item=tab_to_navigate)
    # 3. Verify users page elements availability
    system_admin_deployments_page.verify_deployments_page_elements(headers_text=headers_text)

@dictionary_parametrize(
    {
        "Test_2": SystemAdminDeploymentsParams.Test_2,
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
def test_batch_action_on_deployments_list(environment_to_run, system_admin_deployments_page,
    ontrack_login_page, ontrack_password, ontrack_username, tab_to_navigate, success_message):
    """
        Regression test for users lists Batch action
    """
    # 1. Navigate to ontrack log, in page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(environment_to_run, ontrack_username, ontrack_password)
    # 2. Click and Verify users tab
    system_admin_deployments_page.verify_and_click_on_deployments_tab(side_navigation_item=tab_to_navigate)
    # 3. Verify Batch action functionality
    system_admin_deployments_page.apply_batch_actions_to_deployments_list(success_message=success_message)

@dictionary_parametrize(
    {
        "Test_2": SystemAdminDeploymentsParams.Test_2,
    }
)
@qase.title("system admin should be able to delete single deployment from actions")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "system admin should be able delete single user",
    ),
)
def test_delete_single_deployment_from_deployment_list(environment_to_run, system_admin_deployments_page,
    ontrack_login_page, ontrack_password, ontrack_username, tab_to_navigate, success_message):
    """
        Regression test for users lists delete action
    """
    # 1. Navigate to ontrack log, in page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(environment_to_run, ontrack_username, ontrack_password)
    # 2. Click and Verify users tab
    system_admin_deployments_page.verify_and_click_on_deployments_tab(side_navigation_item=tab_to_navigate)
    # 3. Verify Batch action functionality
    system_admin_deployments_page.delete_deployments_from_actions(success_message = success_message)

@dictionary_parametrize(
    {
        "Test_3": SystemAdminDeploymentsParams.Test_3,
    }
)
@qase.title("system admin should be able to delete single deployment from actions")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "system admin should be able delete single user",
    ),
)
def test_deployments_summary_information(environment_to_run, system_admin_deployments_page,
    ontrack_login_page, ontrack_password, ontrack_username, tab_to_navigate):
    """
        Regression test to check deployments details
    """
    # 1. Navigate to ontrack log, in page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(environment_to_run, ontrack_username, ontrack_password)
    # 2. Click and Verify users tab
    system_admin_deployments_page.verify_and_click_on_deployments_tab(side_navigation_item=tab_to_navigate)
    # 3. Verify Batch action functionality
    system_admin_deployments_page.verify_deployment_summary_pop_up_fields()

@dictionary_parametrize(
    {
        "Test_4": SystemAdminDeploymentsParams.Test_4,
    }
)
@qase.title("system admin should be able to delete single deployment from actions")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "system admin should be able delete single user",
    ),
)
def test_deployment_summary_users_tab_filter(environment_to_run, system_admin_deployments_page,
    ontrack_login_page, ontrack_password, ontrack_username, tab_to_navigate, available_filter_options, expected_statuses):
    """
           Regression test to check deployments summary users tab filter
       """
    # 1. Navigate to ontrack log, in page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(environment_to_run, ontrack_username, ontrack_password)
    # 2. Click and Verify users tab
    system_admin_deployments_page.verify_and_click_on_deployments_tab(side_navigation_item=tab_to_navigate)
    # 3. Verify available filter options
    system_admin_deployments_page.verify_deployment_summary_users_filter(available_filter_options=available_filter_options)
    # 4. Apply filter and verify resulted data
    system_admin_deployments_page.apply_filter_on_deployment_summary_users_data(available_filter_options=available_filter_options, expected_statuses=expected_statuses)

@dictionary_parametrize(
    {
        "Test_5": SystemAdminDeploymentsParams.Test_5,
    }
)
@qase.title("All required fields in the Users tab should be visible within the Users section of the Deployment Summary.")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "verify users tab fields",
    ),
)
def test_deployment_summary_users_tab_fields(environment_to_run, system_admin_deployments_page,
    ontrack_login_page, ontrack_password, ontrack_username, tab_to_navigate, headers_text):
    """
           Regression test to check deployments summary users tab fields
       """
    # 1. Navigate to ontrack log, in page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(environment_to_run, ontrack_username, ontrack_password)
    # 2. Click and Verify users tab
    system_admin_deployments_page.verify_and_click_on_deployments_tab(side_navigation_item=tab_to_navigate)
    # 3. Verify users tab fields
    system_admin_deployments_page.verify_deployment_summary_users_tab_fields(headers_text = headers_text)


@dictionary_parametrize(
    {
        "Test_6": SystemAdminDeploymentsParams.Test_6,
    }
)
@qase.title("All required fields of published items should be visible on the Published Items tab of the Deployment Summary.")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "verify published items tab's fields",
    ),
)
def test_deployment_summary_published_items_tab_fields(environment_to_run, system_admin_deployments_page,
    ontrack_login_page, ontrack_password, ontrack_username, headers_text, tab_to_navigate, deployment_summary_tab_navigation):
    """
           Regression test to check deployments summary published items tab fields
       """
    # 1. Navigate to ontrack log, in page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(environment_to_run, ontrack_username, ontrack_password)
    # 2. Click and Verify users tab
    system_admin_deployments_page.verify_and_click_on_deployments_tab(side_navigation_item=tab_to_navigate)
    # 3. Verify published items tab
    system_admin_deployments_page.verify_deployment_summary_published_items_tab_fields(headers_text = headers_text, tab_to_navigate= deployment_summary_tab_navigation)


@dictionary_parametrize(
    {
        "Test_7": SystemAdminDeploymentsParams.Test_7,
    }
)
@qase.title("All required fields of the Sends tab should be visible inside the Sends tab of the Deployment Summary.")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify sends tab of deployment summary",
    ),
)
def test_deployment_summary_sends_tab_fields(environment_to_run, system_admin_deployments_page,
    ontrack_login_page, ontrack_password, ontrack_username, headers_text, tab_to_navigate, deployment_summary_tab_navigation):
    """
           Regression test to check deployments summary sends tab fields
       """
    # 1. Navigate to ontrack log, in page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(environment_to_run, ontrack_username, ontrack_password)
    # 2. Click and Verify users tab
    system_admin_deployments_page.verify_and_click_on_deployments_tab(side_navigation_item=tab_to_navigate)
    # 3. Verify sends tab
    system_admin_deployments_page.verify_deployment_summary_sends_tab_fields(headers_text = headers_text, tab_to_navigate= deployment_summary_tab_navigation)

@dictionary_parametrize(
    {
        "Test_8": SystemAdminDeploymentsParams.Test_8,
    }
)
@qase.title("All required account balance fields should be visible inside the Account Balance tab of the Deployment Summary.")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify deployment summary's account balance tab fields",
    ),
)
def test_deployment_summary_account_balance_tab_fields(environment_to_run, system_admin_deployments_page,
    ontrack_login_page, ontrack_password, ontrack_username, account_balance_title, tab_to_navigate, deployment_summary_tab_navigation):
    """
           Regression test to check deployments summary account balance tab fields
       """
    # 1. Navigate to ontrack log, in page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(environment_to_run, ontrack_username, ontrack_password)
    # 2. Click and Verify users tab
    system_admin_deployments_page.verify_and_click_on_deployments_tab(side_navigation_item=tab_to_navigate)
    # 3. Verify account balance tab fields
    system_admin_deployments_page.verify_deployment_summary_account_balance_tab_fields(account_balance_title = account_balance_title, tab_to_navigate = deployment_summary_tab_navigation)


@dictionary_parametrize(
    {
        "Test_9": SystemAdminDeploymentsParams.Test_9,
    }
)
@qase.title("System admin should be able to suspect, active and assign group to other users")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify and perform users tab group actions",
    ),
)
def test_deployment_summary_users_tab_group_actions(environment_to_run, system_admin_deployments_page,
                                                    ontrack_login_page, ontrack_password, ontrack_username,error_message,
                                                    tab_to_navigate, success_message, available_filter_options, expected_statuses):
    """
    Regression test to check deployments summary group actions
    """
    # 1. Navigate to ontrack log, in page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(environment_to_run, ontrack_username, ontrack_password)
    # 2. Click and Verify users tab
    system_admin_deployments_page.verify_and_click_on_deployments_tab(side_navigation_item=tab_to_navigate)
    # 3. Verify account balance tab fields
    system_admin_deployments_page.verify_actions_button_on_users_tab(error_message=error_message, success_message=success_message, available_filter_options= available_filter_options,
                                                                     expected_statuses = expected_statuses)

@dictionary_parametrize(
    {
        "Test_10": SystemAdminDeploymentsParams.Test_3,
    }
)
@qase.title("All Required user information should be visible inside the user information pop-up")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verifying particular user information pop-up fields",
    ),
)
def test_deployment_summary_user_information(environment_to_run, system_admin_deployments_page,
                                            ontrack_login_page, ontrack_password, ontrack_username,
                                            tab_to_navigate):
    """
    Regression test to check deployments summary user information
    """
    # 1. Navigate to ontrack log, in page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(environment_to_run, ontrack_username, ontrack_password)
    # 2. Click and Verify users tab
    system_admin_deployments_page.verify_and_click_on_deployments_tab(side_navigation_item=tab_to_navigate)
    # 3. Verify account balance tab fields
    system_admin_deployments_page.verify_user_information_inside_users_tab()


