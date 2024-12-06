"""
Vendor Notification page modules
"""

import time

from playwright.sync_api import Page, expect
from qase.pytest import qase

from pages.base_page import BasePage
from utilities.decorators import qase_screenshot

class VendorNotificationPage(BasePage):
    """
       Module containing objects and methods related to Vendor Notification page
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Notification page locators
        self.change_role_dropdown = page.locator('(//button[@id="dropdown-flags"])[2]')
        self.role_to_select = '//a[text()="<<role_to_change>>"]'
        self.profile_image = page.locator("//a[@href='/dashboard/admin#!']")
        self.notification_setting_dropdown = '//a[text()="<<Notification Settings>>"]'
        self.notification_header = page.locator('//h3[text()="Notification Settings"]')
        self.alert = page.locator('//th[text()="Alert"]')
        self.alert_type = page.locator('//th[text()="Alert Type"]')
        self.email = page.locator('//th[text()="Email"]')
        self.sms = page.locator('//th[text()="SMS"]')
        self.select_all = page.locator('//td[text()="Select All"]')
        self.unacknowledged_orders = page.locator('//td[text()="Unacknowledged orders"]')
        self.orders_created = page.locator('//td[text()="Orders created"]')
        self.orders_not_sent = page.locator('//td[text()="Orders not sent"]')
        self.sms_text = page.locator('//p[text()="SMS alerts are sent to the phone number on file. Standard message & data rates may apply."]')
        self.update_button = page.locator('//button[text()="Update"]')
        self.email_checkbox = page.locator('(//tr[td[text()="Select All"]]//input[@type="checkbox"])[1]')
        self.sms_checkbox = page.locator('(//tr[td[text()="Select All"]]//input[@type="checkbox"])[2]')
        self.alert_message = page.locator('//div[@class="ant-message-custom-content ant-message-success"]')

    @qase_screenshot
    @qase.step(
        title="click on user role dropdown and select role",
        expected="User should be able to change role successfully",
    )
    def click_on_dropdown_and_change_user_role(self, role_to_change):
        """
        Change user role from dropdown
        """
        time.sleep(5)
        self.change_role_dropdown.click()
        time.sleep(5)
        self.page.locator(
            self.role_to_select.replace("<<role_to_change>>", role_to_change)
        ).click()
        print(f"User role changed to {role_to_change}")

    @qase_screenshot
    @qase.step(
        title="click on user profile dropdown and select notification setting option",
        expected="User should be able to select notification setting successfully",
        )
    def click_on_profile_and_click_on_notification(self, change_to_notification):
        """
        navigate to notification page
        """
        self.page.wait_for_selector("//a[@href='/dashboard/admin#!']")
        self.profile_image.click()
        self.page.locator(
            self.notification_setting_dropdown.replace("<<Notification Settings>>", change_to_notification)).click()
        print(f"User role changed to {change_to_notification}")


    @qase_screenshot
    @qase.step(
        title="Verify notification setting page elements",
        expected="User should be able to visible every elements of notification setting page",
    )
    def verify_vendor_notification_page_elements(self):
        """
        Verify and check availability of notification setting page elements
        """
        time.sleep(5)
        elements_to_check = [
            self.notification_header,
            self.alert,
            self.alert_type,
            self.email,
            self.sms,
            self.select_all,
            self.unacknowledged_orders,
            self.orders_created,
            self.orders_not_sent,
            self.sms_text,
            self.update_button,
        ]

        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("items list page elements verified")

    @qase_screenshot
    @qase.step(
        title="Verify notification setting page checkbox checked and unchecked ",
        expected="User should be able to checked and unchecked checkbox of notification setting page",
    )
    def verify_vendor_notification_page_checkbox(self):
        """
        Verify and check of notification setting page checkbox and function
        """
        self.email_checkbox.click()
        self.sms_checkbox.click()
        self.update_button.click()

    @qase_screenshot
    @qase.step(
        title="Verify alert message",
        expected="User should be able see alert message",
    )
    def verify_vendor_notification_page_alert_message(self, success_message_text):
        """
        Verify and toggle notification setting page checkboxes multiple times and check functionality.
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


