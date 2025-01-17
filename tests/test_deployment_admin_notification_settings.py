from qase.pytest import qase
from conftest import dictionary_parametrize
from conftest import deployment_admin_notification_settings_page
from data.deployment_admin_notification_settings import (
    DeploymentAdminNotificationSettingsParams,
)


@dictionary_parametrize(
    {
        "Test_1": DeploymentAdminNotificationSettingsParams.test_1,
    }
)
@qase.title(
    "Verify deployment admin notification settings elements and checked and unchecked functionality "
)
# @qase.id(1)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all available fields on system admin notification settings",
    ),
)
def test_deployment_admin_notification_settings_page_elements(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_notification,
    deployment_admin_notification_settings_page,
    success_message_text,
    change_to_notification,
    select_role,
):
    """
    Regression test for deployment admin notification settings page elements and checked and unchecked functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_notification_settings_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to deployment admin notification settings page
    deployment_admin_notification_settings_page.click_on_profile_and_click_on_notification(
        change_to_notification=change_to_notification
    )
    # 4. Navigate to deployment admin notification settings page and verify all element of notification page
    deployment_admin_notification_settings_page.verify_system_admin_notification_settings_page_elements()
    # 5. Navigate to deployment admin notification settings page and verify alert message
    deployment_admin_notification_settings_page.verify_deployment_admin_notification_page_alert_message(
        success_message_text=success_message_text,
        deployment_admin_notification=deployment_admin_notification,
    )
