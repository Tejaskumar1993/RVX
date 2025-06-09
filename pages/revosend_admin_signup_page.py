import re
import time
from http.client import HTTPException

from playwright.sync_api import Page, expect
from qase.pytest import qase

from utilities import utils
from utilities.decorators import qase_screenshot

class SystemAdminSignupPage:
    """
    Page Object Model for the System Admin Signup Page using Playwright sync API.
    """

    def __init__(self, page: Page):
        """
        Initialize with Playwright page object.

        :param page: Playwright sync page instance
        """
        self.page = page

        # Navigation
        self.url_create_account = page.locator("//a[normalize-space()='Create an Account']")

        # Tabs
        self.contact_tab = page.locator("//body/div[@id='root']/div[@class='wrapper']/div[@id='topBox']/div[@class='accountCreationContainer']/div[1]")
        self.login_tab = page.locator("(//div[@class='accountCreationBox'])[2]")
        self.security_tab = page.locator("(//div[@class='accountCreationBox'])[3]")
        self.complete_tab = page.locator("//div[.='Complete']")

        # Header and Upload
        self.head_title = page.locator("//div[@class='lesserHeadings']")
        self.image_upload = page.locator("div[class='ant-upload-list ant-upload-list-picture-circle'] span[role='button']")
        self.upload_button = page.locator("//button[contains(text(),'Upload')]")
        self.edit_button = page.locator("//button[normalize-space()='Edit']")
        # Contact form fields
        self.first_name = page.locator("//input[@id='userFirstName']")
        self.last_name = page.locator("//input[@id='userLastName']")
        self.business_name = page.locator("//input[@id='businessName']")
        self.employee_id = page.locator("//input[@id='ein']")
        self.business_address_1 = page.locator("//input[@id='businessAddress1']")
        self.business_address_2 = page.locator("//input[@id='businessAddress2']")
        self.city_name = page.locator("//input[@id='businessCity']")
        self.state_dropdown = page.locator("//input[@id='react-select-2-input']")
        self.zip_code = page.locator("//input[@id='businessZip']")
        self.next_button = page.locator("//input[@id='nextButton']")

        #Login_form
        self.login_head_text = page.locator("//h2[normalize-space()='Set up your login details.']")
        self.username_textfield = page.locator("//input[@id='userName']")
        self.email_textfield = page.locator("//input[@id='email']")
        self.phone_textfield = page.locator("//input[@id='phoneNumber']")
        self.password_textfield = page.locator("//input[@id='password']")
        self.confirm_password_textfield = page.locator("//input[@id='confirmPassword']")
        self.password_text_lable = page.locator("//h3[contains(text(),'Passwords must be 8-64 characters long, with at le')]")

        #Security questions
        self.security_head_title = page.locator("//h2[normalize-space()='Set up your security questions.']")
        self.question1_dropdown = page.locator("//div[@id='secId1']//div[@class=' css-19bb58m']")
        self.answer1_textfield = page.locator("//input[@id='secAnswer1']")
        self.question2_dropdown = page.locator("//div[@id='secId2']//div[@class=' css-19bb58m']")
        self.answer2_textfield = page.locator("//input[@id='secAnswer2']")
        self.question3_dropdown =page.locator("//div[@id='secId3']//div[@class=' css-19bb58m']")
        self.answer3_textfield = page.locator("//input[@id='secAnswer3']")


    def _verify_response_and_reload_page_if_needed(self, response):
        """
        Verifies the response and reloads the page if needed.
        Raises HTTPException if the response status is not 200 after reloading N times.

        :param response:
        :raises HTTPException:
        """
        print(f"Type of response: {type(response)}")  # Debug log

        if not hasattr(response, "status"):
            raise TypeError(f"Expected response object with 'status' attribute, got {type(response).__name__}")

        max_reloads = 5
        for reload_counter in range(max_reloads):
            print(f"Reload {reload_counter}: responded as {response.status}")
            self.page.reload()
            if response.status == 200:
                break
        else:
            raise HTTPException(
                response.status,
                f"Response from booking form after reloading {max_reloads} times",
            )

    def open_revosend(self, environment_to_run):
        """
        Open the RevoSend login page.
        :param environment_to_run: e.g., 'test', 'stage', 'prod'
        """
        env = utils.login_form_run_environment(environment_to_run)

        if not env:
            raise ValueError("Environment is empty. Cannot build RevoSend URL.")

        base_url = f"https://app-{env}.revosend.com"

        if "revosend.com" not in base_url:
            raise ValueError("Base URL does not contain 'revosend.com'")

        print("Navigating to:", base_url)
        response = self.page.goto(base_url)

        if response is None:
            raise RuntimeError("Failed to navigate: No response received.")

        print("RevoSend response:", response.status)
        self._verify_response_and_reload_page_if_needed(response)
        print("Navigated to RevoSend login page")

    @qase_screenshot
    @qase.step(
        title="Verify signup page elements",
        expected="User should be able to visible every elements of sing up create Account page",
    )
    def verify_sign_up_contact_page_elements(self):
        #self.open_revosend(environment_to_run)
        """
        Verify and check availability of account balance page elements
        """
        self.url_create_account.click()
        time.sleep(2)
        elements_to_check = [
         self.contact_tab,
         self.login_tab,
         self.security_tab,
         self.complete_tab,
         self.head_title,
         self.first_name,
         self.last_name,
         self.business_name,
         self.employee_id,
         self.business_address_1,
         self.business_address_2,
         self.city_name,
         self.state_dropdown,
         self.zip_code,
         self.next_button
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("account balance page elements verified")

    def fill_signup_form(self, firstname: str,
    lastname: str,
    business_name: str,
    business_address1: str,
    business_address2: str,
    city: str,
    zipcode: str,
    state: str,
    image_path: str):
            self.first_name.fill(firstname)
            self.last_name.fill(lastname)
            self.business_name.fill(business_name)
            self.employee_id.fill("123456789")
            self.business_address_1.fill(business_address1)
            self.business_address_2.fill(business_address2)
            self.city_name.fill(city)
            self.zip_code.fill(zipcode)
            self.state_dropdown.click()
            time.sleep(2)
            # Select state from dropdown robustly
            self.state_dropdown.fill(state)  # Fill the text
            self.state_dropdown.press("Enter")  # Press Enter to sele
            time.sleep(4)
            print("Signup form filled.")
            print(self.page.locator("input[type='file']").count())
            self.page.get_by_role("button", name="avatar").locator("input[type='file']").set_input_files(
            image_path)
            time.sleep(4)
            self.edit_button.is_visible()
            self.upload_button.click()
            time.sleep(2)
            self.next_button.click()
            time.sleep(2)

    @qase_screenshot
    @qase.step(
        title="Verify signup page elements",
        expected="User should be able to visible every elements of sing up create Account page",
    )
    def verify_sign_up_login_page_elements(self):
        """
        Verify and check availability of account balance page elements
        """
        time.sleep(2)
        elements_to_check = [
         self.login_head_text,
         self.username_textfield,
         self.email_textfield,
         self.phone_textfield,
         self.password_textfield,
         self.confirm_password_textfield,
         self.password_text_lable,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("account balance page elements verified")

    def fill_signup_login_form(self,username,email,phone_number,password):
        self.username_textfield.fill(username)
        self.email_textfield.fill(email)
        self.phone_textfield.fill(phone_number)
        self.password_textfield.fill(password)
        self.confirm_password_textfield.fill(password)
        time.sleep(2)
        self.next_button.click()
        time.sleep(2)

    def verify_sign_up_security_question_page_elements(self):
        time.sleep(2)
        elements_to_check = [
            self.security_head_title,
            self.question1_dropdown,
            self.answer1_textfield,
            self.question2_dropdown,
            self.answer2_textfield,
            self.question3_dropdown,
            self.answer3_textfield,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("account balance page elements verified")

    def fill_signup_security_form(self,answer1,answer2,answer3):
         self.question1_dropdown.click()
         time.sleep(3)
         self.question1_dropdown.press("Enter")
         time.sleep(3)
         self.answer1_textfield.fill(answer1)
         self.question2_dropdown.click()
         time.sleep(3)
         self.question2_dropdown.press("Enter")
         time.sleep(3)
         self.answer2_textfield.fill(answer2)
         self.question3_dropdown.click()
         time.sleep(3)
         self.question3_dropdown.press("Enter")
         self.answer3_textfield.fill(answer3)
         time.sleep(1)



