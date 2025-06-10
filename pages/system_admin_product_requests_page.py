"""
System Admin product request page modules
"""

import time
from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class SystemAdminProductRequest(BasePage):
    """
    Module containing objects and methods related to System Admin product request page
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # System admin product request page navigate locators
        self.change_role_dropdown = page.locator('(//button[@id="dropdown-flags"])[2]')
        self.select_tab_from_side_navigation = '//span[text()="<<tab_to_navigate>>"]'
        self.product_request_icon = page.locator('//*[@data-icon="rss"]')

        # System admin product request main page locators
        self.filter_dropdown = page.locator(
            '//select[@class="generic-filter-select ms-2 form-select form-select-sm"]'
        )
        self.filter_options = "//select[@class='generic-filter-select ms-2 form-select form-select-sm']//option"
        self.all_product_status = ' //div[contains(@class, "badge-soft-primary")'

        self.select_rows_per_page_dropdown = page.locator(
            '//div[contains(@class,"ps-3 d-flex flex-wrap rows-page-count")]//select'
        )
        self.pagination_number = page.locator(
            "//div[@class='d-flex pagination-numbers m-auto mb-2']"
        )
        self.pagination_result = page.locator(
            "//div[@class='d-flex align-items-center fs--1 ps-3']"
        )
        self.pagination_row_per_page = page.locator(
            "//div[@class='d-flex align-items-center fs--1 ps-3 d-flex flex-wrap rows-page-count']"
        )
        self.batch_action_text = page.locator(
            "//label[@class='pe-2 mt-1 nowrap form-label']"
        )
        self.batch_action_option = page.locator(
            "//select[@class='form-control form-select form-select-sm']/option"
        )
        self.apply_action_button = page.locator("//button[text()='Apply Action']")
        self.check_box = page.locator(
            "//input[@type='checkbox' and @title='Toggle All Rows Selected']"
        )
        self.vendor_name_header = page.locator("//th[text()='Vendor Name']")
        self.request_date_header = page.locator("//th[text()='Request Date']")
        self.product_header = page.locator("//th[text()='Product']")
        self.price_header = page.locator("//th[text()='Price']")
        self.status_header = page.locator("//th[text()='Status']")
        self.action_header = page.locator("//th[text()='Actions']")

        # Product Requests popup locators
        self.select_product = page.locator(
            "//tr[@class='align-middle white-space-nowrap hover-actions-trigger btn-reveal-trigger hover-bg-100  undefined' and @role='row']"
        )
        self.product_request_popup_header = page.locator(
            "//div[@class='modal-title h4']"
        )
        self.company_name = page.locator("//h6[text()='Company Name']")
        self.phone_number = page.locator("//h6[text()='Phone Number']")
        self.mail = page.locator("//h6[text()='Email']")
        self.product_name = page.locator("//label[text()='Product Name']")
        self.product_price = page.locator("//label[text()='Product Price']")
        self.product_description = page.locator("//label[text()='Product Description']")
        self.approve_button = page.locator("//button[text()='Approve']")
        self.decline_button = page.locator("//button[text()='Decline']")
        self.cancel_button = page.locator("//button[text()='Cancel']")

        # Add item popup of product request popup locators
        self.add_item_title = page.locator("//div[text()='Product Requests']")
        self.item_name = page.locator("//label[text()='Item Name']")
        self.type = page.locator("//label[text()='Type']")
        self.category = page.locator("//label[text()='Category']")
        self.select_category = page.locator(
            "//input[@type='search' and @id='categoryId']"
        )
        self.select_test = page.locator(
            "//div[@class='ant-select-item-option-content' and text()='Test']"
        )
        self.vendor = page.locator("//label[text()='Vendor']")
        self.item_price = page.locator("//label[text()='Item Price']")
        self.shipping_rate = page.locator("//label[text()='Shipping Rate']")
        self.fee = page.locator("//label[text()='Fee']")
        self.enter_fee = page.locator("//input[@placeholder='Enter Fee']")
        self.enter_processing_time = page.locator(
            "//input[@placeholder='Processing time']"
        )
        self.select_status = page.locator("//input[@id='itemStatus']")

        self.processing_time = page.locator(
            "//label[text()='Processing time (in days)']"
        )
        self.status = page.locator("//label[text()='Status']")
        self.select_active = (
            "//div[@class='ant-select-item-option-content' and text()='Active']"
        )
        self.description = page.locator("//label[text()='Description']")
        self.add_item_button = page.locator(
            "//button[@class='ant-btn ant-btn-primary']"
        )
        self.all_orders_status = ' //div[contains(@class, "badge-soft-primary") or contains(@class, "badge-soft-success") or contains(@class,"badge-soft-warning") or contains(@class, "badge-soft-info")]'

    def verify_and_click_on_product_request_tab(self, side_navigation_item):
        """
        Verify Users and click on Product request tab
        """
        # verify icon availability
        expect(self.product_request_icon).to_be_visible()
        print("Product request icon is visible.")
        # clicking on send order list tab
        self.page.click(
            self.select_tab_from_side_navigation.replace(
                "<<tab_to_navigate>>", side_navigation_item
            )
        )
        print(f"Successfully clicked on: {side_navigation_item}")

    def verify_product_request_page_elements(self):
        """
        Verify and check availability of product request page elements
        """
        elements_to_check = [
            self.pagination_number,
            self.pagination_result,
            self.pagination_row_per_page,
            self.batch_action_text,
            self.apply_action_button,
            self.check_box,
            self.vendor_name_header,
            self.request_date_header,
            self.product_header,
            self.price_header,
            self.status_header,
            self.action_header,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("This is for main page -> All elements are visible on the page.")

        # product request popup elements
        self.select_product.click()
        elements_to_check = [
            self.product_request_popup_header,
            self.company_name,
            self.phone_number,
            self.mail,
            self.product_name,
            self.product_price,
            self.product_description,
            self.approve_button,
            self.decline_button,
            self.cancel_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print(
            "This is for product request popup-> All elements are visible on the popup."
        )

        # Add item popup elements
        self.approve_button.click()
        elements_to_check = [
            self.add_item_title,
            self.item_name,
            self.type,
            self.category,
            self.vendor,
            self.item_price,
            self.shipping_rate,
            self.fee,
            self.processing_time,
            self.status,
            self.description,
            self.add_item_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("This is for add item popup -> All elements are visible on the popup.")

    def verify_approve_and_add_item_functionality(self):
        """
        Verify approve and add item functionality
        """
        expect(self.select_product).to_be_visible()
        print("Product is visible.")
        self.select_product.click()
        print("Click on Product")
        self.approve_button.click()
        print("Click on Approve button")
        self.select_category.click()
        print("Click on category dropdown")
        element = self.page.locator(
            "(//div[@class='ant-select-item-option-content'])[1]"
        )
        element.click()
        print("Click on test")
        self.enter_fee.fill("10")
        self.enter_processing_time.fill("5")
        self.select_status.click()
        print("Click on status input field")
        element = self.page.locator(
            "//div[@class='ant-select-item-option-content' and text()='Active']"
        )
        element.click()
        print("Click on Active")

    def apply_filter_on_product_request_and_verify_filtered_data(
        self, available_filter_options, expected_statuses
    ):
        """
        Apply filter on product request and verify filtered data
        """
        expect(self.filter_dropdown).to_be_visible()
        self.select_rows_per_page_dropdown.select_option("250")
        filter_options = self.page.query_selector_all(self.filter_options)
        filter_options_text = [option.inner_text() for option in filter_options]
        assert (
            filter_options_text == available_filter_options
        ), f"Expected: {available_filter_options}, but got: {filter_options_text}"
        print(f"all available filters verified: {available_filter_options}")
        for filter_option in available_filter_options:
            self.filter_dropdown.select_option(filter_option)
            time.sleep(5)
            self.page.wait_for_selector(self.all_orders_status)
            # Query for the status elements after applying the filter
            all_orders_status = self.page.query_selector_all(self.all_orders_status)
            all_orders_status_text = [
                status.inner_text() for status in all_orders_status
            ]
            # Print the text of each status
            print(
                f"Items status after applying '{filter_option}': {all_orders_status_text}"
            )
            # Assertion to verify the expected statuses are present
            if filter_option in expected_statuses:
                expected = expected_statuses[filter_option]
                if expected:
                    for expected_status in expected:
                        assert (
                            expected_status in all_orders_status_text
                        ), f"'{expected_status}' not found in the status text for filter '{filter_option}'"
                else:
                    # If there are no expected statuses, assert that the status list is empty
                    assert (
                        not all_orders_status_text
                    ), f"Expected no statuses for filter '{filter_option}', but found: {all_orders_status_text}"
