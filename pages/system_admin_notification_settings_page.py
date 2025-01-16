"""
System Admin Notification Settings page modules
"""

import time

from playwright.sync_api import Page, expect
from qase.pytest import qase

from pages.base_page import BasePage
from utilities.decorators import qase_screenshot


class SystemAdminNotificationSettingsPage(BasePage):
    """
    Module containing objects and methods related to System Admin Notification settings page
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.profile_image = page.locator("//a[@href='/dashboard/admin#!']")
        self.notification_setting_dropdown = '//a[text()="<<Notification Settings>>"]'
        self.notification_header = page.locator('//h3[text()="Notification Settings"]')
        self.deployment_admin_notification_model = page.locator(
            '(//div[@class="mb-3 overflow-auto notification-settings-card"])[1]'
        )
        self.vendor_notification_model = page.locator(
            '(//div[@class="mb-3 overflow-auto notification-settings-card"])[2]'
        )
        self.sender_notification_model = page.locator(
            '(//div[@class="mb-3 overflow-auto notification-settings-card"])[3]'
        )
        self.deployment_admin_title = page.locator(
            '//div[@class="mb-3 overflow-auto notification-settings-card"]//h4[text()="Deployment Admin"]'
        )
        self.vendor_title = page.locator(
            '//div[@class="mb-3 overflow-auto notification-settings-card"]//h4[text()="Vendor"]'
        )
        self.sender_title = page.locator(
            '//div[@class="mb-3 overflow-auto notification-settings-card"]//h4[text()="Sender"]'
        )
        self.deployment_admin_alert = page.locator(
            "//h4[text()='Deployment Admin']/following-sibling::div//th[text()='Alert']"
        )
        self.deployment_admin_alert_type = page.locator(
            "//h4[text()='Deployment Admin']/following-sibling::div//th[text()='Alert Type']"
        )
        self.deployment_admin_email = page.locator(
            "//h4[text()='Deployment Admin']/following-sibling::div//th[text()='Email']"
        )
        self.deployment_admin_sms = page.locator(
            "//h4[text()='Deployment Admin']/following-sibling::div//th[text()='SMS']"
        )
        self.vendor_alert = page.locator(
            "//h4[text()='Vendor']/following-sibling::div//th[text()='Alert']"
        )
        self.vendor_alert_type = page.locator(
            "//h4[text()='Vendor']/following-sibling::div//th[text()='Alert Type']"
        )
        self.vendor_email = page.locator(
            "//h4[text()='Vendor']/following-sibling::div//th[text()='Email']"
        )
        self.vendor_sms = page.locator(
            "//h4[text()='Vendor']/following-sibling::div//th[text()='SMS']"
        )
        self.sender_alert = page.locator(
            "//h4[text()='Sender']/following-sibling::div//th[text()='Alert']"
        )
        self.sender_alert_type = page.locator(
            "//h4[text()='Sender']/following-sibling::div//th[text()='Alert Type']"
        )
        self.sender_email = page.locator(
            "//h4[text()='Sender']/following-sibling::div//th[text()='Email']"
        )
        self.sender_sms = page.locator(
            "//h4[text()='Sender']/following-sibling::div//th[text()='SMS']"
        )
        self.all_deployment_admin_notification_options = "//h4[text()='Deployment Admin']/following-sibling::div//table//tbody//td[1]"

        self.all_vendor_notification_options = (
            "//h4[text()='Vendor']/following-sibling::div//table//tbody//td[1]"
        )

        self.all_sender_notification_options = (
            "//h4[text()='Sender']/following-sibling::div//table//tbody//td[1]"
        )
        self.deployment_admin_select_all_email_notification = page.locator(
            "//h4[text()='Deployment Admin']//..//td[text()='Select All']/following-sibling::td[1]//input[@type='checkbox']"
        )
        self.vendor_select_all_email_notification = page.locator(
            "//h4[text()='Vendor']//..//td[text()='Select All']/following-sibling::td[1]//input[@type='checkbox']"
        )
        self.sender_select_all_email_notification = page.locator(
            "//h4[text()='Sender']//..//td[text()='Select All']/following-sibling::td[1]//input[@type='checkbox']"
        )
        self.deployment_admin_select_all_sms_notification = page.locator(
            "//h4[text()='Deployment Admin']//..//td[text()='Select All']/following-sibling::td[2]//input[@type='checkbox']"
        )
        self.vendor_select_all_sms_notification = page.locator(
            "//h4[text()='Vendor']//..//td[text()='Select All']/following-sibling::td[2]//input[@type='checkbox']"
        )
        self.sender_select_all_sms_notification = page.locator(
            "//h4[text()='Sender']//..//td[text()='Select All']/following-sibling::td[2]//input[@type='checkbox']"
        )
        self.update_button = page.locator('//button[text()="Update"]')
        self.alert_message = page.locator(
            '//div[@class="ant-message-custom-content ant-message-success"]'
        )

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
            self.deployment_admin_title,
            self.deployment_admin_alert,
            self.deployment_admin_email,
            self.update_button,
            self.vendor_title,
            self.vendor_notification_model,
            self.vendor_sms,
            self.vendor_alert,
            self.vendor_alert_type,
            self.vendor_email,
            self.sender_notification_model,
            self.sender_title,
            self.sender_alert,
            self.sender_alert_type,
            self.sender_email,
            self.sender_sms,
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

    @qase_screenshot
    @qase.step(
        title="Verify alert message and set sender",
        expected="User should be able see alert message after updating notifications for the sender",
    )
    def verify_sender_notification_page_alert_message(
        self, success_message_text, sender_notification
    ):
        """
        Verify and toggle notification setting page checkboxes multiple times and check functionality.
        """
        time.sleep(2)
        notification_list = self.page.query_selector_all(
            self.all_sender_notification_options
        )
        notification_texts = [
            notification.inner_text() for notification in notification_list
        ]
        print("notification_list:", notification_texts)
        # Assert that the extracted texts are in the expected sender notifications list
        assert all(
            notification in sender_notification for notification in notification_texts
        )
        # Toggle the email checkbox
        if self.sender_select_all_email_notification.is_checked():
            self.sender_select_all_email_notification.uncheck()
        else:
            self.sender_select_all_email_notification.check()
        self.sender_select_all_email_notification.uncheck()
        self.sender_select_all_email_notification.check()
        self.sender_select_all_email_notification.uncheck()

        # Toggle the SMS checkbox
        if self.sender_select_all_sms_notification.is_checked():
            self.sender_select_all_sms_notification.uncheck()
        else:
            self.sender_select_all_sms_notification.check()
        self.sender_select_all_sms_notification.uncheck()
        self.sender_select_all_sms_notification.check()
        self.sender_select_all_sms_notification.uncheck()
        time.sleep(4)
        # Click the update button and verify the alert message
        self.update_button.click()
        success_message = self.alert_message.text_content()
        assert success_message == success_message_text
        print("Notification updated successfully")

    @qase_screenshot
    @qase.step(
        title="Verify alert message and set vendor notification",
        expected="User should be able see alert message after updating notifications for the vendor",
    )
    def verify_vendor_notification_page_alert_message(
        self, success_message_text, vendor_notification
    ):
        """
        Verify and toggle notification setting page checkboxes multiple times and check functionality.
        """
        time.sleep(2)
        notification_list = self.page.query_selector_all(
            self.all_vendor_notification_options
        )
        notification_texts = [
            notification.inner_text() for notification in notification_list
        ]
        print("notification_list:", notification_texts)
        # Assert that the extracted texts are in the expected sender notifications list
        assert all(
            notification in vendor_notification for notification in notification_texts
        )
        # Toggle the email checkbox
        if self.vendor_select_all_email_notification.is_checked():
            self.vendor_select_all_email_notification.uncheck()
        else:
            self.vendor_select_all_email_notification.check()
        self.vendor_select_all_email_notification.uncheck()
        self.vendor_select_all_email_notification.check()
        self.vendor_select_all_email_notification.uncheck()

        # Toggle the SMS checkbox
        if self.vendor_select_all_sms_notification.is_checked():
            self.vendor_select_all_sms_notification.uncheck()
        else:
            self.vendor_select_all_sms_notification.check()
        self.vendor_select_all_sms_notification.uncheck()
        self.vendor_select_all_sms_notification.check()
        self.vendor_select_all_sms_notification.uncheck()
        time.sleep(4)
        # Click the update button and verify the alert message
        self.update_button.click()
        success_message = self.alert_message.text_content()
        assert success_message == success_message_text
        print("Notification updated successfully")
