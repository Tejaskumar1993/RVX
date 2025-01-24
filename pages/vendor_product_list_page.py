"""
Vendor Orders List module
"""
import re
import time
from playwright.sync_api import Page, expect
from qase.pytest import qase

from pages.base_page import BasePage
from utilities.decorators import qase_screenshot


class VendorProductListPage(BasePage):
    """
    module for Vendor Orders List page actions
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Locators
        self.change_role_dropdown = page.locator('(//button[@id="dropdown-flags"])[2]')
        self.role_to_select = '//a[text()="<<role_to_change>>"]'
        self.filter_icon = page.locator('//*[@class="filter-text-icon"]')
        self.filter = page.locator('//div[@class="d-flex align-items-center mb-2"]//select')
        self.filter_options = '//select[@class="generic-filter-select ms-2 form-select form-select-sm"]//option'
        self.pagination = page.locator(
            '//div[@class="d-flex pagination-numbers m-auto mb-2"]'
        )
        self.product_list_component = page.locator('//div[@class="card-body"]')
        self.product_list_header = page.locator('//div[@class="simplebar-mask"]')
        self.footer = page.locator('//div[@class="table-footer-border-top card-footer"]')
        self.showing_result = page.locator('//div[@class="d-flex align-items-center fs--1 ps-3"]')
        self.row_per_page = page.locator(
            '//div[@class="d-flex align-items-center fs--1 ps-3 d-flex flex-wrap rows-page-count"]')
        self.product_list_icon = page.locator('//*[@data-icon="box-open"]')
        self.select_tab_from_side_navigation = '//span[text()="<<tab_to_navigate>>"]'
        self.table_headers = page.locator('(//tr)[1]')
        self.product_status = '//div[contains(@class, "badge-soft-success") or contains(@class, "badge-soft-danger")]'
        self.active_and_inactive_action = page.locator('(//*[@data-icon="lock" or @data-icon="unloack"])[1]')
        self.select_product = page.locator('(//tr)[2]')
        self.edit_action = page.locator('(//*[@data-icon="pen-to-square"])[1]')
        self.add_product = page.locator('//button[text()="Add Product"]')
        self.edit_product = page.locator('//div[text()="Edit Product"]')
        self.request_support = page.locator('//button[text()="Request Support"]')
        self.edit_image_component = page.locator('//div[@class="ant-modal-content"]')
        self.edit_image_title = page.locator('//div[text()="Edit image"]')
        self.cancel_button = page.locator('//button//span[text()="Cancel"]')
        self.ok_button = page.locator('//button//span[text()="OK"]')

        # add product component locators
        self.add_product_component = page.locator('//div[@class="modal-content"]')
        self.add_product_title = page.locator('//div[text()="Add Product"]')
        self.product_image_label = page.locator('//label[text()="Product Image"]')
        self.image_area = 'input[type="file"]'
        self.product_name_label = page.locator('//label[text()="Product Name"]')
        self.product_name_input = page.locator('//input[@id="productName"]')
        self.select_category_label = page.locator('//label[text()="Category"]')
        self.category_select_dropdown = page.locator('//input[@id="categoryId"]')
        self.select_category = page.locator('//div[text()="eGift"]')
        self.price_label = page.locator('//label[text()="Price"]')
        self.price_input = page.locator('//input[@id="productPrice"]')
        self.shipping_rate_label = page.locator('//label[text()="Shipping Rate"]')
        self.shipping_rate_input = page.locator('//input[@id="shippingRate"]')
        self.description_label = page.locator('//label[text()="Description"]')
        self.description_input = page.locator('//div[@role="textbox"]')
        self.submit_button = page.locator('//button//span[text()="Submit"]')
        self.draft_button = page.locator('//button//span[text()="Draft"]')
        self.close_button = page.locator('//button[@class="btn-close"]')

        # request support component locators
        self.request_support_component = page.locator('//div[@class="modal-content"]')
        self.request_support_header = page.locator('//div[text()="Request Support"]')
        self.subject_label = page.locator('//label[text()="Subject"]')
        self.subject_input_area = page.locator('//textarea[@id="Summary"]')
        self.additional_description_label = page.locator('//label[text()="Additional Description"]')
        self.additional_description_input_area = page.locator('//textarea[@id="AdditionalDescription"]')
        self.success_message = page.locator(
            '//div[@class="ant-message-custom-content ant-message-success"]'
        )
        self.request_submit_button = page.locator('//button[text()="Submit"]')
        self.request_cancel_button = page.locator('//button[text()="Cancel"]')

    @qase_screenshot
    @qase.step(
        title="click on user role dropdown and select role",
        expected="User should be able to change role successfully",
    )
    def click_on_dropdown_and_change_user_role(self, role_to_change):
        """
        Change user role from dropdown
        """
        time.sleep(2)
        self.change_role_dropdown.click()
        self.page.locator(
            self.role_to_select.replace("<<role_to_change>>", role_to_change)
        ).click()
        print(f"User role changed to {role_to_change}")

    @qase_screenshot
    @qase.step(
        title="Verify and click on product List page",
        expected="User should be able to see product list icon and able to click on product list tab",
    )
    def verify_and_click_on_product_list_tab(self, side_navigation_item):
        """
        Verify Users and click on product List tab
        """
        # verify icon availability
        expect(self.product_list_icon).to_be_visible()
        # clicking on company information
        time.sleep(5)
        self.page.click(
            self.select_tab_from_side_navigation.replace(
                "<<tab_to_navigate>>", side_navigation_item
            )
        )
        print(f"successfully able to click on {side_navigation_item} tab")

    @qase_screenshot
    @qase.step(title="Verify elements of product list page",
               expected="vendor should be able to see all available elements of product list page")
    def verify_product_list_page_elements(self, headers_text):
        """
        Verify product list page elements visibility
        """
        elements_to_check = [
            self.product_list_header,
            self.product_list_component,
            self.filter_icon,
            self.pagination,
            self.footer,
            self.showing_result,
            self.row_per_page,
            self.add_product,
            self.request_support,
            self.active_and_inactive_action,
            self.edit_action,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("items list page elements verified")
        # Extract headers from the UI
        headers_title = self.table_headers.inner_text().strip()
        print("Headers titles before cleanup -->", headers_title)
        # Split the headers on tabs or multiple spaces
        headers_list = re.split(r"[\t]+|\s{2,}", headers_title)
        headers_list = [
            header.strip() for header in headers_list if header
        ]  # Remove empty items
        # Assert the headers match the expected values
        assert (
                headers_list == headers_text
        ), f"Headers do not match: {headers_list} != {headers_text}"
        print("All elements verified")

    @qase_screenshot
    @qase.step(title="Verify filter functionality of vendor product list",
               expected="vendor should be able to apply filter")
    def verify_filter_functionality_of_product_list(self, available_filter_options, expected_statuses):
        """
        Verify and check working of filter functionality and filter status
        """
        expect(self.filter).to_be_visible()
        filter_options = self.page.query_selector_all(self.filter_options)
        filter_options_text = [option.inner_text() for option in filter_options]
        assert (
                filter_options_text == available_filter_options
        ), f"Expected: {available_filter_options}, but got: {filter_options_text}"
        print(f"all available filters verified: {available_filter_options}")
        for filter_option in available_filter_options:
            self.filter.select_option(filter_option)
            time.sleep(5)
            self.page.wait_for_selector(self.product_status)
            # Query for the status elements after applying the filter
            all_products_status = self.page.query_selector_all(self.product_status)
            all_products_status_text = [status.inner_text() for status in all_products_status]
            # Print the text of each status
            print(
                f"Items status after applying '{filter_option}': {all_products_status_text}"
            )
            # Assertion to verify the expected statuses are present
            if filter_option in expected_statuses:
                expected = expected_statuses[filter_option]
                if expected:
                    for expected_status in expected:
                        assert (
                                expected_status in all_products_status_text
                        ), f"'{expected_status}' not found in the status text for filter '{filter_option}'"
                else:
                    # If there are no expected statuses, assert that the status list is empty
                    assert (
                        not all_products_status_text
                    ), f"Expected no statuses for filter '{filter_option}', but found: {all_products_status_text}"

    @qase_screenshot
    @qase.step(title="Verify elements of product list page",
               expected="vendor should be able to see all available elements of product list page")
    def verify_active_inactive_and_edit_action(self):
        """
        Verify product list page elements visibility
        """
        self.edit_action.click()
        elements_to_check = [self.add_product_component,
                             self.edit_product,
                             self.close_button,
                             self.description_label,
                             self.description_input,
                             self.price_input,
                             self.price_label,
                             self.shipping_rate_input,
                             self.shipping_rate_label,
                             self.product_image_label,
                             self.product_name_input,
                             self.select_category_label,
                             self.category_select_dropdown]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        # elements_to_check = [
        #     self.active_and_inactive_action,
        #     self.edit_action,
        # ]
        # for elements in elements_to_check:
        #     expect(elements).to_be_visible()
        # print("actions buttons verified")
        # product_status_element = self.page.locator(
        #     "(//div[contains(@class, 'badge-soft-success') or contains(@class, 'badge-soft-danger')])[1]"
        # )
        # current_status = product_status_element.text_content()
        # print(f"Current status is: {current_status}")
        # if "Declined" in current_status:
        #     self.active_and_inactive_action.click()
        #     self.success_message.wait_for(state="visible")
        #     expect(self.success_message).to_be_visible()
        #     success_message = self.success_message.text_content()
        #     print(success_message)
        #     assert success_message == "User Suspended"
        #     time.sleep(3)
        #     new_status = product_status_element.text_content()
        #     assert (
        #             "Suspended" in new_status
        #     ), f"Expected status to be 'Suspended', but got {new_status}"
        #     print("Status changed to 'Suspected' successfully.")
        # if "Suspended" in current_status:
        #     self.active_and_inactive_action.click()
        #     self.success_message.wait_for(state="visible")
        #     expect(self.success_message).to_be_visible()
        #     success_message = self.success_message.text_content()
        #     print(success_message)
        #     assert success_message == "User Activated"
        #     time.sleep(3)
        #     new_status = product_status_element.text_content()
        #     assert (
        #             "Active" in new_status
        #     ), f"Expected status to be 'Active', but got {new_status}"
        #     print("Status changed back to 'Active' successfully.")

    @qase_screenshot
    @qase.step(title="Verify request support component & functionality",
               expected="vendor should be able to request support")
    def verify_request_support_flow_and_elements(self, request_subject, request_description, success_message_text):
        """
        Verify request support flow
        """
        self.request_support.click()
        elements_to_check = [self.request_support_component,
                             self.request_support_header,
                             self.subject_label,
                             self.subject_input_area,
                             self.additional_description_label,
                             self.additional_description_input_area,
                             self.request_submit_button,
                             self.request_cancel_button]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        self.subject_input_area.fill(request_subject)
        self.additional_description_input_area.fill(request_description)
        self.request_submit_button.click()
        expect(self.success_message).to_be_visible()
        message_text = self.success_message.text_content()
        print("message_text:", message_text)
        assert message_text in success_message_text
        print("request sent successfully")

    @qase_screenshot
    @qase.step(title="Verify add product component elements and add new product",
               expected="vendor should be able to see all available elements of add product component and able to add new product")
    def verify_add_product_component_and_add_new_product(self, product_name, product_price, product_shipping_rate,
                                                         description, image_path, success_message_text):
        """
        Verify add product component and add new product
        """
        expect(self.add_product).to_be_visible()
        self.add_product.click()
        elements_to_check = [self.add_product_component,
                             self.add_product_title,
                             self.close_button,
                             self.submit_button,
                             self.draft_button,
                             self.description_label,
                             self.description_input,
                             self.price_input,
                             self.price_label,
                             self.shipping_rate_input,
                             self.shipping_rate_label,
                             self.product_image_label,
                             self.product_name_input,
                             self.select_category_label,
                             self.category_select_dropdown]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        self.product_name_input.fill(product_name)
        self.price_input.fill(product_price)
        self.shipping_rate_input.fill(product_shipping_rate)
        self.description_input.fill(description)
        self.category_select_dropdown.click()
        self.select_category.click()
        self.page.set_input_files(self.image_area, image_path)
        expect(self.edit_image_component).to_be_visible()
        expect(self.edit_image_title).to_be_visible()
        expect(self.cancel_button).to_be_visible()
        expect(self.ok_button).to_be_visible()
        self.ok_button.click()
        self.submit_button.click()
        expect(self.success_message).to_be_visible()
        message_text = self.success_message.text_content()
        print("message_text:", message_text)
        assert message_text in success_message_text
        print("new product added successfully to the product list")
