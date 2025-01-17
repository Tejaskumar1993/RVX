"""
Deployment admin notification settings page module
"""

import time

from playwright.sync_api import Page, expect
from qase.pytest import qase

from pages.base_page import BasePage
from utilities.decorators import qase_screenshot


class DeploymentAdminNotificationSettingsPage(BasePage):
    """
    Module containing objects and methods related to Deployment admin notification settings page
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.profile_image = page.locator("//a[@href='/dashboard/admin#!']")
        # Role locator
        self.select_role_dropdown = page.locator('(//div[@class="dropdown"])[2]')
        self.select_role = '//a[text()="<<select_role>>"]'
        self.notification_setting_dropdown = '//a[text()="<<Notification Settings>>"]'
        self.notification_header = page.locator('//h3[text()="Notification Settings"]')
        self.deployment_admin_notification_model = page.locator(
            '//div[@class="mb-3 overflow-auto notification-settings-card"]'
        )
        self.deployment_admin_alert = page.locator("//th[text()='Alert']")
        self.deployment_admin_alert_type = page.locator("//th[text()='Alert Type']")
        self.deployment_admin_email = page.locator("//th[text()='Email']")
        self.deployment_admin_sms = page.locator("//th[text()='SMS']")
        self.all_deployment_admin_notification_options = (
            "//following-sibling::div//table//tbody//td[1]"
        )
        self.deployment_admin_select_all_email_notification = page.locator(
            "//td[text()='Select All']/following-sibling::td[1]//input[@type='checkbox']"
        )
        self.deployment_admin_select_all_sms_notification = page.locator(
            "//td[text()='Select All']/following-sibling::td[2]//input[@type='checkbox']"
        )
        self.update_button = page.locator('//button[text()="Update"]')
        self.alert_message = page.locator(
            '//div[@class="ant-message-custom-content ant-message-success"]'
        )

    @qase_screenshot
    @qase.step(
        title="Verify logged in user is able to change role to deployment admin",
        expected="Logged in user should be able to change role",
    )
    def verify_and_change_user_role(self, select_role):
        """
        Verify and change role of user
        """
        expect(self.select_role_dropdown).to_be_visible()
        self.select_role_dropdown.click()
        self.page.wait_for_load_state("domcontentloaded")
        self.page.click(self.select_role.replace("<<select_role>>", select_role))
        print(f"successfully changed role to {select_role}")

    @qase_screenshot
    @qase.step(
        title="click on user profile dropdown and select notification settings option",
        expected="User should be able to select notification settings successfully",
    )
    def click_on_profile_and_click_on_notification(self, change_to_notification):
        """
        navigate to notification page
        """
        self.page.wait_for_selector("//a[@href='/dashboard/admin#!']")
        self.profile_image.click()
        self.page.locator(
            self.notification_setting_dropdown.replace(
                "<<Notification Settings>>", change_to_notification
            )
        ).click()
        print(f"changes page navigation {change_to_notification}")

    @qase_screenshot
    @qase.step(
        title="Verify notification setting page elements",
        expected="User should be able to visible every elements of notification setting page",
    )
    def verify_system_admin_notification_settings_page_elements(self):
        """
        Verify and check availability of notification setting page elements
        """
        time.sleep(5)
        elements_to_check = [
            self.notification_header,
            self.deployment_admin_notification_model,
            self.deployment_admin_sms,
            self.deployment_admin_alert_type,
            self.deployment_admin_alert,
            self.deployment_admin_email,
            self.update_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("items list page elements verified")

    @qase_screenshot
    @qase.step(
        title="Verify alert message and set deployment admin",
        expected="User should be able see alert message after updating notifications for the deployment admin",
    )
    def verify_deployment_admin_notification_page_alert_message(
        self, success_message_text, deployment_admin_notification
    ):
        """
        Verify and toggle notification setting page checkboxes multiple times and check functionality.
        """
        time.sleep(2)
        notification_list = self.page.query_selector_all(
            self.all_deployment_admin_notification_options
        )
        notification_texts = [
            notification.inner_text() for notification in notification_list
        ]
        print("notification_list:", notification_texts)
        # Assert that the extracted texts match the expected list
        assert all(
            notification in deployment_admin_notification
            for notification in notification_texts
        )
        # Toggle the email checkbox
        if self.deployment_admin_select_all_email_notification.is_checked():
            self.deployment_admin_select_all_email_notification.uncheck()
        else:
            self.deployment_admin_select_all_email_notification.check()
        self.deployment_admin_select_all_email_notification.uncheck()
        self.deployment_admin_select_all_email_notification.check()
        self.deployment_admin_select_all_email_notification.uncheck()

        # Toggle the SMS checkbox
        if self.deployment_admin_select_all_sms_notification.is_checked():
            self.deployment_admin_select_all_sms_notification.uncheck()
        else:
            self.deployment_admin_select_all_sms_notification.check()
        self.deployment_admin_select_all_sms_notification.uncheck()
        self.deployment_admin_select_all_sms_notification.check()
        self.deployment_admin_select_all_sms_notification.uncheck()
        time.sleep(4)
        # Click the update button and verify the alert message
        self.update_button.click()
        success_message = self.alert_message.text_content()
        assert success_message == success_message_text
        print("Notification updated successfully")
