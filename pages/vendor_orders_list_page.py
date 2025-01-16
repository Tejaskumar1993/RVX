"""
Vendor Orders List module
"""

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

        # Locators
        self.change_role_dropdown = page.locator('(//button[@id="dropdown-flags"])[2]')
        self.role_to_select = '//a[text()="<<role_to_change>>"]'
        self.filter_option = page.locator('//*[@class="filter-text-icon"]')
        self.pagination_options = page.locator(
            '//div[@class="d-flex pagination-numbers"]'
        )
        self.orders_list_icon = page.locator('//*[@data-icon="truck"]')
        self.select_tab_from_side_navigation = '//span[text()="<<tab_to_navigate>>"]'

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
