import os
from playwright.sync_api import Page, expect
from data.constant_data import TestData


class BasePage:
    """
    Base page class that holds common methods and attributes to be inherited by other page classes
    """

    def __init__(self, page: Page):
        self.page = page

    def set_custom_viewport_size(self):
        """
        Set the viewport size to a custom size
        """
        width = os.environ.get("VIEWPORT_WIDTH", TestData.DEFAULT_WIDTH)
        height = os.environ.get("VIEWPORT_HEIGHT", TestData.DEFAULT_HEIGHT)
        size = {"width": int(width), "height": int(height)}
        self.page.set_viewport_size(size)

    def click_if_visible(self, panel, button=None):
        """
        Clicks the button if the panel is visible
        :param panel: locator of the panel
        :param button: locator of the button
        """
        if button is None:
            button = panel
        if panel.is_visible():
            button.click()

    def verify_element(self, element):
        """
        Verifies the element is visible and enabled
        :param element: locator of the element
        """
        expect(element).to_be_visible()
        expect(element).to_be_enabled()

    def check_element_visibility_and_text(self, element, expected_text=None):
        """
        Check the visibility and text of an element.

        :param element:
        :param expected_text:
        """
        try:
            expect(element).to_be_visible()
            if expected_text is not None:
                expect(element).to_have_text(expected_text)
        except Exception as error:
            raise TimeoutError(
                f"Element '{element}' is not visible or text is not as expected: {error}"
            ) from error
