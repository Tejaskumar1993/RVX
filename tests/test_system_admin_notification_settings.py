from qase.pytest import qase
from conftest import dictionary_parametrize
from conftest import system_admin_notification_settings_page
from data.system_admin_notification_settings import (
    SystemAdminNotificationSettingsParams,
)


@dictionary_parametrize(
    {
        "Test_1": SystemAdminNotificationSettingsParams.test_1,
    }
)
@qase.title(
    "Verify system admin notification settings elements and checked and unchecked functionality "
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
def test_system_admin_notification_settings_page_elements(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_notification,
    system_admin_notification_settings_page,
    success_message_text,
    sender_notification,
    change_to_notification,
    vendor_notification,
):
    """
    Regression test for system admin notification settings page elements and checked and unchecked functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Navigate to system admin notification settings page
    system_admin_notification_settings_page.click_on_profile_and_click_on_notification(
        change_to_notification=change_to_notification
    )
    # 3. Navigate to system admin notification settings page and verify all element of notification page
    system_admin_notification_settings_page.verify_system_admin_notification_settings_page_elements()
    # 4. Navigate to system admin notification settings page and verify alert message
    system_admin_notification_settings_page.verify_deployment_admin_notification_page_alert_message(
        success_message_text=success_message_text,
        deployment_admin_notification=deployment_admin_notification,
    )
    # 4. Navigate to system admin notification settings page and verify alert message
    system_admin_notification_settings_page.verify_sender_notification_page_alert_message(
        success_message_text=success_message_text,
        sender_notification=sender_notification,
    )
    # 4. Navigate to system admin notification settings page and verify alert message
    system_admin_notification_settings_page.verify_vendor_notification_page_alert_message(
        success_message_text=success_message_text,
        vendor_notification=vendor_notification,
    )
