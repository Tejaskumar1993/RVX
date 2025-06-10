"""
Sender account balance page modules
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


class SenderAccountBalancePage:
    """
    Module containing objects and methods related to sender account balance Page
    """

    def __init__(self, page: Page):
        super().__init__()
        self.page = page

        # Role locator
       # self.select_role_dropdown = page.locator('(//div[@class="dropdown"])[2]')
       # self.select_role = '//a[text()="<<select_role>>"]'

        # Side navigation tab
        self.account_balance_icon = page.locator('//*[@data-icon="dollar-sign"]')
        self.account_balance_tab = '//span[text()="<<tab_to_navigate>>"]'

        # account balance page locators
        self.account_balance_page_component = page.locator(
            '(//div[@class="mt-2 col-lg-4"])[1]'
        )
        self.account_balance_title = page.locator('//h4[text()="Account Balance"]')
        self.available_balance_content_box = page.locator('//div[@class="px-2 card"]')
        self.available_balance_title = page.locator('//div[text()="Available Balance"]')
        self.updated_time = page.locator('//div[@class="text-muted text-center"]')
        self.amount_content = page.locator('(//div[@class="pt-4 pb-3 card-body"])[1]')
        self.amount_spent_content_box = page.locator(
            '(//div[@class="mt-2 col-lg-4"])[2]'
        )
        self.amount_spent_title = page.locator('//div[text()="Amount Spent"]')
        self.spent_amount_content = page.locator(
            '(//div[@class="pt-4 pb-3 card-body"])[2]'
        )
        self.total_sends_content_box = page.locator(
            '(//div[@class="mt-2 col-lg-4"])[3]'
        )
        self.total_sends_title = page.locator('//div[text()="Total Sends"]')
        self.total_sends_content = page.locator(
            '(//div[@class="pt-4 pb-3 card-body"])[3]'
        )
        self.account_balance_history_content_box = page.locator(
            '//div[@class="py-3 mb-2 account-balance-card card"]'
        )
        self.debits_credits_tab = page.locator(
            '//button[@id="account-balance-dashboard-tab-tab-debts_&_credits"]'
        )
        self.debits_and_credits_title = page.locator('//h4[text()="Debits & Credits"]')
        self.filter_title = page.locator('//div[text()="Filter:"]')
        self.filter_dropdown = page.locator(
            '//div[@class="d-flex align-items-center mb-2"]'
        )
        self.select_filter_option = page.locator(
            '(//select[@class="generic-filter-select ms-2 form-select form-select-sm"])[1]'
        )
        self.history_table_headers = page.locator('//tr[@class="text-center"]')
        self.footer = page.locator(
            '//div[@class="table-footer-border-top card-footer"]'
        )
        self.pagination = page.locator('//div[@class="d-flex pagination-numbers m-auto mb-2"]')
        self.rows_count = page.locator(
            '//div[@class="d-flex align-items-center fs--1 ps-3 d-flex flex-wrap rows-page-count"]'
        )
        self.result_counter = page.locator(
            '//div[@class="d-flex align-items-center fs--1 ps-3"]'
        )
        self.date = "//time"

    @qase_screenshot
    @qase.step(
        title="Verify logged in user is able to change role to sender",
        expected="Logged in user should be able to change role",
    )
    # def verify_and_change_user_of_role(self, select_role):
    #     """
    #     Verify and change role of sender
    #     """
    #     expect(self.select_role_dropdown).to_be_visible()
    #     self.select_role_dropdown.click()
    #     self.page.wait_for_load_state("domcontentloaded")
    #     self.page.click(self.select_role.replace("<<select_role>>", select_role))
    #     print(f"successfully changed role to {select_role}")

    @qase_screenshot
    @qase.step(
        title="Verify account balance icon and tab working",
        expected="sender should be able to open and view account balance tab",
    )
    def verify_and_click_on_account_balance_tab(self, tab_to_navigate):
        """
        Verify account balance and click on account balance tab
        """
        # verify icon availability
        expect(self.account_balance_icon).to_be_visible()
        # clicking on account balance
        self.page.click(
            self.account_balance_tab.replace("<<tab_to_navigate>>", tab_to_navigate)
        )
        print(f"successfully able to click on {tab_to_navigate} tab")

    @qase_screenshot
    @qase.step(
        title="Verify account balance page elements",
        expected="User should be able to visible every elements of account balance page",
    )
    def verify_account_balance_page_elements(self, history_table_headers):
        """
        Verify and check availability of account balance page elements
        """
        elements_to_check = [
            self.account_balance_page_component,
            self.account_balance_title,
            self.available_balance_content_box,
            self.available_balance_title,
            self.updated_time,
            self.amount_content,
            self.amount_spent_content_box,
            self.amount_spent_title,
            self.spent_amount_content,
            self.total_sends_content_box,
            self.total_sends_title,
            self.total_sends_content,
            self.account_balance_history_content_box,
            self.debits_credits_tab,
            self.debits_and_credits_title,
            self.filter_title,
            self.filter_dropdown,
            self.history_table_headers,
            self.footer,
            self.pagination,
            self.rows_count,
            self.result_counter,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("account balance page elements verified")
        # Extract headers from the UI
        headers_title = self.history_table_headers.inner_text()
        print("Headers titles before cleanup -->", headers_title)
        cleaned_headers_title = re.sub(
            r"[🔼🔽]", "", headers_title
        ).strip()  # Remove sorting icons
        # Split the headers on tabs or multiple spaces
        headers_list = re.split(r"[\t]+|\s{2,}", cleaned_headers_title)
        headers_list = [
            header.strip() for header in headers_list if header
        ]  # Remove empty users
        # Assert the headers match the expected values
        assert (
            headers_list == history_table_headers
        ), f"Headers do not match: {headers_list} != {history_table_headers}"
        print("All elements verified")

    @qase_screenshot
    @qase.step(
        title="Apply filter and verify filtered transaction records",
        expected="Transaction record should be filtered correctly based on applied filter",
    )
    def apply_filter_on_transaction_record_and_verify_it(self, filter_options):
        """
        Apply filter and verify filtered data
        """
        for option in filter_options:
            print(f"Applying filter: {option}")
            time.sleep(3)  # Wait for the page to load before applying the filter
            self.page.wait_for_load_state("domcontentloaded")
            # Apply the filter
            time.sleep(2)
            self.select_filter_option.select_option(option)
            time.sleep(3)

            # Determine the date range based on the selected filter option
            date_range = None
            if option == "Previous Month":
                date_range = get_previous_month_range()
            elif option == "Previous Week":
                date_range = get_previous_week_range()
            elif option == "Quarter-1 : Jan-March":
                date_range = get_quarter_date_range(1)
            elif option == "Quarter-2 : April-June":
                date_range = get_quarter_date_range(2)
            elif option == "Quarter-3 : July-September":
                date_range = get_quarter_date_range(3)
            elif option == "Quarter-4 : October-December":
                date_range = get_quarter_date_range(4)

            # Retrieve all timestamps
            time_stamps = self.page.query_selector_all(self.date)

            # If date_range is set, proceed with validation; otherwise, handle "All Items" case
            if date_range:
                start_date, end_date = date_range
                # Parse dates within date range if they are strings
                start_date = (
                    datetime.strptime(start_date, "%m/%d/%Y").date()
                    if isinstance(start_date, str)
                    else start_date
                )
                end_date = (
                    datetime.strptime(end_date, "%m/%d/%Y").date()
                    if isinstance(end_date, str)
                    else end_date
                )
                print(f"Expected date range for '{option}': {start_date} to {end_date}")

                # Validate timestamps against the date range
                for timestamp in time_stamps:
                    date_str = timestamp.text_content()
                    record_date = None

                    # List of possible date formats
                    possible_formats = ["%m/%d/%Y %H:%M:%S", "%m/%d/%Y", "%Y-%m-%d"]

                    for fmt in possible_formats:
                        try:
                            # Try parsing the date with each format
                            record_date = datetime.strptime(date_str, fmt).date()
                            break  # Exit the loop if successful
                        except ValueError:
                            continue

                    if not record_date:
                        raise ValueError(f"Unrecognized date format: {date_str}")

                    # Assert that the record date is within the expected range
                    assert (
                        start_date <= record_date <= end_date
                    ), f"Record date {record_date} is out of range!"
