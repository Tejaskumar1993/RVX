from qase.pytest import qase
from conftest import dictionary_parametrize
from conftest import vendor_notification_settings_page
from data.vendor_notification_settings import VendorNotificationParams


@dictionary_parametrize(
    {
        "Test_1": VendorNotificationParams.test_1,
    }
)
@qase.title(
    "Verify vendor notification page elements and checked and unchecked functionality "
)
# @qase.id(1)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all available fields on vendor notification page",
    ),
)
def test_verify_vendor_notification_page_elements(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    vendor_notification_settings_page,
    #select_role,
    success_message_text,
    change_to_notification,
):
    """
    Regression test for vendor notification page elements and checked and unchecked functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )

    # 2. Navigate to vendor
   # vendor_notification_settings_page.click_on_dropdown_and_change_user_role(
   #      role_to_change=select_role)
    # 3. Navigate to vendor notification page
    vendor_notification_settings_page.click_on_profile_and_click_on_notification(
        change_to_notification=change_to_notification
    )
    # 4. Navigate to vendor notification page and verify all element of notification page
    vendor_notification_settings_page.verify_vendor_notification_page_elements()
    # 5. Navigate to vendor notification page and verify alert message
    vendor_notification_settings_page.verify_vendor_notification_page_alert_message(
        success_message_text=success_message_text
    )
