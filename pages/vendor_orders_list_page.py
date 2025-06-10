"""
Vendor Orders List module
"""
import re
# u

import time
from playwright.sync_api import Page, expect
from qase.pytest import qase

from pages.base_page import BasePage
from utilities.decorators import qase_screenshot


class VendorOrdersListPage(BasePage):
    """
    module for Vendor Orders List page actions
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Navigate to Orders list page Locators
        self.change_role_dropdown = page.locator('(//button[@id="dropdown-flags"])[2]')
        self.role_to_select = '//a[text()="<<role_to_change>>"]'
        self.filter_option = page.locator('//*[@class="filter-text-icon"]')
        self.filter_dropdown = page.locator("//select[contains(.,'All Orders')]")
        self.pagination_options = page.locator(
            '//div[@class="d-flex pagination-numbers"]'
        )
        self.orders_list_icon = page.locator('//a[contains(@class,"nav-link active")]')
        self.select_tab_from_side_navigation = '//span[text()="<<tab_to_navigate>>"]'

        # Orders list page Locators
        self.filter_option = page.locator('//*[@class="filter-text-icon"]')
        self.order_number_header = page.locator("//th[text()='Order Number']")
        self.order_date_header = page.locator("//th[text()='Order Date']")
        self.item_name_header = page.locator("//th[text()='Item Name']")
        self.current_status_header = page.locator("//th[text()='Current Status']")
        self.action_header = page.locator("//th[text()='Actions']")
        self.order_list_header_titles = page.locator("//thead[@class='bg-200 text-900 text-nowrap align-middle thead']")
        self.select_all_orders = page.locator("//select[contains(.,'All Orders')]")
        self.canceled_status = page.locator("//div[contains(text(),'Canceled')]")
        self.processing_status = page.locator("//div[contains(text(),'Processing')]")
        self.shipping_status = page.locator("//div[contains(text(),'Shipped')]")
        self.acknowledged_status = page.locator("//div[contains(text(),'Acknowledged')]")
        self.completed_status = page.locator("//div[contains(text(),'Completed')]")


        self.pagination_number = page.locator(
            "//div[@class='d-flex pagination-numbers m-auto mb-2']"
        )
        self.pagination_result = page.locator(
            "//div[@class='d-flex align-items-center fs--1 ps-3']"
        )
        self.pagination_row_per_page = page.locator(
            "//div[@class='d-flex align-items-center fs--1 ps-3 d-flex flex-wrap rows-page-count']"
            )

    @qase_screenshot
    @qase.step(
        title="click on user role dropdown and select role for Vendor",
        expected="User should be able to change role successfully for vendor",
    )
    # def click_on_dropdown_and_change_user_role(self, role_to_change):
    #     """
    #     Change user role from dropdown
    #     """
    #     time.sleep(5)
    #     self.change_role_dropdown.click()
    #     time.sleep(5)
    #     self.page.locator(
    #         self.role_to_select.replace("<<role_to_change>>", role_to_change)
    #     ).click()
    #     print(f"User role changed to {role_to_change}")

    @qase_screenshot
    @qase.step(
        title="Verify and click on vendor Orders List page",
        expected="User should be able to see orders list icon and able to click on orders list tab",
    )
    def verify_and_click_on_orders_list_tab(self, side_navigation_item):
        """
        Verify Users and click on Orders List tab
        """
        # verify icon availability
        expect(self.orders_list_icon).to_be_visible()
        # clicking on company information
        time.sleep(5)
        self.page.click(
            self.select_tab_from_side_navigation.replace(
                "<<tab_to_navigate>>", side_navigation_item
            )
        )
        print(f"successfully able to click on {side_navigation_item} tab")

    def verify_vendor_order_list_page_elements(self,users_table_headers):
        """
        Verify and check availability of send order list page elements
        """
        elements_to_check = [
            self.filter_option,
            self.order_number_header,
            self.order_date_header,
            self.item_name_header,
            self.current_status_header,
            self.action_header,
            self.pagination_number,
            self.pagination_result,
            self.pagination_row_per_page,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("This is for main page -> All elements are visible on the page.")
        headers_title = self.order_list_header_titles.inner_text()
        print("Headers titles before cleanup -->", headers_title)
        cleaned_headers_title = re.sub(
            r"[🔼🔽]", "", headers_title
        ).strip()  # Remove sorting icons
        # Split the headers on tabs or multiple spaces
        headers_list = re.split(r"\t+|\s{2,}", cleaned_headers_title)
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
        title="Verify order list filtered data with statues ",
        expected="User should be able to see orders list icon and able to click on orders list tab",
    )
    def verify_vendor_order_list_filter_data(self, available_filter_options, expected_statuses):
        expect(self.select_all_orders).to_be_visible()

        filter_options_text = self.select_all_orders.locator("option").all_inner_texts()
        assert filter_options_text == available_filter_options, (
            f"❌ Mismatch in filter options. Expected: {available_filter_options}, but got: {filter_options_text}"
        )
        print(f"✅ All available filters verified: {available_filter_options}")

        for filter_name in available_filter_options:
            self.select_all_orders.select_option(label=filter_name)
            print(f"🔄 Selected filter: {filter_name}")
            self.page.wait_for_timeout(1000)  # Better to replace with wait for network or locator

            time.sleep(5)
            expected = expected_statuses.get(filter_name, [])
            for status in set(expected):  # Use set to avoid duplicate checks
                status_elements = self.page.locator(f"//div[contains(text(),'{status}')]")
                count = status_elements.count()
                time.sleep(2)
                # Assert at least one matching status is visible
                assert count > 0, f"❌ No visible status '{status}' found for filter '{filter_name}'"
                visible_found = False
                for i in range(count):
                    if status_elements.nth(i).is_visible():
                        visible_found = True
                        break

                assert visible_found, f"❌ Status '{status}' found but not visible for filter '{filter_name}'"
                print(f"✅ Verified status '{status}' is visible for filter '{filter_name}'")
