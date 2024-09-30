from http.client import HTTPException
from playwright.sync_api import Page
from pages.base_page import BasePage
from data.constant_data import TestData

class OntrackLoginPage(BasePage):
    """
    Module containing objects and methods related to booking form's home page
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # login page locators
        self.logo_image = page.locator('//img[@class="ots-Logo"]')
        self.welcome_greetings = page.locator('[id="greetingBox"]')

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

    def open_booking_form(
            self
    ):
        """.open login page
            Navigates to the ontrack login page URL.
        """
        # base url of the ontrack login page
        base_url = f"https://send.ontrackworkflow.com/"
        response = self.page.goto(base_url)
        print("Booking form response:", response.status)
        assert 'ontrackworkflow' in base_url
        print("Navigating to:", base_url)
        self._verify_response_and_reload_page_if_needed(response)
        print("Navigated to ontrack login page")

    def open_and_verify_ontrack_login_page(self):
        """
        open and verify ontrack login page elements
        :return:
        """
        self.open_booking_form()
        self.verify_element(self.logo_image)
        self.verify_element(self.welcome_greetings)
        welcome_message = self.welcome_greetings.text_content()
        print("welcome_message-->", welcome_message)
        assert welcome_message == TestData.greeting_message


