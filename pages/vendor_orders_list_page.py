"""
Vendor Orders List module
"""

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
        self.pagination_options = page.locator(
            '//div[@class="d-flex pagination-numbers"]'
        )
        self.orders_list_icon = page.locator('//*[@data-icon="truck"]')
        self.select_tab_from_side_navigation = '//span[text()="<<tab_to_navigate>>"]'

        # Orders list page Locators
        self.filter_option = page.locator('//*[@class="filter-text-icon"]')
        self.order_number_header = page.locator("//th[text()='Order Number']")
        self.order_date_header = page.locator("//th[text()='Order Date']")
        self.item_name_header = page.locator("//th[text()='Item Name']")
        self.current_status_header = page.locator("//th[text()='Current Status']")
        self.action_header = page.locator("//th[text()='Actions']")

        # Orders list page pagination section Locators
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

    def verify_vendor_order_list_page_elements(self):
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
