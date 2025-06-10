"""
Deployment Admin message templates page modules
"""

import re
import time

from qase.pytest import qase

from pages.base_page import BasePage
from playwright.sync_api import Page, expect

from utilities.decorators import qase_screenshot


class DeploymentAdminMessageTemplatesPage(BasePage):
    """
    Module containing objects and methods related to Deployment admin message templates page
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Role locator
        self.select_role_dropdown = page.locator('(//div[@class="dropdown"])[2]')
        self.select_role = '//a[text()="<<select_role>>"]'

        # Side navigation tab
        self.message_templates_icon = page.locator(
            '(//span[@class="nav-link-icon"])[2]'
        )
        self.message_templates_tab = '//span[text()="<<tab_to_navigate>>"]'

        # Email templates locators
        self.email_tab = page.locator('//button[text()="Email Templates"]')
        #self.sms_tab = page.locator('//button[text()="SMS Templates"]')
        self.d2p_tab = page.locator('//button[text()="D2P Templates"]')
        self.message_templates_to_navigate = '//button[text()="<<tab_to_navigate>>"]'
        self.email_templates_header = page.locator('//h3[text()="Email Templates"]')
        self.email_templates_create_new_templates_button = page.locator(
            '//div[@id="template-tabs-tabpane-EmailTemplates"]//button[text()="Create New Template"]'
        )
        self.email_templates_filter_label = page.locator(
            '(//div[@class="filter-text-icon"][normalize-space()="Filter:"])[1]'
        )
        self.email_templates_filter_select_option = page.locator(
            '(//div[@id="template-tabs-tabpane-EmailTemplates"]//select)[1]'
        )
        self.email_templates_search_label = page.locator(
            '//div[@id="template-tabs-tabpane-EmailTemplates"]//label[text()="Search"]'
        )
        self.email_templates_search_input = page.locator(
            '//div[@id="template-tabs-tabpane-EmailTemplates"]//input'
        )
        self.email_templates_actions_button = page.locator(
            '(//div[@id="template-tabs-tabpane-EmailTemplates"]//div[@class="font-sans-serif btn-reveal-trigger dropend"]//button)[1]'
        )
        self.email_templates_edit_action_button = page.locator(
            '//div[@id="template-tabs-tabpane-EmailTemplates"]//a[text()="Edit"]'
        )
        self.email_templates_delete_action_button = page.locator(
            '//div[@id="template-tabs-tabpane-EmailTemplates"]//a[text()="Delete"]'
        )
        self.email_templates_table_headers = page.locator(
            '(//div[@id="template-tabs-tabpane-EmailTemplates"]//tr)[1]'
        )
        self.email_templates_visibility_status = "//div[@id='template-tabs-tabpane-EmailTemplates']//div[contains(@class, 'badge') and contains(@class, 'btn-outline')]"
        self.email_templates_name = (
            "//div[@id='template-tabs-tabpane-EmailTemplates']//td[1]"
        )
        self.single_email_template_name = page.locator(
            '(//div[@id="template-tabs-tabpane-EmailTemplates"]//td)[1]'
        )
        self.email_templates_footer = page.locator(
            '//div[@id="template-tabs-tabpane-EmailTemplates"]//div[@class="table-footer-border-top card-footer"]'
        )
        self.email_templates_pagination = page.locator(
            '//div[@id="template-tabs-tabpane-EmailTemplates"]//div//div[contains(@class,"d-flex pagination-numbers m-auto mb-2")]'
        )
        self.email_templates_row_per_page = page.locator(
            '//div[@id="template-tabs-tabpane-EmailTemplates"]//div[@class="d-flex align-items-center fs--1 ps-3"]'
        )
        self.email_templates_result_counter = page.locator(
            '//div[@id="template-tabs-tabpane-EmailTemplates"]//div[@class="d-flex align-items-center fs--1 ps-3 d-flex flex-wrap rows-page-count"]'
        )
        self.email_templates_filter_options = (
            '(//div[@id="template-tabs-tabpane-EmailTemplates"]//select)[1]//option'
        )
        self.email_template_select_option = page.locator(
            '(//div[@id="template-tabs-tabpane-EmailTemplates"]//select)[1]'
        )

        # SMS templates locators
        self.sms_templates_header = page.locator('//h3[text()="SMS Templates"]')
        self.sms_templates_create_new_templates_button = page.locator(
            '//div[@id="template-tabs-tabpane-SMS Templates"]//button[text()="Create New Template"]'
        )
        self.sms_templates_filter_label = page.locator(
            '//div[@id="template-tabs-tabpane-SMS Templates"]//label[text()="Filter:"]'
        )
        self.sms_templates_filter_options = (
            '(//div[@id="template-tabs-tabpane-SMS Templates"]//select)[1]//option'
        )
        self.sms_template_select_option = page.locator(
            '(//div[@id="template-tabs-tabpane-SMS Templates"]//select)[1]'
        )

        self.sms_templates_search_label = page.locator(
            '//div[@id="template-tabs-tabpane-SMS Templates"]//label[text()="Search"]'
        )
        self.sms_templates_search_input = page.locator(
            '//div[@id="template-tabs-tabpane-SMS Templates"]//input'
        )
        self.sms_templates_actions_button = page.locator(
            '(//div[@id="template-tabs-tabpane-SMS Templates"]//div[@class="font-sans-serif btn-reveal-trigger dropend"]//button)[1]'
        )
        self.sms_templates_edit_action_button = page.locator(
            '//div[@id="template-tabs-tabpane-SMS Templates"]//a[text()="Edit"]'
        )
        self.sms_templates_delete_action_button = page.locator(
            '//div[@id="template-tabs-tabpane-SMS Templates"]//a[text()="Delete"]'
        )
        self.sms_templates_table_headers = page.locator(
            '(//div[@id="template-tabs-tabpane-SMS Templates"]//tr)[1]'
        )
        self.sms_templates_visibility_status = "//div[@id='template-tabs-tabpane-SMS Templates']//div[contains(@class, 'badge') and contains(@class, 'btn-outline')]"
        self.sms_templates_name = (
            "//div[@id='template-tabs-tabpane-SMS Templates']//td[1]"
        )
        self.single_sms_template_name = page.locator(
            '(//div[@id="template-tabs-tabpane-SMS Templates"]//td)[1]'
        )
        self.sms_templates_footer = page.locator(
            '//div[@id="template-tabs-tabpane-SMS Templates"]//div[@class="table-footer-border-top card-footer"]'
        )
        self.sms_templates_pagination = page.locator(
            '//div[@id="template-tabs-tabpane-SMS Templates"]//div[@class="d-flex pagination-numbers"]'
        )
        self.sms_templates_row_per_page = page.locator(
            '//div[@id="template-tabs-tabpane-SMS Templates"]//div[@class="d-flex align-items-center fs--1 ps-3"]'
        )
        self.sms_templates_result_counter = page.locator(
            '//div[@id="template-tabs-tabpane-SMS Templates"]//div[@class="d-flex align-items-center fs--1 ps-3 d-flex flex-wrap rows-page-count"]'
        )

        # add template locator
        self.add_template_header = page.locator(
            '//div[@class="modal-content"]//div[text()="Add Template"]'
        )
        self.template_variables_header = page.locator(
            '//div[@class="modal-content"]//h4[text()="Template variables"]'
        )
        self.create_template_header = page.locator(
            '//div[@class="modal-content"]//h4[text()="Create Template"]'
        )
        self.template_name_label = page.locator(
            '//div[@class="modal-content"]//label[text()="Template Name"]'
        )
        self.input_templates_name = page.locator(
            '//div[@class="modal-content"]//input[@id="name"]'
        )
        self.make_this_private_text = page.locator(
            '//div[@class="modal-content"]//span[text()="Make this Template Private"]'
        )
        self.make_this_template_private_checkbox = page.locator(
            '//div[@class="modal-content"]//input[@name="isPrivate"]'
        )
        self.view_template_button = page.locator(
            '//div[@class="modal-content"]//ins[text()="View Template"]'
        )
        self.save_button = page.locator('//span[text()="Save"]')
        self.cancel_button = page.locator('//span[text()="Cancel"]')
        self.recipient_name_label = page.locator(
            '(//span[text()="{{recipient_name}}"])'
        )
        self.sender_name_label = page.locator('(//span[text()="{{sender_name}}"])')
        self.signature_label = page.locator('(//span[text()="{{signature}}"])')
        self.toolbar = page.locator('//div[@class="ck ck-toolbar ck-toolbar_grouping"]')
        self.paragraph_dropdown = page.locator(
            '//button[@class="ck ck-button ck-off ck-button_with-text ck-dropdown__button"]'
        )
        self.bold_button = page.locator(
            '//button[@data-cke-tooltip-text="Bold (Ctrl+B)"]'
        )
        self.italic_button = page.locator(
            '//button[@data-cke-tooltip-text="Italic (Ctrl+I)"]'
        )
        self.block_quote_button = page.locator(
            '//button[@data-cke-tooltip-text="Block quote"]'
        )
        self.link_button = page.locator(
            '//button[@data-cke-tooltip-text="Link (Ctrl+K)"]'
        )
        self.numbered_list = page.locator(
            '//button[@data-cke-tooltip-text="Numbered List"]'
        )
        self.bulleted_list = page.locator(
            '//button[@data-cke-tooltip-text="Bulleted List"]'
        )
        self.upload_image_from_computer_button = page.locator(
            '//button[@data-cke-tooltip-text="Upload image from computer"]'
        )
        self.insert_table = page.locator(
            '//button[@data-cke-tooltip-text="Insert table"]'
        )
        self.column = page.locator('//button[@data-cke-tooltip-text="Column"]')
        self.raw = page.locator('//button[@data-cke-tooltip-text="Row"]')
        self.merge_cell = page.locator(
            '//button[@data-cke-tooltip-text="Merge cells"][1]'
        )
        self.insert_media = page.locator(
            '//button[@data-cke-tooltip-text="Insert media"]'
        )
        self.undo = page.locator('//button[@data-cke-tooltip-text="Undo (Ctrl+Z)"]')
        self.redo = page.locator('//button[@data-cke-tooltip-text="Redo (Ctrl+Y)"]')
        self.template_content = page.locator('//div[@class="ck ck-editor__main"]//p')
        self.sms_template_paragraph = page.locator(
            '//div[@class="ant-form-item-control-input-content"]//textarea'
        )
        self.sms_preview_header = page.locator(
            '//div[@class="modal-title h4"][text()="SMS Preview"]'
        )
        self.sms_text = page.locator('//textarea[@id="smsForm_textarea"]')

        # template preview locator
        self.template_preview_header = page.locator('//div[contains(text(),"Template Preview")]')
        self.d2p_preview_header = page.locator('//div[contains(text(),"D2P Preview")]')
        self.close_button = page.locator('//button//span[text()="Close"]')
        self.paragraph_text = page.locator('//a[normalize-space()="Claim Gift"]')
        self.card_header = page.locator('//div[contains(text(),"Template Preview")]')
        self.enter_text = page.locator('//div[@class="ck ck-editor__main"]//p')
        self.model_close = page.locator('//button[@class="btn-close"]')
        self.edit_email_templates_descriptions = page.locator(
            '//div[@class="ck ck-editor__main"]'
        )

        # D2P tem[plates locators
        self.d2p_templates_header = page.locator('//h3[text()="D2P Templates"]')
        self.d2p_templates_create_new_templates_button = page.locator(
            '//div[@id="template-tabs-tabpane-D2P Templates"]//button[text()="Create New Template"]'
        )
        self.d2p_templates_filter_label = page.locator(
            '//div[@id="template-tabs-tabpane-D2P Templates"]//div//div[contains(@class,"filter-text-icon")][normalize-space()="Filter:"]'
        )
        self.d2p_templates_filter_select_option = page.locator(
            '(//div[@id="template-tabs-tabpane-D2P Templates"]//select)[1]'
        )
        self.d2p_templates_search_label = page.locator(
            '//div[@id="template-tabs-tabpane-D2P Templates"]//label[text()="Search"]'
        )
        self.d2p_templates_search_input = page.locator(
            '//div[@id="template-tabs-tabpane-D2P Templates"]//input'
        )
        self.d2p_templates_actions_button = page.locator(
            '(//div[@id="template-tabs-tabpane-D2P Templates"]//div[@class="font-sans-serif btn-reveal-trigger dropend"]//button)[1]'
        )
        self.d2p_templates_edit_action_button = page.locator(
            '//div[@id="template-tabs-tabpane-D2P Templates"]//a[text()="Edit"]'
        )
        self.d2p_templates_delete_action_button = page.locator(
            '//div[@id="template-tabs-tabpane-D2P Templates"]//a[text()="Delete"]'
        )
        self.d2p_templates_table_headers = page.locator(
            '(//div[@id="template-tabs-tabpane-D2P Templates"]//tr)[1]'
        )
        self.d2p_templates_visibility_status = "//div[@id='template-tabs-tabpane-D2P Templates']//div[contains(@class, 'badge') and contains(@class, 'btn-outline')]"
        self.d2p_templates_name = (
            "//div[@id='template-tabs-tabpane-D2P Templates']//td[1]"
        )
        self.single_d2p_template_name = page.locator(
            '(//div[@id="template-tabs-tabpane-D2P Templates"]//td)[1]'
        )
        self.d2p_templates_footer = page.locator(
            '//div[@id="template-tabs-tabpane-D2P Templates"]//div[@class="table-footer-border-top card-footer"]'
        )
        self.d2p_templates_pagination = page.locator(
            '//div[@id="template-tabs-tabpane-D2P Templates"]//div//div[contains(@class,"d-flex pagination-numbers m-auto mb-2")]'
        )
        self.d2p_templates_row_per_page = page.locator(
            '//div[@id="template-tabs-tabpane-D2P Templates"]//div[@class="d-flex align-items-center fs--1 ps-3"]'
        )
        self.d2p_templates_result_counter = page.locator(
            '//div[@id="template-tabs-tabpane-D2P Templates"]//div[@class="d-flex align-items-center fs--1 ps-3 d-flex flex-wrap rows-page-count"]'
        )
        self.d2p_templates_filter_options = (
            '(//div[@id="template-tabs-tabpane-D2P Templates"]//select)[1]//option'
        )
        self.d2p_template_select_option = page.locator(
            '(//div[@id="template-tabs-tabpane-D2P Templates"]//select)[1]'
        )
        self.delete_confirm_message = page.locator('//div[@class="modal-body"]')
        self.generic_update_button = page.locator('//button[text()="Confirm"]')
        self.notice_message = page.locator('//div[@class="ant-message-notice-content"]')

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
        title="Verify account balance icon and tab working",
        expected="deployment admin should be able to open and view account balance tab",
    )
    def verify_and_click_on_message_templates_tab(self, tab_to_navigate):
        """
        Verify message templates and click on message templates tab
        """
        # verify icon availability
        expect(self.message_templates_icon).to_be_visible()
        # clicking on message templates tab
        self.page.click(
            self.message_templates_tab.replace("<<tab_to_navigate>>", tab_to_navigate)
        )
        print(f"successfully able to click on {tab_to_navigate} tab")

    @qase_screenshot
    @qase.step(
        title="Verify email templates page element visibility",
        expected="Deployment admin should be able to visible all elements of the email templates page",
    )
    def verify_email_templates_page_elements(
        self, templates_data_table_headers, available_filter_options
    ):
        """
        Verify email templates page elements
        """
        self.page.wait_for_load_state("domcontentloaded")
        elements_to_check = [
            self.email_tab,
            #self.sms_tab,
            self.d2p_tab,
            self.email_templates_create_new_templates_button,
            self.email_templates_filter_label,
            self.email_templates_search_label,
            self.email_templates_search_input,
            self.email_templates_header,
            self.email_templates_footer,
            self.email_templates_pagination,
            self.email_templates_row_per_page,
            self.email_templates_result_counter,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        header_text = self.email_templates_table_headers.inner_text()
        headers = header_text.strip().split("\t")
        print(f"Extracted Headers: {headers}")
        # Verify that the headers match the expected column titles
        assert (
            headers == templates_data_table_headers
        ), f"Expected headers {templates_data_table_headers}, but found {headers}"
        filter_options_raw = self.email_templates_filter_select_option.inner_text()
        filter_options = [
            option.strip()
            for option in filter_options_raw.splitlines()
            if option.strip()
        ]
        print(f"Extracted Filter Options: {filter_options}")
        assert (
            filter_options == available_filter_options
        ), f"Expected filter options {available_filter_options}, but found {filter_options}"

    @qase_screenshot
    @qase.step(
        title="Verify sms templates page element visibility",
        expected="Deployment admin should be able to visible all elements of the sms templates page",
    )
    def verify_sms_templates_page_elements(
        self, templates_data_table_headers, available_filter_options, tab_to_navigate
    ):
        """
        Verify sms templates page elements
        """
        self.page.wait_for_load_state("domcontentloaded")
        self.page.click(
            self.message_templates_to_navigate.replace(
                "<<tab_to_navigate>>", tab_to_navigate
            )
        )
        elements_to_check = [
            self.email_tab,
           # self.sms_tab,
            self.d2p_tab,
            self.sms_templates_create_new_templates_button,
            self.sms_templates_filter_label,
            self.sms_templates_search_label,
            self.sms_templates_search_input,
            self.sms_templates_header,
            self.sms_templates_footer,
            self.sms_templates_pagination,
            self.sms_templates_row_per_page,
            self.sms_templates_result_counter,
        ]
        # Verify all elements are visible
        for element in elements_to_check:
            expect(element).to_be_visible()
        # Extract and verify table headers
        header_text = self.sms_templates_table_headers.inner_text()
        print(f"Raw Header Text: {repr(header_text)}")  # Debugging log
        # Dynamically split concatenated text based on capitalization or spaces
        headers = re.findall(r"[A-Z][^A-Z]*", header_text)
        # Remove any trailing or leading spaces from the extracted headers
        headers = [header.strip() for header in headers if header.strip()]
        print(f"Extracted Headers: {headers}")
        assert (
            headers == templates_data_table_headers
        ), f"Expected headers {templates_data_table_headers}, but found {headers}"
        # Extract and verify filter options
        filter_options_raw = self.email_templates_filter_select_option.inner_text()
        print(f"Raw Filter Options Text: {repr(filter_options_raw)}")  # Debugging log
        # Adjusted regex to correctly capture full filter options (e.g., "All Templates" instead of separate "All" and "Templates")
        filter_options = re.findall(r"[A-Z][a-z]*\s?[A-Z]?[a-z]*", filter_options_raw)
        # Remove any trailing or leading spaces from the extracted filter options
        filter_options = [option.strip() for option in filter_options if option.strip()]
        print(f"Extracted Filter Options: {filter_options}")
        assert (
            filter_options == available_filter_options
        ), f"Expected filter options {available_filter_options}, but found {filter_options}"

    @qase_screenshot
    @qase.step(
        title="Verify d2p templates page element visibility",
        expected="Deployment admin should be able to visible all elements of the d2p templates page",
    )
    def verify_d2p_templates_page_elements(
        self, templates_data_table_headers, available_filter_options, tab_to_navigate
    ):
        """
        Verify d2p templates page elements
        """
        self.page.wait_for_load_state("domcontentloaded")
        self.page.click(
            self.message_templates_to_navigate.replace(
                "<<tab_to_navigate>>", tab_to_navigate
            )
        )
        elements_to_check = [
            self.email_tab,
           # self.sms_tab,
            self.d2p_tab,
            self.d2p_templates_create_new_templates_button,
            self.d2p_templates_filter_label,
            self.d2p_templates_search_label,
            self.d2p_templates_search_input,
            self.d2p_templates_header,
            self.d2p_templates_footer,
            self.d2p_templates_pagination,
            self.d2p_templates_row_per_page,
            self.d2p_templates_result_counter,
        ]
        # Verify all elements are visible
        for element in elements_to_check:
            expect(element).to_be_visible()
        # Extract and verify table headers
        header_text = self.d2p_templates_table_headers.inner_text()
        print(f"Raw Header Text: {repr(header_text)}")  # Debugging log
        # Dynamically split concatenated text based on capitalization or spaces
        headers = re.findall(r"[A-Z][^A-Z]*", header_text)
        # Remove any trailing or leading spaces from the extracted headers
        headers = [header.strip() for header in headers if header.strip()]
        print(f"Extracted Headers: {headers}")
        assert (
            headers == templates_data_table_headers
        ), f"Expected headers {templates_data_table_headers}, but found {headers}"
        # Extract and verify filter options
        filter_options_raw = self.email_templates_filter_select_option.inner_text()
        print(f"Raw Filter Options Text: {repr(filter_options_raw)}")  # Debugging log
        # Adjusted regex to correctly capture full filter options (e.g., "All Templates" instead of separate "All" and "Templates")
        filter_options = re.findall(r"[A-Z][a-z]*\s?[A-Z]?[a-z]*", filter_options_raw)
        # Remove any trailing or leading spaces from the extracted filter options
        filter_options = [option.strip() for option in filter_options if option.strip()]
        print(f"Extracted Filter Options: {filter_options}")
        assert (
            filter_options == available_filter_options
        ), f"Expected filter options {available_filter_options}, but found {filter_options}"

    @qase_screenshot
    @qase.step(
        title="Verify filter functionality email templates",
        expected="filter functionality should be working as expect inside the email templates",
    )
    def verify_filter_functionality_of_email_templates(
        self, available_filter_options, expected_statuses
    ):
        """
        Verify filter functionality of email templates
        """
        time.sleep(2)
        filter_options = self.page.query_selector_all(
            self.email_templates_filter_options
        )
        print(filter_options)
        filter_options_text = [option.inner_text() for option in filter_options]
        assert (
            filter_options_text == available_filter_options
        ), f"Expected: {available_filter_options}, but got: {filter_options_text}"
        print(f"all available filters verified: {available_filter_options}")
        for filter_option in available_filter_options:
            self.email_template_select_option.select_option(filter_option)
            time.sleep(5)
            self.page.wait_for_selector(self.email_templates_visibility_status)
            # Query for the status elements after applying the filter
            all_items_status = self.page.query_selector_all(
                self.email_templates_visibility_status
            )
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

    @qase_screenshot
    @qase.step(
        title="Verify filter functionality sms templates",
        expected="filter functionality should be working as expect inside the sms templates",
    )
    def verify_filter_functionality_of_sms_templates(
        self, available_filter_options, expected_statuses, tab_to_navigate
    ):
        """
        Verify filter functionality of sms templates
        """
        self.page.click(
            self.message_templates_to_navigate.replace(
                "<<tab_to_navigate>>", tab_to_navigate
            )
        )
        time.sleep(2)
        filter_options = self.page.query_selector_all(self.sms_templates_filter_options)
        print(filter_options)
        filter_options_text = [option.inner_text() for option in filter_options]
        assert (
            filter_options_text == available_filter_options
        ), f"Expected: {available_filter_options}, but got: {filter_options_text}"
        print(f"all available filters verified: {available_filter_options}")
        for filter_option in available_filter_options:
            self.sms_template_select_option.select_option(filter_option)
            time.sleep(5)
            self.page.wait_for_selector(self.sms_templates_visibility_status)
            # Query for the status elements after applying the filter
            all_items_status = self.page.query_selector_all(
                self.sms_templates_visibility_status
            )
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

    @qase_screenshot
    @qase.step(
        title="Verify filter functionality d2p templates",
        expected="filter functionality should be working as expect inside the d2p templates",
    )
    def verify_filter_functionality_of_d2p_templates(
        self, available_filter_options, expected_statuses, tab_to_navigate
    ):
        """
        Verify filter functionality of d2p templates
        """
        self.page.click(
            self.message_templates_to_navigate.replace(
                "<<tab_to_navigate>>", tab_to_navigate
            )
        )
        time.sleep(2)
        filter_options = self.page.query_selector_all(self.d2p_templates_filter_options)
        print(filter_options)
        filter_options_text = [option.inner_text() for option in filter_options]
        assert (
            filter_options_text == available_filter_options
        ), f"Expected: {available_filter_options}, but got: {filter_options_text}"
        print(f"all available filters verified: {available_filter_options}")
        for filter_option in available_filter_options:
            self.d2p_template_select_option.select_option(filter_option)
            time.sleep(5)
            self.page.wait_for_selector(self.d2p_templates_visibility_status)
            # Query for the status elements after applying the filter
            all_items_status = self.page.query_selector_all(
                self.d2p_templates_visibility_status
            )
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

    @qase_screenshot
    @qase.step(
        title="Verify search functionality email templates",
        expected="search functionality should be working as expect inside the email templates",
    )
    def verify_search_functionality_of_email_templates(self):
        """
        verify and check search functionality of email templates
        """
        self.email_templates_search_input.fill("t")
        time.sleep(3)
        # Query for all email template names
        searched_name_elements = self.page.query_selector_all(self.email_templates_name)
        # Extract the text content from each of the elements
        searched_names = [element.text_content() for element in searched_name_elements]
        # Print the extracted names for debugging
        print(searched_names)
        # Assert if "t" or "T" is in any of the template names (case-insensitive)
        assert any("t" in name or "T" in name for name in searched_names)

    @qase_screenshot
    @qase.step(
        title="Verify search functionality sms templates",
        expected="search functionality should be working as expect inside the sms templates",
    )
    def verify_search_functionality_of_sms_templates(self, tab_to_navigate):
        """
        verify and check search functionality of sms templates
        """
        self.page.click(
            self.message_templates_to_navigate.replace(
                "<<tab_to_navigate>>", tab_to_navigate
            )
        )
        time.sleep(2)
        self.sms_templates_search_input.fill("s")
        time.sleep(3)
        searched_name_elements = self.page.query_selector_all(self.sms_templates_name)
        # Extract the text content from each of the elements
        searched_names = [element.text_content() for element in searched_name_elements]
        # Print the extracted names for debugging
        print(searched_names)
        # Assert if "s" or "S" is in any of the template names (case-insensitive)
        assert any("s" in name or "S" in name for name in searched_names)

    @qase_screenshot
    @qase.step(
        title="Verify search functionality d2p templates",
        expected="filter functionality should be working as expect inside the d2p templates",
    )
    def verify_search_functionality_of_d2p_templates(self, tab_to_navigate):
        """
        verify and check search functionality of d2p templates
        """
        self.page.click(
            self.message_templates_to_navigate.replace(
                "<<tab_to_navigate>>", tab_to_navigate
            )
        )
        time.sleep(2)
        self.d2p_templates_search_input.fill("d")
        time.sleep(3)
        searched_name_elements = self.page.query_selector_all(self.d2p_templates_name)
        # Extract the text content from each of the elements
        searched_names = [element.text_content() for element in searched_name_elements]
        # Print the extracted names for debugging
        print(searched_names)
        # Assert if "d" or "D" is in any of the template names (case-insensitive)
        assert any("d" in name or "D" in name for name in searched_names)

    @qase_screenshot
    @qase.step(
        title="Verify create new template functionality email templates",
        expected="create new template functionality should be working as expect inside the email templates",
    )
    def verify_create_new_templates_of_email_templates(
        self, template_name, enter_text_in_paragraph
    ):
        """
        Verify and check create new template functionality of email templates
        """
        self.email_templates_create_new_templates_button.click()
        time.sleep(3)
        elements_to_check = [
            self.add_template_header,
            self.template_variables_header,
            self.recipient_name_label,
            self.sender_name_label,
            self.signature_label,
            self.create_template_header,
            self.template_name_label,
            self.input_templates_name,
            self.paragraph_dropdown,
            self.bold_button,
            self.italic_button,
            self.block_quote_button,
            self.link_button,
            self.bulleted_list,
            self.numbered_list,
            #self.upload_image_from_computer_button,
            self.insert_media,
            self.insert_table,
            self.column,
            self.raw,
            self.undo,
            self.redo,
            self.merge_cell,
            self.make_this_template_private_checkbox,
            self.make_this_private_text,
            self.view_template_button,
            self.save_button,
            self.cancel_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        self.input_templates_name.fill(template_name)
        self.enter_text.fill(enter_text_in_paragraph)
        self.view_template_button.click()
        expect(self.template_preview_header).to_be_visible()
        expect(self.close_button).to_be_visible()
        expect(self.paragraph_text).to_be_visible()
        text_in_template_review = self.card_header.text_content()
        print(text_in_template_review)
        print(enter_text_in_paragraph)
        self.close_button.click()
        return template_name, enter_text_in_paragraph

    @qase_screenshot
    @qase.step(
        title="Verify create new template functionality sms templates",
        expected="create new template functionality should be working as expect inside the sms templates",
    )
    def verify_create_new_templates_of_sms_templates(
        self, tab_to_navigate, template_name, enter_text_in_paragraph
    ):
        """
        Verify and check create new template functionality of sms templates
        """
        self.page.click(
            self.message_templates_to_navigate.replace(
                "<<tab_to_navigate>>", tab_to_navigate
            )
        )
        self.sms_templates_create_new_templates_button.click()
        elements_to_check = [
            self.add_template_header,
            self.template_variables_header,
            self.recipient_name_label,
            self.sender_name_label,
            self.signature_label,
            self.create_template_header,
            self.template_name_label,
            self.input_templates_name,
            self.make_this_template_private_checkbox,
            self.make_this_private_text,
            self.view_template_button,
            self.save_button,
            self.cancel_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        self.input_templates_name.fill(template_name)
        self.sms_template_paragraph.fill(enter_text_in_paragraph)
        self.view_template_button.click()
        expect(self.sms_preview_header).to_be_visible()
        expect(self.close_button).to_be_visible()
        expect(self.sms_text).to_be_visible()
        text_in_template_review = self.sms_text.text_content()
        print(text_in_template_review)
        print(enter_text_in_paragraph)
        assert text_in_template_review == enter_text_in_paragraph
        self.close_button.click()
        return template_name, enter_text_in_paragraph

    @qase_screenshot
    @qase.step(
        title="Verify create new template functionality d2p templates",
        expected="create new template functionality should be working as expect inside the d2p templates",
    )
    def verify_create_new_templates_of_d2p_templates(
        self, tab_to_navigate, template_name, enter_text_in_paragraph
    ):
        """
        Verify and check create new template functionality of d2p templates
        """
        self.page.click(
            self.message_templates_to_navigate.replace(
                "<<tab_to_navigate>>", tab_to_navigate
            )
        )
        self.d2p_templates_create_new_templates_button.click()
        elements_to_check = [
            self.add_template_header,
            self.add_template_header,
            self.template_variables_header,
            self.recipient_name_label,
            self.sender_name_label,
            self.signature_label,
            self.create_template_header,
            self.template_name_label,
            self.input_templates_name,
            self.paragraph_dropdown,
            self.bold_button,
            self.italic_button,
            self.block_quote_button,
            self.link_button,
            self.bulleted_list,
            self.numbered_list,
            #self.upload_image_from_computer_button,
            self.insert_media,
            self.insert_table,
            self.column,
            self.raw,
            self.undo,
            self.redo,
            self.merge_cell,
            self.make_this_template_private_checkbox,
            self.make_this_private_text,
            self.view_template_button,
            self.save_button,
            self.cancel_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        self.input_templates_name.fill(template_name)
        self.enter_text.fill(enter_text_in_paragraph)
        self.view_template_button.click()
        expect(self.d2p_preview_header).to_be_visible()
        expect(self.close_button).to_be_visible()
        expect(self.paragraph_text).to_be_visible()
        text_in_template_review = self.card_header.text_content()
        print(text_in_template_review)
        print(enter_text_in_paragraph)
        assert text_in_template_review == enter_text_in_paragraph
        self.close_button.click()
        return template_name, enter_text_in_paragraph

    @qase_screenshot
    @qase.step(
        title="Verify actions(edit/delete) functionality email templates",
        expected="actions functionality should be working as expect inside the email templates",
    )
    def verify_actions_functionality_of_email_templates(
        self, template_name, enter_text_in_paragraph
    ):
        """
        verify and check actions functionality of email templates
        """
        self.email_templates_create_new_templates_button.click()
        self.input_templates_name.fill(template_name)
        self.enter_text.fill(enter_text_in_paragraph)
        self.save_button.click()
        time.sleep(4)
        name = self.single_email_template_name.text_content()
        print(name)
        print(template_name)
#        assert template_name == name
        self.email_templates_actions_button.click()
        expect(self.email_templates_delete_action_button).to_be_visible()
        expect(self.email_templates_edit_action_button).to_be_visible()
        self.email_templates_edit_action_button.click()
        paragraph_text = self.edit_email_templates_descriptions.text_content()
#        assert enter_text_in_paragraph == paragraph_text
        self.model_close.click()
        self.email_templates_actions_button.click()
        self.email_templates_delete_action_button.click()
        confirm_message_text = self.delete_confirm_message.text_content()
        print(f"Confirm message text is: {confirm_message_text}")
        assert confirm_message_text == "Are you sure you want to delete this record?"
        self.generic_update_button.click()
        expect(self.notice_message).to_be_visible()
        message_text = self.notice_message.text_content()
        print(message_text)
        assert message_text == "Template deleted successfully"

    @qase_screenshot
    @qase.step(
        title="Verify actions(edit/delete) functionality sms templates",
        expected="actions functionality should be working as expect inside the sms templates",
    )
    def verify_actions_functionality_of_sms_templates(
        self, tab_to_navigate, enter_text_in_paragraph, template_name
    ):
        """
        verify and check actions functionality of sms templates
        """
        self.page.click(
            self.message_templates_to_navigate.replace(
                "<<tab_to_navigate>>", tab_to_navigate
            )
        )
        self.sms_templates_create_new_templates_button.click()
        self.input_templates_name.fill(template_name)
        self.sms_template_paragraph.fill(enter_text_in_paragraph)
        self.save_button.click()
        time.sleep(3)
        name = self.single_sms_template_name.text_content()
        print(name)
        print(template_name)
        assert template_name == name
        self.sms_templates_actions_button.click()
        expect(self.sms_templates_delete_action_button).to_be_visible()
        expect(self.sms_templates_edit_action_button).to_be_visible()
        self.sms_templates_edit_action_button.click()
        paragraph_text = self.edit_email_templates_descriptions.text_content()
        assert enter_text_in_paragraph == paragraph_text
        self.model_close.click()
        self.sms_templates_actions_button.click()
        self.sms_templates_delete_action_button.click()
        confirm_message_text = self.delete_confirm_message.text_content()
        print(f"Confirm message text is: {confirm_message_text}")
        assert confirm_message_text == "Are you sure you want to delete this record?"
        self.generic_update_button.click()
        expect(self.notice_message).to_be_visible()
        message_text = self.notice_message.text_content()
        print(message_text)
        assert message_text == "Template deleted successfully"

    @qase_screenshot
    @qase.step(
        title="Verify actions(edit/delete) functionality d2p templates",
        expected="actions functionality should be working as expect inside the d2p templates",
    )
    def verify_actions_functionality_of_d2p_templates(
        self, tab_to_navigate, template_name, enter_text_in_paragraph
    ):
        """
        verify and check actions functionality of d2p templates
        """
        self.page.click(
            self.message_templates_to_navigate.replace(
                "<<tab_to_navigate>>", tab_to_navigate
            )
        )
        self.d2p_templates_create_new_templates_button.click()
        self.input_templates_name.fill(template_name)
        self.enter_text.fill(enter_text_in_paragraph)
        self.save_button.click()
        time.sleep(3)
        name = self.single_d2p_template_name.text_content()
        print(name)
        print(template_name)
        assert template_name == name
        self.d2p_templates_actions_button.click()
        expect(self.d2p_templates_delete_action_button).to_be_visible()
        expect(self.d2p_templates_edit_action_button).to_be_visible()
        self.d2p_templates_edit_action_button.click()
        paragraph_text = self.edit_email_templates_descriptions.text_content()
        assert enter_text_in_paragraph == paragraph_text
        self.model_close.click()
        self.d2p_templates_actions_button.click()
        self.d2p_templates_delete_action_button.click()
        confirm_message_text = self.delete_confirm_message.text_content()
        print(f"Confirm message text is: {confirm_message_text}")
        assert confirm_message_text == "Are you sure you want to delete this record?"
        self.generic_update_button.click()
        expect(self.notice_message).to_be_visible()
        message_text = self.notice_message.text_content()
        print(message_text)
        assert message_text == "Template deleted successfully"
