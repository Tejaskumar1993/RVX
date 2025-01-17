"""
System admin Dashboard page modules
"""

import re
import time

from playwright.sync_api import Page, expect


class SystemAdminDashboardPage:
    """
    Module containing objects and methods related to System Admin Dashboard Page
    """

    def __init__(self, page: Page):
        super().__init__()
        self.page = page

        # User Stats locators
        self.user_stats = page.locator("//h6[text()='User Stats']")
        self.active_users = page.locator("//h6[text()='Active Users']")
        self.suspended_users = page.locator("//h6[text()='Suspended Users']")
        self.archived_users = page.locator("//h6[text()='Archived Users']")

        # Send Statistics locators
        self.send_statistics = page.locator("//h6[text()='Send Statistics']")
        self.created = page.locator("//h6[text()='Created']")
        self.acknowledged = page.locator("//h6[text()='Acknowledged']")
        self.shipped = page.locator("//h6[text()='Shipped']")

        # Send Orders By Day locators
        self.send_orders_by_day = page.locator("//h6[text()='Send Orders By Day']")

        # Order Stats locators
        self.total_deployment = page.locator("//h6[text()='Order Stats']")

        # tab table locators
        self.deployments = page.locator(
            "//button[@id='admin-dashboard-tab-tab-deployments']"
        )
        self.deployments_id = page.locator(
            "//div[@id='admin-dashboard-tab-tabpane-deployments']//th[text()='ID']"
        )
        self.deployments_name = page.locator(
            "//div[@id='admin-dashboard-tab-tabpane-deployments']//th[text()='Name']"
        )
        self.deployments_server_name = page.locator(
            "//div[@id='admin-dashboard-tab-tabpane-deployments']//th[text()='Server Name']"
        )
        self.deployments_database_name = page.locator(
            "//div[@id='admin-dashboard-tab-tabpane-deployments']//th[text()='Database Name']"
        )
        self.vendors = page.locator("//button[@id='admin-dashboard-tab-tab-vendors']")
        self.vendors_id = page.locator(
            "//div[@id='admin-dashboard-tab-tabpane-vendors']//th[text()='ID']"
        )
        self.vendors_name = page.locator(
            "//div[@id='admin-dashboard-tab-tabpane-vendors']//th[text()='Name']"
        )
        self.vendors_order_count = page.locator(
            "//div[@id='admin-dashboard-tab-tabpane-vendors']//th[text()='Order Count']"
        )
        self.vendors_phone = page.locator(
            "//div[@id='admin-dashboard-tab-tabpane-vendors']//th[text()='Phone']"
        )
        self.sent_items = page.locator(
            "//button[@id='admin-dashboard-tab-tab-itemSent']"
        )
        self.sent_items_id = page.locator(
            "//div[@id='admin-dashboard-tab-tabpane-itemSent']//th[text()='ID']"
        )
        self.sent_items_item_name = page.locator(
            "//div[@id='admin-dashboard-tab-tabpane-itemSent']//th[text()='Item Name']"
        )
        self.sent_items_order_count = page.locator(
            "//div[@id='admin-dashboard-tab-tabpane-itemSent']//th[text()='Order Count']"
        )
        self.sent_items_status = page.locator(
            "//div[@id='admin-dashboard-tab-tabpane-itemSent']//th[text()='Status']"
        )

        # interacting with a locator

    def click_user_stats(self):
        self.user_stats.click()

    def get_active_users_text(self) -> str:
        return self.active_users.text_content()

    def click_tab(self, tab_name: str):
        tabs = {
            "deployments": self.deployments,
            "vendors": self.vendors,
            "sent_items": self.sent_items,
        }
        tab = tabs.get(tab_name.lower())
        if tab:
            tab.click()
        else:
            raise ValueError(f"Invalid tab name: {tab_name}")

    # Verify all elements on the dashboard page

    def verify_all_elements(self) -> bool:
        locators = [
            self.user_stats,
            self.active_users,
            self.suspended_users,
            self.archived_users,
            self.send_statistics,
            self.created,
            self.acknowledged,
            self.shipped,
            self.send_orders_by_day,
            self.total_deployment,
            self.deployments,
            self.deployments_id,
            self.deployments_name,
            self.deployments_server_name,
            self.deployments_database_name,
            self.vendors,
            self.vendors_id,
            self.vendors_name,
            self.vendors_order_count,
            self.vendors_phone,
            self.sent_items,
            self.sent_items_id,
            self.sent_items_item_name,
            self.sent_items_order_count,
            self.sent_items_status,
        ]

        for locator in locators:
            if not locator.is_visible():
                print(f"Element not visible: {locator}")
                return False

        print("All elements are visible.")
        return True
