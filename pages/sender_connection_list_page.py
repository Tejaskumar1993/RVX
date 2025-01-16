"""
Sender Connection list page modules
"""

import re
import time
from datetime import datetime

from playwright.sync_api import Page, expect
from qase.pytest import qase

from utilities.date_utils import (
    get_previous_month_range,
    get_previous_week_range,
    get_quarter_date_range,
)
from utilities.decorators import qase_screenshot


class SenderConnectionListPage:
    """
    Module containing objects and methods related to sender Connection list Page
    """

    def __init__(self, page: Page):
        super().__init__()
        self.page = page

        # Role locator
        self.select_role_dropdown = page.locator('(//div[@class="dropdown"])[2]')
        self.select_role = '//a[text()="<<select_role>>"]'
        # Side navigation tab
        self.connection_list_icon = page.locator('//*[@data-icon="circle-arrow-up"]')
        self.connection_list_tab = '//span[text()="<<tab_to_navigate>>"]'
        # connection list page locators
        self.connection_list_page_component = page.locator('//div[@class="content"]')
        self.filter_label = page.locator('//*[text()="Filter:"]')
        # self.filter_drop_down = '//select[@class="generic-filter-select ms-2 form-select form-select-sm"]//option'
        self.filter_option = page.locator('//option[@value="custom"]')
        self.filter_option_sub_option = page.locator(
            '//select[@class="select-width form-select form-select-sm"]'
        )
        self.header_titles = page.locator('//tr[@class="text-center"]')
        self.pagination = page.locator('//div[@class="d-flex pagination-numbers"]')
        self.results_counter = page.locator(
            '//div[@class="d-flex align-items-center fs--1 ps-3"]'
        )
        self.rows_per_page = page.locator(
            '//div[@class="d-flex align-items-center fs--1 ps-3 d-flex flex-wrap rows-page-count"]'
        )
        self.connection_list_filters_options = (
            "//select[@class='select-width form-select form-select-sm']/option"
        )

    @qase_screenshot
    @qase.step(
        title="Verify logged in user is able to change role to sender",
        expected="Logged in user should be able to change role",
    )
    def verify_and_change_user_of_role(self, select_role):
        """
        Verify and change role of sender
        """
        expect(self.select_role_dropdown).to_be_visible()
        self.select_role_dropdown.click()
        self.page.wait_for_load_state("domcontentloaded")
        self.page.click(self.select_role.replace("<<select_role>>", select_role))
        print(f"successfully changed role to {select_role}")

    @qase_screenshot
    @qase.step(
        title="Verify connection list icon and tab working",
        expected="sender should be able to open and view connection list tab",
    )
    def verify_and_click_on_connection_list_tab(self, tab_to_navigate):
        """
        Verify account balance and click on account balance tab
        """
        # verify icon availability
        expect(self.connection_list_icon).to_be_visible()
        # clicking on account balance
        self.page.click(
            self.connection_list_tab.replace("<<tab_to_navigate>>", tab_to_navigate)
        )
        print(f"successfully able to click on {tab_to_navigate} tab")

    @qase_screenshot
    @qase.step(
        title="Verify connection list elements",
        expected="connection list elements should be visible",
    )
    def verify_connection_list_page_elements(self, headers_text=None):
        """
        Verify and check the visibility of items on the connection list page.
        """
        time.sleep(5)

        elements_to_check = [
            self.connection_list_page_component,
            self.filter_label,
            self.header_titles,
            self.pagination,
            self.results_counter,
            self.rows_per_page,
        ]

        for element in elements_to_check:
            try:
                expect(element).to_be_visible()
            except AssertionError as e:
                print(f"Element not visible: {element} - {str(e)}")
                raise
        print("All visible elements verified.")

    @qase_screenshot
    @qase.step(
        title="Apply filter on connection list and verify filtered data",
        expected="Data should be filtered properly based on the applied filter.",
    )
    def apply_filter_on_connection_list_and_verify_filtered_data(
        self, available_filter_options, expected_statuses
    ):
        """
        Apply filter on items list and verify filtered data
        """
        expect(self.connection_list_filters_options).to_be_visible()
        filter_options = self.page.query_selector_all(
            self.connection_list_filters_options
        )
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
