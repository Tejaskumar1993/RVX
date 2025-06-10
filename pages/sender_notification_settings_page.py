"""
Sender Notification module
"""

import time

from playwright.sync_api import Page, expect
from qase.pytest import qase

from pages.base_page import BasePage
from utilities.decorators import qase_screenshot


class SenderNotificationPage(BasePage):
    """
    Module containing objects and methods related to Sender Notification page
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Notification navigate page locators

        self.profile_image_icon = page.locator("//img[@class='mx-auto profile-pic rounded-circle']")
        self.setting = "//a[.='Settings']"
        self.change_role_dropdown = page.locator('(//button[@id="dropdown-flags"])[2]')
        self.role_to_select = '//a[text()="<<role_to_change>>"]'
        self.profile_image = page.locator("//a[@href='/dashboard/admin#!']")
        self.notification_setting_dropdown = '//a[text()="<<Notification Settings>>"]'

        # Notification page locators
        self.notification_header = page.locator('//h3[text()="Notification Settings"]')
        self.alert_header = page.locator('//th[text()="Alert"]')
        self.alert_type_header = page.locator('//th[text()="Alert Type"]')
        self.email_header = page.locator('//th[text()="Email"]')
        self.sms_header = page.locator('//th[text()="SMS"]')
        self.select_all = page.locator('//td[text()="Select All"]')
        self.password_reset = page.locator('//td[contains(text(),"Password reset")]')
        self.account_balance_reminders = page.locator(
            '//td[text()="Account balance reminders"]'
        )
        self.unclaimed_e_gift = page.locator('//td[text()="Unclaimed eGift"]')
        self.order_status_updated = page.locator('//td[text()="Order status updated"]')
        self.sms_message = page.locator(
            '//p[text()="SMS alerts are sent to the phone number on file. Standard message & data rates may apply."]'
        )
        self.update_button = page.locator('//button[text()="Update"]')
        self.email_checkbox = page.locator(
            '(//tr[td[text()="Select All"]]//input[@type="checkbox"])[1]'
        )
        self.sms_checkbox = page.locator(
            '(//tr[td[text()="Select All"]]//input[@type="checkbox"])[2]'
        )
        self.alert_message = page.locator(
            '//div[@class="ant-message-custom-content ant-message-success"]'
        )

    @qase_screenshot
    @qase.step(
        title="click on user role dropdown and select role",
        expected="User should be able to change role successfully",
    )

    @qase_screenshot
    @qase.step(
        title="click on user profile dropdown and select notification setting option",
        expected="User should be able to select notification setting successfully",
    )
    def click_on_profile_and_click_on_notification(self, change_to_notification, profile_option):
        """
        navigate to notification page
        """
        time.sleep(6)
        self.profile_image_icon.click()
        self.page.click(
            self.setting.replace("Settings",profile_option)
        )
        self.page.locator(
            self.notification_setting_dropdown.replace(
                "<<Notification Settings>>", change_to_notification
            )
        )
        print(f"User role changed to {change_to_notification}")

    @qase_screenshot
    @qase.step(
        title="Verify sender notification setting page elements",
        expected="User should be able to visible every elements of sender notification setting page",
    )
    def verify_sender_notification_page_elements(self):
        """
        Verify and check availability of sender notification setting page elements
        """
        time.sleep(6)
        elements_to_check = [
            self.notification_header,
            self.alert_header,
            self.alert_type_header,
            self.email_header,
            self.sms_header,
            self.select_all,
            self.password_reset,
            self.account_balance_reminders,
            self.unclaimed_e_gift,
            self.order_status_updated,
            self.sms_message,
            self.update_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print(" Sender Notification page elements verified")

    @qase_screenshot
    @qase.step(
        title="Verify alert message and set sender notification",
        expected="User should be able see alert message after updating notifications for the sender",
    )
    def verify_sender_notification_page_alert_message(self, success_message_text):
        """
        Verify and toggle notification setting for sender notification page checkboxes multiple times and check functionality.
        """
        time.sleep(2)
        # Toggle the email checkbox
        if self.email_checkbox.is_checked():
            self.email_checkbox.uncheck()
        else:
            self.email_checkbox.check()
        self.email_checkbox.uncheck()
        self.email_checkbox.check()
        self.email_checkbox.uncheck()

        # Toggle the SMS checkbox
        if self.sms_checkbox.is_checked():
            self.sms_checkbox.uncheck()
        else:
            self.sms_checkbox.check()
        self.sms_checkbox.uncheck()
        self.sms_checkbox.check()
        self.sms_checkbox.uncheck()

        # Click the update button and verify the alert message
        self.update_button.click()
        success_message = self.alert_message.text_content()
        assert success_message == success_message_text
        print("Notification updated successfully")
