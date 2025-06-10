"""
System Admin Users page modules
"""

import re
import time

from playwright.sync_api import Page, expect
from qase.pytest import qase
from utilities.decorators import qase_screenshot


class SystemAdminUsersPage:
    """
    Module containing objects and methods related to System Admin Users Page
    """

    def __init__(self, page: Page):
        super().__init__()
        self.page = page

        # System admin users page locators
        self.users_icon = page.locator('(//span[@class="nav-link-icon"])[2]')
        self.users_tab = '//span[text()="<<side_navigation_tabs>>"]'

        # Users list Filters locators
        self.filter_title = page.locator('//label[normalize-space()="Filter:"]')
        #self.filter_drop_down = '(//select[@class="generic-filter-select ms-2 form-select form-select-sm"])'
        #self.filter_drop_down = '//select[@class="generic-filter-select ms-2 form-select form-select-sm"]'
        #self.filter_drop_down = "select.generic-filter-select.ms-2.form-select.form-select-sm"
        dropdown_selector = '//select[@class="generic-filter-select ms-2 form-select form-select-sm"]'

        self.dropdown = page.locator(
            '(//div[@class="d-flex align-items-center"][1]//select)[1]'
        )
        self.all_users_status = '//div[contains(@class, "badge-soft-success") or contains(@class, "badge-soft-danger")]'
        self.batch_action_title = page.locator('//label[text()="Batch Action"]')
        self.user_checkbox = page.locator('(//tr//input[@type="checkbox"])[2]')
        self.batch_action_dropdown = page.locator(
            '(//div[@class="d-flex align-items-center"]//select)[2]'
        )
        self. batch_action_dropdown_locator = page.locator("//select[@class='form-control form-select form-select-sm']")
        self.apply_batch_action_button = page.locator('//button[text()="Apply Action"]')
        self.toggle_all_rows_selected = page.locator("//input[contains(@title,'Toggle All Rows Selected')]")
        self.invite_button = page.locator('//button[text()="Invite"]')
        self.user_page_header_component = page.locator('//div[@class="mb-2 card"]')
        self.user_page_list_component = page.locator('//div[@class="card"]')
        self.user_list_headers = page.locator('//tr[@class="text-center"]')
        self.user_page_footer = page.locator(
            '//div[@class="table-footer-border-top card-footer"]'
        )

        # invite user locators
        self.invite_user_header = page.locator('//div[text()="Invite User"]')
        self.first_name_text = page.locator('//label[text()="First Name"]')
        self.firstname_input = page.locator('[id="firstName"]')
        self.last_name_text = page.locator('//label[text()="Last Name"]')
        self.lastname_input = page.locator('[id="lastName"]')
        self.email_text = page.locator('//label[text()="Email"]')
        self.email_input = page.locator('[id="email"]')
        self.user_type_text = page.locator('//label[text()="User Type"]')
        self.user_type_dropdown = page.locator('//div[@class="col-lg-12"]//select')
        self.send_invite_button = page.locator('//button[normalize-space()="Send Invite"]')
        self.cancel_button = page.locator('//button[text()="Cancel"]')
        self.close_button = page.locator('//button[@class="btn-close"]')
        self.success_message = page.locator(
            '//div[@class="ant-message-notice-content"]'
        )
        self.warning_message = page.locator(
            '//div[@class="ant-message-custom-content ant-message-warning"]'
        )
        self.vendor_select_dropdown = page.locator(
            '//select[@id="vendorList"]'
        )
        self.deployment_dropdown = page.locator(
            '//select[@id="userType"]'
        )
        self.deployment_name_dropdown = page.locator("//div[@class='ant-select-selector']")
        self.select_deployment_name = page.locator("//div[contains(text(),'Development Deployment')]")
        self.select_deployment_admin = '//input[@role="combobox"]'
        self.button_to_change_action = page.locator(
            '(//div[@class="d-flex justify-content-center align-items-center"]//button)[1]'
        )
        self.user_id = page.locator("(//td)[3]")
        self.more_actions_button = page.locator(
            '(//div[@class="font-sans-serif btn-reveal-trigger dropend"])[1]'
        )
        self.delete_button = page.locator('//a[text()="Delete"]')
        self.confirm_button = page.locator('//button[text()="Confirm"]')
        self.confirm_message = page.locator('//div[@class="modal-body"]')
        self.user_infomation_box = page.locator(
            '//tr[@class="align-middle white-space-nowrap hover-actions-trigger btn-reveal-trigger hover-bg-100  undefined"][1]'
        )
        self.user_name = page.locator("(//td)[4]")
        self.edit_button = page.locator('//button[text()="Edit User"]')

    @qase_screenshot
    @qase.step(
        title="Verify available elements of vendors page",
        expected="All expected element should be visible on vendors page",
    )
    def verify_user_page_elements(self, headers_text):
        """
        Verify vendors page elements
        """
        # Verify visibility of various components on the vendors page
        elements_to_check = [
            self.user_page_header_component,
            self.user_page_footer,
            self.user_page_list_component,
            self.invite_button,
            self.apply_batch_action_button,
            self.toggle_all_rows_selected,
            self.batch_action_dropdown_locator,
            self.dropdown
        ]
        for element in elements_to_check:
            expect(element).to_be_visible()
            time.sleep(2)
        # Extract headers from the UI
        headers_title = self.user_list_headers.inner_text()
        # Clean up and split header_title
        cleaned_headers_title = re.sub(r"\s+", " ", headers_title).strip()
        headers_title_list = cleaned_headers_title.split(" ")
        # Combine split header parts (like 'Profile Image', 'Phone Number') into single elements
        headers_title_combined = [
            " ".join(headers_title_list[0:2]),
            headers_title_list[2],
            " ".join(headers_title_list[3:5]),
            headers_title_list[5],
            headers_title_list[6],
            " ".join(headers_title_list[7:9]),
            headers_title_list[9],
            headers_title_list[10],
        ]
        # Assert the headers match the expected values
        assert headers_title_combined == [
            item.strip() for item in headers_text
        ], "Headers do not match"

        # Click toggle_all_rows_selected
        self.toggle_all_rows_selected.click()
        # Wait for the Batch dropdown to be visible
        time.sleep(1)
        expect(self.batch_action_dropdown_locator).to_be_visible()
        self.batch_action_dropdown_locator.click()
        self.batch_action_dropdown_locator.select_option('Deactivate')
        selected_text = self.batch_action_dropdown_locator.locator("option:checked").inner_text()
        assert selected_text == "Deactivate", f"Expected 'Deactivate', but got '{selected_text}'"
        print("Verified :",selected_text)
        self.batch_action_dropdown_locator.click()
        self.batch_action_dropdown_locator.select_option('Activate')
        selected_text = self.batch_action_dropdown_locator.locator("option:checked").inner_text()
        assert selected_text == "Activate", f"Expected 'Activate', but got '{selected_text}'"
        print("Verified :", selected_text)
        self.batch_action_dropdown_locator.click()
        print("All element verified.")

    @qase_screenshot
    @qase.step(
        title="Verify and click on Users tab",
        expected="Verify Users tab icon and click on users tab",
    )
    def verify_and_click_on_users_tab(self, side_navigation_item):
        """
        Verify Users and click on users tab
        """
        # verify icon availability
        expect(self.users_icon).to_be_visible()
        # clicking on users tab
        self.page.click(
            self.users_tab.replace("<<side_navigation_tabs>>", side_navigation_item)
        )
        print(f"successfully able to click on {side_navigation_item} tab")

    @qase_screenshot
    @qase.step(
        title="Verify filter field title and available filters options",
        expected="Filter option should be visible with all available options",
    )
    # def verify_filters_field_and_filter_options(self,available_filter_options):
    #     """
    #     Verify all available filter options
    #     """
    #     expect(self.filter_title).to_be_visible()
    #     # Query all filter option elements
    #     filter_options = self.page.query_selector_all(self.filter_drop_down)
    #     # Extract text content from each option element
    #     filter_options_text = [option.inner_text() for option in filter_options]
    #     if len(filter_options_text) == 1 and "\n" in filter_options_text[0]:
    #         filter_options_text = filter_options_text[0].split("\n")
    #
    #     print(f"Available filter options are: {filter_options_text}")
    #     # Assert that the extracted text matches the expected filter options
    #     assert (
    #             filter_options_text == available_filter_options
    #     ), f"Expected: {available_filter_options}, but got: {filter_options_text}"
    #
    # # Assert that the extracted text matches the expected filter options
    def verify_filters_field_and_filter_options(self, available_filter_options):
        """
        Verify all available filter options in the filter dropdown.
        """
        expect(self.filter_title).to_be_visible()

        # Select all <option> elements inside the dropdown (assuming filter_drop_down is the selector for <select>)
        filter_options = self.page.query_selector_all(self.filter_drop_down + " option")

        # Extract text content from each option element
        filter_options_text = [option.inner_text().strip() for option in filter_options]

        print(f"Available filter options are: {filter_options_text}")

        # Assert that the extracted text matches the expected filter options
        assert filter_options_text == available_filter_options, \
            f"Expected: {available_filter_options}, but got: {filter_options_text}"

    @qase_screenshot
    @qase.step(
        title="Verify User is able to se only filtered data",
        expected="User should be able to see data according to applied filters",
    )
    def apply_filters_and_verify_filtered_data(self, available_filter_options, expected_statuses):
        """
        Verify data visible based on the applied filter.
        """
        dropdown_selector = "your-dropdown-selector"  # Replace with actual selector

        for filter_option in available_filter_options:
            # Debugging step: Pause execution and inspect elements
            self.page.pause()

            # Ensure the dropdown exists in the DOM
            dropdown = self.page.locator(dropdown_selector)
            assert dropdown.count() > 0, "Dropdown not found. Check the selector!"

            # Ensure the dropdown is visible
            dropdown.wait_for(state="visible", timeout=60000)

            # Ensure dropdown is enabled
            self.page.wait_for_function(
                f"document.querySelector('{dropdown_selector}') !== null && "
                f"!document.querySelector('{dropdown_selector}').disabled"
            )

            # Select the option
            self.dropdown.select_option(filter_option)

            # Wait for the filtered results to be displayed
            self.page.wait_for_selector(self.all_users_status, state="visible", timeout=60000)

            # Query for the status elements after applying the filter
            all_users_status = self.page.query_selector_all(self.all_users_status)
            all_users_status_text = [status.inner_text() for status in all_users_status]

            # Print the text of each status
            print(f"Users status after applying '{filter_option}': {all_users_status_text}")

            # Assertion to verify the expected statuses are present
            if filter_option in expected_statuses:
                expected = expected_statuses[filter_option]
                if expected:
                    for expected_status in expected:
                        assert expected_status in all_users_status_text, \
                            f"'{expected_status}' not found in the status text for filter '{filter_option}'"
                else:
                    # If there are no expected statuses, assert that the status list is empty
                    assert not all_users_status_text, \
                        f"Expected no statuses for filter '{filter_option}', but found: {all_users_status_text}"

    @qase_screenshot
    @qase.step(
        title="Verify Batch action functionality on user list page",
        expected="User should be able to apply batch actions on selected users",
    )
    def apply_batch_actions_to_users_list(self):
        """
        Apply batch action to user list
        """
        expect(self.batch_action_title).to_be_visible()
        user_status_element = self.page.locator(
            "(//div[contains(@class, 'badge-soft-success') or contains(@class, 'badge-soft-danger')])[1]"
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
                "Suspected" in new_status
            ), f"Expected status to be 'Suspected', but got {new_status}"
            print("Status changed to 'Suspected' successfully.")
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
        title="Verify Invite users functionality",
        expected="system admin should be able to invite all other users",
    )
    def verify_and_invite_system_admin_and_sender_functionality(
        self, first_name, last_name, email, user_types
    ):
        """
        Verify invite user functionality
        """
        invite_form_element_to_check = [
            self.first_name_text,
            self.last_name_text,
            self.email_input,
            self.user_type_text,
            self.send_invite_button,
            self.cancel_button,
            self.close_button,
        ]
        # Loop through user types and fill the invite form for each type
        for user_type in user_types:
            # Click the invite button to show the invite form
            self.invite_button.click()
            # Verify all elements are visible after clicking the invite button
            for element in invite_form_element_to_check:
                expect(element).to_be_visible()
            # Fill the form and send the invite
            self.firstname_input.fill(first_name)
            print(f"Invited user's firstname: {first_name}")
            self.lastname_input.fill(last_name)
            print(f"Invited user's lastname: {last_name}")
            self.email_input.fill(email)
            print(f"Invited user's email: {email}")
            self.user_type_dropdown.select_option(user_type)
            self.send_invite_button.click()
            # Verify the success message is visible
            self.success_message.wait_for(state="visible")
            expect(self.success_message).to_be_visible()

    @qase_screenshot
    @qase.step(
        title="Verify & Invite deployment admin",
        expected="system admin should be able to invite deployment admin",
    )
    def invite_deployment_admin(
        self, first_name, last_name, email, user_type, deployment_name
    ):
        """
        Verify  and invite deployment admin
        """
        self.invite_button.click()
        invite_form_element_to_check = [
            self.first_name_text,
            self.last_name_text,
            self.email_input,
            self.user_type_text,
            self.send_invite_button,
            self.cancel_button,
            self.close_button,
        ]
        # Verify all elements are visible after clicking the invite button
        for element in invite_form_element_to_check:
            expect(element).to_be_visible()
        # Fill the form and send the invite
        self.firstname_input.fill(first_name)
        print(f"Invited user's firstname: {first_name}")
        self.lastname_input.fill(last_name)
        print(f"Invited user's lastname: {last_name}")
        self.email_input.fill(email)
        print(f"Invited user's email: {email}")
        self.user_type_dropdown.select_option(user_type)
        print(f"Invited user's Deployment Admin: {user_type}")

        # Select deployment
        self.deployment_name_dropdown.wait_for(state="visible")
        self.deployment_name_dropdown.click()
        self.page.click(f"//div[contains(text(),'{deployment_name}')]")
        print(f"Invite user's Deployment_name selected: '{deployment_name}'")
        self.send_invite_button.click()

        # Verify the success message is visible
        self.success_message.wait_for(state="visible")
        expect(self.success_message).to_be_visible()
        success_message = self.success_message.text_content()

        assert success_message == "Invitation Sent Successfully"

    @qase_screenshot
    @qase.step(
        title="Verify & Invite vendor",
        expected="system admin should be able to invite vendor",
    )
    def invite_vendor(self, first_name, last_name, email, user_type_select,vendor_to_select):
        """
        Verify  and invite vendor
        """
        self.invite_button.click()
        invite_form_element_to_check = [
            self.first_name_text,
            self.last_name_text,
            self.email_input,
            self.user_type_text,
            self.send_invite_button,
            self.cancel_button,
            self.close_button,
        ]
        for element in invite_form_element_to_check:
            expect(element).to_be_visible()
        # Fill the form and send the invite
        self.firstname_input.fill(first_name)
        print(f"Invited user's firstname: {first_name}")
        self.lastname_input.fill(last_name)
        print(f"Invited user's lastname: {last_name}")
        self.email_input.fill(email)
        print(f"Invited user's email: {email}")
        time.sleep(5)
        self.user_type_dropdown.select_option(user_type_select)
        print(f"Invited user's user_type: {user_type_select}")
        time.sleep(10)
        self.vendor_select_dropdown.click()
        time.sleep(5)
        self.vendor_select_dropdown.select_option(vendor_to_select)
        time.sleep(4)
        self.send_invite_button.click()
        time.sleep(4)
        # Verify the success message is visible
        self.success_message.wait_for(state="visible")
        expect(self.success_message).to_be_visible()
        success_message = self.success_message.text_content()
        assert success_message == "Invitation Sent Successfully"

    @qase_screenshot
    @qase.step(
        title="Make a change in user status from actions",
        expected="system admin should be able to changes users status from actions",
    )
    def suspend_and_active_user_from_actions(self):
        """
        make user active and suspend from the actions
        """
        user_status_element = self.page.locator(
            "(//div[contains(@class, 'badge-soft-success') or contains(@class, 'badge-soft-danger')])[1]"
        )
        current_status = user_status_element.text_content()
        print(f"Current status is: {current_status}")
        if "Active" in current_status:
            self.button_to_change_action.click()
            time.sleep(2)
            new_status = user_status_element.text_content()
            assert (
                "Suspended" in new_status
            ), f"Expected status to be 'Suspended', but got {new_status}"
            print("Status changed to 'Suspected' successfully.")
            self.success_message.wait_for(state="visible")
            expect(self.success_message).to_be_visible()
            success_message = self.success_message.text_content()
            print(success_message)
            assert success_message == "User Suspended"
        if "Suspended" in current_status:
            self.button_to_change_action.click()
            time.sleep(2)
            new_status = user_status_element.text_content()
            assert (
                "Active" in new_status
            ), f"Expected status to be 'Active', but got {new_status}"
            print("Status changed back to 'Active' successfully.")
            self.success_message.wait_for(state="visible")
            expect(self.success_message).to_be_visible()
            success_message = self.success_message.text_content()
            print(success_message)
            assert success_message == "User Activated"

    @qase_screenshot
    @qase.step(
        title="delete user from the list",
        expected="system admin should be able to delete any users",
    )
    def delete_user_from_list(self):
        """
        system admin is able to delete any user
        """
        time.sleep(5)
        user_id = self.user_id.text_content()
        print(f"user id: {user_id}")
        self.more_actions_button.click()
        self.delete_button.click()
        confirm_message = self.confirm_message.text_content()
        assert confirm_message == "Are you sure you want to delete this record?"
        self.confirm_button.click()
        time.sleep(2)
        user_id_2 = self.user_id.text_content()
        assert user_id != user_id_2
        self.warning_message.wait_for(state="visible")
        expect(self.warning_message).to_be_visible()
        warning_message = self.warning_message.text_content()
        print(warning_message)
        assert warning_message == "User Deleted"
