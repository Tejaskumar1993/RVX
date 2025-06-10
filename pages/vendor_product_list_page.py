"""
Vendor product list page modules
"""

import time

from playwright.sync_api import Page, expect
from qase.pytest import qase

from pages.base_page import BasePage
from utilities.decorators import qase_screenshot


class VendorProductListPage(BasePage):
    """
    Module containing objects and methods related to Vendor product list page
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.change_role_dropdown = page.locator('(//button[@id="dropdown-flags"])[2]')
        #self.role_to_select = '//a[text()="<<role_to_change>>"]'
        self.select_tab_from_side_navigation = '//span[contains(text(),"Product List")]'

        #Header locators
        self.header_titles = page.locator("//thead[contains(@class,'bg-200 text-900 text-nowrap align-middle thead')]")
        self.filter_title = page.locator("//div[@class='filter-text-icon']")
        self.filter_dropdown =page.locator("//select[contains(@class,'generic-filter-select ms-2 form-select form-select-sm')]")
        self.batch_action_title = page.locator("//label[contains(.,'Batch Action:')]")
        self.batch_action_dropdown = page.locator("//select[contains(@class,'form-control form-select form-select-sm')]")
        self.delete_confirm = page.locator("//button[contains(text(),'Confirm')]")
        self.apply_bach_action_button = page.locator("//button[contains(text(),'Apply Action')]")
        self.Add_product_button = page.locator("//button[normalize-space()='Add Product']")
        self.Request_support_button = page.locator("//button[contains(text(),'Request Support')]")
        self.footer_components = page.locator("//div[@class='d-flex align-items-center flex-wrap pagination-content']")
        self.Lock_icon_button = page.locator("(//button[@class='btn rounded-3 me-2 fs--2 action-item-sm btn-outline icon-item icon-item-md'])[1]")
        self.Edit_icon_button = page.locator("(//button[contains(@class,'btn rounded-3 me-2 fs--2 action-item-sm btn-outline icon-item icon-item-md')])[2]")
        self.Rows_per_page_dropdown = page.locator("//select[contains(@class,'w-auto form-select form-select-sm')]")
        self.showing_result_text = page.locator("//span[@class='d-none d-sm-inline-block me-2']")

        #Request support
        self.request_support_button = page.locator("//button[normalize-space()='Request Support']")
        self.request_support_title = page.locator("//div[contains(text(),'Request Support')]")
        self.subject_label = page.locator("//label[normalize-space()='Subject']")
        self.input_subject = page.locator("//textarea[@id='Summary']")
        self.additional_description = page.locator("//label[normalize-space()='Additional Description']")
        self.input_additional_description = page.locator("//textarea[@id='AdditionalDescription']")
        self.request_support_submit_button = page.locator("//button[normalize-space()='Submit']")
        self.success_message = page.locator("//span[contains(text(), 'Your request for support from the system administrators has been sent successfully')]")
        self.delete_success_message = page.locator("//span[text()='Product Deleted Successfully']")

        #Add Product model
        self.new_product_request_title =page.locator("//div[contains(text(),'New Product Request')]")
        self.image_gallery_title = page.locator("//div[contains(text(),'New Product Request')]")
        self.image_upload_button = page.locator("//div[@class='ant-upload-list ant-upload-list-picture-card']")
        self.image_edit_ok_button = page.locator("//button[@class='ant-btn css-1vtf12y ant-btn-primary']")
        self.Edit_Details_title= page.locator("//span[contains(text(),'Edit Details')]")
        self.basic_product_information_title = page.locator("//div[starts-with(text(),'Basic Product Information')]")
        self.input_product_name = page.locator("//input[@id='productName']")
        self.category_dropdown = page.locator("//div[@class='ant-select ant-select-in-form-item ant-select-multiple ant-select-allow-clear ant-select-show-arrow ant-select-show-search']//div[@class='ant-select-selector']")
        self.update_category_dropdown = page.locator("//div[contains(@class,'ant-select ant-select-in-form-item ant-select-status-success ant-select-multiple ant-select-allow-clear ant-select-show-arrow ant-select-show-search')]//div[contains(@class,'ant-select-selector')]")
        self.input_description = page.locator("//div[@aria-label='Editor editing area: main. Press Alt+0 for help.']")
        self.type_dropdown = page.locator("//div[@class='ant-select ant-select-in-form-item ant-select-single ant-select-allow-clear ant-select-show-arrow']//div[@class='ant-select-selector']")
        self.price_and_shipping_information = page.locator("//div[contains(text(),'Price and Shipping Information')]")
        self.input_processing_time = page.locator("//input[@id='processingTime']")
        self.input_price = page.locator("//input[@id='productPrice']")
        self.input_shipping_time = page.locator("//input[@id='shippingTime']")
        self.input_shipping_cost = page.locator("//input[@id='shippingRate']")
        self.total_price_label = page.locator("//div[@class='mb-2 fw-bold']")
        self.submit_product_request = page.locator("//button[@type='submit']")
        self.submit_product_update = page.locator("//button[contains(@type,'submit')]")
        self.submit_change_order = page.locator("//button[contains(@type,'submit')]")
        self.Edit_Action = page.locator(
            "(//button[contains(@class,'btn rounded-3 me-2 fs--2 action-item-sm btn-outline icon-item icon-item-md')])[2]")
        self.Edit_disable_title = page.locator("//span[text()='Disable Sending while request is pending']")
        self.Edit_disable_toggle = page.locator("//button[@role='switch']")
        self.product_select = page.locator("(//input[contains(@title,'Toggle Row Selected')])[1]")


        # Notification page locators
        self.change_role_dropdown = page.locator('(//button[@id="dropdown-flags"])[2]')
        self.role_to_select = '//a[text()="<<role_to_change>>"]'
        self.profile_image = page.locator("//a[@href='/dashboard/admin#!']")
        self.notification_setting_dropdown = '//a[text()="<<Notification Settings>>"]'
        self.notification_header = page.locator('//h3[text()="Notification Settings"]')
        self.alert = page.locator('//th[text()="Alert"]')
        self.alert_type = page.locator('//th[text()="Alert Type"]')
        self.email = page.locator('//th[text()="Email"]')
        self.sms = page.locator('//th[text()="SMS"]')
        self.select_all = page.locator('//td[text()="Select All"]')
        self.unacknowledged_orders = page.locator(
            '//td[text()="Unacknowledged orders"]'
        )
        self.orders_created = page.locator('//td[text()="Orders created"]')
        self.orders_not_sent = page.locator('//td[text()="Orders not sent"]')
        self.sms_text = page.locator(
            '//p[text()="SMS alerts are sent to the phone number on file. Standard message & data rates may apply."]'
        )
        self.update_button = page.locator('//button[text()="Update"]')
        self.email_checkbox = page.locator(
            '(//tr[td[text()="Select All"]]//input[@type="checkbox"])[1]'
        )
        self.sms_checkbox = page.locator(
            '(//tr[td[text()="Select All"]]//input[@type="checkbox"])[2]'
        )
        self.alert_message = page.locator(
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
        title="click on user profile dropdown and select notification setting option",
        expected="User should be able to select notification setting successfully",
    )
    def navigate_to_product_list(
        self,tab_to_navigate
    ):
        """
        navigate to ProductList
        """
        time.sleep(10)
        self.page.click(
            self.select_tab_from_side_navigation.replace(
                "<<tab_to_navigate>>", tab_to_navigate

            )
        )
        time.sleep(5)

    @qase_screenshot
    @qase.step(
        title="Verify notification setting page elements",
        expected="User should be able to visible every elements of notification setting page",
    )
    def verify_vendor_product_list_page_elements(self, tab_to_navigate, headers_text):
        """
        Navigates to the specified tab, verifies page elements, and validates table headers.
        """
        # Navigate to the desired tab
        self.navigate_to_product_list(tab_to_navigate)

        # Wait for the page to load (consider replacing with explicit waits)
        time.sleep(5)

        # List of UI elements to verify
        elements_to_check = [
            self.header_titles,
            self.filter_title,
            self.filter_dropdown,
            self.Add_product_button,
            self.Request_support_button,
            self.footer_components,
            self.Lock_icon_button,
            self.Edit_icon_button,
            self.Rows_per_page_dropdown,
            self.showing_result_text,
        ]
        # Check visibility of all elements
        for element in elements_to_check:
            expect(element).to_be_visible()
        print(f"Elements on '{tab_to_navigate}' tab are visible.")

        # ✅ Get header texts correctly (flat list)
        actual_headers = [
            self.header_titles.nth(i).inner_text().strip().split("\t")
            for i in range(self.header_titles.count())
        ]
        # Compare with expected headers
        assert actual_headers == headers_text, (
            f"Expected: {headers_text}\n"
            f"Found: {actual_headers}"
        )
        print("Header texts match expected values.")

    @qase_screenshot
    @qase.step(
            title="Apply filter on product list and verify filtered data",
            expected="Data should be filtered properly based on the applied filter."
    )
    def apply_filter_and_verify_statuses(self, available_filter_options, expected_statuses):
        """
        Apply each filter on the product list and verify product statuses.
        """
        assert self.filter_dropdown.is_visible(), "Filter dropdown is not visible"

        # Check dropdown options
        filter_options = self.filter_dropdown.locator("option").all()
        filter_options_text = [opt.inner_text().strip() for opt in filter_options]
        assert filter_options_text == available_filter_options, \
            f"Expected: {available_filter_options}, but got: {filter_options_text}"

        print(f"Verified filters: {available_filter_options}")

        for filter_option in available_filter_options:

            self.filter_dropdown.select_option(filter_option)
            self.page.wait_for_selector("//div[contains(@class, 'badge')]")

            # Collect statuses
            status_elements = self.page.locator("//div[contains(@class, 'badge')]").all()
            status_texts = [elem.inner_text().strip() for elem in status_elements]
            print(f"Statuses after '{filter_option}' filter: {status_texts}")
            expected = expected_statuses.get(filter_option, [])
            if expected:
                missing = [s for s in expected if s not in status_texts]
                assert not missing, (
                    f"Missing statuses {missing} for filter '{filter_option}'. "
                    f"Actual: {status_texts}"
                )
            else:
                assert not status_texts, f"Expected no statuses for '{filter_option}', but got: {status_texts}"

    @qase_screenshot
    @qase.step(
        title="Verify 'New Product Request' page elements",
        expected="All elements on the 'New Product Request' page should be visible",
    )
    def verify_new_product_request_page_elements(self):
        """
        Verifies the presence and visibility of all critical elements
        on the 'New Product Request' page.
        """
        time.sleep(5)
        self.Add_product_button.click()
        elements_to_check = [
            self.new_product_request_title,
            self.image_gallery_title,
            self.image_upload_button,
            self.Edit_Details_title,
            self.basic_product_information_title,
            self.input_product_name,
            self.category_dropdown,
            self.input_description,
            self.type_dropdown,
            self.price_and_shipping_information,
            self.input_processing_time,
            self.input_price,
            self.input_shipping_time,
            self.input_shipping_cost,
            self.total_price_label,
            self.submit_product_request,
        ]
        for element in elements_to_check:
            expect(element).to_be_visible()
        print("All 'New Product Request' page elements are visible.")

    @qase.title("Add Product Request and Verify Element Visibility & Values")
    @qase.fields(
        ("severity", "major"),
        ("priority", "high"),
        ("description",
         "Verify that the elements are visible and contain correct values in the Add Product Request process.")
    )

    def verify_and_fill_add_product_request_form(self, product_name, product_price, product_shipping_rate,
                                                 product_description, category, product_type, image_path, success_message_text):
        """
        Verifies the visibility of elements on the 'Add Product Request' page,
        fills in the details, and submits the request.
        """
        # 1. Verify all elements on the page
       # self.verify_new_product_request_page_elements()
        time.sleep(2)
        self.Add_product_button.is_visible()
        self.Add_product_button.click()

        # 2. Fill in product details
        time.sleep(1)
        self.input_product_name.is_visible()
        self.input_product_name.fill(product_name)
        self.input_price.fill(str(product_price))
        self.input_shipping_cost.fill(str(product_shipping_rate))
        self.input_description.fill(product_description)
        time.sleep(1)
        # 3. Select category and type
        self.category_dropdown.wait_for(state="visible")
        self.category_dropdown.click()
        time.sleep(1)
        option = self.page.locator(".ant-select-item-option").filter(has_text=category)
        option.wait_for(state="visible")
        option.click()
        time.sleep(1)
        self.type_dropdown.wait_for(state="visible")
        self.type_dropdown.click()
        time.sleep(1)
        option = self.page.locator(".ant-select-item-option").filter(has_text=product_type)
        option.wait_for(state="visible")
        option.click()
        time.sleep(1)
        # 4. Upload the product image
        self.page.locator("input[type='file']").nth(0).set_input_files(image_path)
        time.sleep(1)
        #self.image_edit_ok_button.click()
        time.sleep(1)
        self.input_processing_time.fill("5")
        self.input_shipping_time.fill("5")
        time.sleep(1)
        # 5. Submit the product request
        self.submit_product_request.click()
        time.sleep(3)
        # 6. Verify the success message
        expect(self.page.locator(f"//span[contains(text(), '{success_message_text}')]")).to_be_visible()
        print(f"Product request for '{product_name}' submitted successfully.")


    @qase.title("Update Product Request and Verify Element Visibility & Values")
    @qase.fields(
        ("severity", "major"),
        ("priority", "high"),
        ("description",
         "Verify that the elements are visible and contain correct values in the Update Product Request process.")
    )
    def verify_and_fill_update_product_form(self, product_name, product_price, product_shipping_rate,
                                            product_description, category, product_type, image_path,
                                            success_message_text):
        """
        Verifies the visibility of elements on the 'Update Product' page,
        fills in the updated details, and submits the request.
        """
        # 1. Locate the product to update and click Edit
        time.sleep(5)
        self.Edit_Action.click()
        # 2. Verify fields are visible and update values
        time.sleep(2)
        self.input_product_name.is_visible()
        self.input_product_name.fill(product_name)
        self.input_price.fill(str(product_price))
        self.input_shipping_cost.fill(str(product_shipping_rate))
        self.input_description.fill(product_description)
        time.sleep(2)
        # 3. Update category and type
        self.update_category_dropdown.wait_for(state="visible")
        self.update_category_dropdown.click()
        time.sleep(1)
        option = self.page.locator(".ant-select-item-option").filter(has_text=category)
        option.wait_for(state="visible")
        option.click()
        # 4. Update the product image if necessary
        self.page.locator("input[type='file']").nth(0).set_input_files(image_path)
        time.sleep(1)
        self.image_edit_ok_button.click()
        # 5. Update processing and shipping time
        self.input_processing_time.fill("5")
        self.input_shipping_time.fill("5")
        # 6. Submit the update
        self.submit_product_update.click()  # Replace with correct update submit button locator
        time.sleep(2)

        # 7. Verify the success message
        expect(self.page.locator(f"//div[contains(text(), '{success_message_text}')]")).to_be_visible()
        print(f"Product '{product_name}' updated successfully.")

    @qase_screenshot
    @qase.step(
        title="Verify 'New Product Request' page elements",
        expected="All elements on the 'New Product Request' page should be visible",
    )
    def verify_request_support_flow_and_elements(self, request_subject, request_description, success_message_text):
        # Verify presence of key elements
        time.sleep(2)
        self.request_support_button.click()
        time.sleep(4)
        assert self.request_support_title.is_visible(), "'Request Support' title not visible"
        assert self.subject_label.is_visible(), "'Subject' label not visible"
        assert self.input_subject.is_visible(), "'Subject' input not visible"
        assert self.additional_description.is_visible(), "'Additional Description' label not visible"
        assert self.input_additional_description.is_visible(), "'Additional Description' input not visible"
        assert self.request_support_submit_button.is_visible(), "'Submit' button not visible"

        # Fill out the form
        self.input_subject.fill(request_subject)
        self.input_additional_description.fill(request_description)

        # Submit the form
        self.request_support_submit_button.click()

        # Verify success message (assuming you have another locator like self.success_message)
        actual_message = self.success_message.text_content()
        assert actual_message.strip() == success_message_text.strip(), f"Expected '{success_message_text}', but got '{actual_message}'"

    def verify_approved_product(self, available_filter_options, expected_statuses):
        for option in available_filter_options:
            # Locate the select element and ensure it is visible
            select_locator = self.page.locator(
                "select.generic-filter-select.ms-2.form-select.form-select-sm"
            )
            select_locator.wait_for(state="visible", timeout=10000)
            print(f"Select element is visible.")
            option_locator = select_locator.locator(f"text='{option}'")
            option_count = option_locator.count()
            if option_count == 0:
                raise AssertionError(f"Option '{option}' not found in select element.")
            print(f"Filter option '{option}' exists in select.")
            select_locator.select_option(label=option)
            print(f"Selected filter option '{option}'.")
            self.page.wait_for_timeout(2000)
            if option in expected_statuses:
                for status in expected_statuses[option]:
                    status_locator = self.page.locator(f":text('{status}'):visible")
                    status_count = status_locator.count()
                    if status_count == 0:
                        print(f"Warning: No element found with text '{status}' for filter '{option}'.")
                    print(f"Status '{status}' is visible for filter '{option}'.")

    def verify_batch_action_delete_product_item(self, available_filter_options, expected_statuses,success_message_text):
        for option in available_filter_options:
            # Locate the select element and ensure it is visible
            select_locator = self.page.locator(
                "select.generic-filter-select.ms-2.form-select.form-select-sm"
            )
            select_locator.wait_for(state="visible", timeout=10000)
            print(f"Select element is visible.")

            option_locator = select_locator.locator(f"text='{option}'")
            option_count = option_locator.count()
            if option_count == 0:
                raise AssertionError(f"Option '{option}' not found in select element.")
            print(f"Filter option '{option}' exists in select.")

            select_locator.select_option(label=option)
            print(f"Selected filter option '{option}'.")
            self.page.wait_for_timeout(2000)

            # Handle the specific "Pending Products" option
            if option == "Pending Products":
                # Logic specific to "Pending Products"
                print("Verifying statuses for Pending Products.")
                if option in expected_statuses:
                    for status in expected_statuses[option]:
                        status_locator = self.page.locator(f":text('{status}'):visible")
                        status_count = status_locator.count()
                        if status_count == 0:
                            print(f"Warning: No element found with text '{status}' for filter '{option}'.")
                        print(f"Status '{status}' is visible for filter '{option}'.")
                        time.sleep(4)
                        self.product_select.click()
                        time.sleep(2)
                        self.batch_action_dropdown.select_option("Delete Item")
                        time.sleep(2)
                        self.apply_bach_action_button.click()
                        time.sleep(1)
                        self.delete_confirm.click()
                        time.sleep(1)
            assert (
                 self.delete_success_message.inner_text() == success_message_text
            ), f"Expected success message: '{success_message_text}', but found: '{self.delete_success_message.inner_text()}'"
            time.sleep(5)
            self.product_select.click()
            time.sleep(2)
            self.batch_action_dropdown.select_option("Delete Item")
            time.sleep(2)
            self.apply_bach_action_button.click()
            time.sleep(1)
            self.delete_confirm.click()
            time.sleep(1)
        assert (
                self.delete_success_message.inner_text() == success_message_text
        ), f"Expected success message: '{success_message_text}', but found: '{self.delete_success_message.inner_text()}'"

    @qase_screenshot
    @qase.step(
        title="Verify 'Edit Submit change Order' functionality",
        expected="All elements on the ' Approved Edit product request' page should be visible",
    )
    def verify_submit_change_order_flow_and_elements(self,product_name,product_price, product_shipping_rate,
                                            product_description, category,image_path,
                                            success_message_text):
        """
               Verifies the visibility of elements on the 'Update Product' page,
               fills in the updated details, and submits the request.
               """
        # 1. Locate the product to update and click Edit
        time.sleep(5)
        self.Edit_Action.click()
        # 2. Verify fields are visible and update values
        time.sleep(2)
        self.input_product_name.is_visible()
        self.input_product_name.fill(product_name)
        self.input_price.fill(str(product_price))
        self.input_shipping_cost.fill(str(product_shipping_rate))
        self.input_description.fill(product_description)
        time.sleep(2)
        # 3. Update category and type
        self.update_category_dropdown.wait_for(state="visible")
        self.update_category_dropdown.click()
        time.sleep(1)
        option = self.page.locator(".ant-select-item-option").filter(has_text=category)
        option.wait_for(state="visible")
        option.click()
        # 4. Update the product image if necessary
        self.page.locator("input[type='file']").nth(0).set_input_files(image_path)
        time.sleep(1)
        self.image_edit_ok_button.click()
        # 5. Update processing and shipping time
        self.input_processing_time.fill("5")
        self.input_shipping_time.fill("5")
        # 6. Submit the update
        self.submit_change_order.click()  # Replace with correct update submit button locator
        time.sleep(2)

        # 7. Verify the success message
        expect(self.page.locator(f"//div[contains(text(), '{success_message_text}')]")).to_be_visible()
        print(f"Product '{product_name}' updated successfully.")

    @qase_screenshot
    @qase.step(
        title="Verify Batch action functionality on user list page",
        expected="User should be able to apply batch actions on selected users",
    )
    def apply_batch_actions_to_users_list(self):
        """
        Apply batch action to user list
        """
        expect(self.batch_action_title).to_be_visible()
        pending_status_element = self.page.locator(
            "(//div[contains(text(),'Pending')])[1]"
        )


    @qase_screenshot
    @qase.step(
        title="Apply disabled in Edit product ",
        expected="toggle button should disable Approved product."
    )
    def verify_vendor_edit_product_disable_functionality(self):
        time.sleep(5)
        self.Edit_Action.click()
        self.Edit_disable_title.is_visible()
        print(self.Edit_disable_title.inner_text())
        time.sleep(5)
        self.Edit_disable_toggle.click()
        time.sleep(2)
        self.input_shipping_time.fill("5")
        self.submit_change_order.click()
        time.sleep(2)

    @qase_screenshot
    @qase.step(
        title="Verify alert message and set vendor notification",
        expected="User should be able see alert message after updating notifications for the vendor",
    )
    def verify_vendor_product_list_page_page_alert_message(self, success_message_text):
        """
        Verify and toggle notification setting page checkboxes multiple times and check functionality.
        """
        time.sleep(2)
        # Toggle the email checkbox
        if self.email_checkbox.is_checked():
            self.email_checkbox.uncheck()
        else:
            self.email_checkbox.check()
        self.email_checkbox.uncheck()
        self.email_checkbox.check()
        self.email_checkbox.uncheck()

        # Toggle the SMS checkbox
        if self.sms_checkbox.is_checked():
            self.sms_checkbox.uncheck()
        else:
            self.sms_checkbox.check()
        self.sms_checkbox.uncheck()
        self.sms_checkbox.check()
        self.sms_checkbox.uncheck()

        # Click the update button and verify the alert message
        self.update_button.click()
        success_message = self.alert_message.text_content()
        assert success_message == success_message_text
        print("Notification updated successfully")
