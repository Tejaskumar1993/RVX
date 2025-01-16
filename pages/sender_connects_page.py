"""
Sender connects page modules
"""

import time

from qase.pytest import qase
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

from utilities.decorators import qase_screenshot


class SenderConnectsPage(BasePage):
    """
    Module containing objects and methods related to sender connects page
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.change_role_dropdown = page.locator('(//button[@id="dropdown-flags"])[2]')
        self.role_to_select = '//a[text()="<<role_to_change>>"]'
        self.connects_icon = page.locator('//*[@data-icon="chart-pie"]')
        self.connects_page_component = page.locator(
            '//div[@class="py-3 mb-2 account-balance-card card"]'
        )
        self.connects_page_title = page.locator('//h3[text()="Make a connection"]')
        self.connects_page_sub_title = page.locator(
            '//p[text()="View your available connects."]'
        )
        self.all_tab = page.locator(
            '//button[@id="account-balance-dashboard-tab-tab-all"]'
        )
        self.egifts_tab = page.locator(
            '//button[@id="account-balance-dashboard-tab-tab-egifts-deposit"]'
        )
        self.ontrack_d2p_tab = page.locator(
            '//button[@id="account-balance-dashboard-tab-tab-ontrack-d2p"]'
        )
        self.filter_label = page.locator('(//label[text()="Filter"])[1]')
        self.filter_dropdown = page.locator(
            '(//select[@class="form-select form-select-sm"])[1]'
        )
        self.select_all_filter_option = page.locator(
            '(//div[@class="d-flex align-items-center justify-content-between"]//select)[1]'
        )
        self.egift_label = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-all"]//p[text()="eGifts"]'
        )
        self.egift_headline = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-all"]//p[text()="Send an eGift."]'
        )
        self.gift_card_component = page.locator(
            '(//div[@class="d-flex gap-6 w-100 flex-wrap"])[1]'
        )
        self.ontrack_d2p_label = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-all"]//p[text()="Ontrack D2P"]'
        )
        self.ontrack_d2p_headline = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-all"]//p[text()="Send a gift."]'
        )
        self.egifts_tab_component = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-egifts-deposit"]'
        )
        self.egifts_tab_title = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-egifts-deposit"]//p[text()="eGifts"]'
        )
        self.egifts_tab_headline = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-egifts-deposit"]//p[text()="Send an eGift."]'
        )
        self.ontrack_d2p_tab_component = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-ontrack-d2p"]'
        )
        self.ontrack_d2p_tab_title = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-ontrack-d2p"]//p[text()="Ontrack D2P"]'
        )
        self.ontrack_d2p_tab_headline = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-ontrack-d2p"]//p[text()="Send a gift."]'
        )
        self.select_gift = page.locator(
            '(//div[@class="ant-image sender-gifts-D2p-image"])[1]'
        )
        self.make_a_connection_component = page.locator(
            '(//div[@class="py-3 mb-2 account-balance-card card"])[1]'
        )
        self.make_a_connection_header = page.locator('//h3[text()="Make a connection"]')
        self.sending_method_process = page.locator('//div[text()="Sending Method"]')
        self.recipient_details_process = page.locator(
            '//div[text()="Recipient Details"]'
        )
        self.sending_method_page_slogan = page.locator(
            '//p[text()="How would you like to make your connection?"]'
        )
        self.selected_connect_component = page.locator('//div[@class="card"]')
        self.selected_connect_title = page.locator('//h4[text()="Selected connect"]')
        self.connect_details_title = page.locator('//h5[text()="Connect details"]')
        self.egift_label = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-all"]//p[text()="eGifts"]'
        )
        self.egift_expires_in = page.locator('//p[text()="Expires in"]')
        self.email_button = page.locator(
            '//div[@class="text-center px-3 sending-opt-btn max "][1]'
        )
        self.email_label = page.locator('//p[text()="Email"]')
        self.shareable_link_button = page.locator(
            '//div[@class="text-center px-3 sending-opt-btn max "][2]'
        )
        self.shareable_link_label = page.locator('//p[text()="Shareable Link"]')
        self.sms_button = page.locator(
            '//div[@class="text-center px-3 sending-opt-btn max "][3]'
        )
        self.sms_label = page.locator('//p[text()="SMS"]')
        self.select_your_gift_amount_label = page.locator(
            '//p[text()="Select your eGift amount"]'
        )
        self.amount_component = page.locator('//div[@class="d-flex gap-3"]')
        self.enter_recipients_details_label = page.locator(
            '//p[text()="Enter Recipient Details"]'
        )
        self.recipients_email_address = page.locator(
            '//label[text()="Recipient\'s Email Address"]'
        )
        self.recipient_email_address_input = page.locator(
            '//input[@id="Email_recipientEmail"]'
        )
        self.email_subject_label = page.locator('//label[text()="Email subject"]')
        self.email_subject_input = page.locator('//input[@id="D2pForm_emailSubject"]')
        self.insert_template_dropdown = page.locator(
            '//div[@class="ant-select-selector"]'
        )
        self.select_template = page.locator('//div[text()="egift card template"]')
        self.email_message_label = page.locator('//label[text()="Email Message"]')
        self.email_message_input = page.locator(
            '//div[@class="ck-blurred ck ck-content ck-editor__editable ck-rounded-corners ck-editor__editable_inline"]'
        )
        self.view_email_preview = page.locator(
            '//button//span[text()="View email preview"]'
        )
        self.connect_button = page.locator('//button//span[text()="Connect"]')
        self.cancel_button = page.locator('//button//span[text()="Cancel"]')

        # egifts page locators
        self.egifts_tab_filter_label = page.locator('(//label[text()="Filter"])[2]')
        self.egifts_tab_filter_dropdown = page.locator(
            '(//select[@class="form-select form-select-sm"])[2]'
        )
        self.egifts_tab_filter_dropdown_options = page.locator(
            '(//select[@class="form-select form-select-sm"])[2]//option'
        )
        self.egifts_tab_select_all_filter_option = page.locator(
            '(//div[@class="d-flex align-items-center justify-content-between"]//select)[2]'
        )
        self.egifts_tab_egift_label = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-egifts-deposit"]//p[text()="eGifts"]'
        )
        self.egifts_tab_egift_headline = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-egifts-deposit"]//p[text()="Send an eGift."]'
        )
        self.egifts_tab_egift_card_component = page.locator(
            '(//div[@class="d-flex gap-6 w-100 flex-wrap"])[3]'
        )
        self.select_egift = page.locator(
            '(//div[@id="account-balance-dashboard-tab-tabpane-egifts-deposit"]//div[@class="rounded-4 overflow-hidden"])[1]'
        )
        # email preview locators
        self.email_preview_component = page.locator(
            '(//div[@class="modal-content"])[2]'
        )
        self.email_preview_header = page.locator('//div[text()="Email Preview"]')
        self.email_to_label = page.locator('//div[text()="To"]')
        self.subject_label = page.locator('//div[text()="Subject"]')
        self.from_label = page.locator('//div[text()="From"]')
        self.claim_egift_card_label = page.locator('//p[text()="Claim eGift Card"]')
        self.close_button = page.locator('//button//span[text()="Close"]')

        # ontrack d2p page locators
        self.ontrack_d2p_tab_filter_label = page.locator(
            '(//label[text()="Filter"])[3]'
        )
        self.ontrack_d2p_tab_filter_dropdown = page.locator(
            '(//select[@class="form-select form-select-sm"])[3]'
        )
        self.ontrack_d2p_tab_filter_dropdown_options = page.locator(
            '(//select[@class="form-select form-select-sm"])[2]//option'
        )
        self.ontrack_d2p_tab_select_all_filter_option = page.locator(
            '(//div[@class="d-flex align-items-center justify-content-between"]//select)[3]'
        )
        self.ontrack_d2p_tab_d2p_label = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-ontrack-d2p"]//p[text()="Ontrack D2P"]'
        )
        self.ontrack_d2p_tab_headline = page.locator(
            '//div[@id="account-balance-dashboard-tab-tabpane-ontrack-d2p"]//p[text()="Send a gift."]'
        )
        self.ontrack_d2p_tab_d2p_card_component = page.locator(
            '(//div[@class="d-flex gap-6 w-100 flex-wrap"])[4]'
        )
        self.ontrack_d2p_gift = page.locator(
            '(//div[@id="account-balance-dashboard-tab-tabpane-ontrack-d2p"]//div[@class="rounded-4 overflow-hidden"])[1]'
        )

        # Make connection via shareable-link page locators
        self.link_recipient_email_input = page.locator(
            '//input[@id="Link_recipientEmail"]'
        )
        self.create_a_link_button = page.locator(
            '//button//span[text()="Create a link"]'
        )
        # Make connection via sms page locators
        self.view_message_preview_button = page.locator(
            '//button//ins[text()="View message preview"]'
        )
        self.text_message_label = page.locator('//label[text()="Text Message"]')
        self.text_message_input = page.locator('//textarea[@id="SMS_textMessage"]')
        self.recipient_phone_number_input = page.locator(
            '//input[@id="SMS_recipientPhoneNumber"]'
        )
        self.recipient_phone_number_label = page.locator(
            '//label[@for="SMS_recipientPhoneNumber"]'
        )
        self.text_message_preview_box = page.locator(
            '(//div[@class="modal-content"])[2]'
        )
        self.text_message_preview_title = page.locator(
            '//div[text()="Text Message Preview"]'
        )
        self.recipient_phone_number_label_in_preview = page.locator(
            '//span[text()="Recipient\'s Phone Number"]'
        )
        self.sms_text_label = page.locator('//span[text()="SMS Text"]')
        self.accept_button = page.locator('//button//span[text()="Accept"]')
        self.success_message = page.locator(
            '//div[@class="ant-message-custom-content ant-message-success"]'
        )

        # Make a connection page of D2P gifts locators
        self.make_a_connection_component_of_d2p = page.locator(
            '//div[@class="modal-content"]'
        )
        self.make_a_connection_header_of_d2p = page.locator(
            '//div[text()="Make a connection"]'
        )
        self.enter_the_recipients_address_sentence = page.locator(
            '//p[text()="Enter the recipient\'s address"]'
        )
        self.recipient_known_address_button = page.locator(
            '//button//span[text()="I Know the recipient\'s address"]'
        )
        self.recipient_unknown_address_button = page.locator(
            "//button//span[text()=\"I Don't Know the recipient's address\"]"
        )
        self.address_confirmation_text = page.locator(
            '//p[text()="Ask recipients to confirm their address"]'
        )
        self.address_confirmation_switch = page.locator('//button[@role="switch"]')
        self.dont_send_package_radio_button = page.locator(
            "//span[text()=\"Don't send package if the recipient doesn't confirm\"]//..//input"
        )
        self.send_package_radio_button = page.locator(
            '//span[text()="Send package even if the recipient doesn\'t confirm"]//..//input'
        )
        self.enter_recipients_details_title = page.locator(
            '//p[text()="Enter the recipient\'s details"]'
        )
        self.name_label = page.locator('//label[text()="Name"]')
        self.name_input = page.locator('//input[@id="D2pForm_name"]')
        self.company_label = page.locator('//label[text()="Company"]')
        self.company_input = page.locator('//input[@id="D2pForm_company"]')
        self.street_address_label = page.locator('//label[text()="Street address"]')
        self.street_address_input = page.locator('//input[@id="D2pForm_streetAddress"]')
        self.city_label = page.locator('//label[text()="City"]')
        self.city_input = page.locator('//input[@id="D2pForm_city"]')
        self.zip_label = page.locator('//label[text()="Zip"]')
        self.zip_input = page.locator('//input[@id="D2pForm_zipCode"]')
        self.state_label = page.locator('//label[text()="State"]')
        self.state_dropdown = page.locator(
            '(//div[@class="ant-form-item-control-input-content"]//select)[1]'
        )
        self.country_label = page.locator('//label[text()="Country"]')
        self.country_dropdown = page.locator(
            '(//div[@class="ant-form-item-control-input-content"]//select)[2]'
        )
        self.insert_template_label = page.locator('//label[text()="Insert template"]')
        self.email_label = page.locator('//label[text()="Email subject"]')
        self.email_input = page.locator('//input[@id="D2pForm_emailSubject"]')
        self.recipient_email_address_label = page.locator(
            '//label[text()="Recipient Email Address"]'
        )
        self.recipient_email_address_input = page.locator(
            '//input[@id="D2pForm_recipientEmail"]'
        )
        self.enter_email_message_label = page.locator(
            '//label[text()="Enter email message"]'
        )
        self.enter_email_message_input_area = page.locator('//div[@role="textbox"]')
        self.connect_method_label = page.locator('//span[text()="Connect Method"]')
        self.connect_method_dropdown = page.locator(
            '//div[@class="ant-select-selector"]'
        )
        self.d2p_selected_connect_box = page.locator(
            '//div[@class="my-4  justify-content-end d-flex align-items-center"]//select'
        )
        self.d2p_connect_details_label = page.locator('//h5[text()="Connect details"]')
        self.d2p_shipping_details_label = page.locator(
            '//h5[text()="Shipping details"]'
        )
        self.processing_time_label = page.locator('//p[text()="Processing time"]')
        self.shipping_time_label = page.locator('//p[text()="Shipping time"]')
        self.estimated_total_time_label = page.locator(
            '//p[text()="Estimated total time"]'
        )
        self.d2p_view_email_preview = page.locator(
            '//button//ins[text()="View email preview"]'
        )
        self.claim_d2pgift_card_label = page.locator('//p[text()="Claim Gift"]')

    @qase_screenshot
    @qase.step(
        title="Verify logged in user is able to change role to sender",
        expected="Logged in user should be able to change role",
    )
    def verify_and_change_user_role(self, select_role):
        """
        Verify and change role of user
        """
        expect(self.change_role_dropdown).to_be_visible()
        self.change_role_dropdown.click()
        self.page.wait_for_load_state("domcontentloaded")
        self.page.click(self.role_to_select.replace("<<select_role>>", select_role))
        print(f"successfully changed role to {select_role}")

    @qase_screenshot
    @qase.step(
        title="Verify account balance icon and tab working",
        expected="deployment admin should be able to open and view account balance tab",
    )
    def verify_connects_tab(self):
        """
        Verify message templates and click on message templates tab
        """
        # verify icon availability
        expect(self.connects_icon).to_be_visible()

    @qase_screenshot
    @qase.step(
        title="Verify all gifts page element visibility",
        expected="sender should be able to visible all elements of the all gifts page",
    )
    def verify_all_gifts_page_elements(self, available_filter_options):
        """
        Verify all gifts page elements
        """
        self.page.wait_for_load_state("domcontentloaded")
        elements_to_check = [
            self.make_a_connection_component,
            self.make_a_connection_header,
            self.connects_page_sub_title,
            self.all_tab,
            self.egifts_tab,
            self.ontrack_d2p_tab,
            self.filter_label,
            self.filter_dropdown,
            self.egift_label,
            self.ontrack_d2p_label,
            self.egift_headline,
            self.ontrack_d2p_headline,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        time.sleep(3)
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

    @qase_screenshot
    @qase.step(
        title="Verify egifts page element visibility",
        expected="sender should be able to visible all elements of the egifts page",
    )
    def verify_egifts_page_elements(self, available_filter_options):
        """
        Verify egifts page elements
        """
        self.egifts_tab.click()
        time.sleep(4)
        self.page.wait_for_load_state("domcontentloaded")
        elements_to_check = [
            self.make_a_connection_component,
            self.make_a_connection_header,
            self.connects_page_sub_title,
            self.all_tab,
            self.egifts_tab,
            self.ontrack_d2p_tab,
            self.egifts_tab_egift_label,
            self.egifts_tab_filter_label,
            self.egifts_tab_filter_dropdown,
            self.egifts_tab_egift_headline,
            self.egifts_tab_component,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        time.sleep(2)
        filter_options_raw = self.egifts_tab_filter_dropdown.inner_text()
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
        title="Verify ontrack_d2p page element visibility",
        expected="sender should be able to visible all elements of the ontrack_d2p page",
    )
    def verify_ontrack_d2p_page_elements(self, available_filter_options):
        """
        Verify ontrack_d2p page elements
        """
        self.ontrack_d2p_tab.click()
        time.sleep(4)
        self.page.wait_for_load_state("domcontentloaded")
        elements_to_check = [
            self.make_a_connection_component,
            self.make_a_connection_header,
            self.connects_page_sub_title,
            self.all_tab,
            self.egifts_tab,
            self.ontrack_d2p_tab,
            self.ontrack_d2p_tab_d2p_label,
            self.ontrack_d2p_tab_filter_label,
            self.ontrack_d2p_tab_filter_dropdown,
            self.ontrack_d2p_tab_headline,
            self.ontrack_d2p_tab_component,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        filter_options_raw = self.ontrack_d2p_tab_filter_dropdown.inner_text()
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
        title="Select filter option on all gifts page and share gift via email",
        expected="sender should be able to send gifts via email",
    )
    def verify_and_send_gifts_via_email(
        self, item_category_to_select, recipient_email, email_subject, email_message
    ):
        """
        Verify and send gifts item via email
        """
        time.sleep(2)
        if self.select_all_filter_option.is_visible():
            self.select_all_filter_option.select_option(item_category_to_select)
            time.sleep(5)
            self.page.wait_for_load_state("domcontentloaded")
            expect(self.gift_card_component).to_be_visible()
            expect(self.select_gift).to_be_visible()
            self.select_gift.click()
        else:
            self.egifts_tab_select_all_filter_option.select_option(
                item_category_to_select
            )
            time.sleep(5)
            self.page.wait_for_load_state("domcontentloaded")
            expect(self.egifts_tab_egift_card_component).to_be_visible()
            expect(self.select_egift).to_be_visible()
            self.select_egift.click()
        elements_to_check = [
            self.make_a_connection_component,
            self.make_a_connection_header,
            self.selected_connect_title,
            self.selected_connect_component,
            self.sending_method_page_slogan,
            self.sending_method_process,
            self.recipient_details_process,
            self.egift_expires_in,
            self.email_button,
            self.email_label,
            self.shareable_link_label,
            self.shareable_link_button,
            self.sms_label,
            self.sms_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        self.email_button.click()
        time.sleep(5)
        elements_to_check = [
            self.select_your_gift_amount_label,
            self.enter_recipients_details_label,
            self.recipients_email_address,
            self.recipient_email_address_input,
            self.email_subject_label,
            self.email_subject_input,
            self.insert_template_dropdown,
            self.email_message_label,
            self.email_message_input,
            self.view_email_preview,
            self.connect_button,
            self.cancel_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        self.recipient_email_address_input.fill(recipient_email)
        self.email_subject_input.fill(email_subject)
        self.email_message_input.fill(email_message)
        self.view_email_preview.click()
        elements_to_check = [
            self.email_preview_component,
            self.email_preview_header,
            self.email_to_label,
            self.subject_label,
            self.from_label,
            self.claim_egift_card_label,
            self.close_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        self.close_button.click()
        self.connect_button.click()

    @qase_screenshot
    @qase.step(
        title="Select filter option on all gifts page and share gift via shareable link",
        expected="sender should be able to send gifts via shareable link",
    )
    def verify_and_send_gifts_via_shareable_link(
        self, item_category_to_select, recipient_email
    ):
        """
        Verify and send gifts item via shareable link
        """
        time.sleep(2)
        if self.select_all_filter_option.is_visible():
            self.select_all_filter_option.select_option(item_category_to_select)
            time.sleep(5)
            self.page.wait_for_load_state("domcontentloaded")
            expect(self.gift_card_component).to_be_visible()
            expect(self.select_gift).to_be_visible()
            self.select_gift.click()
        else:
            self.egifts_tab_select_all_filter_option.select_option(
                item_category_to_select
            )
            time.sleep(5)
            self.page.wait_for_load_state("domcontentloaded")
            expect(self.egifts_tab_egift_card_component).to_be_visible()
            expect(self.select_egift).to_be_visible()
            self.select_egift.click()
        elements_to_check = [
            self.make_a_connection_component,
            self.make_a_connection_header,
            self.selected_connect_title,
            self.selected_connect_component,
            self.sending_method_page_slogan,
            self.sending_method_process,
            self.recipient_details_process,
            self.egift_expires_in,
            self.email_button,
            self.email_label,
            self.shareable_link_label,
            self.shareable_link_button,
            self.sms_label,
            self.sms_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        self.shareable_link_button.click()
        time.sleep(5)
        elements_to_check = [
            self.select_your_gift_amount_label,
            self.enter_recipients_details_label,
            self.recipients_email_address,
            self.link_recipient_email_input,
            self.create_a_link_button,
            self.cancel_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        self.link_recipient_email_input.fill(recipient_email)
        self.create_a_link_button.click()

    @qase_screenshot
    @qase.step(
        title="Select filter option on all gifts page and share gift via sms",
        expected="sender should be able to send gifts via sms",
    )
    def verify_and_send_gifts_via_sms(
        self,
        item_category_to_select,
        recipient_phone_number,
        text_message,
        success_message,
    ):
        """
        Verify and send gifts item via sms
        """
        time.sleep(2)
        if self.select_all_filter_option.is_visible():
            self.select_all_filter_option.select_option(item_category_to_select)
            time.sleep(5)
            self.page.wait_for_load_state("domcontentloaded")
            expect(self.gift_card_component).to_be_visible()
            expect(self.select_gift).to_be_visible()
            self.select_gift.click()
        else:
            self.egifts_tab_select_all_filter_option.select_option(
                item_category_to_select
            )
            time.sleep(5)
            self.page.wait_for_load_state("domcontentloaded")
            expect(self.egifts_tab_egift_card_component).to_be_visible()
            expect(self.select_egift).to_be_visible()
            self.select_egift.click()
        elements_to_check = [
            self.make_a_connection_component,
            self.make_a_connection_header,
            self.selected_connect_title,
            self.selected_connect_component,
            self.sending_method_page_slogan,
            self.sending_method_process,
            self.recipient_details_process,
            self.egift_expires_in,
            self.email_button,
            self.email_label,
            self.shareable_link_label,
            self.shareable_link_button,
            self.sms_label,
            self.sms_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        self.sms_button.click()
        time.sleep(5)
        elements_to_check = [
            self.select_your_gift_amount_label,
            self.enter_recipients_details_label,
            self.recipient_phone_number_label,
            self.recipient_phone_number_input,
            self.text_message_label,
            self.text_message_input,
            self.view_message_preview_button,
            self.connect_button,
            self.cancel_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        self.recipient_phone_number_input.fill(recipient_phone_number)
        self.text_message_input.fill(text_message)
        self.view_message_preview_button.click()
        elements_to_check = [
            self.text_message_preview_box,
            self.text_message_preview_title,
            self.recipient_phone_number_label_in_preview,
            self.sms_text_label,
            self.accept_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        self.accept_button.click()
        self.page.wait_for_selector(
            '//div[@class="ant-message-custom-content ant-message-success"]'
        )
        expect(self.success_message).to_be_visible()
        message_text = self.success_message.text_content()
        print(f"success message text : {message_text}")
        assert message_text == success_message

    @qase_screenshot
    @qase.step(
        title="navigate to ontarck d2p tab and make a connection",
        expected="sender should be able to make a connection of ontarck d2p gift",
    )
    def navigate_to_ontrack_d2p_tab_and_send_a_gift_with_address(
        self,
        item_category_to_select,
        state,
        email_message,
        user_address,
        user_name,
        user_city,
        email_subject,
        zip_code,
        country,
        recipient_email,
    ):
        """
        Navigate to ontarck d2p tab and make a connection
        """
        expect(self.ontrack_d2p_tab_filter_label).to_be_visible()
        self.ontrack_d2p_tab_filter_dropdown.select_option(item_category_to_select)
        time.sleep(5)
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.ontrack_d2p_gift).to_be_visible()
        self.ontrack_d2p_gift.click()
        elements_to_check = [
            self.make_a_connection_component_of_d2p,
            self.make_a_connection_header,
            self.enter_the_recipients_address_sentence,
            self.recipient_known_address_button,
            self.recipient_unknown_address_button,
            self.address_confirmation_text,
            self.address_confirmation_switch,
            self.dont_send_package_radio_button,
            self.send_package_radio_button,
            self.enter_recipients_details_title,
            self.name_input,
            self.name_label,
            self.company_label,
            self.name_input,
            self.street_address_label,
            self.street_address_input,
            self.city_label,
            self.city_input,
            self.zip_input,
            self.zip_label,
            self.state_label,
            self.country_label,
            self.insert_template_label,
            self.insert_template_dropdown,
            self.email_subject_label,
            self.email_subject_input,
            self.recipient_email_address_label,
            self.recipient_email_address_input,
            self.enter_email_message_label,
            self.enter_email_message_input_area,
            self.connect_method_label,
            self.selected_connect_title,
            self.selected_connect_component,
            self.d2p_connect_details_label,
            self.d2p_shipping_details_label,
            self.processing_time_label,
            self.shipping_time_label,
            self.estimated_total_time_label,
            self.d2p_view_email_preview,
            self.connect_button,
            self.cancel_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        self.name_input.fill(user_name)
        self.street_address_input.fill(user_address)
        self.city_input.fill(user_city)
        self.zip_input.fill(zip_code)
        self.state_dropdown.select_option(state)
        self.country_dropdown.select_option(country)
        self.email_subject_input.fill(email_subject)
        self.recipient_email_address_input.fill(recipient_email)
        self.enter_email_message_input_area.fill(email_message)
        self.d2p_view_email_preview.click()
        elements_to_check = [
            self.email_to_label,
            self.subject_label,
            self.from_label,
            self.claim_d2pgift_card_label,
            self.email_preview_component,
            self.email_preview_header,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        self.close_button.click()
        self.connect_button.click()

    @qase_screenshot
    @qase.step(
        title="navigate to ontarck d2p tab and make a connection",
        expected="sender should be able to make a connection of ontarck d2p gift",
    )
    def navigate_to_ontrack_d2p_tab_and_send_a_gift_without_address(
        self,
        item_category_to_select,
        email_message,
        user_name,
        email_subject,
        recipient_email,
    ):
        """
        Navigate to ontarck d2p tab and make a connection
        """
        expect(self.ontrack_d2p_tab_filter_label).to_be_visible()
        self.ontrack_d2p_tab_filter_dropdown.select_option(item_category_to_select)
        time.sleep(5)
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.ontrack_d2p_gift).to_be_visible()
        self.ontrack_d2p_gift.click()
        self.recipient_unknown_address_button.click()
        elements_to_check = [
            self.make_a_connection_component_of_d2p,
            self.make_a_connection_header,
            self.enter_the_recipients_address_sentence,
            self.recipient_known_address_button,
            self.recipient_unknown_address_button,
            self.enter_recipients_details_title,
            self.name_input,
            self.name_label,
            self.name_input,
            self.insert_template_label,
            self.insert_template_dropdown,
            self.email_subject_label,
            self.email_subject_input,
            self.recipient_email_address_label,
            self.recipient_email_address_input,
            self.enter_email_message_label,
            self.enter_email_message_input_area,
            self.connect_method_label,
            self.selected_connect_title,
            self.selected_connect_component,
            self.d2p_connect_details_label,
            self.d2p_shipping_details_label,
            self.processing_time_label,
            self.shipping_time_label,
            self.estimated_total_time_label,
            self.d2p_view_email_preview,
            self.connect_button,
            self.cancel_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        self.name_input.fill(user_name)
        self.email_subject_input.fill(email_subject)
        self.recipient_email_address_input.fill(recipient_email)
        self.enter_email_message_input_area.fill(email_message)
        self.d2p_view_email_preview.click()
        elements_to_check = [
            self.email_to_label,
            self.subject_label,
            self.from_label,
            self.claim_d2pgift_card_label,
            self.email_preview_component,
            self.email_preview_header,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        self.close_button.click()
        self.connect_button.click()
