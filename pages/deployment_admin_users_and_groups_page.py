"""
Deployment Admin Users & Groups page modules
"""

import re
import time

from playwright.sync_api import Page, expect
from qase.pytest import qase

from pages.base_page import BasePage
from utilities.decorators import qase_screenshot


class DeploymentAdminUsersAndGroupsPage(BasePage):
    """
    Module containing objects and methods related to Deployment admin Users & Groups page
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Role locator
        self.select_role_dropdown = page.locator('(//div[@class="dropdown"])[2]')
        self.select_role = '//a[text()="<<select_role>>"]'

        # Side navigation tab
        self.users_and_groups_icon = page.locator('//*[@data-icon="users"]')
        self.users_and_groups_tab = '//span[text()="<<tab_to_navigate>>"]'

        # Users tab locators
        self.users_tab = page.locator('//button[@id="user-&-groups-tab-tab-users"]')
        self.groups_tab = page.locator('//button[@id="user-&-groups-tab-tab-groups"]')
        self.batch_action_title = page.locator('//label[text()="Batch Action"]')
        self.batch_action_dropdown = page.locator(
            '//div[@class="col-lg-9 col-sm-7"]//select'
        )
        self.users_filter_label = page.locator('(//div[text()="Filter:"])[1]')
        self.user_filter_dropdown = page.locator(
            '(//select[@class="generic-filter-select ms-2 form-select form-select-sm"])[1]'
        )
        self.users_filters_options = '(//select[@class="generic-filter-select ms-2 form-select form-select-sm"])[1]//option'
        self.users_filter = page.locator(
            '(//div[@class="d-flex align-items-center"]//select)[1]'
        )
        self.users_status = '//div[contains(@class, "badge-soft-success") or contains(@class, "badge-soft-danger")]'
        self.users_list_headers = page.locator('(//tr[@class="text-center"])[1]')
        self.users_list_component = page.locator('(//div[@class="card"])[1]')
        self.users_page_footer = page.locator(
            '(//div[@class="table-footer-border-top card-footer"])[1]'
        )
        self.apply_batch_action_button = page.locator('//button[text()="Apply Action"]')
        self.invite_button = page.locator('//button[text()="Invite"]')
        self.users_footer_pagination = page.locator(
            '(//div[@class="d-flex pagination-numbers"])[1]'
        )
        self.users_row_per_page = page.locator(
            '(//div[@class="d-flex align-items-center fs--1 ps-3"])[1]'
        )
        self.suspend_action = page.locator(
            '(//*[@data-icon="user"] | //*[@data-icon="user-slash"])[1]'
        )
        self.manage_groups_action = page.locator('(//*[@data-icon = "user-group"])[1]')
        self.more_info_action = page.locator('(//*[@data-icon = "ellipsis"])[1]')
        self.nudge_action = page.locator('(//*[@data-icon = "arrow-left-long"])[1]')

        # Manage User Groups locators
        self.manage_users_groups_filter = page.locator(
            '(//div[@class="d-flex align-items-center"]//select)[4]'
        )
        self.manage_users_groups_title = page.locator(
            '//div[text()="Manage User Groups"]'
        )
        self.manage_users_groups_header = page.locator(
            '(//div[@class="modal-content"]//tr)[1]'
        )
        self.manage_users_groups_component = page.locator(
            '//div[@class="modal-content"]'
        )
        self.manage_users_group_filter_title = page.locator(
            '(//div[text()="Filter:"])[3]'
        )
        self.manage_users_group_footer = page.locator(
            '(//div[@class="table-footer-border-top card-footer"])[3]'
        )
        self.accept_changes_button = page.locator('//button[text()="Accept Changes"]')
        self.cancel_button = page.locator('//button[text()="Cancel"]')
        self.notice_message = page.locator('//div[@class="ant-message-notice-content"]')
        self.select_group = page.locator('(//div[@class="modal-content"]//input)[2]')
        self.confirm_nudge_component = page.locator('//div[@class="modal-content"]')
        self.confirm_nudge_header = page.locator('//div[text()="Confirm Nudge"]')
        self.nudge_button = page.locator('//button[text()="Nudge"]')
        self.nudge_content = page.locator('//div[@class="nudge-content"]')

        # invite user locators
        self.invite_user_component = page.locator('//div[@class="modal-content"]')
        self.invite_user_header = page.locator('//div[text()="Invite User"]')
        self.name_label = page.locator('//label[text()="Name"]')
        self.name_input = page.locator('//input[@name="recipientName"]')
        self.email_label = page.locator('//label[text()="Email"]')
        self.email_input = page.locator('//input[@name="recipientEmail"]')
        self.user_type_dropdown_label = page.locator('//label[text()="User Type"]')
        self.user_type_dropdown = page.locator('//div[@class="col-lg-12"]//select')
        self.user_invite_button = page.locator(
            '//div[@class="modal-content"]//button[text()="Invite"]'
        )
        self.user_type_dropdown_option = '//select[@class="form-select"]//option'

        # groups tab locators
        self.groups_filter_label = page.locator('(//div[text()="Filter:"])[2]')
        self.groups_filters_options = '//select[@class="generic-filter-select ms-2 form-select form-select-sm"]//option'
        self.groups_filter = page.locator(
            '(//div[@class="d-flex align-items-center"]//select)[1]'
        )
        self.groups_status = '//div[contains(@class, "badge-soft-primary") or contains(@class, "badge-soft-secondary")]'
        self.groups_list_headers = page.locator('(//tr[@class="text-center"])[2]')
        self.groups_list_component = page.locator('//div[@class="simplebar-offset"]')
        self.groups_page_footer = page.locator(
            '(//div[@class="table-footer-border-top card-footer"])[2]'
        )
        self.create_button = page.locator('//button[text()="Invite"]')
        self.footer_pagination = page.locator(
            '(//div[@class="d-flex pagination-numbers"])[2]'
        )
        self.row_per_page = page.locator(
            '(//div[@class="d-flex align-items-center fs--1 ps-3"])[2]'
        )
        self.user_checkbox = page.locator('(//tr//input[@type="checkbox"])[2]')
        self.search_label = page.locator('//label[text()="Search"]')
        self.search_area = page.locator('//input[@placeholder="Search Group Name"]')
        self.add_member_action_button = page.locator(
            '(//*[@data-icon="people-group"])[1]'
        )
        self.edit_group_button = page.locator('(//*[@data-icon="pen"])[1]')
        self.edit_status_button = page.locator('(//*[@data-icon="user-group"])[1]')
        self.more_info_button = page.locator(
            '(//div[@id="user-&-groups-tab-tabpane-groups"]//*[@data-icon="ellipsis"])[1]'
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
        title="Verify users & groups icon and tab working",
        expected="deployment admin should be able to open and view users & groups tab",
    )
    def verify_and_click_on_account_balance_tab(self, tab_to_navigate):
        """
        Verify users & groups and click on users & groups tab
        """
        # verify icon availability
        expect(self.users_and_groups_icon).to_be_visible()
        # clicking on users & groups
        self.page.click(
            self.users_and_groups_tab.replace("<<tab_to_navigate>>", tab_to_navigate)
        )
        print(f"successfully able to click on {tab_to_navigate} tab")

    @qase_screenshot
    @qase.step(
        title="Verify users & groups page elements",
        expected="User should be able to visible every elements of users & groups page",
    )
    def verify_users_and_groups_page_elements(self, users_table_headers):
        """
        Verify and check availability of users & groups page elements
        """
        elements_to_check = [
            self.users_filter_label,
            self.user_filter_dropdown,
            self.batch_action_title,
            self.apply_batch_action_button,
            self.invite_button,
            self.users_list_headers,
            self.users_list_component,
            self.users_page_footer,
            self.users_footer_pagination,
            self.users_row_per_page,
            self.nudge_action,
            self.more_info_action,
            self.manage_groups_action,
            self.suspend_action,
            self.groups_tab,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("users & groups page elements verified")
        # Extract headers from the UI
        headers_title = self.users_list_headers.inner_text()
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
            headers_list == users_table_headers
        ), f"Headers do not match: {headers_list} != {users_table_headers}"
        print("All elements verified")

    @qase_screenshot
    @qase.step(
        title="Apply filter on users list and verify filtered data",
        expected="Data should be filtered properly based on the applied filter.",
    )
    def apply_filter_on_users_list_and_verify_filtered_data(
        self, available_filter_options, expected_statuses
    ):
        """
        Apply filter on users list and verify filtered data
        """
        expect(self.user_filter_dropdown).to_be_visible()
        filter_options = self.page.query_selector_all(self.users_filters_options)
        filter_options_text = [option.inner_text() for option in filter_options]
        assert (
            filter_options_text == available_filter_options
        ), f"Expected: {available_filter_options}, but got: {filter_options_text}"
        print(f"all available filters verified: {available_filter_options}")
        for filter_option in available_filter_options:
            self.users_filter.select_option(filter_option)
            time.sleep(5)
            self.page.wait_for_selector(self.users_status)
            # Query for the status elements after applying the filter
            all_users_status = self.page.query_selector_all(self.users_status)
            all_users_status_text = [status.inner_text() for status in all_users_status]
            # Print the text of each status
            print(
                f"users status after applying '{filter_option}': {all_users_status_text}"
            )
            # Assertion to verify the expected statuses are present
            if filter_option in expected_statuses:
                expected = expected_statuses[filter_option]
                if expected:
                    for expected_status in expected:
                        assert (
                            expected_status in all_users_status_text
                        ), f"'{expected_status}' not found in the status text for filter '{filter_option}'"
                else:
                    # If there are no expected statuses, assert that the status list is empty
                    assert (
                        not all_users_status_text
                    ), f"Expected no statuses for filter '{filter_option}', but found: {all_users_status_text}"

    @qase_screenshot
    @qase.step(
        title="Apply batch action on users and verify users status",
        expected="Status should be changed based on batch action",
    )
    def apply_batch_action_to_users(self):
        """
        Apply batch action on users and verify users status
        """
        expect(self.batch_action_title).to_be_visible()
        user_status_element = self.page.locator(
            '(//div[contains(@class, "badge-soft-success") or contains(@class, "badge-soft-danger")])[1]'
        )
        current_status = user_status_element.text_content()
        print(f"Current status is: {current_status}")
        # Verify the status is either 'Active' or 'Suspected'
        if "Active" in current_status:
            self.user_checkbox.click()
            self.batch_action_dropdown.select_option("Suspend")
            self.apply_batch_action_button.click()
            time.sleep(2)
            new_status = user_status_element.text_content()
            assert (
                "Suspended" in new_status
            ), f"Expected status to be 'Suspended', but got {new_status}"
            print("Status changed to 'Suspended' successfully.")
            # Now change the status back to 'Active'
            self.user_checkbox.click()
            self.batch_action_dropdown.select_option("Activate")
            self.apply_batch_action_button.click()
            # Wait for the status to revert to 'Active' and verify
            time.sleep(2)
            reverted_status = user_status_element.text_content()
            assert (
                "Active" in reverted_status
            ), f"Expected status to be 'Active', but got {reverted_status}"
            print("Status reverted to 'Active' successfully.")
        elif "Suspended" in current_status:
            self.user_checkbox.click()
            self.batch_action_dropdown.select_option("Activate")
            self.apply_batch_action_button.click()
            time.sleep(2)
            reverted_status = user_status_element.text_content()
            assert (
                "Active" in reverted_status
            ), f"Expected status to be 'Active', but got {reverted_status}"
            print("Status changed back to 'Active' successfully.")
        else:
            raise ValueError(f"Unexpected user status: {current_status}")

    @qase_screenshot
    @qase.step(
        title="Add item to the user list",
        expected="user should be able to add item to the item list",
    )
    def verify_and_test_invite_user_functionality(
        self,
        user_name,
        user_email,
        available_filter_options,
        success_message,
        user_type_to_select,
    ):
        """
        add item to the user list and ready it to send
        """
        self.invite_button.click()
        time.sleep(2)
        # Extract and clean headers for the main section
        elements_to_check = [
            self.invite_user_component,
            self.invite_user_header,
            self.name_label,
            self.name_input,
            self.email_label,
            self.email_input,
            self.user_type_dropdown_label,
            self.user_invite_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        self.name_input.fill(user_name)
        self.email_input.fill(user_email)
        dropdown_options = [
            option.inner_text().strip()
            for option in self.page.query_selector_all(self.user_type_dropdown_option)
        ]
        assert (
            dropdown_options == available_filter_options
        ), f"Dropdown options mismatch. Expected: {available_filter_options}, Found: {dropdown_options}"
        self.user_type_dropdown.select_option(user_type_to_select)
        # Click the invite button and verify success
        self.user_invite_button.click()
        time.sleep(4)  # Wait for the action to complete
        expect(self.notice_message).to_be_visible()
        message_text = self.notice_message.text_content()
        print(f"Notice message: {message_text}")
        # Verify success message
        assert (
            message_text == success_message
        ), f"Expected success message: '{success_message}', but found: '{message_text}'"

    @qase_screenshot
    @qase.step(
        title="Verify and perform edit status and delete functionality from the actions",
        expected="Actions functionality should be working as expected",
    )
    def verify_and_perform_status_and_delete_actions_functionality_from_actions(self):
        """
        Verify and perform edit status and delete functionality from the actions
        """
        elements_to_check = [
            self.suspend_action,
            self.more_info_action,
            self.nudge_action,
            self.manage_groups_action,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("actions buttons verified")
        user_status_element = self.page.locator(
            "(//div[contains(@class, 'badge-soft-success') or contains(@class, 'badge-soft-danger')])[1]"
        )
        current_status = user_status_element.text_content()
        print(f"Current status is: {current_status}")
        if "Active" in current_status:
            self.suspend_action.click()
            self.notice_message.wait_for(state="visible")
            expect(self.notice_message).to_be_visible()
            success_message = self.notice_message.text_content()
            print(success_message)
            assert success_message == "User Suspended"
            time.sleep(3)
            new_status = user_status_element.text_content()
            assert (
                "Suspended" in new_status
            ), f"Expected status to be 'Suspended', but got {new_status}"
            print("Status changed to 'Suspected' successfully.")
        if "Suspended" in current_status:
            self.suspend_action.click()
            self.notice_message.wait_for(state="visible")
            expect(self.notice_message).to_be_visible()
            success_message = self.notice_message.text_content()
            print(success_message)
            assert success_message == "User Activated"
            time.sleep(3)
            new_status = user_status_element.text_content()
            assert (
                "Active" in new_status
            ), f"Expected status to be 'Active', but got {new_status}"
            print("Status changed back to 'Active' successfully.")

    @qase_screenshot
    @qase.step(
        title="Verify and perform manage user group and nudge functionality from the actions",
        expected="Actions functionality should be working as expected",
    )
    def verify_and_perform_manage_user_group_and_nudge_actions_functionality_from_actions(
        self, headers, success_message
    ):
        """
        Verify and perform manage user group and nudge functionality from the actions
        """
        time.sleep(4)
        self.manage_groups_action.click()
        self.page.wait_for_load_state("domcontentloaded")
        elements_to_check = [
            self.manage_users_groups_component,
            self.manage_users_groups_title,
            self.manage_users_group_filter_title,
            self.manage_users_group_footer,
            self.accept_changes_button,
            self.cancel_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        header_text = self.manage_users_groups_header.inner_text()
        print("Raw header text:", header_text)
        # Normalize headers
        headers_list = re.split(r"[\t]+|\s{2,}", header_text)
        headers_list = [header.strip().lower() for header in headers_list if header]
        expected_headers = [header.lower() for header in headers]
        print("Expected headers:", expected_headers)
        print("Actual headers:", headers_list)
        assert (
            headers_list == expected_headers
        ), f"Headers mismatch! Expected: {expected_headers}, Got: {headers_list}"
        self.accept_changes_button.click()
        expect(self.notice_message).to_be_visible()
        message_text = self.notice_message.text_content()
        assert message_text == success_message
        self.nudge_action.click()
        time.sleep(2)
        elements_to_check = [
            self.confirm_nudge_component,
            self.nudge_button,
            self.nudge_content,
            self.confirm_nudge_header,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        self.nudge_button.click()

    @qase_screenshot
    @qase.step(
        title="Verify groups page elements",
        expected="User should be able to visible every elements of groups page",
    )
    def verify_groups_page_elements(self, users_table_headers):
        """
        Verify and check availability of groups page elements
        """
        self.groups_tab.click()
        elements_to_check = [
            self.groups_filter,
            self.groups_filter_label,
            self.groups_page_footer,
            self.groups_list_component,
            self.groups_list_headers,
            self.footer_pagination,
            self.row_per_page,
            self.create_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("groups page elements verified")
        # Extract headers from the UI
        headers_title = self.users_list_headers.inner_text()
        print("Headers titles before cleanup -->", headers_title)
        # Split the headers on tabs or multiple spaces
        headers_list = re.split(r"[\t]+|\s{2,}", headers_title)
        headers_list = [
            header.strip() for header in headers_list if header
        ]  # Remove empty users
        # Assert the headers match the expected values
        assert (
            headers_list == users_table_headers
        ), f"Headers do not match: {headers_list} != {users_table_headers}"
        print("All elements verified")
