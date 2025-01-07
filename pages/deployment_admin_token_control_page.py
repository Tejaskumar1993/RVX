"""
Deployment Admin token control page modules
"""

import re
import time

from qase.pytest import qase

from pages.base_page import BasePage
from playwright.sync_api import Page, expect

from utilities.decorators import qase_screenshot


class DeploymentAdminTokenControlPage(BasePage):
    """
    Module containing objects and methods related to Deployment admin token control page
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Role locator
        self.select_role_dropdown = page.locator('(//div[@class="dropdown"])[2]')
        self.select_role = '//a[text()="<<select_role>>"]'

        # Side navigation tab
        self.token_control_icon = page.locator('//*[@data-icon="coins"]')
        self.token_control_tab = '//span[text()="<<tab_to_navigate>>"]'

        self.token_bucket_header = page.locator('//h5[text()="Token Buckets"]')
        self.create_a_bucket_button = page.locator('//button[text()="Create a Bucket"]')
        self.token_bucket_filter_label = page.locator('//div[text()="Filter:"]')
        self.token_bucket_filter_select_option = page.locator("(//select)[1]")
        self.token_bucket_actions_button = page.locator(
            '(//div[@class="font-sans-serif btn-reveal-trigger dropend"]//button)[1]'
        )
        self.token_bucket_manage_action_button = page.locator('//a[text()="Manage"]')
        self.token_bucket_delete_action_button = page.locator('//a[text()="Delete"]')
        self.token_bucket_table_headers = page.locator("(//tr)[1]")
        self.token_bucket_visibility_status = (
            "//div[contains(@class, 'badge') and contains(@class, 'btn-outline')]"
        )
        self.token_bucket_footer = page.locator(
            '//div[@class="table-footer-border-top card-footer"]'
        )
        self.token_bucket_pagination = page.locator(
            '//div[@class="d-flex pagination-numbers"]'
        )
        self.token_bucket_row_per_page = page.locator(
            '//div[@class="d-flex align-items-center fs--1 ps-3 d-flex flex-wrap rows-page-count"]'
        )
        self.token_bucket_result_counter = page.locator(
            '//div[@class="d-flex align-items-center fs--1 ps-3"]'
        )
        self.token_control_switch = page.locator(
            '//label[text()="Enable Token Control"]//..//button'
        )
        self.notice_message = page.locator('//div[@class="ant-message-notice-content"]')

        # create bucket dialog locators

        self.create_a_bucket_component = page.locator('//div[@class="modal-content"]')
        self.create_bucket_header = page.locator('//div[text()="Create Bucket"]')
        self.bucket_name_label = page.locator('//label[text()="Bucket Name"]')
        self.bucket_name_input = page.locator('//input[@id="bucketName"]')
        self.bucket_description_label = page.locator(
            '//label[text()="Bucket Description"]'
        )
        self.bucket_description_input = page.locator(
            '//textarea[@id="bucketDescription"]'
        )
        self.total_limit_label = page.locator('//label[text()="Total Limit"]')
        self.total_limit_input = page.locator('//input[@id="totalLimit"]')
        self.max_token_per_user_label = page.locator(
            '//label[text()="Max token Per User"]'
        )
        self.max_token_per_user_input = page.locator('//input[@id="maxTokenPerUser"]')
        self.tokens_label = page.locator('//label[text()="Tokens"]')
        self.tokens_input = page.locator('//input[@id="tokens"]')
        self.create_bucket_button = page.locator('//button[text()="Create Bucket"]')
        self.cancel_button = page.locator('//button[text()="Cancel"]')
        self.action_button = "//tr[td[text()='<<bucket_name>>']]//button[contains(@class, 'dropdown-toggle')]"
        self.manage_button = "//tr[td[text()='<<bucket_name>>']]//a[contains(@class, 'dropdown-item') and text()='Manage']"
        self.delete_button = "//tr[td[text()='<<bucket_name>>']]//a[contains(@class, 'dropdown-item') and text()='Delete']"

        # manage_bucket_locators
        self.manage_bucket_title = page.locator('//div[text()="Manage Bucket"]')
        self.manage_bucket_name_label = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-summary"]//label[text()="Bucket Name"]'
        )
        self.manage_bucket_name_input = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-summary"]//input[@id="formInputLabel"]'
        )
        self.active_deactive_switch = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-summary"]//input[@id="bucket-switch"]'
        )
        self.manage_description_label = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-summary"]//label[text()="Description"]'
        )
        self.manage_description_input = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-summary"]//textarea[@id="formTextAreaLabel"]'
        )
        self.token_available_content_box = page.locator(
            '(//div[@id="account-balance-dashboard-tab-tabpane-summary"]//div[@class="mb-2  card"])[1]'
        )
        self.token_available_title = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-summary"]//div[text()="Token Available"]'
        )
        self.token_limit_title = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-summary"]//div[text()="Token Limit"]'
        )
        self.token_limit_content_box = page.locator(
            '(//div[@id="account-balance-dashboard-tab-tabpane-summary"]//div[@class="mb-2  card"])[2]'
        )
        self.token_button = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-summary"]//button[text()="Token"]'
        )
        self.token_limit_button = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-summary"]//button[text()="Token Limit"]'
        )
        self.connects_title = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-summary"]//h5[text()="Connects"]'
        )
        self.connects_table = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-summary"]//table'
        )
        self.update_button = page.locator('//button[text()="Update"]')
        self.summary_tab = page.locator(
            '//button[@id="account-balance-dashboard-tab-tab-summary"]'
        )
        self.schedule_deposits_tab = page.locator(
            '//button[@id="account-balance-dashboard-tab-tab-schedule-deposits"]'
        )
        self.balance_title = page.locator('//div[text()="Balance"]')
        self.balance_content_box = page.locator('//div[@class="mb-2 h-100 card"]')
        self.delete_confirm_message = page.locator('//div[@class="modal-body"]')
        self.generic_update_button = page.locator('//button[text()="Confirm"]')
        self.success_message = page.locator(
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
        title="Verify token control icon and tab working",
        expected="deployment admin should be able to open and view token control tab",
    )
    def verify_and_click_on_token_control_tab(self, tab_to_navigate):
        """
        Verify token control and click on token control tab
        """
        # verify icon availability
        expect(self.token_control_icon).to_be_visible()
        # clicking on token control tab
        self.page.click(
            self.token_control_tab.replace("<<tab_to_navigate>>", tab_to_navigate)
        )
        print(f"successfully able to click on {tab_to_navigate} tab")

    @qase_screenshot
    @qase.step(
        title="Verify token control page element visibility",
        expected="Deployment admin should be able to visible all elements of the token control page",
    )
    def verify_token_control_page_elements(
        self, token_bucket_table_headers, available_filter_options
    ):
        """
        Verify token control page elements
        """
        self.page.wait_for_load_state("domcontentloaded")
        elements_to_check = [
            self.token_bucket_filter_label,
            self.token_bucket_header,
            self.token_bucket_table_headers,
            self.token_bucket_pagination,
            self.token_bucket_result_counter,
            self.token_control_switch,
            self.create_a_bucket_button,
            self.token_bucket_actions_button,
            self.token_bucket_row_per_page,
            self.token_bucket_footer,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
            # Extract headers from the UI
            headers_title = self.token_bucket_table_headers.inner_text()
            print("Headers titles before cleanup -->", headers_title)
            cleaned_headers_title = re.sub(
                r"[🔼🔽]", "", headers_title
            ).strip()  # Remove sorting icons
            # Split the headers on tabs or multiple spaces
            headers_list = re.split(r"[\t]+|\s{2,}", cleaned_headers_title)
            headers_list = [
                header.strip() for header in headers_list if header
            ]  # Remove empty users
            # Assert the headers match the expected values
            assert (
                headers_list == token_bucket_table_headers
            ), f"Headers do not match: {headers_list} != {token_bucket_table_headers}"
            print("All elements verified")
        filter_options_raw = self.token_bucket_filter_select_option.inner_text()
        filter_options = [
            option.strip()
            for option in filter_options_raw.splitlines()
            if option.strip()
        ]
        print(f"Extracted Filter Options: {filter_options}")
        assert (
            filter_options == available_filter_options
        ), f"Expected filter options {available_filter_options}, but found {filter_options}"

    @qase_screenshot
    @qase.step(
        title="Apply filter on token bucket data of token control",
        expected="deployment admin should be able to apply filter on token bucket data",
    )
    def apply_filter_on_token_bucket_data(
        self, available_filter_options, expected_statuses
    ):
        """
        apply filter on token bucket data and verify  filtered data
        """
        for filter_option in available_filter_options:
            self.token_bucket_filter_select_option.select_option(filter_option)
            self.page.wait_for_selector(self.token_bucket_visibility_status)
            # Query for the status elements after applying the filter
            token_bucket_visibility_status = self.page.query_selector_all(
                self.token_bucket_visibility_status
            )
            token_bucket_visibility_status_text = [
                status.inner_text() for status in token_bucket_visibility_status
            ]
            # Print the text of each status
            print(
                f"Users status after applying '{filter_option}': {token_bucket_visibility_status_text}"
            )
            # Assertion to verify the expected statuses are present
            if filter_option in expected_statuses:
                expected = expected_statuses[filter_option]
                if expected:
                    for expected_status in expected:
                        assert (
                            expected_status in token_bucket_visibility_status_text
                        ), f"'{expected_status}' not found in the status text for filter '{filter_option}'"
                else:
                    # If there are no expected statuses, assert that the status list is empty
                    assert (
                        not token_bucket_visibility_status_text
                    ), f"Expected no statuses for filter '{filter_option}', but found: {token_bucket_visibility_status_text}"

    @qase_screenshot
    @qase.step(
        title="Verify and test token buckets enable and disable functionality",
        expected="deployment admin should be able to enable and disable token buckets",
    )
    def apply_filter_on_token_bucket_data(
        self, disable_message_text, enable_message_text
    ):
        """
        verify and test token control functionality
        """
        self.token_control_switch.click()
        time.sleep(2)
        expect(self.notice_message).to_be_visible()
        success_message = self.notice_message.text_content()
        print(f"token bucket updated {success_message}")
        assert success_message == disable_message_text
        time.sleep(3)
        self.token_control_switch.click()
        expect(self.notice_message).to_be_visible()
        success_message = self.notice_message.text_content()
        print(f"token bucket updated {success_message}")
        assert success_message == enable_message_text

    @qase_screenshot
    @qase.step(
        title="Verify all elements of create bucket dialog and create a new bucket",
        expected="deployment admin should be able to create new bucket",
    )
    def verify_and_create_a_new_bucket(
        self, tokens_count, max_token, token_limit, bucket_description, bucket_name
    ):
        """
        Verify all elements of create bucket dialog and create a new bucket
        """
        self.create_a_bucket_button.click()
        elements_to_check = [
            self.create_a_bucket_component,
            self.create_bucket_header,
            self.bucket_name_label,
            self.bucket_name_input,
            self.bucket_description_input,
            self.bucket_description_label,
            self.total_limit_input,
            self.total_limit_label,
            self.max_token_per_user_input,
            self.max_token_per_user_label,
            self.tokens_input,
            self.tokens_label,
            self.create_bucket_button,
            self.cancel_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        self.bucket_name_input.fill(bucket_name)
        self.bucket_description_input.fill(bucket_description)
        self.total_limit_input.fill(token_limit)
        self.max_token_per_user_input.fill(max_token)
        self.tokens_input.fill(tokens_count)
        self.create_bucket_button.click()
        expect(self.notice_message).to_be_visible()
        success_message = self.notice_message.text_content()
        print(f"token bucket updated {success_message}")
        print("bucket created successfully")
        return bucket_name, bucket_description

    @qase_screenshot
    @qase.step(
        title="Verify and perform manage action on token bucket",
        expected="deployment admin should be able to manage created token",
    )
    def verify_manage_and_delete_action_on_token_bucket(
        self, bucket_name, bucket_description, new_description
    ):
        """
        Verify and perform manage action on token bucket
        """
        time.sleep(1)
        self.page.click(self.action_button.replace("<<bucket_name>>", bucket_name))
        self.page.click(self.manage_button.replace("<<bucket_name>>", bucket_name))
        elements_to_check = [
            self.create_a_bucket_component,
            self.manage_bucket_title,
            self.manage_bucket_name_label,
            self.manage_description_input,
            self.manage_bucket_name_input,
            self.manage_description_label,
            self.active_deactive_switch,
            self.token_available_content_box,
            self.token_available_title,
            self.token_button,
            self.token_limit_button,
            self.token_limit_content_box,
            self.token_limit_button,
            self.connects_table,
            self.connects_title,
            self.update_button,
            self.cancel_button,
            self.schedule_deposits_tab,
            self.summary_tab,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        self.schedule_deposits_tab.click()
        expect(self.balance_title).to_be_visible()
        expect(self.balance_content_box).to_be_visible()
        self.summary_tab.click()
        time.sleep(3)
        bucket_name_text = self.manage_bucket_name_input.input_value()
        assert bucket_name_text == bucket_name
        description = self.manage_description_input.input_value()
        assert description == bucket_description
        self.manage_description_input.fill(new_description)
        self.update_button.click()
        success_text = self.success_message.text_content()
        assert success_text == "Bucket updated successfully"
        time.sleep(2)
        self.page.click(self.action_button.replace("<<bucket_name>>", bucket_name))
        self.page.click(self.delete_button.replace("<<bucket_name>>", bucket_name))
        confirm_message_text = self.delete_confirm_message.text_content()
        print(f"Confirm message text is: {confirm_message_text}")
        assert confirm_message_text == "Are you sure you want to delete this record?"
        self.generic_update_button.click()
        time.sleep(2)
        expect(self.notice_message).to_be_visible()
        message_text = self.notice_message.text_content()
        print(message_text)
        assert message_text == "Bucket Deletion Successful"
        print("bucket creation, mange and delete functionality verified successfully")
