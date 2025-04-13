"""
System Admin Deployments page modules
"""

import re
import time

import playwright
from playwright.sync_api import Page, expect
from qase.pytest import qase
from pages.base_page import BasePage
from utilities.decorators import qase_screenshot


class SystemAdminDeploymentsPage(BasePage):
    """
    Module containing objects and methods related to System Admin deployments Page
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # System admin Deployments page locators
        self.deployments_icon = page.locator('(//span[@class="nav-link-icon"])[3]')
        self.deployments_tab = '//span[text()="<<side_navigation_tabs>>"]'

        # Deployments list Filters locators
        self.deployment_summary_tab_navigation = (
            '//button[text()="<<tab_to_navigate>>"]'
        )
        self.dropdown = page.locator(
            '//*[@id="root"]/div/div/div[1]/div/div/div[1]/div/select'
        )
        self.all_users_status = '//div[contains(@class, "badge-soft-success") or contains(@class, "badge-soft-danger")]'
        self.batch_action_title = page.locator('//label[text()="Batch Action"]')
        self.batch_action_dropdown = page.locator(
            '//div[@class="d-flex align-items-center"]//select'
        )
        self.user_page_header_component = page.locator('//div[@class="mb-2 card"]')
        self.user_page_list_component = page.locator('//div[@class="card"]')
        self.user_list_headers = page.locator('//tr[@class="text-center"]')
        self.user_page_footer = page.locator(
            '//div[@class="table-footer-border-top card-footer"]'
        )
        self.user_checkbox = page.locator('(//tr//input[@type="checkbox"])[2]')
        self.deployment_name = page.locator("(//td)[3]")
        self.apply_batch_action_button = page.locator('//button[text()="Apply Action"]')
        self.deployment_delete_success_message = page.locator(
            '//div[@class="ant-message-custom-content ant-message-success"]'
        )
        self.button_to_change_action = page.locator(
            '(//div[@class="d-flex justify-content-center align-items-center"]//button)[1]'
        )
        self.delete_button = page.locator('//a[text()="Delete"]')
        self.confirm_button = page.locator("//button[text() = 'Confirm']")
        self.select_deployment = page.locator("(//tr)[2]")
        self.deployment_summary_model = page.locator('//div[@class="modal-content"]')
        self.deployment_summary_title = page.locator(
            '//div[text()="Deployment Summary"]'
        )
        self.deployment_summary_users_tab = page.locator('//button[text()="Users"]')
        self.deployment_summary_published_items_tab = page.locator(
            '//button[text()="Published Items"]'
        )
        self.deployment_summary_sends_tab = page.locator('//button[text()="Sends"]')
        self.deployment_summary_account_balance_tab = page.locator(
            '//button[text()="Account Balance"]'
        )
        self.deployment_summary_information_tab = page.locator(
            '//button[text()="Information"]'
        )
        self.deployment_summary_users_filter = page.locator(
            '//*[@id="order-information-tab-tabpane-users"]/div/div[1]/div/div/div[1]/div/select'
        )
        self.deployment_summary_user_filter_dropdown = page.locator(
            '//div[@class="deployment-summary-content"]//div[@class="card-body"]//select'
        )
        self.deployment_summary_user_dropdown_options = '//div[@class="deployment-summary-content"]//select[@class="form-select form-select-sm"]//option'

        # Users tab locators
        self.users_profile_image = page.locator('//div[text()="Profile Image"]')
        self.users_id = page.locator('(//th[text()="ID"])[2]')
        self.user_name = page.locator("//th[text()='Username']")
        self.user_tab_header = page.locator('(//tr[@class="text-center"])[2]')
        self.users_first_name = page.locator('//th[text()="First Name"]')
        self.users_last_name = page.locator('//th[text()="Last Name"]')
        self.users_email = page.locator('//th[text()="Email"]')
        self.users_phone_numbers = page.locator('//th[text()="Phone Number"]')
        self.users_status = page.locator('(//th[text()="Status"])[1]')
        self.users_actions = page.locator('(//th[text()="Actions"])[2]')
        self.user_action_button = page.locator(
            '(//button[@class="btn rounded-3 me-2 fs--2 action-item-sm btn-outline icon-item icon-item-md"])[1]'
        )
        self.multi_actions_button = page.locator(
            '(//div[@id="order-information-tab-tabpane-users"]//div[@class="font-sans-serif btn-reveal-t                            rigger dropend"])[1]'
        )
        self.assign_group_button = page.locator('//a[text()="Assign Group"]')
        self.success_message = page.locator(
            '//div[@class="ant-message-custom-content ant-message-success"]'
        )
        self.group_filter = page.locator('(//div[@class="modal-body"]//label)[2]')
        self.group_filter_options = page.locator(
            '((//div[@class="modal-content"])[2]//select)[1]'
        )
        self.group_status = '//div[@class="me-2 badge badge-soft-primary btn-outline rounded-pill" or @class="me-2 badge badge-soft-secondary btn-outline rounded-pill"]'
        self.user_info = page.locator('((//div[@class="simplebar-mask"])[2]//tr)[2]')
        self.user_information = page.locator('//button[text()="User Information"]')
        self.user_info_first_name = page.locator('//label[text()="First Name"]')
        self.user_info_last_name = page.locator('//label[text()="Last Name"]')
        self.user_info_email = page.locator('//label[text()="Email"]')
        self.user_info_phone = page.locator('//label[text()="Phone"]')
        self.user_control = page.locator('//h5[text()="User Controls"]')
        self.active_user_button = page.locator(
            '//button[text()="Activate User" or text()="Suspend User"]'
        )
        self.archive_user_button = page.locator(
            '//button[text()="Archive User" or text()="Unarchive User"]'
        )
        self.apply_button = page.locator('//button[text()="Apply"]')
        self.cancel_button = page.locator('//button[text()="Cancel"]')
        # Published items tab locators
        self.published_items_tab_header = page.locator(
            '(//tr[@class="text-center"])[3]'
        )
        self.published_items_Thumbnail = page.locator("//*[@id='order-information-tab-tabpane-publishedItems']/div/div/div[1]/div/div[1]/div[2]/div/div/div/table/thead/tr/th[1]")
        self.published_items_id = page.locator("//*[@id='order-information-tab-tabpane-publishedItems']/div/div/div[1]/div/div[1]/div[2]/div/div/div/table/thead/tr/th[2]")
        self.published_items_Name=page.locator("//*[@id='order-information-tab-tabpane-publishedItems']/div/div/div[1]/div/div[1]/div[2]/div/div/div/table/thead/tr/th[3]")
        self.published_items_item_type = page.locator("//*[@id='order-information-tab-tabpane-publishedItems']/div/div/div[1]/div/div[1]/div[2]/div/div/div/table/thead/tr/th[4]")
        self.published_items_price =page.locator("//*[@id='order-information-tab-tabpane-publishedItems']/div/div/div[1]/div/div[1]/div[2]/div/div/div/table/thead/tr/th[5]")
        self.published_items_fee = page.locator("//*[@id='order-information-tab-tabpane-publishedItems']/div/div/div[1]/div/div[1]/div[2]/div/div/div/table/thead/tr/th[6]")
        self.published_items_status = page.locator("//*[@id='order-information-tab-tabpane-publishedItems']/div/div/div[1]/div/div[1]/div[2]/div/div/div/table/thead/tr/th[7]")

        # Sends tab locators
        self.sends_tab_header = page.locator('(//tr[@class="text-center"])[4]')
        self.sends_thumbnail = page.locator('//*[@id="order-information-tab-tabpane-sends"]/div/div/div[1]/div/div[1]/div[2]/div/div/div/table/thead/tr/th[1]')
        self.sends_id = page.locator('//*[@id="order-information-tab-tabpane-sends"]/div/div/div[1]/div/div[1]/div[2]/div/div/div/table/thead/tr/th[2]')
        self.sends_item_sent = page.locator("//*[@id='order-information-tab-tabpane-sends']/div/div/div[1]/div/div[1]/div[2]/div/div/div/table/thead/tr/th[3]")
        self.sends_price = page.locator("//*[@id='order-information-tab-tabpane-sends']/div/div/div[1]/div/div[1]/div[2]/div/div/div/table/thead/tr/th[4]")
        self.sends_send_date = page.locator("//*[@id='order-information-tab-tabpane-sends']/div/div/div[1]/div/div[1]/div[2]/div/div/div/table/thead/tr/th[5]")
        self.sends_date_created_ = page.locator("//*[@id='order-information-tab-tabpane-sends']/div/div/div[1]/div/div[1]/div[2]/div/div/div/table/thead/tr/th[6]")
        self.sends_status = page.locator("//*[@id='order-information-tab-tabpane-sends']/div/div/div[1]/div/div[1]/div[2]/div/div/div/table/thead/tr/th[7]")
        self.sends_deployment_id = page.locator('//th[text()="Deployment ID"]')

        #self.sends_item_id = page.locator('//th[text()="Item ID"]')
        self.sends_deployment_name = page.locator('//th[text()="Deployment ID"]')
        self.sends_send_time = page.locator('//th[text()="Send Time"]')
        self.sends_date_created = page.locator('//th[text()="Date Created"]')
        self.sends_status = page.locator('(//th[text()="Status"])[3]')
        # Account Balance tab locators
        self.account_balance_title = page.locator('//div[text()="Balance"]')
        self.accountbalance_balance = page.locator(
            '//div[@class="pt-4 pb-3 card-body"]'
        )

    @qase_screenshot
    @qase.step(
        title="Verify and click on Deployments tab",
        expected="Verify deployment tab icon and click on deployments tab",
    )
    def verify_and_click_on_deployments_tab(self, side_navigation_item):
        """
        Verify Users and click on deployments tab
        """
        # verify icon availability
        expect(self.deployments_icon).to_be_visible()
        # clicking on deployments tab
        self.page.click(
            self.deployments_tab.replace(
                "<<side_navigation_tabs>>", side_navigation_item
            )
        )
        print(f"successfully able to click on {side_navigation_item} tab")

    @qase_screenshot
    @qase.step(
        title="Verify available elements of deployments page",
        expected="All expected element should be visible on deployments page",
    )
    def verify_deployments_page_elements(self, headers_text):
        """
        Verify deployments page elements
        """
        # Verify visibility of various components on the deployments page
        elements_to_check = [
            self.user_page_header_component,
            self.user_page_footer,
            self.user_page_list_component,
            self.apply_batch_action_button,
            self.batch_action_dropdown,
            self.dropdown,
        ]
        for element in elements_to_check:
            expect(element).to_be_visible()
        # Extract headers from the UI
        headers_title = self.user_list_headers.inner_text()
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
        title="Verify Batch action functionality on user Deployments page",
        expected="User should be able to apply batch actions on selected users",
    )
    def apply_batch_actions_to_deployments_list(self, success_message):
        """
        Apply batch action to user list
        """
        expect(self.batch_action_title).to_be_visible()
        deployments_name = self.page.query_selector_all("//td[3]")
        time.sleep(2)
        name = [de_name.text_content() for de_name in deployments_name]
        print(name)
        deployment_name = self.deployment_name.text_content()
        print(deployment_name)
        self.user_checkbox.click()
        time.sleep(2)
        self.apply_batch_action_button.click()

       # self.page.wait_for_selector("//div[contains(text(), '" + success_message + "')]", timeout=5000)

        # Retry checking the deployments list to ensure deletion
        max_retries = 10
        for attempt in range(max_retries):
            time.sleep(1)  # Small delay before retrying
            deployments_name1 = self.page.query_selector_all("//td[3]")
            name1 = [de_name.text_content().strip() for de_name in deployments_name1]
            print(f"After deletion attempt {attempt + 1}:", name1)

            if deployment_name not in name1:
                print(f"✅ Deployment '{deployment_name}' successfully removed after {attempt + 1} attempts.")
                break  # Success, exit loop

        success_text = self.deployment_delete_success_message.text_content()
        assert success_text == success_message

    @qase_screenshot
    @qase.step(
        title="Delete deployments from actions",
        expected="system admin should be able to delete deployments from actions",
    )
    def delete_deployments_from_actions(self, success_message):
        """
        Delete deployment from the actions button
        """
        self.button_to_change_action.click()
        self.delete_button.click()
        self.confirm_button.click()
        success_text = self.deployment_delete_success_message.text_content()
        assert success_text == success_message
        print("Deployment deleted successfully.")

    @qase_screenshot
    @qase.step(
        title="Delete deployments from actions",
        expected="system admin should be able to delete deployments from actions",
    )
    def verify_deployment_summary_pop_up_fields(self):
        """
        Verify deployment summary fields in the deployment summary pop-up.
        """
        time.sleep(2)
        self.page.wait_for_load_state("domcontentloaded")
        self.select_deployment.click()

        # List of elements to check
        elements_to_check = [
            self.deployment_summary_model,
            self.deployment_summary_users_tab,
            self.deployment_summary_published_items_tab,
            self.deployment_summary_sends_tab,
            self.deployment_summary_information_tab,
        ]

        for element in elements_to_check:
            element.wait_for(state="visible")  # Ensures the element is visible
            assert element.is_visible(), f"{element} is not visible!"
        print("Deployment summary pop-up fields verified successfully.")

    @qase_screenshot
    @qase.step(
        title="verify deployment summary users filter options",
        expected="User should be able to see available filter options on deployment summary pop-up",
    )
    def verify_deployment_summary_users_filter(self, available_filter_options):
        """
        verify deployment summary users filters
        """
        time.sleep(2)
        self.select_deployment.click()
        time.sleep(2)
        self.deployment_summary_users_tab.click()
        time.sleep(5)
        #expect(self.deployment_summary_users_filter).to_be_visible()
        self.page.wait_for_selector('select.generic-filter-select', state='visible')

        # Click the dropdown to open it
        self.page.click('select.generic-filter-select', force=True)  # Force click if needed

        # Get all text from the options
        # Get all the options' text
        options_text = [option.inner_text() for option in
                        self.page.query_selector_all('select.generic-filter-select option')]

        print(f"Retrieved options: {options_text}")

        # Remove duplicates by converting to a set and back to a list (preserving order)
        unique_options_text = list(dict.fromkeys(options_text))

        # Filter out any irrelevant options (e.g., "All Deployments")
        filtered_options_text = [option for option in unique_options_text if option != 'All Deployments']
        filtered_options_text.sort()
        available_filter_options.sort()
        print(f"Filtered options: {filtered_options_text}")

        # Check if options match the expected ones
        assert filtered_options_text == available_filter_options, f"Expected: {available_filter_options}, but got: {filtered_options_text}"

        print(f"All available filters verified: {available_filter_options}")

    @qase_screenshot
    @qase.step(
        title="Apply filter on users data of deployment summary",
        expected="system admin should be able to apply filter on users data",
    )
    def apply_filter_on_deployment_summary_users_data(
            self, available_filter_options, expected_statuses
    ):
        """
        Apply filter on deployment summary users data and verify filtered data.
        Handles cases where no user data is present.
        """
        for filter_option in available_filter_options:
            print(f"\nApplying filter: '{filter_option}'")
            time.sleep(5)
            self.deployment_summary_users_filter.select_option(filter_option)

            # Wait for the UI to update (increase time if needed)
            time.sleep(2)  # Small delay to ensure page updates

            try:
                # Wait for elements to appear
                self.page.wait_for_selector(self.all_users_status, state="visible", timeout=5000)
            except :
                print(f"Timeout: No data found for filter '{filter_option}'.")
                continue  # Skip this iteration if no elements are found

            # Query for status elements
            all_users_status = self.page.query_selector_all(self.all_users_status)

            if not all_users_status:  # Handle case when no user data is found
                print(f"No user data found after applying '{filter_option}' filter.")
                continue

            # Get text content of all status elements
            all_users_status_text = [status.text_content().strip() for status in all_users_status]

            print(f"Extracted statuses for '{filter_option}': {all_users_status_text}")

            # Retrieve expected statuses, handling case insensitivity
            expected = expected_statuses.get(filter_option, [])
            expected_cleaned = [e.strip() for e in expected]

            print(f"Expected statuses for '{filter_option}': {expected_cleaned}")

            # Assertion to verify expected statuses are in extracted statuses
            for expected_status in expected_cleaned:
                assert expected_status in all_users_status_text, (
                    f"Expected '{expected_status}' but found: {all_users_status_text}"
                )

    @qase_screenshot
    @qase.step(
        title="Verify users tab fields",
        expected="Profile Image, ID, First Name, Last Name, Email, Phone Number, Status, Actions fields should be visible under the deployment summary users tab ",
    )
    def verify_deployment_summary_users_tab_fields(self, headers_text):
        """
        Verify that all fields in the deployment summary's users tab are correctly displayed
        """
        time.sleep(2)
        self.page.wait_for_load_state("domcontentloaded")
        self.select_deployment.click()
        self.page.wait_for_load_state("domcontentloaded")
        self.deployment_summary_users_tab.click()
        # Verify visibility of various components on the deployments summary mode
        elements_to_check = [
           # self.users_profile_image,
           # self.users_id,
            self.user_name,
            self.users_first_name,
            self.users_last_name,
            self.users_email,
           # self.users_phone_numbers,
            self.users_status,
            self.users_actions,
        ]
        for element in elements_to_check:
            expect(element).to_be_visible()
            # Extract headers from the UI
            headers_title = self.user_tab_header.inner_text()
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
        print("deployment summary's account published users tab verified successfully")

    @qase_screenshot
    @qase.step(
        title="Verify published items tab fields",
        expected="ID, Name, Description, Price, Status fields should be visible under the deployment summary published items tab",
    )
    def verify_deployment_summary_published_items_tab_fields(
        self, headers_text, tab_to_navigate
    ):
        """
        Verify that all fields in the deployment summary's published items tab are correctly displayed
        """
        time.sleep(2)
        self.select_deployment.click()
        self.page.wait_for_load_state("domcontentloaded")
        self.page.click(
            self.deployment_summary_tab_navigation.replace(
                "<<tab_to_navigate>>", tab_to_navigate
            )
        )
        print(f"successfully able to click on {tab_to_navigate} tab")
        self.page.wait_for_load_state("domcontentloaded")
        # Verify visibility of various components on the deployments summary mode
        time.sleep(2)
        elements_to_check = [
            self.published_items_Thumbnail,
            self.published_items_id,
            self.published_items_Name,
            self.published_items_item_type,
            self.published_items_price,
            self.published_items_fee,
            self.published_items_status
        ]
        for element in elements_to_check:
            expect(element).to_be_visible()
            # Extract headers from the UI
            headers_title = self.published_items_tab_header.inner_text()
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
        print("deployment summary's account published items tab verified successfully")

    @qase_screenshot
    @qase.step(
        title="Verify deployment summary sends tab fields",
        expected="Thumbnail, ID, Item ID, Deployment ID, Deployment Name, Send Time, Date Created, Status fields should be visible under the deployment summary sends tab",
    )
    def verify_deployment_summary_sends_tab_fields(self, headers_text, tab_to_navigate):
        """
        Verify that all fields in the deployment summary's sends tab are correctly displayed
        """
        time.sleep(2)
        self.select_deployment.click()
        self.page.wait_for_load_state("domcontentloaded")
        self.page.click(
            self.deployment_summary_tab_navigation.replace(
                "<<tab_to_navigate>>", tab_to_navigate
            )
        )
        print(f"successfully able to click on {tab_to_navigate} tab")
        self.page.wait_for_load_state("domcontentloaded")
        # Verify visibility of various components on the deployments summary mode
        elements_to_check = [
            self.sends_thumbnail,
            self.sends_id,
            self.sends_item_sent,
            self.sends_price,
            self.sends_send_date,
            self.sends_date_created,
            self.sends_status,
        ]
        for element in elements_to_check:
            expect(element).to_be_visible()
            # Extract headers from the UI
            headers_title = self.sends_tab_header.inner_text()
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
        print("deployment summary's account sends tab verified successfully")

    @qase_screenshot
    @qase.step(
        title="Verify account balance tab",
        expected="available balance should be visible inside the deployment summary account balance tab",
    )
    def verify_deployment_summary_account_balance_tab_fields(
        self, account_balance_title, tab_to_navigate
    ):
        """
        Verify that all fields in the deployment summary's account balance tab are correctly displayed
        """
        time.sleep(2)
        self.select_deployment.click()
        self.page.wait_for_load_state("domcontentloaded")
        # Verify visibility of various components on the deployments summary mode
        elements_to_check = [
            self.accountbalance_balance,
            self.account_balance_title,
        ]
        for element in elements_to_check:
            expect(element).to_be_visible()
        title = self.account_balance_title.text_content()
        assert title == account_balance_title
        print("a few seconds ago Balance is :",self.accountbalance_balance.inner_text())
        print("deployment summary's account balance tab verified successfully")

    @qase_screenshot
    @qase.step(
        title="Verify actions button og users tab",
        expected="system admin should be able to active, suspend and assign group to users",
    )
    def verify_actions_button_on_users_tab(
        self,
        success_message,
        available_filter_options,
        expected_statuses,
        error_message,
    ):
        """
        Verify actions buttons on users tab
        """
        time.sleep(2)
        self.select_deployment.click()
        self.page.wait_for_load_state("domcontentloaded")
        time.sleep(2)
        self.deployment_summary_users_tab.click()
        time.sleep(2)
        self.user_action_button.click()
        time.sleep(2)
        if self.success_message.is_visible():
            message_text = self.success_message.text_content().strip()
            print(f"Message displayed: '{message_text}'")
            # Check if the message matches the expected success or error text
            if message_text == success_message:
                print ("Success message verified.")
                assert (
                    message_text == success_message
                ), f"Expected success message '{success_message}', but got '{message_text}'"
            elif message_text == error_message:
                print("Error message verified.")
                assert (
                    message_text == error_message
                ), f"Expected error message '{error_message}', but got '{message_text}'"
            else:
                print(f"Unexpected message found: '{message_text}'")
                assert False, f"Unexpected message: '{message_text}'"
        else:
            print("No message is visible.")
            assert False, "Neither success nor error message appeared as expected."
        self.page.wait_for_load_state("domcontentloaded")
        self.multi_actions_button.click()
        self.assign_group_button.click()
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.group_filter).to_be_visible()
        for filter_option in available_filter_options:
            self.group_filter_options.select_option(filter_option)
            self.page.wait_for_selector(self.all_users_status)
            time.sleep(5)
            # Query for the status elements after applying the filter
            all_users_status = self.page.query_selector_all(self.group_status)
            all_users_status_text = [status.inner_text() for status in all_users_status]
            # Print the text of each status
            print(
                f"Users status after applying '{filter_option}': {all_users_status_text}"
            )
            # Assertion to verify the expected statuses are present
            if filter_option in expected_statuses:
                expected = expected_statuses[filter_option]
                if expected:
                    for expected_status in expected:
                        assert (
                            expected_status in all_users_status_text
                        ), f"'{expected_status}' not found in the status text for filter '{filter_option}'"
                else:
                    # If there are no expected statuses, assert that the status list is empty
                    assert (
                        not all_users_status_text
                    ), f"Expected no statuses for filter '{filter_option}', but found: {all_users_status_text}"

    @qase_screenshot
    @qase.step(
        title="Verify user information's",
        expected="User information should be visible inside the user information pop-up",
    )
    def verify_user_information_inside_users_tab(self):
        """
        Verify users information inside users tab
        """
        self.page.wait_for_load_state("domcontentloaded")
        time.sleep(5)
        self.select_deployment.click()
        time.sleep(5)
        self.user_info.click(position={"x": 10, "y": 10})
        time.sleep(3)
        elements_to_check = [
            self.user_information,
            self.user_info_first_name,
            self.user_info_last_name,
            self.user_info_email,
            self.user_info_phone,
            self.user_control,
            self.active_user_button,
            self.archive_user_button,
            self.apply_button,
            self.cancel_button,
        ]
        for element in elements_to_check:
            expect(element).to_be_visible()
