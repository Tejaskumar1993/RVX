"""
Vendor Orders List module
"""
import re
import time
from playwright.sync_api import Page, expect
from qase.pytest import qase

from pages.base_page import BasePage
from utilities.decorators import qase_screenshot


class VendorUsersListPage(BasePage):
    """
    module for Vendor Orders List page actions
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Locators
        self.change_role_dropdown = page.locator('(//button[@id="dropdown-flags"])[2]')
        self.role_to_select = '//a[text()="<<role_to_change>>"]'
        # Users list Filters locators
        self.filter_title = page.locator('//div[text()="Filter:"]')
        self.filter_drop_down = '//select[@class="generic-filter-select ms-2 form-select form-select-sm"]//option'
        self.dropdown = page.locator(
            '//div[@class="d-flex align-items-center mb-2"]//select'
        )
        self.all_users_status = '//div[contains(@class, "badge-soft-success") or contains(@class, "badge-soft-danger")]'
        self.batch_action_title = page.locator('//label[text()="Batch Action"]')
        self.user_checkbox = page.locator('(//tr//input[@type="checkbox"])[2]')
        self.batch_action_dropdown = page.locator(
            '//div[@class="d-flex align-items-center"]'
        )
        self.apply_batch_action_button = page.locator('//button[text()="Apply Action"]')
        self.select_batch_action_options = page.locator('//div[@class="d-flex align-items-center"]//select')
        self.invite_button = page.locator('//button[text()="Invite"]')
        self.user_page_header_component = page.locator('//div[@class="mb-2 card"]')
        self.user_page_list_component = page.locator('//div[@class="card"]')
        self.user_list_headers = page.locator('//tr[@class="text-center"]')
        # invite user locators
        self.invite_user_header = page.locator('//div[text()="Invite Vendor"]')
        self.first_name_text = page.locator('//label[text()="First Name"]')
        self.firstname_input = page.locator('[id="firstName"]')
        self.last_name_text = page.locator('//label[text()="Last Name"]')
        self.lastname_input = page.locator('[id="lastName"]')
        self.email_text = page.locator('//label[text()="Email"]')
        self.email_input = page.locator('[id="email"]')
        self.send_invite_button = page.locator('//button[text()="Send Invite"]')
        self.cancel_button = page.locator('//button[text()="Cancel"]')
        self.close_button = page.locator('//button[@class="btn-close"]')
        self.success_message = page.locator(
            '//div[@class="ant-message-notice-content"]'
        )
        self.warning_message = page.locator(
            '//div[@class="ant-message-custom-content ant-message-warning"]'
        )
        self.active_and_inactive_action_button = page.locator('(//*[@data-icon="lock-open" or @data-icon="lock"])[1]')
        self.delete_action_button = page.locator('(//*[@data-icon="trash"])[1]')
        self.footer = page.locator(
            '//div[@class="table-footer-border-top card-footer"]'
        )
        self.pagination = page.locator('//div[@class="d-flex pagination-numbers m-auto mb-2"]')
        self.result_counter = page.locator('//div[@class="d-flex align-items-center fs--1 ps-3"]')
        self.rows_per_page = page.locator(
            '//div[@class="d-flex align-items-center fs--1 ps-3 d-flex flex-wrap rows-page-count"]')
        self.users_list_icon = page.locator('//*[@data-icon="users"]')
        self.select_tab_from_side_navigation = '//span[text()="<<tab_to_navigate>>"]'
        self.select_user = page.locator('//tr[2]')
        self.user_information_component = page.locator('//div[@class="modal-content"]')
        self.user_information_title = page.locator('//div[text()="User Information"]')
        self.details_title = page.locator('//h5[text()="Details"]')
        self.user_image = page.locator('//div[@class="ant-upload-list-item-container"]')
        self.user_name = page.locator('//p[text()="Username"]')
        self.first_name = page.locator('//p[text()="First Name"]')
        self.last_name = page.locator('//p[text()="Last Name"]')
        self.email = page.locator('//p[text()="Email"]')
        self.phone_number = page.locator('//p[text()="Phone Number"]')
        self.status = page.locator('//p[text()="Status"]')
        self.account_type = page.locator('//p[text()="Account Type"]')
        self.edit_user_button = page.locator('//button[text()="Edit User"]')
        self.user_controls_component = page.locator('(//div[@class="mb-3 card"])[2]')
        self.user_controls_title = page.locator('//h5[text()="User Controls"]')
        self.reset_password_button = page.locator('//button[text()="Reset Password"]')
        self.active_and_inactive_user_button = page.locator(
            '//button[text()="inactivate User" or text()="Activate User"]')
        self.change_deployment = page.locator('//button[text()="Change Deployment"]')
        self.change_account_type = page.locator('//button[text()="Change Account Type"]')

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
        title="Verify and click on Orders List page",
        expected="User should be able to see orders list icon and able to click on orders list tab",
    )
    def verify_and_click_on_users_list_tab(self, side_navigation_item):
        """
        Verify Users and click on Orders List tab
        """
        # verify icon availability
        expect(self.users_list_icon).to_be_visible()
        # clicking on company information
        time.sleep(5)
        self.page.click(
            self.select_tab_from_side_navigation.replace(
                "<<tab_to_navigate>>", side_navigation_item
            )
        )
        print(f"successfully able to click on {side_navigation_item} tab")

    @qase_screenshot
    @qase.step(
        title="Verify users page elements",
        expected="User should be able to visible every elements of users page",
    )
    def verify_users_page_elements(self, users_table_headers):
        """
        Verify and check availability of users page elements
        """
        elements_to_check = [
            self.user_page_list_component,
            self.user_page_header_component,
            self.filter_title,
            self.dropdown,
            self.batch_action_title,
            self.apply_batch_action_button,
            self.result_counter,
            self.rows_per_page,
            self.pagination,
            self.footer,
            self.apply_batch_action_button,
            self.invite_button,
            self.delete_action_button,
            self.active_and_inactive_action_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("users & groups page elements verified")
        # Extract headers from the UI
        headers_title = self.user_list_headers.inner_text()
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
        expect(self.dropdown).to_be_visible()
        filter_options = self.page.query_selector_all(self.filter_drop_down)
        filter_options_text = [option.inner_text() for option in filter_options]
        assert (
                filter_options_text == available_filter_options
        ), f"Expected: {available_filter_options}, but got: {filter_options_text}"
        print(f"all available filters verified: {available_filter_options}")
        for filter_option in available_filter_options:
            self.dropdown.select_option(filter_option)
            time.sleep(5)
            self.page.wait_for_selector(self.all_users_status)
            # Query for the status elements after applying the filter
            all_users_status = self.page.query_selector_all(self.all_users_status)
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
            self.batch_action_dropdown.select_option("Inactive")
            self.apply_batch_action_button.click()
            time.sleep(2)
            new_status = user_status_element.text_content()
            assert (
                    "Inactive" in new_status
            ), f"Expected status to be 'Inactive', but got {new_status}"
            print("Status changed to 'Inactive' successfully.")
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
        elif "Inactive" in current_status:
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
            user_last_name,
            success_message,
    ):
        """
        add item to the user list and ready it to send
        """
        self.invite_button.click()
        time.sleep(2)
        # Extract and clean headers for the main section
        elements_to_check = [
            self.invite_user_header,
            self.first_name_text,
            self.firstname_input,
            self.email_text,
            self.email_input,
            self.last_name_text,
            self.lastname_input,
            self.send_invite_button,
            self.cancel_button
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        self.firstname_input.fill(user_name)
        self.lastname_input.fill(user_last_name)
        self.email_input.fill(user_email)
        # Click the invite button and verify success
        self.send_invite_button.click()
        time.sleep(4)  # Wait for the action to complete
        expect(self.success_message).to_be_visible()
        message_text = self.success_message.text_content()
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
            self.active_and_inactive_action_button,
            self.delete_action_button
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
            self.active_and_inactive_action_button.click()
            self.success_message.wait_for(state="visible")
            expect(self.success_message).to_be_visible()
            success_message = self.success_message.text_content()
            print(success_message)
            assert success_message == "User Inactivate"
            time.sleep(3)
            new_status = user_status_element.text_content()
            assert (
                    "Inactive" in new_status
            ), f"Expected status to be 'Inactive', but got {new_status}"
            print("Status changed to 'Suspected' successfully.")
        if "Inactive" in current_status:
            self.active_and_inactive_action_button.click()
            self.success_message.wait_for(state="visible")
            expect(self.success_message).to_be_visible()
            success_message = self.success_message.text_content()
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
        title="Verify user information content",
        expected="user information content box should need to contains related user information",
    )
    def verify_user_information_content(self):
        """
        Verify user information component
        """
        elements_to_check = [
            self.user_information_component,
            self.user_information_title,
            self.details_title,
            self.user_image,
            self.user_name,
            self.first_name,
            self.last_name,
            self.email,
            self.phone_number,
            self.status,
            self.account_type,
            self.edit_user_button,
            self.user_controls_component,
            self.user_controls_title,
            self.close_button,
            self.reset_password_button,
            self.change_deployment,
            self.active_and_inactive_user_button,
            self.change_account_type

        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("user information component elements verified")
