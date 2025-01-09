"""
test cases for deployment admin token control page
"""

from qase.pytest import qase
from conftest import dictionary_parametrize
from data.deployment_admin_token_control import DeploymentAdminTokenControlParams
from conftest import deployment_admin_token_control


@dictionary_parametrize(
    {
        "Test_1": DeploymentAdminTokenControlParams.Test_1,
    }
)
@qase.title("Verify token control page elements")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all available fields on token control page",
    ),
)
def test_verify_token_control_page_elements(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_token_control,
    tab_to_navigate,
    token_bucket_table_headers,
    available_filter_options,
    select_role,
):
    """
    Regression test for token control page elements verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_token_control.verify_and_change_user_role(select_role=select_role)
    # 3. Navigate to token control tab
    deployment_admin_token_control.verify_and_click_on_token_control_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. Verify token control page elements availability
    deployment_admin_token_control.verify_token_control_page_elements(
        token_bucket_table_headers=token_bucket_table_headers,
        available_filter_options=available_filter_options,
    )


@dictionary_parametrize(
    {
        "Test_2": DeploymentAdminTokenControlParams.Test_2,
    }
)
@qase.title("apply all filter on bucket status and verify result")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "apply all filter on bucket status and verify result",
    ),
)
def test_verify_token_buckets_filter_functionality(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_token_control,
    tab_to_navigate,
    available_filter_options,
    expected_statuses,
    select_role,
):
    """
    Regression test for filter functionality of token buckets list
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_token_control.verify_and_change_user_role(select_role=select_role)
    # 3. Navigate to token control tab
    deployment_admin_token_control.verify_and_click_on_token_control_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. apply filter and verify results
    deployment_admin_token_control.apply_filter_on_token_bucket_data(
        available_filter_options=available_filter_options,
        expected_statuses=expected_statuses,
    )


@dictionary_parametrize(
    {
        "Test_3": DeploymentAdminTokenControlParams.Test_3,
    }
)
@qase.title("Verify token buckets enable and disable functionality")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify token buckets enable and disable functionality",
    ),
)
def test_enable_and_disable_token_bucket(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_token_control,
    tab_to_navigate,
    enable_message_text,
    disable_message_text,
    select_role,
):
    """
    Regression test for the token control functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_token_control.verify_and_change_user_role(select_role=select_role)
    # 3. Navigate to token control tab
    deployment_admin_token_control.verify_and_click_on_token_control_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. enable/disable token bucket
    deployment_admin_token_control.apply_filter_on_token_bucket_data(
        disable_message_text=disable_message_text,
        enable_message_text=enable_message_text,
    )


@dictionary_parametrize(
    {
        "Test_4": DeploymentAdminTokenControlParams.Test_4,
    }
)
@qase.title(
    "Verify all elements of create bucket dialog and create a new bucket,Verify and perform manage action on token bucket"
)
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all elements of create bucket dialog and create a new bucket , Verify and perform manage action on token bucket and delete bucket",
    ),
)
def test_add_new_bucket_manage_bucket_and_delete_bucket(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_token_control,
    tab_to_navigate,
    tokens_count,
    max_token,
    total_limit,
    bucket_description,
    bucket_name,
    select_role,
    new_description,
):
    """
    Regression test for the new token bucket creation, manage bucket and delete bucket
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_token_control.verify_and_change_user_role(select_role=select_role)
    # 3. Navigate to token control tab
    deployment_admin_token_control.verify_and_click_on_token_control_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. create a new bucket
    bucket_name, bucket_description = (
        deployment_admin_token_control.verify_and_create_a_new_bucket(
            tokens_count=tokens_count,
            max_token=max_token,
            token_limit=total_limit,
            bucket_description=bucket_description,
            bucket_name=bucket_name,
        )
    )
    # 5. manage and delete token bucket
    deployment_admin_token_control.verify_manage_and_delete_action_on_token_bucket(
        bucket_name, bucket_description, new_description=new_description
    )
