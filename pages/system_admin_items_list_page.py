"""
System Admin items list page modules
"""

import re
import time

from playwright.sync_api import Page, expect
from qase.pytest import qase

from pages.base_page import BasePage
from utilities.decorators import qase_screenshot


class SystemAdminItemsListPage(BasePage):
    """
    Module containing objects and methods related to System Admin items list Page
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # System admin items list page locators
        self.items_list_icon = page.locator('//*[@data-icon="list"]')
        self.items_list_tab = '//span[text()="<<side_navigation_tabs>>"]'

        self.add_item_button = page.locator('//button[text()="Add Item"]')
        self.filter_label = page.locator('//*[text()="Filter:"]')
        self.filter_drop_down = '//select[@class="generic-filter-select ms-2 form-select form-select-sm"]//option'

        self.filter_option = page.locator(
            '(//div[@class="d-flex align-items-center"]//select)[1]'
        )
        self.batch_action_label = page.locator('//*[text()="Batch Action"]')
        self.batch_action_dropdown = page.locator(
            '//select[@class="form-control form-select form-select-sm"]'
        )
        self.batch_action_option = page.locator(
            '(//div[@class="d-flex align-items-center"]//select)[2]'
        )
        self.apply_action_button = page.locator('//button[text()="Apply Action"]')
        self.items_list_headers = page.locator('//tr[@class="text-center"]')
        self.items_status = "//div[contains(@class, 'badge') and (contains(@class, 'badge-soft-primary') or contains(@class, 'badge-soft-danger'))]"
        self.items_list_footer = page.locator(
            '//div[@class="table-footer-border-top card-footer"]'
        )
        self.pagination = page.locator('//div[@class="d-flex pagination-numbers"]')
        self.results_counter = page.locator(
            '//div[@class="d-flex align-items-center fs--1 ps-3"]'
        )
        self.rows_per_page = page.locator(
            '//div[@class="d-flex align-items-center fs--1 ps-3 d-flex flex-wrap rows-page-count"]'
        )
        self.items_list_component = page.locator('//div[@class="simplebar-content"]')
        self.items_list_page_header = page.locator('//div[@class="mb-2 card"]')
        self.active_deactive_action_button = page.locator('(//*[@data-icon="lock"])[1]')
        self.revoke_action_button = page.locator(
            '(//*[@data-icon="arrow-rotate-left"])[1]'
        )
        self.delete_action_button = page.locator('(//*[@data-icon="trash"])[1]')
        self.item_checkbox = page.locator("(//input)[2]")

        # add item locators
        self.add_item_header = page.locator(
            '//div[@class="modal-title h4"][text()="Add Item"]'
        )
        self.item_image_title = page.locator('//label[text()="Item Image"]')
        self.upload_image_button = page.locator(
            '//span[@class="ant-upload-wrapper css-1vtf12y"]//span[@class="ant-upload"]'
        )
        self.add_item_image_area = page.locator(
            '//div[@class="ant-upload-list ant-upload-list-picture-circle"]//span[@class="ant-upload"]'
        )
        self.add_item_name_label = page.locator('//label[text()="Name"]')
        self.add_item_name = page.locator('//input[@id="name"]')
        self.add_item_category_label = page.locator('//label[text()="Category"]')
        self.add_item_category_dropdown = page.locator(
            '//label[text()="Category"]//..//select[@class="form-select-md form-control form-select"]'
        )
        self.add_item_select_category = page.locator(
            '//label[text()="Category"]//..//select'
        )
        self.add_item_description_label = page.locator('//label[text()="Description"]')
        self.add_item_description_text_area = page.locator(
            '//div[@class="ck ck-editor__main"]//p'
        )
        self.add_item_item_prince_label = page.locator('//label[text()="Price"]')
        self.add_item_price_input = page.locator('//input[@id="price"]')
        self.add_item_fee_label = page.locator('//label[text()="Fee"]')
        self.add_item_fee_input = page.locator('//input[@id="fee"]')
        self.add_item_processing_time_label = page.locator(
            '//label[text()="Processing time (in days)"]'
        )
        self.add_item_processing_time_input = page.locator(
            '//input[@id="processing_time"]'
        )
        self.add_item_status_label = page.locator('//label[text()="Status"]')
        self.add_item_status_dropdown = page.locator(
            '//label[text()="Status"]//..//select[@class="form-select-md form-control form-select"]'
        )
        self.add_item_select_status_option = page.locator(
            '//label[text()="Status"]//..//select'
        )
        self.add_item = page.locator('//button[@type="submit"]')
        self.add_item_success_message = page.locator(
            '//div[@class="ant-message-custom-content ant-message-success"]'
        )
        self.item_id_on_list = page.locator("//tbody//tr[1]//td[3]")
        self.item_name_on_list = page.locator("//tbody//tr[1]//td[4]")
        self.item_category_on_list = page.locator("//tbody//tr[1]//td[5]")
        self.item_description_on_list = page.locator("//tbody//tr[1]//td[7]")
        self.item_price_on_list = page.locator("//tbody//tr[1]//td[8]")
        self.item_status_on_list = page.locator(
            '(//div[contains(@class, "me-2 badge badge-soft-primary btn-outline rounded-pill") or contains(@class, "badge-soft-danger")])[1]'
        )
        self.delete_confirm_message = page.locator('//div[@class="modal-body"]')
        self.generic_update_button = page.locator('//button[text()="Confirm"]')
        self.notice_message = page.locator('//div[@class="ant-message-notice-content"]')
        self.active_and_deactive_notice_message = page.locator(
            '//div[@class="ant-message-notice-content"]'
        )
        self.select_item = page.locator("(//tr)[2]")
        self.item_information_header = page.locator('//div[text()="Item Information"]')
        self.item_information_tabs = '//button[text()="<<tab_to_navigate>>"]'
        self.Basic_information_component = page.locator(
            '(//div[@class="mt-4 card"])[1]'
        )
        self.edit_button = page.locator('//button[text()="Edit"]')
        self.vendor_info_modal_component = page.locator('//div[@class="p-3 card"]')
        self.company_name_info = page.locator('(//h6[@class="text-700 mb-0"])[2]')
        self.company_name = page.locator('//h6[text()="Company Name"]')
        self.phone_number_info = page.locator('(//h6[@class="text-700 mb-0"])[4]')
        self.phone_number = page.locator('//h6[text()="Phone Number"]')
        self.email = page.locator('//h6[text()="Email"]')
        self.email_info = page.locator('(//h6[@class="text-700 mb-0"])[6]')
        self.vendor_info_button = page.locator('//button[text()="Vendor More Info"]')
        self.item_control_component = page.locator(
            '//div[@class="mt-4 shadow-lg card"]'
        )
        self.item_control_header = page.locator('//h5[text()="Item Controls"]')
        self.active_item_button = page.locator(
            '//button[text()="Activate Item" or text()="Suspend Item"]'
        )
        self.delete_item_button = page.locator('//button[text()="Delete Item"]')
        self.basic_information_component = page.locator('//div[@class="mt-4 card"]')
        self.basic_information_header = page.locator('//h5[text()="Basic Information"]')
        self.item_id = page.locator('//p[text()="ID"]')
        self.item_id_text = page.locator(
            '(//div[@class="row"]//div[@class="col"]//p)[1]'
        )
        self.item_name = page.locator('//p[text()="Name"]')
        self.item_name_text = page.locator(
            '(//div[@class="row"]//div[@class="col"]//p)[2]'
        )
        self.item_price = page.locator('//p[text()="Price"]')
        self.item_price_text = page.locator(
            '(//div[@class="row"]//div[@class="col"]//p)[3]'
        )
        self.item_fee = page.locator('//p[text()="Fee"]')
        self.item_fee_text = page.locator(
            '(//div[@class="row"]//div[@class="col"]//p)[4]'
        )
        self.item_status = page.locator('//p[text()="Status"]')
        self.item_status_text = page.locator(
            '(//div[@class="row"]//div[@class="col"]//p)[5]'
        )
        self.item_type = page.locator('//p[text()="Item Type"]')
        self.item_type_text = page.locator(
            '(//div[@class="row"]//div[@class="col"]//p)[6]'
        )
        self.lead_time = page.locator('//p[text()="Lead Time"]')
        self.lead_time_text = page.locator(
            '(//div[@class="row"]//div[@class="col"]//p)[7]'
        )
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
            '(//div[@id="item-information-tab-tabpane-itemsInfo"]//..//div[@class="table-footer-border-top card-footer"])[1]'
        )
        self.send_orders_row_per_page = page.locator(
            '(//div[@id="item-information-tab-tabpane-itemsInfo"]//..//div//p[text()="Rows per page:"])[1]'
        )
        self.send_orders_pagination = page.locator(
            '(//div[@id="item-information-tab-tabpane-sendOrders"]//..//div[@class="d-flex pagination-numbers"])[1]'
        )
        self.send_orders_result_count = page.locator(
            '(//div[@id="item-information-tab-tabpane-itemsInfo"]//..//span[@class="d-none d-sm-inline-block me-2"])[1]'
        )
        self.deployments_headers = page.locator("(//thead)[3]")
        self.deployments_components = page.locator(
            '//div[@id="item-information-tab-tabpane-deployments"]'
        )
        self.deployments_page_footer = page.locator(
            '(//div[@id="item-information-tab-tabpane-deployments"]//..//div[@class="table-footer-border-top card-footer"])[2]'
        )
        self.deployments_row_per_page = page.locator(
            '(//div[@id="item-information-tab-tabpane-deployments"]//..//div//p[text()="Rows per page:"])[2]'
        )
        self.deployments_pagination = page.locator(
            '(//div[@id="item-information-tab-tabpane-deployments"]//..//div[@class="d-flex pagination-numbers"])[2]'
        )
        self.deployments_result_count = page.locator(
            '(//div[@id="item-information-tab-tabpane-deployments"]//..//span[@class="d-none d-sm-inline-block me-2"])[2]'
        )
        self.close_button = page.locator('//button[@class="btn-close"]')

        # vendor information model locator
        self.vendor_information_component = page.locator(
            '(//div[@class="modal-content"])[2]'
        )
        self.vendor_information_header = page.locator(
            '//div[text()="Vendor Information"]'
        )
        self.vendor_info_body = page.locator(
            '//div[@id="vendor-information-tab-tabpane-vendorInfo"]//div[@class="card-body"]'
        )
        self.vendor_company_name = page.locator('(//h6[@class="text-700 mb-0"])[8]')
        self.vendor_phone_number = page.locator('(//h6[@class="text-700 mb-0"])[10]')
        self.vendor_email = page.locator('(//h6[@class="text-700 mb-0"])[12]')
        self.vendor_controls = page.locator(
            '//div[@id="vendor-information-tab-tabpane-vendorInfo"]//div[@class="card"]'
        )
        self.suspend_vendor_button = page.locator(
            '//div[@id="vendor-information-tab-tabpane-vendorInfo"]//button[text()="Suspend Vendor"]'
        )
        self.invite_vendor = page.locator(
            '//div[@id="vendor-information-tab-tabpane-vendorInfo"]//button[text()="Invite Vendor"]'
        )
        self.view_dashboard = page.locator(
            '//div[@id="vendor-information-tab-tabpane-vendorInfo"]//button[text()="View Dashboard"]'
        )
        self.delete_vendor = page.locator(
            '//div[@id="vendor-information-tab-tabpane-vendorInfo"]//button[text()="Delete Vendor"]'
        )
        self.vendor_orders_tab = page.locator(
            '//button[@id="vendor-information-tab-tab-orders"]'
        )
        self.vendor_orders_tab_headers = page.locator(
            '//div[@id="vendor-information-tab-tabpane-orders"]//tr'
        )
        self.vendor_products_tab = page.locator(
            '//button[@id="vendor-information-tab-tab-products"]'
        )
        self.vendor_products_tab_headers = page.locator(
            '//div[@id="vendor-information-tab-tabpane-products"]//tr'
        )
        self.vendor_users_tab = page.locator(
            '//button[@id="vendor-information-tab-tab-users"]'
        )
        self.vendor_users__tab_headers = page.locator(
            '//div[@id="vendor-information-tab-tabpane-users"]//tr'
        )

    @qase_screenshot
    @qase.step(
        title="Verify and click on items list tab",
        expected="items list tab and icon should be visible and user should be able to navigate on items list page",
    )
    def verify_and_click_on_items_list_tab(self, side_navigation_item):
        """
        Verify and click on items list tab
        """
        # verify icon availability
        expect(self.items_list_icon).to_be_visible()
        # clicking on items list tab
        self.page.click(
            self.items_list_tab.replace(
                "<<side_navigation_tabs>>", side_navigation_item
            )
        )
        print(f"successfully able to click on {side_navigation_item} tab")

    @qase_screenshot
    @qase.step(
        title="Verify items list elements",
        expected="items list  elements should be visible",
    )
    def verify_items_list_page_elements(self, headers_text):
        """
        Verify and check items list page elements
        """
        time.sleep(5)
        elements_to_check = [
            self.items_list_component,
            self.items_list_page_header,
            self.items_list_footer,
            self.pagination,
            self.results_counter,
            self.rows_per_page,
            self.add_item_button,
            self.apply_action_button,
            self.filter_drop_down,
            self.filter_label,
            self.batch_action_label,
            self.batch_action_dropdown,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
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
        title="Verify Batch action functionality on items list page",
        expected="User should be able to apply batch actions on selected items",
    )
    def apply_batch_actions_to_items_list(self):
        """
        Apply batch action to items list
        """
        expect(self.batch_action_label).to_be_visible()
        items_status_element = self.page.locator(
            '(//div[contains(@class, "me-2 badge badge-soft-primary btn-outline rounded-pill") or contains(@class, "badge-soft-danger")])[1]'
        )
        current_status = items_status_element.text_content()
        print(f"Current status is: {current_status}")
        # Verify the status is either 'Active' or 'Suspected'
        if "Active" in current_status:
            self.item_checkbox.click()
            self.batch_action_dropdown.select_option("Deactivate")
            self.apply_action_button.click()
            time.sleep(2)
            new_status = items_status_element.text_content()
            assert (
                "Inactive" in new_status
            ), f"Expected status to be 'Inactive', but got {new_status}"
            print("Status changed to 'Deactivate' successfully.")
            # Now change the status back to 'Active'
            self.item_checkbox.click()
            self.batch_action_dropdown.select_option("Activate")
            self.apply_action_button.click()
            # Wait for the status to revert to 'Active' and verify
            time.sleep(2)
            reverted_status = items_status_element.text_content()
            assert (
                "Active" in reverted_status
            ), f"Expected status to be 'Active', but got {reverted_status}"
            print("Status reverted to 'Active' successfully.")
        elif "Inactive" in current_status:
            self.item_checkbox.click()
            self.batch_action_dropdown.select_option("Activate")
            self.apply_action_button.click()
            time.sleep(2)
            reverted_status = items_status_element.text_content()
            assert (
                "Active" in reverted_status
            ), f"Expected status to be 'Active', but got {reverted_status}"
            print("Status changed back to 'Active' successfully.")
        else:
            raise ValueError(f"Unexpected user status: {current_status}")

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
        time.sleep(2)
        filter_options = self.page.query_selector_all(self.filter_drop_down)
        filter_options_text = [option.inner_text() for option in filter_options]
        assert (
            filter_options_text == available_filter_options
        ), f"Expected: {available_filter_options}, but got: {filter_options_text}"
        print(f"all available filters verified: {available_filter_options}")
        for filter_option in available_filter_options:
            self.filter_option.select_option(filter_option)
            time.sleep(5)
            self.page.wait_for_selector(self.items_status)
            # Query for the status elements after applying the filter
            all_items_status = self.page.query_selector_all(self.items_status)
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
        title="Verify and add new item, check added item information, and perform actions",
        expected="Item should be added successfully, its information should be verified, and actions performed on it.",
    )
    def verify_and_add_new_item_and_check_added_item_information_and_perform_action_on_added_item(
        self,
        item_price,
        item_fee,
        processing_time,
        item_status,
        item_category,
        item_name,
        item_description,
        tab_to_change,
        headers_text,
        deployment_tab,
        deployments_header,
        add_item_success_message,
    ):
        """
        Verify and add a new item, verify added item details on the item list,
        check item information in the item information box, and perform actions on the added item.
        """
        print("Clicking 'Add Item' button.")
        self.add_item_button.click()
        time.sleep(2)

        print("Verifying visibility of elements on the 'Add Item' page.")
        elements_to_check = [
            self.add_item_header,
            self.add_item_image_area,
            self.add_item_name_label,
            self.item_image_title,
            self.add_item_category_label,
            self.add_item_category_dropdown,
            self.add_item_name,
            self.add_item_description_label,
            self.add_item_description_text_area,
            self.add_item_status_label,
            self.add_item_status_dropdown,
            self.add_item_item_prince_label,
            self.add_item_price_input,
            self.add_item_fee_label,
            self.add_item_fee_input,
            self.add_item,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()

        print(
            f"Filling item details: Name: {item_name}, Category: {item_category}, "
            f"Description: {item_description}, Price: {item_price}, Fee: {item_fee}, "
            f"Processing Time: {processing_time}, Status: {item_status}"
        )
        self.add_item_name.fill(item_name)
        self.add_item_select_category.select_option(item_category)
        self.add_item_description_text_area.fill(item_description)
        self.add_item_price_input.fill(item_price)
        self.add_item_fee_input.fill(item_fee)
        self.add_item_processing_time_input.fill(processing_time)
        self.add_item_select_status_option.select_option(item_status)

        print("Clicking 'Add Item' button to save.")
        self.add_item.click()
        expect(self.add_item_success_message).to_be_visible()
        success_message = self.add_item_success_message.text_content()
        print(f"success message: {success_message}")
        assert success_message == add_item_success_message
        time.sleep(5)
        print("Verifying added item details on the list.")
        item_name_on_list = self.item_name_on_list.text_content()
        print(f"Expected Item Name: {item_name}, Actual: {item_name_on_list}")
        assert (
            item_name_on_list == item_name
        ), f"Item name mismatch: {item_name_on_list} != {item_name}"

        category_on_list = self.item_category_on_list.text_content()
        print(f"Expected Category: {item_category}, Actual: {category_on_list}")
        # assert (
        #     category_on_list == item_category
        # ), f"Item category mismatch: {category_on_list} != {item_category}"

        item_description_on_list = self.item_description_on_list.text_content()
        print(
            f"Expected Description: {item_description}, Actual: {item_description_on_list}"
        )
        # assert (
        #     item_description_on_list == item_description
        # ), f"Item description mismatch: {item_description_on_list} != {item_description}"

        item_price_on_list = self.item_price_on_list.text_content()
        print(f"Expected Price: ${item_price}, Actual: {item_price_on_list}")
        assert (
            item_price_on_list == f"${item_price}"
        ), f"Item price mismatch: {item_price_on_list} != ${item_price}"

        item_status_on_list = self.item_status_on_list.text_content()
        print(f"Expected Status: {item_status}, Actual: {item_status_on_list}")
        assert (
            item_status_on_list == item_status
        ), f"Item status mismatch: {item_status_on_list} != {item_status}"

        print("Selecting the newly added item.")
        expect(self.select_item).to_be_visible()
        self.select_item.click()
        time.sleep(5)

        print("Verifying item information box components.")
        elements_to_check = [
            self.item_information_header,
            self.basic_information_header,
            self.basic_information_component,
            self.item_id,
            self.item_name,
            self.item_price,
            self.item_fee,
            self.item_status,
            self.item_type,
            self.lead_time,
            self.edit_button,
            self.company_name,
            self.phone_number,
            self.email,
            self.vendor_info_button,
            self.item_control_header,
            self.item_control_component,
            self.active_item_button,
            self.delete_item_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()

        print("Validating item information details.")
        item_id = self.item_id_text.text_content()
        print(
            f"Expected Item ID: {self.item_id_on_list.text_content()}, Actual: {item_id}"
        )
        assert item_id == self.item_id_on_list.text_content(), "Item ID mismatch"

        name = self.item_name_text.text_content()
        print(f"Expected Item Name: {item_name_on_list}, Actual: {name}")
        assert name == item_name_on_list, "Item name mismatch"

        price = self.item_price_text.text_content()
        print(f"Expected Price: {item_price_on_list}, Actual: {price}")
        assert price == item_price_on_list, "Item price mismatch"

        fee = self.item_fee_text.text_content()
        print(f"Expected Fee: ${item_fee}, Actual: {fee}")
        assert fee == f"${item_fee}", f"Item fee mismatch: {fee} != ${item_fee}"

        status = self.item_status_text.text_content()
        print(f"Expected Status: {item_status_on_list}, Actual: {status}")
        assert status == item_status_on_list, "Item status mismatch"

        # item_type = self.item_type_text.text_content()
        # print(f"Expected Category: {category_on_list}, Actual: {item_type}")
        # assert item_type == category_on_list, "Item type mismatch"

        lead_time = self.lead_time_text.text_content()
        normalized_lead_time = lead_time.split()[0]
        print(f"Expected Lead Time: {processing_time}, Actual: {normalized_lead_time}")
        assert (
            normalized_lead_time == processing_time
        ), f"Processing time mismatch: {normalized_lead_time} != {processing_time}"

        print(f"Navigating to tab: {tab_to_change}")
        tab_locator = self.page.locator(
            self.item_information_tabs.replace("<<tab_to_navigate>>", tab_to_change)
        )
        expect(tab_locator).to_be_visible()
        tab_locator.click()
        time.sleep(3)

        print("Verifying headers on the 'Send Orders' tab.")
        headers_title = self.send_order_headers.inner_text()
        cleaned_headers = re.sub(r"[🔼🔽]", "", headers_title).strip()
        headers_list = [
            header.strip()
            for header in re.split(r"\t|\s{2,}", cleaned_headers)
            if header
        ]
        print(f"Expected Headers: {headers_text}, Actual: {headers_list}")
        assert (
            headers_list == headers_text
        ), f"Headers do not match: {headers_list} != {headers_text}"

        print("Verifying components on the 'Send Orders' tab.")
        elements_go_check = [
            self.send_orders_components,
            self.send_orders_pagination,
            self.send_orders_page_footer,
            self.send_orders_result_count,
            self.send_orders_row_per_page,
        ]
        for element in elements_go_check:
            expect(element).to_be_visible()
        print("Send order components verified successfully.")

        print(f"Navigating to tab: {deployment_tab}")
        tab_locator = self.page.locator(
            self.item_information_tabs.replace("<<tab_to_navigate>>", deployment_tab)
        )
        expect(tab_locator).to_be_visible()
        tab_locator.click()
        time.sleep(3)

        print("Verifying headers on the 'Deployments' tab.")
        headers_title = self.deployments_headers.inner_text()
        cleaned_headers = re.sub(r"[🔼🔽]", "", headers_title).strip()
        headers_list = [
            header.strip()
            for header in re.split(r"\t|\s{2,}", cleaned_headers)
            if header
        ]
        print(f"Expected Headers: {deployments_header}, Actual: {headers_list}")
        assert (
            headers_list == deployments_header
        ), f"Headers do not match: {headers_list} != {deployments_header}"

        print("Verifying components on the 'Deployments' tab.")
        elements_go_check = [
            self.deployments_components,
            self.deployments_pagination,
            self.deployments_page_footer,
            self.deployments_result_count,
            self.deployments_row_per_page,
        ]
        for element in elements_go_check:
            expect(element).to_be_visible()
        print("Deployment components verified successfully.")

        print("Closing item details.")
        self.close_button.click()
        time.sleep(3)
        self.delete_action_button.click()
        confirm_message_text = self.delete_confirm_message.text_content()
        print(f"Confirm message text is: {confirm_message_text}")
        assert confirm_message_text == "Are you sure you want to delete this record?"
        self.generic_update_button.click()
        expect(self.notice_message).to_be_visible()
        message_text = self.notice_message.text_content()
        print(message_text)
        assert message_text == "Item Deleted Successfully"

    @qase_screenshot
    @qase.step(
        title="Verify Vendor 'More Info' Section Inside Item Information",
        expected="Vendor 'More Info' section should be visible with all accurate details inside the item information page.",
    )
    def verify_vendor_more_info_inside_item_information(
        self, orders_header, products_header, users_header
    ):
        """
        verify and test vendor more info inside item information
        """
        time.sleep(2)
        expect(self.select_item).to_be_visible()
        self.select_item.click()
        time.sleep(5)
        expect(self.vendor_info_modal_component).to_be_visible()
        company_name = self.company_name_info.text_content()
        print(f"vendor company name: {company_name}")
        phone_number = self.phone_number_info.text_content()
        print(f"vendor phone number: {phone_number}")
        email = self.email_info.text_content()
        print(f"vendor email: {email}")
        self.vendor_info_button.click()
        expect(self.vendor_information_header).to_be_visible()
        expect(self.vendor_info_body).to_be_visible()
        vendor_phone_number = self.vendor_phone_number.text_content()
        assert vendor_phone_number == phone_number
        elements_to_check = [
            self.vendor_controls,
            self.suspend_vendor_button,
            self.view_dashboard,
            self.delete_vendor,
            self.vendor_orders_tab,
            self.vendor_products_tab,
            self.vendor_users_tab,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        tabs_info = [
            (self.vendor_orders_tab, self.vendor_orders_tab_headers, orders_header),
            (
                self.vendor_products_tab,
                self.vendor_products_tab_headers,
                products_header,
            ),
            (self.vendor_users_tab, self.vendor_users__tab_headers, users_header),
        ]

        for tab, headers_title_locator, expected_header in tabs_info:
            # Click tab and wait for content to load
            tab.click()
            time.sleep(2)

            # Extract and clean the header
            headers_title = headers_title_locator.inner_text()
            cleaned_headers = re.sub(r"[🔼🔽]", "", headers_title).strip()
            headers_list = [
                header.strip()
                for header in re.split(r"\t|\s{2,}", cleaned_headers)
                if header
            ]

            # Print expected vs actual headers
            print(f"Expected Headers: {expected_header}, Actual: {headers_list}")
