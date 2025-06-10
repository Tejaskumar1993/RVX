"""
Deployment Admin send order list page modules
"""
import re
import time
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class DeploymentAdminSendOrderList(BasePage):
    """
    Module containing objects and methods related to Deployment admin send order list page
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Send Order List page navigate locators
        self.change_role_dropdown = page.locator('(//button[@id="dropdown-flags"])[2]')
        self.role_to_select = '//a[text()="<<role_to_change>>"]'
        self.select_tab_from_side_navigation = '//span[text()="<<tab_to_navigate>>"]'
        self.Send_order_list_icon = page.locator('//*[@data-icon="truck"]')

        # Send Order List page locators
        # Send Order List page pagination locators
        self.pagination_number = page.locator(
            "//div[contains(@class,'d-flex pagination-numbers m-auto mb-2')]"
        )
        self.pagination_result = page.locator(
            "//div[@class='d-flex align-items-center fs--1 ps-3']"
        )
        self.pagination_row_per_page = page.locator(
            "//div[@class='d-flex align-items-center fs--1 ps-3 d-flex flex-wrap rows-page-count']"
        )

        # Filters Locators
        self.filter_icon = page.locator("//div[@class='filter-text-icon']")
        self.filter_main = page.locator(
            "//div[contains(@class,'d-flex align-items-center col-lg-3')]"
        )
        self.filter_dropdown = page.locator('//select[@class="generic-filter-select ms-2 form-select form-select-sm"]')
        self.filter_options = "//select[@class='generic-filter-select ms-2 form-select form-select-sm']//option"
        self.filter_option_custom_campaign = page.locator("//option[text()='Campaign']")
        self.filter_option_custom_date_sent = page.locator(
            "//option[text()='Date Sent']"
        )
        self.filter_option_custom_status = page.locator("//option[text()='Status']")
        self.enter_value_text_box = page.locator("//input[@id='columnValue']")

        # Table header locators
        self.send_order_headers = page.locator("//thead[@class='bg-200 text-900 text-nowrap align-middle thead']")
        self.thumbnail_header = page.locator("//th[text()='Thumbnail']")
        self.id_header = page.locator("//th[text()='ID']")
        self.date_created_header = page.locator("//th[text()='Date Created']")
        self.date_sent_header = page.locator("//th[text()='Date Sent']")
        self.status_header = page.locator("//th[text()='Status']")

        # Summary locators
        self.clik_on_send_order = page.locator("//tr[2]")
        self.summary_header = page.locator("//div[@class='modal-title h4']")

        # Send Information locators
        self.send_information = page.locator(
            "//button[@id='order-information-tab-tab-sendInformation']"
        )
        self.name = page.locator(
            "//p[text()='Name']"
        )
        self.send_order_status = page.locator("th:nth-child(6)")
        self.description = page.locator("//label[normalize-space()='Description']")
        self.order_id = page.locator("//p[normalize-space()='Send Id']")
        self.batch_id = page.locator("//p[text()='Batch ID']")
        self.item_sent = page.locator("//th[contains(text(),'Sent To')]")
        self.total_price = page.locator("//p[text()='Total Price']")
        self.item_vendor = page.locator("//p[text()='Item Vendor']")
        self.date_placed = page.locator("//p[text()='Date Placed']")

        # Delivery Information locators
        self.delivery_information = page.locator(
            "//button[@id='order-information-tab-tab-deliveryInformation']"
        )
        self.tracking_number = page.locator("//p[normalize-space()='Tracking Number :']")
        self.shipping_company = page.locator("//p[normalize-space()='Shipping Company :']")
        self.send_time = page.locator("//p[normalize-space()='EST.Arrival']")
        self.date_sent = page.locator("div[class='col-lg-6 col-12'] div:nth-child(1) div:nth-child(1) div:nth-child(1)")
        self.apply_button = page.locator("//button[text()='Apply']")
        self.cancel_button = page.locator("//button[text()='Cancel']")

        # Prospect Details locators
        self.prospect_hearder = page.locator("//div[@class='item-info-modal-admin']//thead[@class='bg-200 text-900 text-nowrap align-middle thead']")
        self.prospect_details = page.locator(
            "//button[@id='order-information-tab-tab-prospectDetails']"
        )
        self.prospact_info = page.locator("//div[@class='col-lg-5 col-12']")
        self.pd_name = page.locator(
            "//span[normalize-space()='Prospect Name']"
        )
        self.email = page.locator(
            "//div[@class='col-lg-5 col-12']//div[1]//div[1]"
        )
        self.select_rows_per_page_dropdown = page.locator(
            '//div[contains(@class,"ps-3 d-flex flex-wrap rows-page-count")]//select')

        # cross button locators
        self.cross_button = page.locator("//button[@class='btn-close']")
        self.all_orders_status = 'tbody tr:nth-child(1) td:nth-child(6) div:nth-child(1)'

    def click_on_dropdown_and_change_user_role(self, role_to_change):
        """
        Change user role from dropdown
        """
        self.change_role_dropdown.click()
        self.page.locator(
            self.role_to_select.replace("<<role_to_change>>", role_to_change)
        ).click()
        print(f"User role changed to {role_to_change}")

    def verify_and_click_on_send_order_list_tab(self, side_navigation_item):
        """
        Verify Users and click on send order list tab
        """
        # verify icon availability
        expect(self.Send_order_list_icon).to_be_visible()
        # clicking on send order list tab
        self.page.click(
            self.select_tab_from_side_navigation.replace(
                "<<tab_to_navigate>>", side_navigation_item
            )
        )
        print(f"successfully able to click on {side_navigation_item} tab")

    def verify_send_order_list_page_elements(self, headers_text):
        """
        Verify and check availability of send order list page elements
        """
        time.sleep(4)
        elements_to_check = [
            self.filter_icon,
            self.filter_main,
            self.thumbnail_header,
            self.id_header,
            self.date_created_header,
            self.date_sent_header,
            self.status_header,
            self.pagination_number,
            self.pagination_result,
            self.pagination_row_per_page,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("This is for main page -> All elements are visible on the page.")
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
        print("Verified send Order list Headers:" ,headers_text)

    def verify_click_on_send_order_summary(self,prospact_header):
        """
        Verify and check availability of send order list summary page elements
        """
        time.sleep(4)
        # Send Information tab elements
        self.clik_on_send_order.click()
        self.send_information.click()

        elements_to_check = [
            self.send_information,
            self.name,
            self.send_order_status,
            self.description,
            self.order_id,
            # self.batch_id,
            self.item_sent,
            self.total_price,
            self.item_vendor,
            self.date_placed,
        ]
        for element in elements_to_check:
            expect(element).to_be_visible()
        print(
            "This is for summary page -> Send Information tab -> All elements are visible on the page."
        )

        time.sleep(2)
        # Delivery Information tab elements
        self.delivery_information.click()
        elements_to_check = [
            self.delivery_information,
            self.tracking_number,
            self.shipping_company,
            self.send_time,
            self.date_sent,
           # self.apply_button,
           # self.cancel_button,
        ]
        for element in elements_to_check:
            expect(element).to_be_visible()
        print(
            "This is for summary page -> Delivery Information tab -> All elements are visible on the page."
        )

        # Prospect Details Tab elements
        self.prospect_details.click()
        elements_to_check = [
            self.prospect_details,
            self.prospact_info,
            self.pd_name,
            self.email,
        ]
        for element in elements_to_check:
            expect(element).to_be_visible()
        print(
            "This is for summary page -> Prospect Details Tab -> All elements are visible on the page."
        )
        headers_title = self.prospect_hearder.inner_text()
        cleaned_headers = re.sub(r"[🔼🔽]", "", headers_title).strip()
        # Split using either tabs or two or more spaces
        headers_list = [
            header.strip()
            for header in re.split(r"\t|\s{2,}", cleaned_headers)
            if header
        ]
        assert (
                headers_list == prospact_header
        ), f"Headers do not match: {headers_list} != {prospact_header}"
        print("Verified send Order list Headers:", prospact_header)

    def apply_filter_on_send_order_list_and_verify_filtered_data(
            self, available_filter_options, expected_statuses
    ):
        """
        Apply filter on send order list and verify filtered data
        """
        expect(self.filter_dropdown).to_be_visible()
        self.select_rows_per_page_dropdown.select_option('250')
        filter_options = self.page.query_selector_all(self.filter_options)
        filter_options_text = [option.inner_text() for option in filter_options]
        assert [filter_options_text] == available_filter_options, \
            f"Expected: {available_filter_options}, but got: {filter_options_text}"
        print(f"all available filters verified: {available_filter_options}")
        for filter_option in available_filter_options[
            0]:  # or just `available_filter_options` if it's already flattened
            self.filter_dropdown.select_option(filter_option)
            time.sleep(6)
            self.page.wait_for_selector(self.all_orders_status)

            all_orders_status = self.page.query_selector_all(self.all_orders_status)
            all_orders_status_text = [status.inner_text() for status in all_orders_status]

            print(f"Items status after applying '{filter_option}': {all_orders_status_text}")

            if filter_option in expected_statuses:
                expected = expected_statuses[filter_option]
                if expected:
                    for expected_status in expected:
                        assert (
                                expected_status in all_orders_status_text
                        ), f"'{expected_status}' not found in the status text for filter '{filter_option}'"
                else:
                    assert (
                        not all_orders_status_text
                    ), f"Expected no statuses for filter '{filter_option}', but found: {all_orders_status_text}"