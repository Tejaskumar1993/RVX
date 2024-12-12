"""
System Admin Vendors page modules
"""

import re
import time

from playwright.sync_api import Page, expect
from qase.pytest import qase
from utilities.decorators import qase_screenshot


class SystemAdminVendorsPage:
    """
    Module containing objects and methods related to System Admin Vendors Page
    """

    def __init__(self, page: Page):
        super().__init__()
        self.page = page

        # System admin vendors page locators
        self.vendors_icon = page.locator('(//span[@class="nav-link-icon"])[4]')
        self.vendors_tab = '//span[text()="<<side_navigation_tabs>>"]'

        # Vendors list Filters locators
        self.filter_title = page.locator('//div[text()="Filter:"]')
        self.filter_drop_down = '//select[@class="generic-filter-select ms-2 form-select form-select-sm"]//option'
        self.dropdown = page.locator(
            '(//div[@class="d-flex align-items-center"][1]//select)[1]'
        )
        self.all_vendors_status = '//div[contains(@class, "soft-primary btn-outline rounded-pill") or contains(@class, "soft-danger btn-outline rounded-pill")]'
        self.batch_action_title = page.locator('//label[text()="Batch Action"]')
        self.vendors_checkbox = page.locator('(//tr//input[@type="checkbox"])[2]')
        self.batch_action_dropdown = page.locator(
            '(//div[@class="d-flex align-items-center"]//select)[2]'
        )
        self.apply_batch_action_button = page.locator('//button[text()="Apply Action"]')
        self.add_vendor_button = page.locator('//button[text()="Add Vendor"]')
        self.vendors_page_header_component = page.locator('//div[@class="mb-2 card"]')
        self.vendors_page_list_component = page.locator('//div[@class="card"]')
        self.vendors_list_headers = page.locator('//tr[@class="text-center"]')
        self.vendors_page_footer = page.locator(
            '//div[@class="table-footer-border-top card-footer"]'
        )
        self.success_message = page.locator(
            '//div[@class="ant-message-custom-content ant-message-success"]'
        )

        # add vendor page locators
        self.add_vendor_component = page.locator('//div[@class="modal-content"]')
        self.add_vendor_title = page.locator('//div[text()="Add Vendor"]')
        self.vendor_image_title = page.locator('//label[text()="Vendor Image"]')
        self.name_header = page.locator('//label[text()="Name"]')
        self.name_input = page.locator('//input[@id="name"]')
        self.email_header = page.locator('//label[text()="Email"]')
        self.email_input = page.locator('//input[@id="email"]')
        self.address_line1_header = page.locator('//label[text()="Address Line 1"]')
        self.address_line1_input = page.locator('//input[@id="addressLine1"]')
        self.address_line2_header = page.locator('//label[text()="Address Line 2"]')
        self.address_line2_input = page.locator('//input[@id="addressLine2"]')
        self.city_header = page.locator('//label[text()="City"]')
        self.city_input = page.locator('//input[@id="city"]')
        self.state_header = page.locator('//label[text()="State"]')
        self.select_state_drop_down = page.locator('//div[@class="col-lg-4"]//select')
        self.zip_code_header = page.locator('//label[text()="Zip Code"]')
        self.zip_code_input = page.locator('//input[@id="zip"]')
        self.phone_header = page.locator('//div[text()="Phone"]')
        self.phone_number_input = page.locator(
            '//input[@class="form-control vendor-phone-input"]'
        )
        self.select_company_header = page.locator('//label[text()="Select Company"]')
        self.select_company_dropdown = page.locator(
            '//input[@class="ant-select-selection-search-input"]'
        )
        self.select_company_option = page.locator(
            '(//div[@class="ant-select-item-option-content"])[2]'
        )
        self.select_vendor_header = page.locator('//label[text()="Select Vendor"]')
        self.select_vendor_option = page.locator('//div[@class="col-lg-12"]//select')
        self.add_vendor = page.locator(
            '//div[@class="mt-2 text-end"]//button[text()="Add Vendor"]'
        )
        self.success_message_vendor = page.locator(
            '//div[@class="ant-message-notice-content"]'
        )
        self.active_inactive_action = page.locator(
            '(//*[@data-icon="lock" or @data-icon="lock-open"])[1]'
        )
        self.vendor_status = page.locator(
            "(//div[contains(@class, 'badge-soft-primary') or contains(@class, 'badge-soft-danger')])[1]"
        )
        self.more_info_button = page.locator('(//*[@data-icon="ellipsis"])[1]')
        self.manage_button = page.locator('//a[text()="Manage"]')
        self.delete_button = page.locator('//a[text()="Delete"]')

        # vendor information locators
        self.vendor_information_model = page.locator('//div[@class="modal-content"]')
        self.vendor_information_header = page.locator(
            '//div[text()="Vendor Information"]'
        )
        self.vendor_information_tab = page.locator(
            '//button[@id="vendor-information-tab-tab-vendorInfo"]'
        )
        self.orders_tab = page.locator(
            '//button[@id="vendor-information-tab-tab-orders"]'
        )
        self.products_tab = page.locator(
            '//button[@id="vendor-information-tab-tab-products"]'
        )
        self.users_tab = page.locator(
            '//button[@id="vendor-information-tab-tab-users"]'
        )
        self.vendor_company_name = page.locator('//div//h6[text()="Company Name"]')
        self.vendor_phone_number = page.locator('//div//h6[text()="Phone Number"]')
        self.vendor_email = page.locator('//div//h6[text()="Email"]')
        self.vendor_control_header = page.locator('//div//h5[text()="Vendor Controls"]')
        self.suspend_vendor_button = page.locator('//button[text()="Suspend Vendor"]')
        self.invite_vendor_button = page.locator('//button[text()="Invite Vendor"]')
        self.view_dashboard_button = page.locator('//button[text()="View Dashboard"]')
        self.delete_vendor_button = page.locator('//button[text()="Delete Vendor"]')
        self.orders_tab_header = page.locator(
            '//div[@id="vendor-information-tab-tabpane-orders"]//thead'
        )
        self.orders_tab_footer = page.locator(
            '//div[@id="vendor-information-tab-tabpane-orders"]//div[@class="table-footer-border-top card-footer"]'
        )
        self.products_tab_footer = page.locator(
            '//div[@id="vendor-information-tab-tabpane-products"]//div[@class="table-footer-border-top card-footer"]'
        )
        self.products_tab_header = page.locator(
            '//div[@id="vendor-information-tab-tabpane-products"]//thead'
        )
        self.users_tab_header = page.locator(
            '//div[@id="vendor-information-tab-tabpane-users"]//thead'
        )
        self.users_tab_footer = page.locator(
            '//div[@id="vendor-information-tab-tabpane-users"]//div[@class="table-footer-border-top card-footer"]'
        )

    @qase_screenshot
    @qase.step(
        title="Verify and click on Vendors tab",
        expected="Verify Vendors tab icon and click onVendors tab",
    )
    def verify_and_click_on_vendors_tab(self, side_navigation_item):
        """
        Verify Vendors and click on Vendors tab
        """
        # verify icon availability
        expect(self.vendors_icon).to_be_visible()
        # clicking on vendors tab
        self.page.click(
            self.vendors_tab.replace("<<side_navigation_tabs>>", side_navigation_item)
        )
        print(f"successfully able to click on {side_navigation_item} tab")

    @qase_screenshot
    @qase.step(
        title="Verify available elements of vendors page",
        expected="All expected element should be visible on vendors page",
    )
    def verify_vendors_page_elements(self, headers_text):
        """
        Verify vendors page elements
        """
        # Verify visibility of various components on the vendors page
        elements_to_check = [
            self.vendors_page_header_component,
            self.vendors_page_footer,
            self.vendors_page_list_component,
            self.add_vendor_button,
            self.apply_batch_action_button,
            self.batch_action_dropdown,
            self.dropdown,
        ]
        for element in elements_to_check:
            expect(element).to_be_visible()
        # Extract headers from the UI
        headers_title = self.vendors_list_headers.inner_text()
        print("Headers titles before cleanup -->", headers_title)
        cleaned_headers_title = re.sub(
            r"[🔼🔽]", "", headers_title
        ).strip()  # Remove sorting icons
        # Split the headers on tabs or multiple spaces
        headers_list = re.split(r"[\t]+|\s{2,}", cleaned_headers_title)
        headers_list = [
            header.strip() for header in headers_list if header
        ]  # Remove empty items
        # Assert the headers match the expected values
        assert (
            headers_list == headers_text
        ), f"Headers do not match: {headers_list} != {headers_text}"
        print("All elements verified")

    @qase_screenshot
    @qase.step(
        title="Verify filter field title and available filters options",
        expected="Filter option should be visible with all available options",
    )
    def verify_filters_field_and_filter_options(self, available_filter_options):
        """
        Verify all available filters options
        """
        expect(self.filter_title).to_be_visible()
        # Query all filter option elements
        filter_options = self.page.query_selector_all(self.filter_drop_down)
        # Extract text content from each option element
        filter_options_text = [option.inner_text() for option in filter_options]
        print(f"Available filter options are: {filter_options_text}")
        # Assert that the extracted text matches the expected filter options
        assert (
            filter_options_text == available_filter_options
        ), f"Expected: {available_filter_options}, but got: {filter_options_text}"

    @qase_screenshot
    @qase.step(
        title="Verify vendors is able to se only filtered data",
        expected="vendors should be able to see data according to applied filters",
    )
    def apply_filters_and_verify_filtered_data(
        self, available_filter_options, expected_statuses
    ):
        """
        Verify data visible based on the applied filter
        """
        for filter_option in available_filter_options:
            self.dropdown.select_option(filter_option)
            self.page.wait_for_selector(self.all_vendors_status)
            # Query for the status elements after applying the filter
            all_vendors_status = self.page.query_selector_all(self.all_vendors_status)
            all_vendors_status_text = [
                status.inner_text() for status in all_vendors_status
            ]
            # Print the text of each status
            print(
                f"Users status after applying '{filter_option}': {all_vendors_status_text}"
            )
            # Assertion to verify the expected statuses are present
            if filter_option in expected_statuses:
                expected = expected_statuses[filter_option]
                if expected:
                    for expected_status in expected:
                        assert (
                            expected_status in all_vendors_status_text
                        ), f"'{expected_status}' not found in the status text for filter '{filter_option}'"
                else:
                    # If there are no expected statuses, assert that the status list is empty
                    assert (
                        not all_vendors_status_text
                    ), f"Expected no statuses for filter '{filter_option}', but found: {all_vendors_status_text}"

    @qase_screenshot
    @qase.step(
        title="Verify Batch action functionality on vendors list page",
        expected="vendors should be able to apply batch actions on selected vendors",
    )
    def apply_batch_actions_to_vendors_list(self, success_message_text):
        """
        Apply batch action to vendors list
        """
        expect(self.batch_action_title).to_be_visible()
        vendors_status_element = self.page.locator(
            "(//div[contains(@class, 'badge-soft-primary') or contains(@class, 'badge-soft-danger')])[1]"
        )
        current_status = vendors_status_element.text_content()
        print(f"Current status is: {current_status}")
        # Apply batch actions based on the current status
        if "Active" in current_status:
            self.vendors_checkbox.click()
            self.batch_action_dropdown.select_option("Suspend")
            self.apply_batch_action_button.click()
            success_message = self.success_message.text_content()
            assert (
                success_message in success_message_text
            ), f"Unexpected success message: {success_message}"
            time.sleep(3)
            new_status = vendors_status_element.text_content()
            assert (
                "Inactive" in new_status
            ), f"Expected status to be 'Inactive', but got {new_status}"
            print("Status changed to 'Inactive' successfully.")

            # Now change the status back to 'Active'
            self.vendors_checkbox.click()
            self.batch_action_dropdown.select_option("Activate")
            self.apply_batch_action_button.click()
            success_message = self.success_message.text_content()
            assert (
                success_message in success_message_text
            ), f"Unexpected success message: {success_message}"
            time.sleep(3)
            inactive_reverted_status = vendors_status_element.text_content()
            assert (
                "Active" in inactive_reverted_status
            ), f"Expected status to be 'Active', but got {inactive_reverted_status}"
            print("Status reverted to 'Active' successfully.")

        elif "Inactive" in current_status:
            self.vendors_checkbox.click()
            self.batch_action_dropdown.select_option("Activate")
            self.apply_batch_action_button.click()
            success_message = self.success_message.text_content()
            assert (
                success_message in success_message_text
            ), f"Unexpected success message: {success_message}"
            time.sleep(3)
            active_reverted_status = vendors_status_element.text_content()
            assert (
                "Active" in active_reverted_status
            ), f"Expected status to be 'Active', but got {active_reverted_status}"
            print("Status changed back to 'Active' successfully.")

    @qase_screenshot
    @qase.step(
        title="Verify add new vendor functionality on vendors list page",
        expected="System admin should be able to add new vendor to the selected vendors list.",
    )
    def add_new_vendor_in_vendors_list(
        self,
        success_message_text,
        vendor_name,
        vendor_email,
        vendor_addressline_1,
        vendor_addressline_2,
        vendor_city,
        state_to_select,
        zipcode,
        phone_number,
        select_vendor,
    ):
        """
        Adds a new vendor to the vendor list and verifies success message.
        """
        expect(self.add_vendor_button).to_be_visible()
        self.add_vendor_button.click()

        # Define elements to check visibility
        required_elements = [
            self.add_vendor_component,
            self.add_vendor_title,
            self.vendor_image_title,
            self.name_input,
            self.name_header,
            self.email_header,
            self.email_input,
            self.address_line1_header,
            self.address_line1_input,
            self.address_line2_header,
            self.city_header,
            self.city_input,
            self.state_header,
            self.zip_code_header,
            self.zip_code_input,
            self.phone_header,
            self.phone_number_input,
            self.select_company_header,
            self.select_vendor_header,
            self.add_vendor,
        ]

        for element in required_elements:
            expect(element).to_be_visible()

        # Fill in vendor details
        self.name_input.fill(vendor_name)
        self.email_input.fill(vendor_email)
        self.address_line1_input.fill(vendor_addressline_1)
        self.address_line2_input.fill(vendor_addressline_2)
        self.city_input.fill(vendor_city)
        self.select_state_drop_down.select_option(state_to_select)
        self.zip_code_input.fill(zipcode)
        self.phone_number_input.fill(phone_number)
        self.select_company_dropdown.click()
        self.select_company_option.click()
        self.select_vendor_option.select_option(select_vendor)

        # Submit and verify success
        self.add_vendor.click()
        actual_success_message = self.success_message_vendor.text_content()
        assert actual_success_message == success_message_text, (
            f"Expected success message '{success_message_text}', "
            f"but got '{actual_success_message}'."
        )

    @qase_screenshot
    @qase.step(
        title="Verify and check active and inactive feature from the actions",
        expected="system admin should be able active or inactive any vendor from the actions",
    )
    def verify_active_and_inactive_functionality_from_action(
        self, updated_vendor_message_text
    ):
        """
        Verify and check active and inactive functionality from the actions.
        """
        # Get the current status of the vendor
        initial_status = self.vendor_status.text_content()
        # Click on the action button to toggle status
        self.active_inactive_action.click()
        # Verify the success message text matches the expected value
        message_text = self.success_message.text_content()
        assert (
            message_text in updated_vendor_message_text
        ), f"Expected message '{updated_vendor_message_text}' but got '{message_text}'"
        time.sleep(5)
        # Check if the status has been updated
        updated_status = self.vendor_status.text_content()
        assert (
            initial_status != updated_status
        ), f"Status did not change. Initial: {initial_status}, Updated: {updated_status}"
        # Revert the status back to the original if needed
        if updated_status == "Inactive":
            self.active_inactive_action.click()

    @qase_screenshot
    @qase.step(
        title="Verify and check manage and delete feature from the actions",
        expected="system admin should be able manage and delete any vendor from the actions",
    )
    def verify_manage_and_delete_functionality_from_action(
        self, orders_headers_text, products_headers_text, users_headers_text
    ):
        """
        Verify and check manage and delete features from the actions
        """
        def validate_headers(tab, header_element, expected_headers):
            tab.click()
            time.sleep(3)
            raw_headers = header_element.inner_text()
            print("Raw headers title -->", repr(raw_headers))
            cleaned_headers = re.sub(r"[🔼🔽]", "", raw_headers).strip()
            cleaned_headers = re.sub(
                r"([a-z])([A-Z])", r"\1 \2", cleaned_headers
            )  # Handle camel case
            cleaned_headers = re.sub(
                r"Current Orders", "Current_Orders", cleaned_headers
            )
            headers_list = re.split(r"[\t]+|\s{2,}", cleaned_headers)
            headers_list = [header.strip() for header in headers_list if header]
            headers_list = [
                header.replace("Current_Orders", "Current Orders")
                for header in headers_list
            ]
            print("Final headers list -->", headers_list)
            assert (
                headers_list == expected_headers
            ), f"Headers do not match: {headers_list} != {expected_headers}"

        expect(self.more_info_button).to_be_visible()
        self.more_info_button.click()
        expect(self.manage_button).to_be_visible()
        expect(self.delete_button).to_be_visible()
        self.manage_button.click()
        elements_to_check = [
            self.vendor_information_model,
            self.vendor_information_header,
            self.vendor_information_tab,
            self.vendor_company_name,
            self.vendor_phone_number,
            self.vendor_email,
            self.vendor_control_header,
            self.suspend_vendor_button,
            self.invite_vendor_button,
            self.view_dashboard_button,
            self.delete_vendor_button,
            self.orders_tab,
            self.products_tab,
            self.users_tab,
        ]
        for element in elements_to_check:
            expect(element).to_be_visible()
        validate_headers(self.orders_tab, self.orders_tab_header, orders_headers_text)
        expect(self.orders_tab_footer).to_be_visible()
        validate_headers(
            self.products_tab, self.products_tab_header, products_headers_text
        )
        expect(self.products_tab_footer).to_be_visible()
        validate_headers(self.users_tab, self.users_tab_header, users_headers_text)
