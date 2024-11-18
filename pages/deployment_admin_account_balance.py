"""
Deployment Admin Account Balance page modules
"""

import re
import time

from playwright.sync_api import Page, expect
from qase.pytest import qase
from datetime import datetime, timedelta

from pages.base_page import BasePage
from utilities.decorators import qase_screenshot
from utilities.date_utils import (
    get_previous_month_range,
    get_previous_week_range,
    get_quarter_date_range,
)


class DeploymentAdminAccountBalancePage(BasePage):
    """
    Module containing objects and methods related to Deployment admin account balance page
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Role locator
        self.select_role_dropdown = page.locator('(//div[@class="dropdown"])[2]')
        self.select_role = '//a[text()="<<select_role>>"]'

        # Side navigation tab
        self.account_balance_icon = page.locator('(//span[@class="nav-link-icon"])[2]')
        self.account_balance_tab = '//span[text()="<<tab_to_navigate>>"]'

        # Account balance page locator
        self.balance_tab = page.locator('//button[text()="Balance"]')
        self.schedule_deposits = page.locator('//button[text()="Schedule Deposits"]')
        self.payment_method = page.locator('//button[text()="Payment Method"]')
        self.account_balance_tabs = '//button[text()="<<tab_to_navigate>>"]'
        self.balance_container = page.locator('//div[@class="mb-2  card"]')
        self.as_of_header = page.locator(
            '//div[@class="mb-2  card"]//div[text()="As Of"]'
        )
        self.balance_content_box_title = page.locator(
            '//div[@class="mb-2  card"]//div[text()="Balance"]'
        )
        self.account_balance_amount = page.locator(
            '(//div//span[@class="numeric-input"])[1]'
        )
        self.deposit_funds_button = page.locator('//button[text()="Deposit Funds"]')
        self.transaction_record_component = page.locator('(//div[@class="card"])[1]')
        self.transaction_record_header = page.locator('//tr[@class="text-center"]')
        self.filter_label = page.locator('//label[text()="Filter:"]')
        self.filter_dropdown = page.locator(
            '//select[@class="form-select form-select-sm"]'
        )
        self.select_option = page.locator(
            '//div[@class="d-flex align-items-center justify-content-between"]//select'
        )
        self.record_containers_header = "(//tr)[1]"
        self.time_stamp = "//td[7]"
        # Page footer locators
        self.footer_component = page.locator(
            '//div[@class="table-footer-border-top card-footer"]'
        )
        self.footer_pagination = page.locator(
            '//div[@class="d-flex pagination-numbers"]'
        )
        self.row_dropdown = page.locator(
            '//div[@class="d-flex align-items-center fs--1 ps-3 d-flex flex-wrap rows-page-count"]'
        )
        self.result_counter = page.locator(
            '//div[@class="d-flex align-items-center fs--1 ps-3"]'
        )

        # schedule deposits locators
        self.schedule_deposits_component = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-schedule-deposit"]'
        )
        self.schedule_deposits_balance_component = page.locator(
            '//div[@class="mt-2 col-lg-5 col-md-6"]'
        )
        self.schedule_deposits_balance_title = page.locator(
            '(//div[text()="Balance"])[2]'
        )
        self.schedule_deposits_as_of_header = page.locator('(//div[text()="As Of"])[2]')
        self.schedule_deposits_balace_amount = page.locator(
            '(//span[@class="numeric-input"])[3]'
        )
        self.current_auto_refills_component = page.locator(
            '//div[@class="h-100 current-auto-refill-card card"]'
        )
        self.current_auto_refills_header = page.locator(
            '//div[text()="Current Auto Refills"]'
        )
        self.current_auto_refill_switch = page.locator(
            '//div[@class="d-flex justify-content-end"]//button'
        )
        self.minimum_account_balance_component = page.locator(
            '(//div[@class="mt-5 pt-4 pb-3 px-4 rounded-5 input-cards card"])[1]'
        )
        self.when_balance_is_below_title = page.locator(
            '//label[text()="When balance is below"]'
        )
        self.minimum_account_balance_add_this_amount = page.locator(
            '(//label[text() = "Add This Amount"])[1]'
        )
        self.minimum_account_balance_start_date = page.locator(
            '(//label[text() = "Start Date"])[1]'
        )
        self.minium_account_balance_start_date_input = page.locator(
            '//input[@name="startDate"]'
        )
        self.minium_account_balance_end_date_input = page.locator(
            '//input[@name="endDate"]'
        )
        self.minimum_account_balance_end_date = page.locator(
            '(//label[text() = "End Date"])[1]'
        )
        self.minium_account_balance_header = page.locator(
            '//h5[text()="Minimum Account Balance"]'
        )
        self.minium_account_balance_accept_changes_button = page.locator(
            '(//button[text()="Accept Changes"])[1]'
        )
        self.minium_account_balance_clear_button = page.locator(
            '(//button[text()="Clear"])[1]'
        )
        self.minium_account_balance_below_amount_input = page.locator(
            '//input[@name="belowAmount"]'
        )
        self.minium_account_balance_auto_fund_input = page.locator(
            '//input[@name="autoFundAmount"]'
        )
        self.set_up_new_auto_refill_component = page.locator(
            '(//div[@class="mt-5 pt-4 pb-3 px-4 rounded-5 input-cards card"])[2]'
        )
        self.set_up_new_auto_refill_header = page.locator(
            '//h5[text()="Set Up New Auto Refill"]'
        )
        self.set_up_new_auto_refill_every = page.locator('//label[text()="Every"]')
        self.set_up_new_auto_refill_add_this_amount = page.locator(
            '(//label[text() = "Add This Amount"])[2]'
        )
        self.set_up_new_auto_refill_start_date = page.locator(
            '(//label[text() = "Start Date"])[2]'
        )
        self.set_up_new_auto_refill_end_date = page.locator(
            '(//label[text() = "End Date"])[2]'
        )
        self.set_up_new_auto_refill_accept_changes_button = page.locator(
            '(//button[text()="Accept Changes"])[2]'
        )
        self.set_up_new_auto_refill_clear_button = page.locator(
            '(//button[text()="Clear"])[2]'
        )
        self.set_up_new_auto_refill_fund_amount_input = page.locator(
            '//input[@name="fundAmount"]'
        )
        self.set_up_new_auto_refill_select_occurence_dropdown = page.locator(
            '//span[@class="ant-select-selection-item"]'
        )
        self.select_occurence_option = '//div[text()="<<select_occurence>>"]'
        self.set_up_new_auto_refill_start_date_input = page.locator(
            '//input[@name="autoFundPeriodStart"]'
        )
        self.set_up_new_auto_refill_end_date_input = page.locator(
            '//input[@name="autoFundPeriodEnd"]'
        )
        self.current_auto_refill_dialog_box = page.locator(
            '//div[@class="modal-content"]'
        )
        self.current_auto_refill_confirm_message = page.locator(
            '//div[@class="modal-body"]'
        )
        self.generic_update_button = page.locator('//button[text()="Confirm"]')
        self.current_auto_refill_cancel_button = page.locator(
            '//button[text()="Cancel"]'
        )
        self.added_minium_account_balance_in_current_auto_refills = page.locator(
            '//div[@class="h-100 current-auto-refill-card card"]//div[@class="pt-0 card-body"]'
        )
        self.added_minium_amount = page.locator('//div[@class="col-md-7"]')
        self.remove_button_of_current_auto_refills = page.locator(
            "//div[@class='pt-0 card-body']/div/div[@class='col-md-2']/div/button[1]"
        )
        self.edit_button_of_current_auto_refills = page.locator(
            "//div[@class='pt-0 card-body']/div/div[" "@class='col-md-2']/div/button[2]"
        )
        self.success_message = page.locator(
            '//div[@class="ant-message-custom-content ant-message-success"]'
        )

        # card details
        self.card_details_header = page.locator('//h3[text()="Card Details"]')
        self.name_on_card_label = page.locator('//label[text()="Name on Card"]')
        self.name_on_card_input = page.locator('//input[@name="nameOnCard"]')
        self.card_number_label = page.locator('//label[text()="Card Number"]')
        self.card_number_input = page.locator('//input[@name="cardNumber"]')
        self.expiry_date_label = page.locator('//label[text()="Expiry Date"]')
        self.expiry_date_input = page.locator('//input[@name="expireDate"]')
        self.cvv_label = page.locator('//label[text()="CVV"]')
        self.cvv_input = page.locator('//input[@name="cvv"]')
        # billing address
        self.billing_address_header = page.locator('//h3[text()="Billing Address"]')
        self.name_label = page.locator('//label[text()="Name"]')
        self.name_input = page.locator('//input[@name="fullName"]')
        self.address_line_1_label = page.locator('//label[text()="Address Line 1"]')
        self.address_line_1_input = page.locator('//input[@name="address1"]')
        self.address_line_2_label = page.locator('//label[text()="Address Line 2"]')
        self.address_line_2_input = page.locator('//input[@name="address2"]')
        self.city_label = page.locator('//label[text()="City"]')
        self.city_input = page.locator('//input[@name="city"]')
        self.select_state_label = page.locator('//label[text()="Select State"]')
        self.select_state_dropdown = page.locator(
            '(//input[@class="ant-select-selection-search-input"])[2]'
        )
        self.select_state = '//div[text()="<<state_to_select>>"]'
        self.zip_label = page.locator('//label[text()="Zip"]')
        self.zip_input = page.locator('//input[@name="zipCode"]')
        self.cards_we_accept_image = page.locator(
            'img[src="/static/media/WeAcceptCards.9c53dd7959e40bbaa392.png"]'
        )
        self.save_button = page.locator('//button[text()="Save"]')
        self.clear_button = page.locator(
            '//button[@class="my-3 px-4 cancel-btn btn"][text()="Clear"]'
        )
        self.alert_message = page.locator('//div[@class="ant-message-notice-content"]')

        # deposit funds locators
        self.deposit_funds_header = page.locator('//div[text()="Deposit Funds"]')
        self.select_card_label = page.locator('//label[@title="Select Card"]')
        self.select_card_dropdown = page.locator(
            '//div[@class="modal-content"]//div[@class="ant-select-selector"]'
        )
        self.deposit_amount_label = page.locator('//label[@title="Deposit Amount"]')
        self.deposit_amount_input = page.locator('//input[@id="amount"]')
        self.deposit_funds_save_button = page.locator(
            '//div[@class="modal-content"]//button[text()="Save"]'
        )
        self.deposit_funds_clear_button = page.locator(
            '//div[@class="modal-content"]//button[text()="Clear"]'
        )

    @qase_screenshot
    @qase.step(
        title="Verify account balance icon and tab working",
        expected="deployment admin should be able to open and view account balance tab",
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
        title="Verify logged in user is able to change role to deployment admin",
        expected="Logged in user should be able to change role",
    )
    def verify_and_change_user_role(self, select_role):
        """
        Verify and change role of user
        """
        expect(self.select_role_dropdown).to_be_visible()
        self.select_role_dropdown.click()
        self.page.wait_for_load_state("domcontentloaded")
        self.page.click(self.select_role.replace("<<select_role>>", select_role))
        print(f"successfully changed role to {select_role}")

    @qase_screenshot
    @qase.step(
        title="Verify Account Balance page element visibility",
        expected="Deployment admin should be able to visible all elements of the account balance page",
    )
    def verify_account_balance_page_elements(
        self, transaction_record_columns_title, available_filter_options
    ):
        """
        Verify account balance page elements
        """
        self.page.wait_for_load_state("domcontentloaded")
        elements_to_check = [
            self.balance_tab,
            self.schedule_deposits,
            self.payment_method,
            self.balance_container,
            self.balance_content_box_title,
            self.as_of_header,
            self.deposit_funds_button,
            self.transaction_record_header,
            self.transaction_record_component,
            self.footer_component,
            self.footer_pagination,
            self.row_dropdown,
            self.result_counter,
            self.filter_label,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        header_text = self.transaction_record_header.inner_text()
        headers = header_text.strip().split("\t")
        print(f"Extracted Headers: {headers}")
        # Verify that the headers match the expected column titles
        assert (
            headers == transaction_record_columns_title
        ), f"Expected headers {transaction_record_columns_title}, but found {headers}"
        filter_options_raw = self.filter_dropdown.inner_text()
        filter_options = [
            option.strip()
            for option in filter_options_raw.splitlines()
            if option.strip()
        ]
        print(f"Extracted Filter Options: {filter_options}")
        assert (
            filter_options == available_filter_options
        ), f"Expected filter options {available_filter_options}, but found {filter_options}"
        time.sleep(2)
        balance_amount = self.account_balance_amount.text_content()
        print(f"available balance {balance_amount}")

    @qase_screenshot
    @qase.step(
        title="Verify deposit funds functionality",
        expected="deposit funds functionality should be working as expected and added funds get reflected in balance",
    )
    def verify_deposit_funds_functionality(self, select_card, amount_to_add):
        """
        verify deposit funds functionality of balance page
        """
        time.sleep(5)
        # Get current account balance and extract numerical value using regex
        current_amount_str = self.account_balance_amount.text_content()
        current_amount = float(
            re.sub(r"[^\d.]", "", current_amount_str)
        )  # Remove any non-numeric characters
        # Ensure amount_to_add is a numeric type (float or int)
        amount_to_add = float(
            amount_to_add
        )  # Convert to float in case it's passed as a string
        # Click on the deposit funds button
        self.deposit_funds_button.click()
        elements_to_check = [
            self.select_card_label,
            self.deposit_amount_label,
            self.deposit_amount_input,
            self.select_card_dropdown,
            self.deposit_funds_save_button,
            self.deposit_funds_clear_button,
        ]
        # Ensure all required elements are visible
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        # Select the card and fill in the deposit amount
        self.select_card_dropdown.click()
        time.sleep(2)
        self.page.locator(f'(//div[text()="{select_card}"])[1]').click()
        self.deposit_amount_input.fill(
            str(amount_to_add)
        )  # Convert amount_to_add to string if necessary
        # Click the save button to deposit funds
        self.deposit_funds_save_button.click()
        time.sleep(10)
        # Get updated account balance and convert to float
        updated_amount_str = self.account_balance_amount.text_content()
        updated_amount = float(
            re.sub(r"[^\d.]", "", updated_amount_str)
        )  # Remove any non-numeric characters
        # Print debug information
        print(f"Current Amount: {current_amount}")
        print(f"Amount to Add: {amount_to_add}")
        expected_amount = current_amount + amount_to_add
        print(f"Expected Amount: {expected_amount}")
        # Assert that the updated balance is the current balance plus the added amount
        assert (
            expected_amount == updated_amount
        ), f"Expected {expected_amount}, but got {updated_amount}"

    @qase_screenshot
    @qase.step(
        title="Apply filter and verify filtered transaction records",
        expected="Transaction record should be filtered correctly based on applied filter",
    )
    def apply_filter_on_transaction_record__and_verify_it(self, filter_options):
        """
        Apply filter and verify filtered data
        """
        for option in filter_options:
            print(f"Applying filter: {option}")
            time.sleep(3)  # Wait for the page to load before applying the filter
            self.page.wait_for_load_state("domcontentloaded")

            # Apply the filter
            self.filter_dropdown.select_option(option)
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
            time_stamps = self.page.query_selector_all(self.time_stamp)

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
                    # Parsing each timestamp date
                    date_str = timestamp.text_content()
                    try:
                        record_date = datetime.strptime(
                            date_str, "%m/%d/%Y %H:%M:%S"
                        ).date()
                    except ValueError:
                        record_date = datetime.strptime(date_str, "%m/%d/%Y").date()

                    # Assert that the record date is within the expected range
                    assert (
                        start_date <= record_date <= end_date
                    ), f"Record date {record_date} is out of range!"

    @qase_screenshot
    @qase.step(
        title="Verify Schedule deposits page elements",
        expected="user should be able to see all elements of the schedule deposits page",
    )
    def verify_schedule_deposits_page_elements(self, tab_to_navigate):
        """
        Verify schedule deposits page locators
        """
        self.page.click(
            self.account_balance_tabs.replace("<<tab_to_navigate>>", tab_to_navigate)
        )
        elements_to_check = [
            self.schedule_deposits_component,
            self.schedule_deposits_balance_component,
            self.schedule_deposits_balance_title,
            self.schedule_deposits_as_of_header,
            self.schedule_deposits_balace_amount,
            self.current_auto_refills_component,
            self.current_auto_refills_header,
            self.current_auto_refill_switch,
            self.minimum_account_balance_component,
            self.set_up_new_auto_refill_component,
            self.minium_account_balance_header,
            self.set_up_new_auto_refill_header,
            self.when_balance_is_below_title,
            self.minimum_account_balance_add_this_amount,
            self.minimum_account_balance_start_date,
            self.set_up_new_auto_refill_end_date,
            self.minimum_account_balance_end_date,
            self.set_up_new_auto_refill_start_date,
            self.set_up_new_auto_refill_add_this_amount,
            self.set_up_new_auto_refill_every,
            self.minium_account_balance_accept_changes_button,
            self.set_up_new_auto_refill_accept_changes_button,
            self.set_up_new_auto_refill_clear_button,
            self.minium_account_balance_clear_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("elements verified successfully")

    @qase_screenshot
    @qase.step(
        title="Verify minimum account balance functionality",
        expected="user should be able to add edit and cancel minium amount balance and verified balance in current auto refills",
    )
    def add_and_verify_new_added_minimum_account_balance(
        self,
        confirm_message,
        below_amount,
        auto_fund_amount,
        confirm_message_of_auto_refill_deletion,
        new_auto_fund_amount,
    ):
        """
        Add and verify newly added minimum account balance, update and delete it.
        """
        # Click the auto refill switch and expect dialog box
        self.current_auto_refill_switch.click()
        expect(self.current_auto_refill_dialog_box).to_be_visible()

        # Verify confirm message and click the confirm button
        confirm_message_text = self.current_auto_refill_confirm_message.text_content()
        print(f"Confirm message text is: {confirm_message_text}")
        assert confirm_message_text == confirm_message
        self.generic_update_button.click()

        # Fill the below amount and auto fund amount inputs
        print(
            f"Filling below amount: {below_amount} and auto fund amount: {auto_fund_amount}"
        )
        self.minium_account_balance_below_amount_input.fill(below_amount)
        self.minium_account_balance_auto_fund_input.fill(auto_fund_amount)

        # Select start and end dates (current and next day)
        print("Selecting start and end dates (current day and next day).")
        current_day = datetime.now().day
        self.minium_account_balance_start_date_input.click()
        self.page.locator(f'(//div[text()="{current_day}"])[1]').click()

        next_day = (datetime.now() + timedelta(days=1)).day
        self.minium_account_balance_end_date_input.click()
        self.page.locator(f'(//div[text()="{next_day}"])[1]').click()

        # Click accept changes and verify the message
        self.minium_account_balance_accept_changes_button.click()
        expect(self.current_auto_refill_dialog_box).to_be_visible()
        confirm_message_text = self.current_auto_refill_confirm_message.text_content()
        print(f"Confirm message text is: {confirm_message_text}")
        assert confirm_message_text == confirm_message
        self.generic_update_button.click()

        # Verify the success message and the added amount
        print("Expecting success message and verifying added amount.")
        expect(self.success_message).to_be_visible()
        success_message_text = self.success_message.text_content()
        print(success_message_text)

        expect(
            self.added_minium_account_balance_in_current_auto_refills
        ).to_be_visible()
        added_amount_text = (
            self.added_minium_account_balance_in_current_auto_refills.text_content()
        )
        print(f"Added amount text: {added_amount_text}")
        assert (
            added_amount_text
            == f"when amount is below ${below_amount} - ADD ${auto_fund_amount}"
        )

        # Edit the added auto fund amount
        print("Editing auto fund amount.")
        self.edit_button_of_current_auto_refills.click()
        self.minium_account_balance_auto_fund_input.fill(new_auto_fund_amount)
        self.minium_account_balance_end_date_input.click()
        self.page.locator(f'(//div[text()="{next_day}"])[1]').click()
        self.minium_account_balance_accept_changes_button.click()

        # Verify edited changes
        expect(self.current_auto_refill_dialog_box).to_be_visible()
        confirm_message_text = self.current_auto_refill_confirm_message.text_content()
        print(f"Confirm message text is: {confirm_message_text}")
        assert confirm_message_text == confirm_message
        self.generic_update_button.click()

        # Verify success message and the edited amount
        print("Expecting success message for edited amount.")
        expect(self.success_message).to_be_visible()
        success_message_text = self.success_message.text_content()
        print(success_message_text)

        time.sleep(2)  # Wait for changes to reflect
        edited_amount_text = (
            self.added_minium_account_balance_in_current_auto_refills.text_content()
        )
        print(f"Edited amount text: {edited_amount_text}")
        assert (
            edited_amount_text
            == f"when amount is below ${below_amount} - ADD ${new_auto_fund_amount}"
        )

        # Delete the auto refill and verify confirmation message
        print("Deleting auto refill and verifying deletion confirmation.")
        self.remove_button_of_current_auto_refills.click()
        expect(self.current_auto_refill_dialog_box).to_be_visible()

        confirm_message_text_1 = self.current_auto_refill_confirm_message.text_content()
        print(f"Confirm message text for deletion: {confirm_message_text_1}")
        assert confirm_message_text_1 == confirm_message_of_auto_refill_deletion
        self.generic_update_button.click()

        # Final click on the auto refill switch to complete the process
        self.current_auto_refill_switch.click()

    @qase_screenshot
    @qase.step(
        title="Add and verify newly set auto refill, update, and delete it.",
        expected="The auto refill should be added, updated, and deleted successfully with proper messages.",
    )
    def add_and_verify_set_up_new_auto_refill(
        self,
        confirm_message,
        below_amount,
        select_occurence,
        new_auto_fund_amount,
        confirm_message_of_auto_refill_deletion,
    ):
        """
        verify set up new auto refill functionality
        """
        # Click the auto refill switch and expect dialog box
        self.current_auto_refill_switch.click()
        expect(self.current_auto_refill_dialog_box).to_be_visible()

        # Verify confirm message and click the confirm button
        confirm_message_text = self.current_auto_refill_confirm_message.text_content()
        print(f"Confirm message text is: {confirm_message_text}")
        assert confirm_message_text == confirm_message
        self.generic_update_button.click()

        # Fill the below amount and auto fund amount inputs
        print(f"Filling below amount: {below_amount}")
        self.set_up_new_auto_refill_fund_amount_input.fill(below_amount)
        self.set_up_new_auto_refill_select_occurence_dropdown.click()
        self.page.locator(
            self.select_occurence_option.replace(
                "<<select_occurence>>", select_occurence
            )
        ).click()
        current_day = datetime.now().day
        self.set_up_new_auto_refill_start_date_input.click()
        self.page.locator(f'(//div[text()="{current_day}"])[1]').click()
        self.set_up_new_auto_refill_end_date_input.click()
        next_day = (datetime.now() + timedelta(days=1)).day
        self.page.locator(f'(//div[text()="{next_day}"])[1]').click()

        # Click accept changes and verify the message
        self.set_up_new_auto_refill_accept_changes_button.click()
        expect(self.current_auto_refill_dialog_box).to_be_visible()
        confirm_message_text = self.current_auto_refill_confirm_message.text_content()
        print(f"Confirm message text is: {confirm_message_text}")
        assert confirm_message_text == confirm_message
        self.generic_update_button.click()

        # Verify the success message and the added amount
        print("Expecting success message and verifying added amount.")
        expect(self.success_message).to_be_visible()
        success_message_text = self.success_message.text_content()
        print(success_message_text)

        expect(
            self.added_minium_account_balance_in_current_auto_refills
        ).to_be_visible()
        added_amount_text = (
            self.added_minium_account_balance_in_current_auto_refills.text_content()
        )
        print(f"Added amount text: {added_amount_text}")
        assert added_amount_text == f"Monthly- ADD${below_amount}"

        # Edit the added auto fund amount
        print("Editing auto fund amount.")
        self.edit_button_of_current_auto_refills.click()
        self.set_up_new_auto_refill_fund_amount_input.fill(new_auto_fund_amount)
        self.minium_account_balance_end_date_input.click()
        self.page.locator(f'(//div[text()="{next_day}"])[1]').click()
        self.set_up_new_auto_refill_accept_changes_button.click()

        # Verify edited changes
        expect(self.current_auto_refill_dialog_box).to_be_visible()
        confirm_message_text = self.current_auto_refill_confirm_message.text_content()
        print(f"Confirm message text is: {confirm_message_text}")
        assert confirm_message_text == confirm_message
        self.generic_update_button.click()

        # Verify success message and the edited amount
        print("Expecting success message for edited amount.")
        expect(self.success_message).to_be_visible()
        success_message_text = self.success_message.text_content()
        print(success_message_text)

        time.sleep(2)  # Wait for changes to reflect
        edited_amount_text = (
            self.added_minium_account_balance_in_current_auto_refills.text_content()
        )
        print(f"Edited amount text: {edited_amount_text}")
        assert edited_amount_text == f"Monthly- ADD${new_auto_fund_amount}"

        # Delete the auto refill and verify confirmation message
        print("Deleting auto refill and verifying deletion confirmation.")
        self.remove_button_of_current_auto_refills.click()
        expect(self.current_auto_refill_dialog_box).to_be_visible()

        confirm_message_text_1 = self.current_auto_refill_confirm_message.text_content()
        print(f"Confirm message text for deletion: {confirm_message_text_1}")
        assert confirm_message_text_1 == confirm_message_of_auto_refill_deletion
        self.generic_update_button.click()

        # Final click on the auto refill switch to complete the process
        self.current_auto_refill_switch.click()

    @qase_screenshot
    @qase.step(
        title="Verify Payment Method Elements and Add New Card Functionality",
        expected="Payment Method Elements:All elements are displayed correctly and are functional."
        "Add New Card Functionality:User can successfully add a valid card.Appropriate error messages "
        "are shown for invalid inputs.Newly added card appears in the list of payment methods.",
    )
    def verify_payment_method_page_elements(
        self,
        tab_to_navigate,
        card_number,
        cvv,
        expiry_date,
        name_on_card,
        name,
        addressline1,
        city,
        zip,
        success_message_text,
        state_to_select,
        delete_message_text,
    ):
        """
        Verify payment method page elements and add new card
        """
        self.page.click(
            self.account_balance_tabs.replace("<<tab_to_navigate>>", tab_to_navigate)
        )
        elements_to_verify = [
            self.card_details_header,
            self.name_on_card_label,
            self.card_number_label,
            self.expiry_date_label,
            self.cvv_label,
            self.billing_address_header,
            self.name_label,
            self.address_line_1_label,
            self.address_line_2_label,
            self.city_label,
            self.zip_label,
            self.save_button,
            self.clear_button,
            self.cards_we_accept_image,
        ]
        for elements in elements_to_verify:
            expect(elements).to_be_visible()
        self.name_on_card_input.fill(name_on_card)
        self.card_number_input.fill(card_number)
        self.expiry_date_input.fill(expiry_date)
        self.name_input.fill(name)
        self.address_line_1_input.fill(addressline1)
        self.city_input.fill(city)
        self.zip_input.fill(zip)
        self.save_button.click()
        self.cvv_input.fill(cvv)
        self.select_state_dropdown.click()
        self.select_state_dropdown.fill("Te")
        # Replace <<state_to_select>> in the XPath with the selected state
        xpath = f'//div[@class="ant-select-item-option-content"][text()="{state_to_select}"]'
        time.sleep(5)
        # Find and click the element matching the state name
        self.page.locator(xpath).click()
        self.save_button.click()
        time.sleep(5)
        expect(self.alert_message).to_be_visible()
        success_card_message = self.alert_message.text_content()
        print(f"success message : {success_card_message}")
        assert success_card_message == success_message_text
        self.page.locator(
            f'//div//label[text()="{name_on_card}"]//..//button[text()="Delete Card"]'
        ).click()
        time.sleep(3)
        self.generic_update_button.click()
        expect(self.alert_message).to_be_visible()
        delete_card_message = self.alert_message.text_content()
        print(f"delete message : {delete_card_message}")
        assert delete_card_message == delete_message_text
