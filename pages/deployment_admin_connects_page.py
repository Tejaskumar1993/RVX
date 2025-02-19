"""
Deployment Admin Connects Page Module
"""
import re
import select
import time

import page
import self
from playwright.sync_api import Page, expect
from qase.pytest import qase
from utilities.decorators import qase_screenshot


class DeploymentAdminConnectsPage:
    """
    Page Object Model for Deployment Admin Connects Page.
    """

    def __init__(self, page: Page):
        self.page = page

        # Role locator
        self.select_role_dropdown = page.locator('(//div[@class="dropdown"])[2]')
        self.select_role = '//a[text()="<<select_role>>"]'

        # Side navigation tab
        self.connects_icon = page.locator('//*[@data-icon="circle-nodes"]')
        self.connects_tab = '//span[text()="<<tab_to_navigate>>"]'

        # headers, filter and search locators
        self.connects_page_component = page.locator('//div[@class="connects"]')
        self.connects_page_header = page.locator("//thead[@class='bg-200 text-900 text-nowrap align-middle thead']")
        self.filter_label = page.locator('//div[text()="Filter:"]')
        self.filter_dropdown = page.locator(
            '//select[@class="generic-filter-select ms-2 form-select form-select-sm"]'
        )
        self.filter_option_to_select = page.locator(
            '//div[@class="d-flex align-items-center mb-2"]//select'
        )
        self.filter_options = '//select[@class="generic-filter-select ms-2 form-select form-select-sm"]//option'
        self.search_label = page.locator('//label[text()="Search"]')
        self.search_box = page.locator('//input[@placeholder="Input Search Text"]')
        self.create_new_connect_button = page.locator(
            '//button[text()="Create New Connect"]'
        )

        # connects locators
        self.connects_list_component = page.locator('//div[@class="simplebar-mask"]')
        self.connects_title = page.locator('//h5[text()="Connects"]')
        self.connects_table_header = page.locator("(//table//tr)[1]")
        self.connects_status = '//div[contains(@class, "badge-soft-primary") or contains(@class, "badge-soft-secondary")]'

        # footer locators
        self.footer_component = page.locator(
            '//div[contains(@class, "table-footer-border-top card-footer")]'
        )
        self.pagination = page.locator(
            '//div[contains(@class, "d-flex pagination-numbers")]'
        )
        self.result_counter = page.locator(
            "//span[@class='d-none d-sm-inline-block me-2']"
        )
        self.rows_per_page = page.locator(
            '//div[contains(@class, "d-flex align-items-center fs--1 ps-3 d-flex flex-wrap rows-page-count")]'
        )

        # create new connects locators
        self.create_a_connect_model = page.locator('//div[@class="modal-content"]')
        self.create_a_connect_title = page.locator('//div[text()="Create a Connect"]')
        self.select_an_ontrack_connect_type_title = page.locator(
            '//h3[text()="Select an Ontrack Connect Type"]'
        )
        self.ontrack_egift_title = page.locator('//h5[text()="Ontrack eGift"]')
        self.ontrack_egift_radio_button = page.locator('//input[@id="On Track eGift"]')
        self.ontrack_egift_label = page.locator('//label[text()="Ontrack eGift"]')
        self.ontrack_direct_2_prospect_title = page.locator(
            '//h5[text()="Ontrack Direct-2-Prospect"]'
        )
        self.ontrack_direct_2_prospect_radio_button = page.locator(
            '//input[@id="Marketplace"]'
        )
        self.marketplace_label = page.locator('//label[text()="MarketPlace"]')
        self.close_button = page.locator('//button[@class="btn-close"]')
        self.continue_button = page.locator('//button[text()="Continue"]')

        # create egift connects locators

        self.select_ontrack_egift = page.locator("//input[@id='On Track eGift']")
        self.select_item_list = page.locator("//p[contains(text(),'flipkart')]")

        self.egits_process = page.locator(
            '//div[@class="ant-steps-item-title"][text()="eGifts"]'
        )
        self.connects_settings_process = page.locator(
            '//div[@class="ant-steps-item-title"][text()="Connect Settings"]'
        )
        self.send_options_process = page.locator(
            '//div[@class="ant-steps-item-title"][text()="Send Options"]'
        )
        self.connect_summary = page.locator(
            '//div[@class="ant-steps-item-title"][text()="Connect Summary"]'
        )
        self.select_a_gift_title = page.locator('//h5[text()="Select a Gift"]')
        self.egift_filter_label = page.locator('//label[text()="Filter:"]')
        self.egift_filter_dropdown = page.locator(
            '//select[@class="form-select form-select-sm"]'
        )
        self.egift_filter_options = (
            '//select[@class="form-select form-select-sm"]//option'
        )
        self.egift_filter_select_option = page.locator(
            '//div[@class="d-flex align-items-center justify-content-between"]//select'
        )
        self.egift_amount_label = page.locator('//label[text()="eGift Amount:"]')
        self.egift_amount_input = page.locator('//input[@name="amount"]')
        self.allow_sender_to_decide_range_checkbox = page.locator(
            '//input[@id="custom-checkbox"]'
        )
        self.enter_minimum_amount = page.locator('//input[@name="from"]')
        self.enter_maximum_locator = page.locator('//input[@name="to"]')
        self.all_available_items = page.locator(
            '//div[@class="g-3 my-3 row row-cols-lg-3 row-cols-md-2 row-cols-1"]'
        )
        self.select_item = page.locator("(//div[contains(@role,'button')])[122]")
        self.select_item_D2P = page.locator("(//div[contains(@role,'button')])[10]")
        self.recipients_choice_component = page.locator(
            '//div[@class="d-flex flex-column h-100 overflow-hidden"]'
        )
        self.recipients_choice_title = page.locator('//p[text()="Recipient\'s Choice"]')
        self.select_up_to_label = page.locator('//p[text()="Select up to 20 eGifts"]')
        self.next_button = page.locator('//button[text()="Next"]')
        self.warning_message = page.locator(
            '//span[text()="Please fill out all required fields"]'
        )
        self.delete_button = page.locator('//*[@data-icon="trash"]')
        self.ontrack_connect_details_title = page.locator(
            '//h4[text()="Ontrack Connect Details"]'
        )
        self.enter_details_message = page.locator(
            '//p[text()="Enter details for your connect"]'
        )
        self.details_component = page.locator('//div[@class="ant-card-body"]')
        self.internal_connect_name_label = page.locator(
            '//label[text()="Internal Connect Name"]'
        )
        self.internal_name_input = page.locator(
            '//input[@id="connectSettings_internalName"]'
        )
        self.display_name_for_sender_label = page.locator(
            '//label[text()="Display Name for Sender"]'
        )
        self.display_name_for_sender_input = page.locator(
            '//input[@id="connectSettings_displayName"]'
        )
        self.connect_description_label = page.locator(
            '//label[text()="Connect Description"]'
        )
        self.connect_description_input = page.locator(
            '//textarea[@id="connectSettings_description"]'
        )
        self.start_date_label = page.locator('//label[text()="Start Date"]')
        self.start_date_input = page.locator('//input[@id="connectSettings_startDate"]')
        self.select_start_date = "//div[@aria-label='Choose <<tomorrow>>']"
        self.end_date_label = page.locator('//label[text()="End Date"]')
        self.end_date_input = page.locator('//input[@id="connectSettings_endDate"]')
        self.select_end_date = "//div[@aria-label='Choose <<tomorrow>>']"
        self.days_until_offer_expires_label = page.locator(
            '//label[text()="Days until offer expires ?"]'
        )
        self.days_until_dropdown = page.locator(
            '(//div[@class="ant-form-item-control-input-content"]//select)[1]'
        )
        self.assign_a_token_bucket_label = page.locator(
            '//label[text()="Assign a token bucket"]'
        )
        self.assign_a_token_bucket_dropdown = page.locator(
            '(//div[@class="ant-form-item-control-input-content"]//select)[2]'
        )
        self.assign_template_button = page.locator(
            '//button//span[text()="(0) Assign Templates"]'
        )
        self.assign_user_to_connect_button = page.locator(
            '//button//span[text()="Assign User To Connect"]'
        )
        self.select_all_assign_user =page.locator("//div[@class='modal-body']//input[@title='Toggle All Rows Selected']")
        self.accept_changes_btn =page.locator("//button[normalize-space()='Accept Changes']")
        self.assign_your_connects_title = page.locator(
            '//div[text()="Assign Your Connects"]'
        )
        self.groups_title = page.locator('//h4[text()="Groups"]')
        self.users_title = page.locator('//h4[text()="Users"]')
        self.group_search = page.locator('//p[text()="(1) Group Selected"]')
        self.users_search = page.locator('//p[text()="(1) User Selected"]')
        self.select_group = page.locator(
            '(//div[@class="list-group"]//input[@class="form-check-input"])[1]'
        )
        self.select_users = page.locator(
            '((//div[@class="card"])[4]//input[@type="checkbox"])[1]'
        )
        self.submit_button = page.locator('//button[text()="Submit"]')
        self.cancel_button = page.locator('//button[text()="Cancel"]')
        self.send_options_label = page.locator(
            '//div[@class="mb-5 container"]//h4[text()="Send Options"]'
        )
        self.send_egift_via_label = page.locator(
            '//div[@class="mb-5 container"]//p[text()="Send eGift Via"]'
        )
        self.via_email = page.locator('//div[@role="button"]//p[text()="Email"]')
        self.via_shareable_link = page.locator(
            '//div[@role="button"]//p[text()="Shareable Link"]'
        )
        self.via_sms = page.locator('//div[@role="button"]//p[text()="SMS"]')
        self.via_senders_choice = page.locator(
            '//div[@role="button"]//p[text()="Sender\'s Choice"]'
        )
        self.connect_summary_label = page.locator('//h4[text()="Connect Summary"]')
        self.active_new_connect = page.locator(
            '//button[text()="Activate New Connect"]'
        )

        self.egift_selection_section = page.locator(
            '//div[@class="d-flex align-content-center row"]//div[text()="eGift Selection"]'
        )

        self.gift_selection_section = page.locator('//div[@class="d-flex align-content-center row"]//div[text()="Gift Selection"]')
        self.connect_settings_details_section = page.locator(
            '//div[@class="d-flex align-content-center row"]//div[text()="Connect Settings & Details"]'
        )
        self.sending_options_section = page.locator(
            '//div[@class="d-flex align-content-center row"]//div[text()="Sending Options"]'
        )


        # Connect page Locators
        self.menu_connects = page.locator("//a[.='Connects']")
        self.expected_title = page.locator("//h5[normalize-space()='Connects']")
        self.table_headers = page.locator("//table/thead/tr/th")
        self.filter_label = page.locator("//div[.=' Filter:']")
        self.filter_dropdown = page.locator("//select[@class='generic-filter-select ms-2 form-select form-select-sm']")
        self.filter_value = page.locator("//select[contains(.,'All Connects')]")
        self.search_input = page.locator("//input[@placeholder='Input Search Text']")
        self.pagination_btn = page.locator("//div[@class='d-flex pagination-numbers m-auto mb-2']")
        self.show_result_txt = page.locator("//span[@class='d-none d-sm-inline-block me-2']")
        self.section_dropdown = page.locator("//select[contains(.,'25')]")
        self.create_connect_btn = page.locator("//button[normalize-space()='Create New Connect']")


        #Edit Locators
        self.view_port = page.locator("//tbody/tr[1]/td[8]/div[1]/div[1]")
        self.edit_item = page.locator("//a[normalize-space()='Edit']")
        self.egift_selection_edit = page.locator(
            "//div[@class='ant-collapse ant-collapse-icon-position-start']//div[1]//div[1]//span[1]//div[1]//div[2]//div[1]//button[1]"
        )
        self.delete = page.locator(
            "//div[@class='col-lg-2']//div//*[name()='svg']//*[name()='path' and contains(@fill,'currentCol')]"
        )
        self.item_add_1 = page.locator("//div[122]//div[1]//div[2]//div[1]//p[1]")
        self.item_add_range_item = page.locator("//p[normalize-space()='Tango_variable_1']")
        self.edit_choice = page.locator("//button[@class='btn rounded-3 me-1 fs--1 mb-1 ml-4 btn-outline icon-item icon-item-sm']")
        self.input_choice = page.locator("//input[@placeholder='Enter value']")
        self.add_choice_btn = page.locator("//span[normalize-space()='Add']")
        self.confirm_btn = page.locator("//span[normalize-space()='Confirm']")
        self.save_btn = page.locator("//button[normalize-space()='Save']")
        self.update_connect_btn = page.locator("//button[normalize-space()='Update Connect']")
        self.success_message_txt = page.locator('//div[contains(@class, "ant-message-success")]//span[contains(text(), "Edit Connect Successfully")]')

    @qase_screenshot
    @qase.step(
        title="Verify and click on connects tab",
        expected="User should be able to see connects icon and able to click on connects tab",
    )
    def verify_and_click_on_connects_tab(self, side_navigation_item):
        """
        Verify Users and click on connects tab
        """
        # verify icon availability
        expect(self.connects_icon).to_be_visible()
        # clicking on  connects tab
        self.page.click(
            self.connects_tab.replace("<<tab_to_navigate>>", side_navigation_item)
        )
        print(f"successfully able to click on {side_navigation_item} tab")

    @qase_screenshot
    @qase.step(
        title="Verify connects page elements",
        expected="User should be able to visible every elements of connects page",
    )
    def verify_connects_page_elements(self, headers_text):
        """
        Verify and check availability of connects page elements
        """
        elements_to_check = [
            self.connects_page_header,
            self.connects_page_component,
            self.filter_dropdown,
            self.filter_label,
            self.search_box,
            self.search_label,
            self.create_new_connect_button,
            self.connects_list_component,
            self.connects_title,
            self.footer_component,
            self.pagination,
            self.rows_per_page,
            self.result_counter,
        ]

        for element in elements_to_check:
            expect(element).to_be_visible()

        print("Connects page elements verified")
        time.sleep(5)
        # Extract headers from the UI
        actual_headers = [header.strip() for header in self.connects_page_header.all_inner_texts()[0].split("\t") if header.strip()]
        assert actual_headers == headers_text, f"Expected headers {headers_text}, but got {actual_headers}"
        print(f"✅ Table header Titles verified: {actual_headers}")

    @qase_screenshot
    @qase.step(
        title="Create connect with e-gift functionality via Email ",
        expected="connect with e-gift functionality via Email"
    )
    def verify_create_connect_with_e_gift_functionality_via_email(self, Select_Ontrack_Connect_Type: str,
                                                        Internal_Connect_Name: str, Sender_Name: str,
                                                        Connect_Description: str, Start_Date: str, End_Date: str,
                                                        Days_expires: str, Assign_token: str,via_email :str,Success_message : str):
        """
        This test verifies the creation of a connect with e-gift functionality.
        Steps:
        1. Click on create new connect button.
        2. Select Ontrack eGift and proceed.
        3. Fill out necessary details like name, sender, description, dates, etc.
        4. Assign token bucket and template.
        5. Assign users and confirm the selections.
        6. Configure sending options and finalize the connect.
        """

        def wait_and_click(element):
            """Wait for element to be visible and then click."""
            expect(element).to_be_visible()
            element.click()
            self.page.wait_for_timeout(2000)

        def wait_and_fill(element, value):
            """Wait for element to be visible and then fill the given value ."""
            expect(element).to_be_visible()
            element.fill(value)
            self.page.wait_for_timeout(2000)

        # Step 1: Initiate connect creation process
        wait_and_click(self.create_new_connect_button)
        wait_and_click(self.select_ontrack_egift)

        # Step 2: Select eGift type
        Ontrack_eGift = self.page.locator(f"//input[@id='{Select_Ontrack_Connect_Type}']")
        wait_and_click(Ontrack_eGift)
        print(f"✅ Selected Ontrack Connect Type: Ontrack eGift")

        # Step 3: Continue to item selection
        time.sleep(5)
        wait_and_click(self.continue_button)
        time.sleep(10)
        wait_and_click(self.select_item)
        wait_and_click(self.next_button)

        # Step 4: Fill in connect details
        wait_and_fill(self.internal_name_input, Internal_Connect_Name)
        wait_and_fill(self.display_name_for_sender_input, Sender_Name)
        wait_and_fill(self.connect_description_input, Connect_Description)
        wait_and_fill(self.start_date_input, Start_Date)
        wait_and_fill(self.end_date_input, End_Date)

        # Step 5: Configure expiration and token assignment
        wait_and_click(self.days_until_dropdown)
        self.days_until_dropdown.select_option(Days_expires)
        wait_and_click(self.assign_a_token_bucket_dropdown)
        self.assign_a_token_bucket_dropdown.select_option(Assign_token)

        # Step 6: Assign users and templates
        wait_and_click(self.assign_template_button)
        wait_and_click(self.select_all_assign_user)
        wait_and_click(self.accept_changes_btn)
        print("✅ Selected all assigned users and saved changes.")

        wait_and_click(self.assign_user_to_connect_button)
        wait_and_click(self.select_group)
        wait_and_click(self.select_users)
        print(f" -> {self.group_search.all_inner_texts()}")
        print(f" -> {self.users_search.all_inner_texts()}")

        # Step 7: Submit and finalize user assignment
        wait_and_click(self.submit_button)
        print("✅ Submitted Group and User.")

        # Step 8: Select sending options
        wait_and_click(self.next_button)
        send_options = [
            self.send_options_label, self.send_egift_via_label, self.via_email,
            self.via_shareable_link, self.via_sms, self.via_senders_choice
        ]
        for option in send_options:
            expect(option).to_be_visible()


        via_email_locator = self.page.locator(f'//div[@role="button"]//p[text()="{via_email}"]')
        wait_and_click(via_email_locator)
        print(f"Selection: {via_email}")
        wait_and_click(self.next_button)

        # Step 9: Verify summary sections
        summary_sections = [
            self.connect_summary_label, self.egift_selection_section,
            self.connect_settings_details_section, self.sending_options_section
        ]
        for section in summary_sections:
            expect(section).to_be_visible()

            self.egift_selection_section.click()
            self.connect_settings_details_section.click()
            self.sending_options_section.click()

        # Step 10: Activate the new connect
        wait_and_click(self.active_new_connect)

        # Step 11: Verify the success message after activation
        success_message = self.page.locator(f"//span[contains(text(), '{Success_message}')]")
        expect(success_message).to_be_visible()
        print(f"✅ Success: {Success_message}!")

    @qase_screenshot
    @qase.step(
        title="Create connect with e-gift functionality via Shareable Link",
        expected="connect with e-gift functionality via Shareable Link"
    )
    def verify_create_connect_with_e_gift_functionality_via_shareable_link(self, Select_Ontrack_Connect_Type: str,
                                                        Internal_Connect_Name: str, Sender_Name: str,
                                                        Connect_Description: str, Start_Date: str, End_Date: str,
                                                        Days_expires: str, Assign_token: str,via_shareable_link : str, Success_message: str):
        """
        This test verifies the creation of a connect with e-gift functionality.
        Steps:
        1. Click on create new connect button.
        2. Select Ontrack eGift and proceed.
        3. Fill out necessary details like name, sender, description, dates, etc.
        4. Assign token bucket and template.
        5. Assign users and confirm the selections.
        6. Configure sending options and finalize the connect.
        """

        def wait_and_click(element):
            """Wait for element to be visible and then click."""
            expect(element).to_be_visible()
            element.click()
            self.page.wait_for_timeout(2000)

        def wait_and_fill(element, value):
            """Wait for element to be visible and then fill the given value."""
            expect(element).to_be_visible()
            element.fill(value)
            self.page.wait_for_timeout(2000)

        # Step 1: Initiate connect creation process
        wait_and_click(self.create_new_connect_button)
        wait_and_click(self.select_ontrack_egift)

        # Step 2: Select eGift type
        Ontrack_eGift = self.page.locator(f"//input[@id='{Select_Ontrack_Connect_Type}']")
        wait_and_click(Ontrack_eGift)
        print(f"✅ Selected Ontrack Connect Type: Ontrack eGift")

        # Step 3: Continue to item selection
        wait_and_click(self.continue_button)
        time.sleep(10)
        wait_and_click(self.select_item)
        wait_and_click(self.next_button)

        # Step 4: Fill in connect details
        wait_and_fill(self.internal_name_input, Internal_Connect_Name)
        wait_and_fill(self.display_name_for_sender_input, Sender_Name)
        wait_and_fill(self.connect_description_input, Connect_Description)
        wait_and_fill(self.start_date_input, Start_Date)
        wait_and_fill(self.end_date_input, End_Date)

        # Step 5: Configure expiration and token assignment
        wait_and_click(self.days_until_dropdown)
        self.days_until_dropdown.select_option(Days_expires)
        wait_and_click(self.assign_a_token_bucket_dropdown)
        self.assign_a_token_bucket_dropdown.select_option(Assign_token)

        # Step 6: Assign users and templates
        wait_and_click(self.assign_template_button)
        wait_and_click(self.select_all_assign_user)
        wait_and_click(self.accept_changes_btn)
        print("✅ Selected all assigned users and saved changes.")

        wait_and_click(self.assign_user_to_connect_button)
        wait_and_click(self.select_group)
        wait_and_click(self.select_users)
        print(f" -> {self.group_search.all_inner_texts()}")
        print(f" -> {self.users_search.all_inner_texts()}")

        # Step 7: Submit and finalize user assignment
        wait_and_click(self.submit_button)
        print("✅ Submitted Group and User.")

        # Step 8: Select sending options
        wait_and_click(self.next_button)
        send_options = [
            self.send_options_label, self.send_egift_via_label, self.via_email,
            self.via_shareable_link, self.via_sms, self.via_senders_choice
        ]
        for option in send_options:
            expect(option).to_be_visible()

        via_shareable_link_locator = self.page.locator(f'//div[@role="button"]//p[text()="{via_shareable_link}"]')
        wait_and_click(via_shareable_link_locator)
        print(f"Selection: {via_shareable_link}")
        wait_and_click(self.next_button)

        # Step 9: Verify summary sections
        summary_sections = [
            self.connect_summary_label, self.egift_selection_section,
            self.connect_settings_details_section, self.sending_options_section
        ]
        for section in summary_sections:
            expect(section).to_be_visible()

            self.egift_selection_section.click()
            self.connect_settings_details_section.click()
            self.sending_options_section.click()

        # Step 10: Activate the new connect
        wait_and_click(self.active_new_connect)

        # Step 11: Verify the success message after activation
        success_message = self.page.locator(f"//span[contains(text(), '{Success_message}')]")
        expect(success_message).to_be_visible()
        print(f"✅ Success: {Success_message}!")

    @qase_screenshot
    @qase.step(
        title="Create connect with e-gift functionality via SMS",
        expected="connect with e-gift functionality via SMS"
    )
    def verify_create_connect_with_e_gift_functionality_via_sms(self, Select_Ontrack_Connect_Type: str,
                                                                           Internal_Connect_Name: str, Sender_Name: str,
                                                                           Connect_Description: str, Start_Date: str,
                                                                           End_Date: str,
                                                                           Days_expires: str, Assign_token: str,
                                                                           via_sms :str,
                                                                           Success_message: str):
        """
        This test verifies the creation of a connect with e-gift functionality.
        Steps:
        1. Click on create new connect button.
        2. Select Ontrack eGift and proceed.
        3. Fill out necessary details like name, sender, description, dates, etc.
        4. Assign token bucket and template.
        5. Assign users and confirm the selections.
        6. Configure sending options and finalize the connect.
        """

        def wait_and_click(element):
            """Wait for element to be visible and then click."""
            expect(element).to_be_visible()
            element.click()
            self.page.wait_for_timeout(2000)

        def wait_and_fill(element, value):
            """Wait for element to be visible and then fill the given value."""
            expect(element).to_be_visible()
            element.fill(value)
            self.page.wait_for_timeout(2000)

        # Step 1: Initiate connect creation process
        wait_and_click(self.create_new_connect_button)
        wait_and_click(self.select_ontrack_egift)

        # Step 2: Select eGift type
        Ontrack_eGift = self.page.locator(f"//input[@id='{Select_Ontrack_Connect_Type}']")
        wait_and_click(Ontrack_eGift)
        print(f"✅ Selected Ontrack Connect Type: Ontrack eGift")

        # Step 3: Continue to item selection
        time.sleep(5)
        wait_and_click(self.continue_button)
        time.sleep(10)
        wait_and_click(self.select_item)
        wait_and_click(self.next_button)

        # Step 4: Fill in connect details
        wait_and_fill(self.internal_name_input, Internal_Connect_Name)
        wait_and_fill(self.display_name_for_sender_input, Sender_Name)
        wait_and_fill(self.connect_description_input, Connect_Description)
        wait_and_fill(self.start_date_input, Start_Date)
        wait_and_fill(self.end_date_input, End_Date)

        # Step 5: Configure expiration and token assignment
        wait_and_click(self.days_until_dropdown)
        self.days_until_dropdown.select_option(Days_expires)
        wait_and_click(self.assign_a_token_bucket_dropdown)
        self.assign_a_token_bucket_dropdown.select_option(Assign_token)

        # Step 6: Assign users and templates
        wait_and_click(self.assign_template_button)
        wait_and_click(self.select_all_assign_user)
        wait_and_click(self.accept_changes_btn)
        print("✅ Selected all assigned users and saved changes.")

        wait_and_click(self.assign_user_to_connect_button)
        wait_and_click(self.select_group)
        wait_and_click(self.select_users)
        print(f" -> {self.group_search.all_inner_texts()}")
        print(f" -> {self.users_search.all_inner_texts()}")

        # Step 7: Submit and finalize user assignment
        wait_and_click(self.submit_button)
        print("✅ Submitted Group and User.")

        # Step 8: Select sending options
        wait_and_click(self.next_button)
        send_options = [
            self.send_options_label, self.send_egift_via_label, self.via_email,
            self.via_shareable_link, self.via_sms, self.via_senders_choice
        ]
        for option in send_options:
            expect(option).to_be_visible()

        via_sms_link_locator = self.page.locator(f'//div[@role="button"]//p[text()="{via_sms}"]')
        wait_and_click(via_sms_link_locator)
        print(f"Selection: {via_sms}")
        wait_and_click(self.next_button)

        # Step 9: Verify summary sections
        summary_sections = [
            self.connect_summary_label, self.egift_selection_section,
            self.connect_settings_details_section, self.sending_options_section
        ]
        for section in summary_sections:
            expect(section).to_be_visible()

            self.egift_selection_section.click()
            self.connect_settings_details_section.click()
            self.sending_options_section.click()

        # Step 10: Activate the new connect
        wait_and_click(self.active_new_connect)

        # Step 11: Verify the success message after activation
        success_message = self.page.locator(f"//span[contains(text(), '{Success_message}')]")
        expect(success_message).to_be_visible()
        print(f"✅ Success: {Success_message}!")

    @qase_screenshot
    @qase.step(
        title="Create connect with e-gift functionality via Sender's Choice",
        expected="connect with e-gift functionality via Sender's Choice"
    )
    def verify_create_connect_with_e_gift_functionality_via_Sender_Choice(self, Select_Ontrack_Connect_Type: str,
                                                                Internal_Connect_Name: str, Sender_Name: str,
                                                                Connect_Description: str, Start_Date: str,
                                                                End_Date: str,
                                                                Days_expires: str, Assign_token: str,
                                                                via_sender_Choice: str,
                                                                Success_message: str):
        """
        This test verifies the creation of a connect with e-gift functionality.
        Steps:
        1. Click on create new connect button.
        2. Select Ontrack eGift and proceed.
        3. Fill out necessary details like name, sender, description, dates, etc.
        4. Assign token bucket and template.
        5. Assign users and confirm the selections.
        6. Configure sending options and finalize the connect.
        """

        def wait_and_click(element):
            """Wait for element to be visible and then click."""
            expect(element).to_be_visible()
            element.click()
            self.page.wait_for_timeout(2000)

        def wait_and_fill(element, value):
            """Wait for element to be visible and then fill the given value."""
            expect(element).to_be_visible()
            element.fill(value)
            self.page.wait_for_timeout(2000)

        # Step 1: Initiate connect creation process
        wait_and_click(self.create_new_connect_button)
        wait_and_click(self.select_ontrack_egift)

        # Step 2: Select eGift type
        Ontrack_eGift = self.page.locator(f"//input[@id='{Select_Ontrack_Connect_Type}']")
        wait_and_click(Ontrack_eGift)
        print(f"✅ Selected Ontrack Connect Type: Ontrack eGift")

        # Step 3: Continue to item selection
        time.sleep(5)
        wait_and_click(self.continue_button)
        time.sleep(10)
        wait_and_click(self.select_item)
        wait_and_click(self.next_button)

        # Step 4: Fill in connect details
        wait_and_fill(self.internal_name_input, Internal_Connect_Name)
        wait_and_fill(self.display_name_for_sender_input, Sender_Name)
        wait_and_fill(self.connect_description_input, Connect_Description)
        wait_and_fill(self.start_date_input, Start_Date)
        wait_and_fill(self.end_date_input, End_Date)

        # Step 5: Configure expiration and token assignment
        wait_and_click(self.days_until_dropdown)
        self.days_until_dropdown.select_option(Days_expires)
        wait_and_click(self.assign_a_token_bucket_dropdown)
        self.assign_a_token_bucket_dropdown.select_option(Assign_token)

        # Step 6: Assign users and templates
        wait_and_click(self.assign_template_button)
        wait_and_click(self.select_all_assign_user)
        wait_and_click(self.accept_changes_btn)
        print("✅ Selected all assigned users and saved changes.")

        wait_and_click(self.assign_user_to_connect_button)
        wait_and_click(self.select_group)
        wait_and_click(self.select_users)
        print(f" -> {self.group_search.all_inner_texts()}")
        print(f" -> {self.users_search.all_inner_texts()}")

        # Step 7: Submit and finalize user assignment
        wait_and_click(self.submit_button)
        print("✅ Submitted Group and User.")

        # Step 8: Select sending options
        wait_and_click(self.next_button)
        send_options = [
            self.send_options_label, self.send_egift_via_label, self.via_email,
            self.via_shareable_link, self.via_sms, self.via_senders_choice
        ]
        for option in send_options:
            expect(option).to_be_visible()

        via_sender_choice_locator = self.page.locator(f'//div[@role="button"]//p[text()="{via_sender_Choice}"]')
        wait_and_click(via_sender_choice_locator)
        print(f"Selection: {via_sender_Choice}")
        wait_and_click(self.next_button)

        # Step 9: Verify summary sections
        summary_sections = [
            self.connect_summary_label, self.egift_selection_section,
            self.connect_settings_details_section, self.sending_options_section
        ]
        for section in summary_sections:
            expect(section).to_be_visible()

            self.egift_selection_section.click()
            self.connect_settings_details_section.click()
            self.sending_options_section.click()

        # Step 10: Activate the new connect
        wait_and_click(self.active_new_connect)

        # Step 11: Verify the success message after activation
        success_message = self.page.locator(f"//span[contains(text(), '{Success_message}')]")
        expect(success_message).to_be_visible()
        print(f"✅ Success: {Success_message}!")


    @qase_screenshot
    @qase.step(
        title="Create connect with e-gift functionality",
        expected="connect with e-gift functionality"
    )
    def verify_create_connect_with_e_gift_range_item_functionality(self, Select_Ontrack_Connect_Type: str,Custom_Value:str,
                                                        Internal_Connect_Name: str, Sender_Name: str,
                                                        Connect_Description: str, Start_Date: str, End_Date: str,
                                                        Days_expires: str, Assign_token: str, Success_message: str):
        """
        This test verifies the creation of a connect with e-gift functionality.
        Steps:
        1. Click on create new connect button.
        2. Select Ontrack eGift and proceed.
        3. Fill out necessary details like name, sender, description, dates, etc.
        4. Assign token bucket and template.
        5. Assign users and confirm the selections.
        6. Configure sending options and finalize the connect.
        """

        def wait_and_click(element):
            """Wait for element to be visible and then click."""
            expect(element).to_be_visible()
            element.click()
            self.page.wait_for_timeout(2000)

        def wait_and_fill(element, value):
            """Wait for element to be visible and then fill the given value."""
            expect(element).to_be_visible()
            element.fill(value)
            self.page.wait_for_timeout(2000)

        # Step 1: Initiate connect creation process
        wait_and_click(self.create_new_connect_button)
        wait_and_click(self.select_ontrack_egift)

        # Step 2: Select eGift type
        Ontrack_eGift = self.page.locator(f"//input[@id='{Select_Ontrack_Connect_Type}']")
        wait_and_click(Ontrack_eGift)
        print(f"✅ Selected Ontrack Connect Type: Ontrack eGift")

        # Step 3: Continue to item selection
        time.sleep(5)
        wait_and_click(self.continue_button)
        time.sleep(10)
        wait_and_click(self.item_add_range_item)
        expect(self.item_add_range_item).to_be_visible(timeout=5000)
        time.sleep(5)
        self.item_add_range_item.click()
        self.edit_choice.click()
        time.sleep(10)
        self.input_choice.fill(str(Custom_Value))
        self.add_choice_btn.click()
        time.sleep(5)
        self.confirm_btn.click()
        time.sleep(2)
        wait_and_click(self.next_button)

        # Step 4: Fill in connect details
        wait_and_fill(self.internal_name_input, Internal_Connect_Name)
        wait_and_fill(self.display_name_for_sender_input, Sender_Name)
        wait_and_fill(self.connect_description_input, Connect_Description)
        wait_and_fill(self.start_date_input, Start_Date)
        wait_and_fill(self.end_date_input, End_Date)

        # Step 5: Configure expiration and token assignment
        wait_and_click(self.days_until_dropdown)
        self.days_until_dropdown.select_option(Days_expires)
        wait_and_click(self.assign_a_token_bucket_dropdown)
        self.assign_a_token_bucket_dropdown.select_option(Assign_token)

        # Step 6: Assign users and templates
        wait_and_click(self.assign_template_button)
        wait_and_click(self.select_all_assign_user)
        wait_and_click(self.accept_changes_btn)
        print("✅ Selected all assigned users and saved changes.")

        wait_and_click(self.assign_user_to_connect_button)
        wait_and_click(self.select_group)
        wait_and_click(self.select_users)
        print(f" -> {self.group_search.all_inner_texts()}")
        print(f" -> {self.users_search.all_inner_texts()}")

        # Step 7: Submit and finalize user assignment
        wait_and_click(self.submit_button)
        print("✅ Submitted Group and User.")

        # Step 8: Select sending options
        wait_and_click(self.next_button)
        send_options = [
            self.send_options_label, self.send_egift_via_label, self.via_email,
            self.via_shareable_link, self.via_sms, self.via_senders_choice
        ]
        for option in send_options:
            expect(option).to_be_visible()

        wait_and_click(self.via_email)
        wait_and_click(self.next_button)

        # Step 9: Verify summary sections
        summary_sections = [
            self.connect_summary_label, self.egift_selection_section,
            self.connect_settings_details_section, self.sending_options_section
        ]
        for section in summary_sections:
            expect(section).to_be_visible()

            self.egift_selection_section.click()
            self.connect_settings_details_section.click()
            self.sending_options_section.click()

        # Step 10: Activate the new connect
        wait_and_click(self.active_new_connect)

        # Step 11: Verify the success message after activation
        success_message = self.page.locator(f"//span[contains(text(), '{Success_message}')]")
        expect(success_message).to_be_visible()
        print(f"✅ Success: {Success_message}!")

    @qase_screenshot
    @qase.step(
        title="Create connect with Ontrack Direct-2-Prospect functionality",
        expected="Connect with Ontrack Direct-2-Prospect functionality"
    )
    def verify_create_connect_Direct_2_Prospect_functionality(self, Select_Ontrack_Connect_Type: str,
                                                              Internal_Connect_Name: str, Sender_Name: str,
                                                              Connect_Description: str, Start_Date: str, End_Date: str,
                                                              Days_expires: str, Assign_token: str,
                                                              Success_message: str):
        def wait_and_click(element):
            """Wait for element to be visible and then click."""
            expect(element).to_be_visible()
            element.click()
            self.page.wait_for_timeout(2000)

        def wait_and_fill(element, value):
            """Wait for element to be visible and then fill the given value."""
            expect(element).to_be_visible()
            element.fill(value)
            self.page.wait_for_timeout(2000)

        # Step 1: Initiate connect creation process
        wait_and_click(self.create_new_connect_button)
        wait_and_click(self.ontrack_direct_2_prospect_radio_button)

        # Step 2: Select Connect Type
        Direct_2_Prospect = self.page.locator(f"//input[@id='{Select_Ontrack_Connect_Type}']")
        wait_and_click(Direct_2_Prospect)
        print(f"✅ Selected Ontrack Connect Type: '{Select_Ontrack_Connect_Type}'")

        wait_and_click(self.continue_button)
        wait_and_click(self.select_item_D2P)
        wait_and_click(self.next_button)

        # Step 4: Fill in connect details
        wait_and_fill(self.internal_name_input, Internal_Connect_Name)
        wait_and_fill(self.display_name_for_sender_input, Sender_Name)
        wait_and_fill(self.connect_description_input, Connect_Description)
        wait_and_fill(self.start_date_input, Start_Date)
        wait_and_fill(self.end_date_input, End_Date)

        # Step 5: Configure expiration and token assignment
        self.days_until_dropdown.select_option(label=Days_expires)
        self.assign_a_token_bucket_dropdown.select_option(label=Assign_token)

        # Step 6: Assign users and templates
        wait_and_click(self.assign_template_button)
        wait_and_click(self.select_all_assign_user)
        wait_and_click(self.accept_changes_btn)
        print("✅ Selected all assigned users and saved changes.")

        wait_and_click(self.assign_user_to_connect_button)
        wait_and_click(self.select_group)
        wait_and_click(self.select_users)
        print(f" -> {self.group_search.all_inner_texts()}")
        print(f" -> {self.users_search.all_inner_texts()}")

        # Step 7: Submit and finalize user assignment
        wait_and_click(self.submit_button)
        print("✅ Submitted Group and User.")

        # Step 8: Select sending options
        wait_and_click(self.next_button)

        # Step 9: Verify summary sections
        summary_sections = [
            self.connect_summary_label, self.gift_selection_section,
            self.connect_settings_details_section
        ]
        for section in summary_sections:
            expect(section).to_be_visible()
        self.gift_selection_section.click()
        self.page.wait_for_timeout(5000)
        self.connect_settings_details_section.click()

        # Step 10: Activate the new connect
        wait_and_click(self.active_new_connect)

        # Step 11: Verify the success message after activation
        success_message = self.page.locator(f"//span[contains(text(), '{Success_message}')]")
        expect(success_message).to_be_visible()
        print(f"✅ Success: {Success_message}!")


    @qase_screenshot
    @qase.step(
        title="Apply filter on connects and verify filtered data",
        expected="Data should be filtered properly based on the applied filter.",
    )
    def apply_filter_on_connects_and_verify_filtered_data(
            self, available_filter_options, expected_statuses
    ):
        """
        Apply filter on connects and verify filtered data
        """
        expect(self.filter_dropdown).to_be_visible()
        filter_options = self.page.query_selector_all(self.filter_options)
        filter_options_text = [option.inner_text() for option in filter_options]
        assert (
                filter_options_text == available_filter_options
        ), f"Expected: {available_filter_options}, but got: {filter_options_text}"
        print(f"all available filters verified: {available_filter_options}")
        for filter_option in available_filter_options:
            self.filter_option_to_select.select_option(filter_option)
            time.sleep(5)
            self.page.wait_for_selector(self.connects_status)
            # Query for the status elements after applying the filter
            connects_status = self.page.query_selector_all(self.connects_status)
            connects_status_text = [status.inner_text() for status in connects_status]
            # Print the text of each status
            print(
                f"Items status after applying '{filter_option}': {connects_status_text}"
            )
            # Assertion to verify the expected statuses are present
            if filter_option in expected_statuses:
                expected = expected_statuses[filter_option]
                if expected:
                    for expected_status in expected:
                        assert (
                                expected_status in connects_status_text
                        ), f"'{expected_status}' not found in the status text for filter '{filter_option}'"
                else:
                    # If there are no expected statuses, assert that the status list is empty
                    assert (
                        not connects_status_text
                    ), f"Expected no statuses for filter '{filter_option}', but found: {connects_status_text}"

    @qase_screenshot
    @qase.step(
        title="Verify create a new connect model elements",
        expected="User should be able to visible every elements of connect model",
    )
    def verify_create_a_new_connect_model_elements(self):
        """
        Verify and check availability of create a connect model elements
        """
        self.create_a_connect_title.click()
        elements_to_check = [
            self.close_button,
            self.continue_button,
            self.create_a_connect_model,
            self.create_a_connect_title,
            self.select_an_ontrack_connect_type_title,
            self.ontrack_egift_title,
            self.ontrack_egift_label,
            self.ontrack_egift_radio_button,
            self.ontrack_direct_2_prospect_radio_button,
            self.ontrack_direct_2_prospect_title,
            self.marketplace_label,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("create a connects model elements verified")


    @qase_screenshot
    @qase.step(title="Navigate to menu", expected="User should be able to navigate to the specified menu")
    def navigate_to_menu(self, menu_to_select: str):
        """
        Clicks on the specified menu item.
        """
        menu_locator = self.page.locator(f"//a[normalize-space()='{menu_to_select}']")
        expect(menu_locator).to_be_visible(timeout=5000)
        menu_locator.click()
        print(f"✅ Navigated to menu: {menu_to_select}")

    @qase_screenshot
    @qase.step(title="Verify Connects Page Elements",
               expected="All key elements on the Connects page should be visible and correct")
    def verify_connects_page__connect_table_elements(self, expected_title: str,
                                      expected_filter_label: str, expected_filter_value: str,
                                      expected_search_placeholder: str):
        """
        Verifies key elements on the Deployment Admin Connects Page:
        - Page title
        - Table headers
        - Filter label and selected value
        - Search input placeholder
        """

        # Verify page title
        expect(self.expected_title).to_be_visible(timeout=5000)
        actual_title = self.expected_title.inner_text().strip()
        assert actual_title == expected_title, f"Expected '{expected_title}', but got '{actual_title}'"
        print(f"✅ Page title verified: '{actual_title}'")

        # Verify Create Connect Button
        expect(self.create_connect_btn).to_be_visible(timeout=5000)
        actual_create_button_txt = self.create_connect_btn.inner_text().strip()
        assert actual_create_button_txt == "Create New Connect", f"Expected 'Create New Connect', but got '{actual_create_button_txt}'"
        print(f"✅ 'Create New Connect' button verified: '{actual_create_button_txt}'")

        # Verify table headers
        # actual_headers = [header.strip() for header in self.table_headers.all_inner_texts() if header.strip()]
        # assert actual_headers == headers_text, f"Expected headers {headers_text}, but got {actual_headers}"
        # print(f"✅ Table headers verified: {actual_headers}")

        # Verify filter label and value
        expect(self.filter_label).to_be_visible(timeout=5000)
        expect(self.filter_value).to_be_visible(timeout=5000)
        actual_label = self.filter_label.inner_text().strip()
        actual_value = self.filter_value.input_value().strip()
        assert actual_label == expected_filter_label, f"Expected label '{expected_filter_label}', but got '{actual_label}'"
        assert actual_value == expected_filter_value, f"Expected value '{expected_filter_value}', but got '{actual_value}'"
        print(f"✅ Filter label and value verified: Label='{actual_label}', Value='{actual_value}'")

        # Verify search input placeholder
        expect(self.search_input).to_be_visible(timeout=5000)
        actual_placeholder = self.search_input.get_attribute("placeholder")
        assert actual_placeholder == expected_search_placeholder, f"Expected placeholder '{expected_search_placeholder}', but got '{actual_placeholder}'"
        print(f"✅ Search input placeholder verified: '{actual_placeholder}'")

        # Verify pagination
        expect(self.pagination_btn).to_be_visible(timeout=5000)
        expect(self.show_result_txt).to_be_visible(timeout=5000)
        showing_results = self.show_result_txt.inner_text().strip()
        expect(self.section_dropdown).to_be_visible(timeout=5000)
        print(f"✅ Pagination elements are present '{showing_results}")

    def verify_edit_connect_page_elements_single_item_add(self ,success_message_text,):
        """
        Edit Connect page: Add a single item and save.
        """
        self.view_port.scroll_into_view_if_needed()
        expect(self.view_port).to_be_visible(timeout=10000)
        self.view_port.click()
        expect(self.edit_item).to_be_visible(timeout=10000)
        self.edit_item.click()
        time.sleep(10)
        expect(self.egift_selection_edit).to_be_visible(timeout=500000)
        self.egift_selection_edit.click()
        time.sleep(10)
        expect(self.delete).to_be_visible(timeout=5000)
        self.delete.click()
        self.view_port.scroll_into_view_if_needed()
        expect(self.view_port).to_be_visible(timeout=10000)  # Pass timeout inside expect()
        expect(self.item_add_1).to_be_visible(timeout=5000)
        time.sleep(5)
        self.item_add_1.click()
        self.save_btn.click()
        time.sleep(5)
        self.update_connect_btn.click()
        print("✅ Single item added and saved.")
        expect(self.success_message_txt).to_have_text(success_message_text)
        print("Edit Connect Successfully message verified")

    def verify_edit_connect_page_elements_range_item_add(self,Custom_Value: str, success_message_text):
        """
        Edit Connect page: Add a range of items and save.
        """
        self.view_port.scroll_into_view_if_needed()
        expect(self.view_port).to_be_visible(timeout=10000)
        self.view_port.click()
        expect(self.edit_item).to_be_visible(timeout=10000)
        self.edit_item.click()
        time.sleep(5)
        expect(self.egift_selection_edit).to_be_visible(timeout=500000)
        self.egift_selection_edit.click()
        time.sleep(5)
        expect(self.delete).to_be_visible(timeout=5000)
        self.delete.click()
        time.sleep(5)
        expect(self.item_add_range_item).to_be_visible(timeout=5000)
        time.sleep(10)
        self.item_add_range_item.click()
        self.edit_choice.click()
        time.sleep(5)
        self.input_choice.fill(str(Custom_Value))
        time.sleep(5)
        self.add_choice_btn.click()
        time.sleep(5)
        self.confirm_btn.click()
        time.sleep(2)
        self.save_btn.click()
        time.sleep(2)
        self.update_connect_btn.click()
        print("✅ Range item added and saved.")
        expect(self.success_message_txt).to_have_text(success_message_text)
        print("Edit Connect Successfully message verified")

