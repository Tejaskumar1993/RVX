"""
Vendor Company Information page modules
"""

import time

from playwright.sync_api import Page, expect
from qase.pytest import qase

from pages.base_page import BasePage
from utilities.decorators import qase_screenshot


class VendorCompanyInformationPage(BasePage):
    """
    Module containing objects and methods related to Vendor Company Information page
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Company information page locators
        #self.change_role_dropdown = page.locator('(//button[@id="dropdown-flags"])[2]')
        self.role_to_select = '//a[text()="<<role_to_change>>"]'
        self.select_tab_from_side_navigation = '//span[text()="<<tab_to_navigate>>"]'
        self.company_information_icon = page.locator(
            '//span[text()="Company Information"]//..//span[@class="nav-link-icon"]'
        )
        self.dashboard_hyperlink = page.locator('//a[text()="Dashboard"]')
        self.company_information_tab = page.locator(
            '//li[text()="Company Information"]'
        )
        self.company_information_header = page.locator(
            '//h5[text()="Company Information"]'
        )
        self.upload_image_button = page.locator(
            '//span[text()="Upload"]//..//..//button'
        )
        self.company_information_card = page.locator(
            '//div[@class="company-setting-page mt-1 card"]'
        )
        self.upload_image_area = page.locator(
            '(//div[contains(@class,"ant-upload-list-item ant-upload-list-item-undefined")])[1]'
        )
        self.companyname_label = page.locator('//label[text()="Company Name"]')
        self.companyname_input = page.locator('//input[@name="companyName"]')
        self.address_line1_label = page.locator('//label[text()="Address Line 1"]')
        self.address_line1_input = page.locator('//input[@name="line1"]')
        self.address_line2_label = page.locator('//label[text()="Address Line 2"]')
        self.address_line2_input = page.locator('//input[@name="line2"]')
        self.city_label = page.locator('//label[text()="City"]')
        self.city_input = page.locator('//input[@name="city"]')
        self.state_label = page.locator('//label[text()="State"]')
        self.state_dropdown = page.locator('//select[@id="stateName"]')
        self.zip_code_label = page.locator('//label[text()="Zip Code"]')
        self.zip_code_input = page.locator('//input[@name="zip"]')
        self.company_phone_number_label = page.locator(
            '//label[text()="Company Phone Number"]'
        )
        self.company_phone_number_input = page.locator(
            '//div[@class="mb-2 col-lg-12"]//input[@type="tel"]'
        )
        self.company_email_label = page.locator('//label[text()="Company Email"]')
        self.company_email_input = page.locator('//input[@name="companyEmail"]')
        self.update_button = page.locator('//button[text()="Update"]')
        self.controls_label = page.locator('//h5[text()="Controls"]')
        self.controls_refill = page.locator('//input[@id="disable-bussiness"]')
        self.primary_contact_component = page.locator('//div[@class="mt-3 card"]')
        self.primary_contact_information_title = page.locator(
            '//h5[text()="Primary Contact Information"]'
        )
        self.contact_name_label = page.locator('//label[text()="Contact Name"]')
        self.contact_number_input = page.locator('//input[@name="contactName"]')
        self.support_phone_number_label = page.locator(
            '//label[text()="Support Phone Number"]'
        )
        self.support_phone_number_input = page.locator(
            '//div[@class="col-lg-12"]//input[@type="tel"]'
        )
        self.support_email_label = page.locator('//label[text()="Support Email"]')
        self.support_email_input = page.locator('//input[@name="supportEmail"]')
        self.apply_button = page.locator('//button[text()="Apply"]')
        self.cancel_button = page.locator('//button[text()="Cancel"]')
        self.success_update_message = page.locator(
            '//div[@class="ant-message-custom-content ant-message-success"]'
        )

    @qase_screenshot
    @qase.step(
        title="click on user role dropdown and select role",
        expected="User should be able to change role successfully",
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
        title="Verify and click on company information tab",
        expected="User should be able to see company information icon and able to click on company information tab",
    )
    def verify_and_click_on_company_information_tab(self, side_navigation_item):
        """
        Verify Users and click on company information
        """
        # verify icon availability
        expect(self.company_information_icon).to_be_visible()
        # clicking on company information
        time.sleep(5)
        self.page.click(
            self.select_tab_from_side_navigation.replace(
                "<<tab_to_navigate>>", side_navigation_item
            )
        )
        print(f"successfully able to click on {side_navigation_item} tab")

    @qase_screenshot
    @qase.step(
        title="Verify items list page elements",
        expected="User should be able to visible every elements of company information page",
    )
    def verify_company_information_page_elements(self):
        """
        Verify and check availability of company information page elements
        """
        time.sleep(5)
        elements_to_check = [
            self.dashboard_hyperlink,
            self.company_information_tab,
            self.company_information_header,
            self.upload_image_area,
            self.upload_image_button,
            self.companyname_label,
            self.companyname_input,
            self.address_line1_label,
            self.address_line1_input,
            self.address_line2_label,
            self.address_line2_input,
            self.city_label,
            self.city_input,
            self.state_label,
            self.state_dropdown,
            self.zip_code_input,
            self.zip_code_label,
            self.company_phone_number_label,
            self.company_phone_number_input,
            self.company_email_input,
            self.company_email_label,
            self.update_button,
            self.company_information_card,
            self.controls_label,
            self.controls_refill,
            self.primary_contact_component,
            self.primary_contact_information_title,
            self.support_email_label,
            self.support_email_input,
            self.apply_button,
            self.cancel_button,
            self.support_phone_number_input,
            self.support_phone_number_label,
            self.contact_name_label,
            self.contact_number_input,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("items list page elements verified")

    @qase_screenshot
    @qase.step(
        title="Verify edit company information functionality",
        expected="User should be able to update company information",
    )
    def verify_edit_functionality(self, updated_email, success_message_text):
        """
        verify edit functionality of company information
        """
        time.sleep(5)
        existing_email = self.company_email_input.input_value()
        print(f"existing_email: {existing_email}")
        self.company_email_input.fill(updated_email)
        self.update_button.click()
        expect(self.success_update_message).to_be_visible()
        message_text = self.success_update_message.text_content()
        print(f"MESSAGE TEXT : {message_text}")
        assert message_text == success_message_text
        updated_email = self.company_email_input.input_value()
        print(f"updated_email: {updated_email}")
        assert existing_email != updated_email
        print("information edited successfully")
