"""
deployment admin Dashboard page modules
"""

import re
import time

from playwright.sync_api import Page, expect
from qase.pytest import qase
from utilities.decorators import qase_screenshot


class DeploymentAdminDashboardPage:
    """
    Module containing objects and methods related to Deployment Admin Dashboard Page
    """

    def __init__(self, page: Page):
        super().__init__()
        self.page = page

        self.change_role_dropdown = page.locator('(//button[@id="dropdown-flags"])[2]')
        self.role_to_select = '//a[text()="<<role_to_change>>"]'
        self.dashboard_icon = page.locator('//*[@data-icon="chart-pie"]')

        # daily sends locators
        self.daily_sends_summary_component = page.locator(
            '//div[@id="charts-dashboard-tab-tabpane-bar_chart"]'
        )
        self.daily_sends_orders_tab = page.locator(
            '//button[@id="charts-dashboard-tab-tab-bar_chart"]'
        )
        self.top_sent_items_tab = page.locator(
            '//button[@id="charts-dashboard-tab-tab-pie_chart"]'
        )
        self.top_sent_component = page.locator(
            '//div[@id="charts-dashboard-tab-tabpane-pie_chart"]'
        )

        # summary locators
        self.summary_component = page.locator('//div[@class="p-3 mb-2 card"]')
        self.top_10_users_tab = page.locator(
            '//button[@id="table-dashboard-tab-tab-top_users"]'
        )
        self.top_10_items_tab = page.locator(
            '//button[@id="table-dashboard-tab-tab-top_items"]'
        )
        self.newest_sends_tab = page.locator(
            '//button[@id="table-dashboard-tab-tab-new_sends_status"]'
        )
        self.user_tabel_headers = page.locator(
            "//div[@id='table-dashboard-tab-tabpane-top_users']//table//thead/tr"
        )
        self.items_table_headers = page.locator(
            "//div[@id='table-dashboard-tab-tabpane-top_items']//table//thead/tr"
        )
        self.newest_sends_headers = page.locator(
            "//div[@id='table-dashboard-tab-tabpane-new_sends_status']//table//thead/tr"
        )

        # send statistics locators
        self.send_statistics_component = page.locator(
            '(//div[@class="py-3 mb-2 card"])[2]'
        )
        self.send_statistics_title = page.locator('//h6[text()="Send Statistics"]')
        self.created_sends_title = page.locator('//h6[text()="Created"]')
        self.acknowledge_sends_title = page.locator('//h6[text()="Acknowledged"]')
        self.shipped_sends_title = page.locator('//h6[text()="Shipped"]')

        # user statistics locators
        self.user_statistics_component = page.locator(
            '(//div[@class="py-3 mb-2 card"])[1]'
        )
        self.user_statistics_title = page.locator('//h6[text()="User Stats"]')
        self.active_users_title = page.locator('//h6[text()="Active Users"]')
        self.suspended_users_title = page.locator('//h6[text()="Acknowledged"]')
        self.archived_users_title = page.locator('//h6[text()="Archived Users"]')

    @qase_screenshot
    @qase.step(
        title="click on user role dropdown and select role",
        expected="User should be able to change role successfully",
    )
    def click_on_dropdown_and_change_user_role(self, role_to_change):
        """
        Change user role from dropdown
        """
        self.change_role_dropdown.click()
        self.page.locator(
            self.role_to_select.replace("<<role_to_change>>", role_to_change)
        ).click()
        print(f"User role changed to {role_to_change}")

    @qase_screenshot
    @qase.step(
        title="Verify and click on items list tab",
        expected="User should be able to see items list icon and able to click on items list tab",
    )
    def verify_dashboard_tab(self):
        """
        Verify Users and click on items list tab
        """
        # verify icon availability
        expect(self.dashboard_icon).to_be_visible()

    @qase_screenshot
    @qase.step(
        title="Verify visual graphs component elements",
        expected="User should be able to visible every elements of graph page",
    )
    def verify_visual_graphs_component(self):
        """
        Verify and check availability of visual graphs elements
        """
        expect(self.daily_sends_summary_component).to_be_visible()
        expect(self.daily_sends_orders_tab).to_be_visible()
        expect(self.top_sent_items_tab).to_be_visible()
        self.top_sent_items_tab.click()
        expect(self.top_sent_component).to_be_visible()
        print("visual graphs elements verified")

    @qase_screenshot
    @qase.step(
        title="Verify order summary component",
        expected="User should be able to visible every elements of order summary",
    )
    def verify_order_summary_component(
        self,
        user_data_table_headers,
        item_data_table_headers,
        newest_sends_data_table_headers,
    ):
        """
        Verify and check availability of order summary
        """
        expect(self.summary_component).to_be_visible()
        expect(self.top_10_users_tab).to_be_visible()
        expect(self.top_10_items_tab).to_be_visible()
        expect(self.newest_sends_tab).to_be_visible()
        header_text = self.user_tabel_headers.inner_text()
        headers = header_text.strip().split("\t")
        print(f"Extracted Headers: {headers}")
        # Verify that the headers match the expected column titles
        assert (
            headers == user_data_table_headers
        ), f"Expected headers {user_data_table_headers}, but found {headers}"
        self.top_10_items_tab.click()
        # Extract raw text from headers
        headers_title = self.items_table_headers.inner_text()
        print(f"Raw headers title: '{headers_title}'")
        headers_title = re.sub(r"[🔼🔽]", "", headers_title).strip()
        headers_title = re.sub(r"\s+", " ", headers_title)
        headers_list = re.findall(
            r"ID|[A-Z][a-z]*|[A-Z]+(?=[A-Z])|[a-z]+", headers_title
        )
        print(f"Extracted headers list: {headers_list}")
        assert (
            headers_list == item_data_table_headers
        ), f"Headers do not match: {headers_list} != {item_data_table_headers}"
        header_text = self.newest_sends_headers.inner_text()
        print(f"Raw header text: '{header_text}'")
        header_text = re.sub(
            r"\s+", " ", header_text
        ).strip()
        header_text = header_text.replace(
            "\u00A0", " "
        )
        print(f"Normalized header text: '{header_text}'")
        headers = re.findall(r"[A-Z][a-z]+(?: [A-Z][a-z]+)*", header_text)
        print(f"Extracted Headers: {headers}")
        assert (
            headers == newest_sends_data_table_headers
        ), f"Expected headers {newest_sends_data_table_headers}, but found {headers}"
        print("Headers match the expected values!")

    @qase_screenshot
    @qase.step(
        title="Verify send statistic component",
        expected="User should be able to visible every elements of send statistic component",
    )
    def verify_send_statistic_component(self):
        """
        Verify and check availability of items list page elements
        """
        elements_to_check = [
            self.send_statistics_component,
            self.send_statistics_title,
            self.created_sends_title,
            self.acknowledge_sends_title,
            self.shipped_sends_title,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("send statistic component verified")

    @qase_screenshot
    @qase.step(
        title="Verify statistic components",
        expected="User should be able to visible every elements of user statistic components",
    )
    def verify_user_statistics_component(self):
        """
        Verify and check availability of user statistic components
        """
        elements_to_check = [
            self.user_statistics_component,
            self.user_statistics_title,
            self.active_users_title,
            self.suspended_users_title,
            self.archived_users_title,
        ]
        for elements in elements_to_check:
            expect(elements).to_be_visible()
        print("user statistic components verified")
