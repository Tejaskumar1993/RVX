import re
import time

from playwright.sync_api import Page, expect
from qase.pytest import qase

from utilities import utils
from utilities.decorators import qase_screenshot


class SystemAdminForgotPasswordPage:
    """
    Page Object Model for the System Admin Forgot Password Page using Playwright sync API.
    """

    def __init__(self, page: Page):
        """
        Initialize with Playwright page object.

        :param page: Playwright sync page instance
        """
        self.page = page
        self.url_forgot_password = page.locator("//a[normalize-space()='Forgot Password']")
        self.forgot_password_head = page.locator("//h1[normalize-space()='Forgot your password?']")
        self.forgot_password_description = page.locator("//h1[contains(text(),'Enter your User ID or email to receive a password ')]")
        self.input_email = page.locator("//input[@id='userNameOrEmail']")
        self.button_next = page.locator("//input[@id='nextButton']")
        self.cancel_button = page.locator("//a[normalize-space()='Cancel']")
        self.reset_question_info = page.locator("//h1[contains(text(),'“We must verify your identity. Answer the followin')]")
        self.question = page.locator("//h1[@class='lesserHeadingTwo']")
        self.answer = page.locator("//input[@id='answer']")
        self.Email_sent = page.locator("//div[contains(text(),'An Email has been sent to your email address.')]")


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
        print("Navigated to RevoSend login page")

    def verify_forgot_password_page_elements(self):
        """
        Click on the Forgot Password link and validate navigation.
        """
        self.url_forgot_password.click()
        expect(self.page).to_have_url(re.compile(".*forgot-user"))
        time.sleep(2)
        elements_to_check = [
            self.forgot_password_head,
            self.forgot_password_description,
            self.input_email,
            self.button_next,
            self.cancel_button,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("account balance page elements verified")


    def verify_forgot_password_email(self,email):
        expect(self.input_email).to_be_visible()
        self.input_email.fill(email)
        time.sleep(4)
        self.button_next.click()

    def verify_forgot_password_questions_form_elements(self):
        time.sleep(2)
        elements_to_check = [
            self.reset_question_info,
            self.question,
            self.answer,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("account balance page elements verified")

    def verify_forgot_password_question_answer(self, answer1):
        expect(self.answer).to_be_visible()
        self.answer.fill(answer1)
        time.sleep(2)
        self.button_next.click()
        expect(self.Email_sent).to_be_visible(timeout=5000)
        actual_text = self.Email_sent.inner_text()
        assert actual_text == "An Email has been sent to your email address.", f"Expected confirmation message not found. Got: {actual_text}"






