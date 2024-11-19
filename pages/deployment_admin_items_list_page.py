"""
deployment admin items list page modules
"""

import re
import time

from playwright.sync_api import Page, expect
from qase.pytest import qase
from utilities.decorators import qase_screenshot


class DeploymentAdminitemsListPage:
    """
    Module containing objects and methods related to Deployment Admin items list Page
    """

    def __init__(self, page: Page):
        super().__init__()
        self.page = page

        self.change_role_dropdown = page.locator('(//button[@id="dropdown-flags"])[2]')
        self.role_to_select = '//a[text()="<<role_to_change>>"]'
        self.select_tab_from_side_navigation = '//span[text()="<<tab_to_navigate>>"]'
        self.items_list_icon = page.locator(
            '//span[text()="Items List"]//..//span[@class="nav-link-icon"]'
        )
        self.batch_action_title = page.locator('//label[text()="Batch Action"]')
        self.batch_action_dropdown = page.locator(
            '//div[@class="d-flex align-items-center"]//select'
        )
        self.items_list_filter_label = page.locator('//label[text()="Filter:"]')
        self.item_list_filter_dropdown = page.locator(
            '//select[@class="form-select form-select-sm"]'
        )
        self.item_list_filters_options = (
            '//select[@class="form-select form-select-sm"]//option'
        )
        self.item_list_filter = page.locator(
            '//div[@class="d-flex align-items-center justify-content-between"]//select'
        )
        self.all_items_status = '//div[contains(@class, "me-2 badge badge-soft-primary btn-outline rounded-pill") or contains(@class, "badge-soft-danger")]'
        self.items_list_headers = page.locator('//tr[@class="text-center"]')
        self.items_page_list_component = page.locator('//div[@class="card"]')
        self.items_page_footer = page.locator(
            '//div[@class="table-footer-border-top card-footer"]'
        )
        self.apply_batch_action_button = page.locator('//button[text()="Apply Action"]')
        self.add_item_button = page.locator('//button[text()="Add Item"]')
        self.footer_pagination = page.locator(
            '//div[@class="d-flex pagination-numbers"]'
        )
        self.row_per_page = page.locator(
            '//div[@class="d-flex align-items-center fs--1 ps-3"]'
        )
        self.result_counter = page.locator(
            '//div[@class="d-flex align-items-center fs--1 ps-3 d-flex flex-wrap rows-page-count"]'
        )
        self.display_item_name = page.locator("(//td)[4]")
        self.item_checkbox = page.locator('(//tr//input[@type="checkbox"])[2]')

        # add item page locators
        self.add_item_item_checkbox = page.locator(
            '(//div[@class="modal-content"]//td//input[@type="checkbox"])[1]'
        )
        self.add_item_apply_batch_action_button = page.locator(
            '(//button[text()="Apply Action"])[2]'
        )
        self.item_details = page.locator(
            '((//div[@class="p-0 false card-body"])[2]//tr)[2]'
        )
        self.add_item_summary_dialog_box_component = page.locator(
            '(//div[@class="modal-content"])[2]'
        )
        self.item_information_component = page.locator(
            '(//div[@class="modal-content"])[1]'
        )
        self.summary_title = page.locator('//div[text()="Summary"]')
        self.summary_box_text = page.locator(
            '//div[text()="The following items will be added to your list of items available to send:"]'
        )
        self.summary_box_data_column_title = page.locator("(//thead)[3]")
        self.item_summary = page.locator('((//div[@class="modal-content"])[2]//tr)[2]')
        self.summary_cancel_button = page.locator('//button[text()="Cancel"]')
        self.summary_confirm_button = page.locator('//button[text()="Confirm"]')
        self.add_item_page_title = page.locator("(//thead)[2]")
        self.select_item = page.locator("(//tr)[2]")
        self.item_information_header = page.locator('//div[text()="Item Information"]')
        self.item_information_tabs = '//button[text()="<<tab_to_navigate>>"]'
        self.display_information_header = page.locator(
            '//h5[text()="Display Information"]'
        )
        self.display_information_component = page.locator(
            '(//div[@class="mt-4 card"])[1]'
        )
        self.display_thumbnail_header = page.locator('//p[text()="Display Thumbnail"]')
        self.display_name = page.locator('//p[text()="Display Name "]')
        self.display_gallery = page.locator('//p[text()="Display Gallery"]')
        self.edit_button = page.locator('//button[text()="Edit"]')
        self.vendor_info_modal_component = page.locator('//div[@class="p-3 card"]')
        self.company_name = page.locator('//h6[text()="Company Name"]')
        self.phone_number = page.locator('//h6[text()="Phone Number"]')
        self.email = page.locator('//h6[text()="Email"]')
        self.vendor_info_button = page.locator('//button[text()="Vendor More Info"]')
        self.item_control_component = page.locator(
            '//div[@class="mt-2 shadow-lg card"]'
        )
        self.item_control_header = page.locator('//h5[text()="Item Controls"]')
        self.active_item_button = page.locator('//button[text()="Activate Item"]')
        self.delete_item_button = page.locator('//button[text()="Delete Item"]')
        self.basic_information_component = page.locator(
            '(//div[@class="mt-4 card"])[2]'
        )
        self.basic_information_header = page.locator('//h5[text()="Basic Information"]')
        self.item_id = page.locator('//p[text()="ID"]')
        self.item_name = page.locator('//p[text()="Name"]')
        self.item_price = page.locator('//p[text()="Price"]')
        self.item_status = page.locator('//p[text()="Status"]')
        self.edit_action = page.locator('(//*[@data-icon="pen"])[1]')
        self.active_inactive_action = page.locator(
            '(//*[@data-icon="lock" and "lock-open"])[1]'
        )
        self.delete_icon = page.locator('(//*[@data-icon="trash"])[1]')
        self.send_order_headers = page.locator("(//thead)[2]")
        self.send_orders_components = page.locator(
            '//div[@id="item-information-tab-tabpane-sendOrders"]'
        )
        self.send_orders_page_footer = page.locator(
            '//div[@id="item-information-tab-tabpane-itemsInfo"]//..//div[@class="table-footer-border-top card-footer"]'
        )
        self.send_orders_row_per_page = page.locator(
            '//div[@id="item-information-tab-tabpane-itemsInfo"]//..//div//p[text()="Rows per page:"]'
        )
        self.send_orders_pagination = page.locator(
            '//div[@id="item-information-tab-tabpane-itemsInfo"]//..//div[@class="d-flex pagination-numbers"]'
        )
        self.send_orders_result_count = page.locator(
            '//div[@id="item-information-tab-tabpane-itemsInfo"]//..//span[@class="d-none d-sm-inline-block me-2"]'
        )

        # add item filter locators
        self.add_item_status = '//div[@class="modal-content"]//div[contains(@class, "me-2 badge badge-soft-primary btn-outline rounded-pill") or contains(@class, "badge-soft-danger")]'
        self.add_item_filter_label = page.locator(
            '//div[@class="modal-content"]//label[text()="Filter"]'
        )
        self.filter_option_to_select = page.locator(
            '(//div[@class="modal-content"]//select)[1]'
        )
        self.filter_dropdown = page.locator(
            '(//div[@class="modal-content"]//select[@class="form-select form-select-sm"])[1]'
        )
        self.filter_options = '(//div[@class="modal-content"]//select[@class="form-select form-select-sm"])[1]//option'
        self.close_button = page.locator('//button[@class="btn-close"]')
        self.single_item_status = page.locator("(//td)[6]")
        self.success_message = page.locator(
            '//div[@class="ant-message-custom-content ant-message-success"]'
        )

    @qase_screenshot
    @qase.step(
        title="click on user role dropdown and select role",
        expected="User should be able to change role successfully",
    )
    def click_on_dropdown_and_change_user_role(self, role_to_change):
        """
        Change user role from dropdown
        """
        self.change_role_dropdown.click()
        self.page.locator(
            self.role_to_select.replace("<<role_to_change>>", role_to_change)
        ).click()
        print(f"User role changed to {role_to_change}")

    @qase_screenshot
    @qase.step(
        title="Verify and click on items list tab",
        expected="User should be able to see items list icon and able to click on items list tab",
    )
    def verify_and_click_on_items_list_tab(self, side_navigation_item):
        """
        Verify Users and click on items list tab
        """
        # verify icon availability
        expect(self.items_list_icon).to_be_visible()
        # clicking on  items list tab
        self.page.click(
            self.select_tab_from_side_navigation.replace(
                "<<tab_to_navigate>>", side_navigation_item
            )
        )
        print(f"successfully able to click on {side_navigation_item} tab")

    @qase_screenshot
    @qase.step(
        title="Verify items list page elements",
        expected="User should be able to visible every elements of items lists page",
    )
    def verify_items_list_page_elements(self, headers_text):
        """
        Verify and check availability of items list page elements
        """
        elements_to_check = [
            self.items_list_filter_label,
            self.item_list_filter_dropdown,
            self.batch_action_title,
            self.apply_batch_action_button,
            self.add_item_button,
            self.items_list_headers,
            self.items_page_list_component,
            self.items_page_footer,
            self.footer_pagination,
            self.row_per_page,
            self.result_counter,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("items list page elements verified")
        # Extract headers from the UI
        headers_title = self.items_list_headers.inner_text()
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
        title="Apply filter on items list and verify filtered data",
        expected="Data should be filtered properly based on the applied filter.",
    )
    def apply_filter_on_items_list_and_verify_filtered_data(
        self, available_filter_options, expected_statuses
    ):
        """
        Apply filter on items list and verify filtered data
        """
        expect(self.item_list_filter_dropdown).to_be_visible()
        filter_options = self.page.query_selector_all(self.item_list_filters_options)
        filter_options_text = [option.inner_text() for option in filter_options]
        assert (
            filter_options_text == available_filter_options
        ), f"Expected: {available_filter_options}, but got: {filter_options_text}"
        print(f"all available filters verified: {available_filter_options}")
        for filter_option in available_filter_options:
            self.item_list_filter.select_option(filter_option)
            time.sleep(5)
            self.page.wait_for_selector(self.all_items_status)
            # Query for the status elements after applying the filter
            all_items_status = self.page.query_selector_all(self.all_items_status)
            all_items_status_text = [status.inner_text() for status in all_items_status]
            # Print the text of each status
            print(
                f"Items status after applying '{filter_option}': {all_items_status_text}"
            )
            # Assertion to verify the expected statuses are present
            if filter_option in expected_statuses:
                expected = expected_statuses[filter_option]
                if expected:
                    for expected_status in expected:
                        assert (
                            expected_status in all_items_status_text
                        ), f"'{expected_status}' not found in the status text for filter '{filter_option}'"
                else:
                    # If there are no expected statuses, assert that the status list is empty
                    assert (
                        not all_items_status_text
                    ), f"Expected no statuses for filter '{filter_option}', but found: {all_items_status_text}"

    @qase_screenshot
    @qase.step(
        title="Apply batch action on item and verify item status",
        expected="Status should be changed based on batch action",
    )
    def apply_batch_action_to_items(self):
        """
        Apply batch action on item and verify item status
        """
        expect(self.batch_action_title).to_be_visible()
        user_status_element = self.page.locator(
            '(//div[contains(@class, "me-2 badge badge-soft-primary btn-outline rounded-pill") or contains(@class, "badge-soft-danger")])[1]'
        )
        current_status = user_status_element.text_content()
        print(f"Current status is: {current_status}")
        # Verify the status is either 'Active' or 'Suspected'
        if "Active" in current_status:
            self.item_checkbox.click()
            self.batch_action_dropdown.select_option("Deactivate")
            self.apply_batch_action_button.click()
            time.sleep(2)
            new_status = user_status_element.text_content()
            assert (
                "Suspected" in new_status
            ), f"Expected status to be 'Deactivate', but got {new_status}"
            print("Status changed to 'Deactivate' successfully.")
            # Now change the status back to 'Active'
            self.item_checkbox.click()
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
            self.item_checkbox.click()
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
        title="Verify item information inside the item information pop-up",
        expected="Item information pop-up should be contained all the item details",
    )
    def verify_item_information_modal_content(self, tab_to_change, headers_text):
        """
        test item information modal content
        """
        time.sleep(5)
        expect(self.select_item).to_be_visible()
        self.select_item.click()
        time.sleep(2)
        # Step 2: Verify visibility of elements in the item information tab
        elements_to_be_visible = [
            self.item_information_component,
            self.item_information_header,
            self.display_information_component,
            self.display_information_header,
            self.display_thumbnail_header,
            self.display_name,
            self.display_gallery,
            self.basic_information_component,
            self.basic_information_header,
            self.item_id,
            self.item_price,
            self.item_name,
            self.item_status,
            self.edit_button,
            self.item_control_component,
            self.item_control_header,
            self.active_item_button,
            self.delete_item_button,
            self.company_name,
            self.phone_number,
            self.email,
            self.vendor_info_button,
            self.vendor_info_modal_component,
        ]
        for element in elements_to_be_visible:
            expect(element).to_be_visible()
        print("Item information tab elements verified successfully")

        # Step 3: Navigate to the specified tab
        tab_locator = self.page.locator(
            self.item_information_tabs.replace("<<tab_to_navigate>>", tab_to_change)
        )
        expect(tab_locator).to_be_visible()
        tab_locator.click()
        time.sleep(3)
        # Step 4: Verify header titles
        headers_title = self.send_order_headers.inner_text()
        cleaned_headers = re.sub(r"[🔼🔽]", "", headers_title).strip()
        # Split using either tabs or two or more spaces
        headers_list = [
            header.strip()
            for header in re.split(r"\t|\s{2,}", cleaned_headers)
            if header
        ]
        assert (
            headers_list == headers_text
        ), f"Headers do not match: {headers_list} != {headers_text}"
        # Step 5: Verify visibility of additional elements
        elements_go_check = [
            self.send_orders_components,
            self.send_orders_pagination,
            self.send_orders_page_footer,
            self.send_orders_result_count,
            self.send_orders_row_per_page,
        ]
        for element in elements_go_check:
            expect(element).to_be_visible()
        print("Send order components verified successfully")

    @qase_screenshot
    @qase.step(
        title="Add item to the user list",
        expected="user should be able to add item to the item list",
    )
    def add_item_to_user_list_and_make_it_ready_to_send(
        self, headers_text, headers_text_of_summary
    ):
        """
        add item to the user list and ready it to send
        """
        self.add_item_button.click()
        time.sleep(2)
        # Extract and clean headers for the main section
        headers_title = self.add_item_page_title.inner_text()
        print("Headers titles before cleanup -->", headers_title)
        headers_list = [
            header.strip()
            for header in re.split(
                r"[\t]+|\s{2,}", re.sub(r"[🔼🔽]", "", headers_title).strip()
            )
            if header
        ]
        assert (
            headers_list == headers_text
        ), f"Headers do not match: {headers_list} != {headers_text}"
        # Perform batch action
        self.add_item_item_checkbox.click()
        self.add_item_apply_batch_action_button.click()
        # Extract and clean headers for the summary section
        summary_headers_title = self.summary_box_data_column_title.inner_text()
        print("Summary Headers titles before cleanup -->", summary_headers_title)
        headers_list = [
            header.strip()
            for header in re.split(
                r"[\t]+|\s{2,}", re.sub(r"[🔼🔽]", "", summary_headers_title).strip()
            )
            if header
        ]
        assert (
            headers_list == headers_text_of_summary
        ), f"Summary headers do not match: {headers_list} != {headers_text_of_summary}"
        # Clean item details and summary, then verify
        cleaned_details = re.sub(r"</?p>", "", self.item_details.text_content())
        print(f"Cleaned Details: {cleaned_details}")
        cleaned_summary = re.sub(r"</?p>", "", self.item_summary.text_content())
        print(f"Cleaned Summary: {cleaned_summary}")
        assert (
            cleaned_details == cleaned_summary
        ), "Item details and summary details do not match"
        # Verify dialog box components
        expect(self.add_item_summary_dialog_box_component).to_be_visible()
        expect(self.summary_title).to_be_visible()
        expect(self.summary_box_text).to_be_visible()
        # Verify action buttons
        expect(self.summary_cancel_button).to_be_visible()
        expect(self.summary_confirm_button).to_be_visible()

    @qase_screenshot
    @qase.step(
        title="Verify filter functionality inside add item",
        expected="filter functionality should be working as expect inside the add item",
    )
    def verify_filter_functionality_of_add_item(
        self, available_filter_options, expected_statuses
    ):
        """
        Verify filter functionality inside add item
        """
        self.add_item_button.click()
        time.sleep(5)
        expect(self.add_item_filter_label).to_be_visible()
        expect(self.filter_dropdown).to_be_visible()
        filter_options = self.page.query_selector_all(self.filter_options)
        filter_options_text = [option.inner_text() for option in filter_options]
        assert (
            filter_options_text == available_filter_options
        ), f"Expected: {available_filter_options}, but got: {filter_options_text}"
        print(f"all available filters verified: {available_filter_options}")
        for filter_option in available_filter_options:
            self.filter_option_to_select.select_option(filter_option)
            time.sleep(5)
            self.page.wait_for_selector(self.add_item_status)
            # Query for the status elements after applying the filter
            all_items_status = self.page.query_selector_all(self.add_item_status)
            all_items_status_text = [status.inner_text() for status in all_items_status]
            # Print the text of each status
            print(
                f"Items status after applying '{filter_option}': {all_items_status_text}"
            )
            # Assertion to verify the expected statuses are present
            if filter_option in expected_statuses:
                expected = expected_statuses[filter_option]
                if expected:
                    for expected_status in expected:
                        assert (
                            expected_status in all_items_status_text
                        ), f"'{expected_status}' not found in the status text for filter '{filter_option}'"
                else:
                    # If there are no expected statuses, assert that the status list is empty
                    assert (
                        not all_items_status_text
                    ), f"Expected no statuses for filter '{filter_option}', but found: {all_items_status_text}"

    @qase_screenshot
    @qase.step(
        title="Verify and perform edit status and delete functionality from the actions",
        expected="Actions functionality should be working as expected",
    )
    def verify_and_perform_edit_status_and_delete_actions_functionality_from_actions(
        self, tab_to_change, headers_text
    ):
        """
        Verify and perform edit status and delete functionality from the actions
        """
        elements_to_check = [
            self.edit_action,
            self.active_inactive_action,
            self.delete_icon,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("actions buttons verified")
        self.edit_action.click()
        elements_to_be_visible = [
            self.item_information_component,
            self.item_information_header,
            self.display_information_component,
            self.display_information_header,
            self.display_thumbnail_header,
            self.display_name,
            self.display_gallery,
            self.basic_information_component,
            self.basic_information_header,
            self.item_id,
            self.item_price,
            self.item_name,
            self.item_status,
            self.edit_button,
            self.item_control_component,
            self.item_control_header,
            self.active_item_button,
            self.delete_item_button,
            self.company_name,
            self.phone_number,
            self.email,
            self.vendor_info_button,
            self.vendor_info_modal_component,
        ]
        for element in elements_to_be_visible:
            expect(element).to_be_visible()
        print("Item information tab elements verified successfully")

        # Step 3: Navigate to the specified tab
        tab_locator = self.page.locator(
            self.item_information_tabs.replace("<<tab_to_navigate>>", tab_to_change)
        )
        expect(tab_locator).to_be_visible()
        tab_locator.click()
        time.sleep(3)
        # Step 4: Verify header titles
        headers_title = self.send_order_headers.inner_text()
        cleaned_headers = re.sub(r"[🔼🔽]", "", headers_title).strip()
        # Split using either tabs or two or more spaces
        headers_list = [
            header.strip()
            for header in re.split(r"\t|\s{2,}", cleaned_headers)
            if header
        ]
        assert (
            headers_list == headers_text
        ), f"Headers do not match: {headers_list} != {headers_text}"
        # Step 5: Verify visibility of additional elements
        elements_go_check = [
            self.send_orders_components,
            self.send_orders_pagination,
            self.send_orders_page_footer,
            self.send_orders_result_count,
            self.send_orders_row_per_page,
        ]
        for element in elements_go_check:
            expect(element).to_be_visible()
        print("Send order components verified successfully")
        self.close_button.click()
        item_status = self.single_item_status.text_content()
        self.active_inactive_action.click()
        time.sleep(2)
        expect(self.success_message).to_be_visible()
        changed_item_status = self.single_item_status.text_content()
        assert item_status != changed_item_status
        self.active_inactive_action.click()
        print("Actions functionality verified")
