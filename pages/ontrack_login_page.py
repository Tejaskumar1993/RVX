"""
login page modules
"""

from http.client import HTTPException
from playwright.sync_api import Page
from pages.base_page import BasePage
from data.constant_data import TestData
from qase.pytest import qase

from utilities import utils
from utilities.decorators import qase_screenshot


class OntrackLoginPage(BasePage):
    """
    Module containing objects and methods related to login page
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # login page locators
        self.logo_image = page.locator('//img[@class="ots-Logo"]')
        self.welcome_greetings = page.locator('[id="greetingBox"]')
        self.username_input = page.locator('[id="userName"]')
        self.password_input = page.locator('[id="password"]')
        self.login_button = page.locator('[id="loginButton"]')

    def _verify_response_and_reload_page_if_needed(self, response):
        """
        Verifies the response and reloads the page if needed.
        Raises HTTPException if the response status is not 200 after reloading N times.

        :param response:
        :raises HTTPException:
        """
        max_reloads = 5
        for reload_counter in range(max_reloads):
            print(
                f"Reload {reload_counter}: Booking form responded as {response.status}"
            )
            self.page.reload()
            if response.status == 200:
                break
        else:
            raise HTTPException(
                response.status,
                f"Response from booking form after reloading {max_reloads} times",
            )

    def open_booking_form(self, environment_to_run):
        """.open login page
        :param environment_to_run:
        Navigates to the ontrack login page URL.
        """
        env = utils.login_form_run_environment(environment_to_run)
        # base url of the ontrack login page
        base_url = f"https://send-{env}.ontrackworkflow.com"
        response = self.page.goto(base_url)
        print("Booking form response:", response.status)
        if "ontrackworkflow" not in base_url:
            raise ValueError("Base URL does not contain 'ontrackworkflow'")
        print("Navigating to:", base_url)
        self._verify_response_and_reload_page_if_needed(response)
        print("Navigated to ontrack login page")

    @qase_screenshot
    @qase.step(
        title="Navigate to ontrack login page",
        expected="open and verify login page elements",
    )
    def open_and_verify_ontrack_login_page(
        self, environment_to_run, ontrack_username, ontrack_password
    ):
        """
        open and verify ontrack login page elements
        :return:
        """
        self.open_booking_form(environment_to_run)
        self.verify_element(self.logo_image)
        self.verify_element(self.welcome_greetings)
        welcome_message = self.welcome_greetings.text_content()
        print("welcome_message -->", welcome_message)
        # Verify if the welcome message matches the expected message
        if welcome_message != TestData.greeting_message:
            raise AssertionError(
                f"Expected greeting message '{TestData.greeting_message}', but got '{welcome_message}'"
            )
        # Fill in username and password and perform login
        self.username_input.fill(ontrack_username)
        self.password_input.fill(ontrack_password)
        self.login_button.click()
        # Wait until the username input is no longer visible (indicating successful login)
        self.username_input.wait_for(state="hidden")
        # Verify the URL of the dashboard page after login
        dashboard_page_url = self.page.url
        assert (
            "dashboard/admin" in dashboard_page_url
        ), "The dashboard URL is incorrect."
        # Print a welcome message indicating successful login
        print(
            f"Welcome '{ontrack_username}' on OnTrack, and the dashboard page is visible."
        )
