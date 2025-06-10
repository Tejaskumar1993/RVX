"""
Vendor Dashboard page modules
"""

import time

from playwright.sync_api import Page, expect
from qase.pytest import qase
from pages.base_page import BasePage
from utilities.decorators import qase_screenshot


class VendorDashboardPage(BasePage):
    """
    Module containing objects and methods related to Vendor dashboard page
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Company information page locators
        self.change_role_dropdown = page.locator('(//button[@id="dropdown-flags"])[2]')
        self.role_to_select = '//a[text()="<<role_to_change>>"]'
        self.dashboard_icon = page.locator('//*[@data-icon="chart-pie"]')
        self.dashboard_tab = page.locator('//span[text()="Dashboard"]')

        self.company_information_content_box = page.locator('//div[@class="h-md-100 card"]')
        self.company_logo = page.locator('(//div[@class="d-flex align-items-center"])[1]')
        self.company_name = page.locator('//h6[text()="Company Name"]')
        self.company_phone_number = page.locator('//h6[text()="Phone Number"]')
        self.company_email = page.locator('//h6[text()="Email"]')
        self.new_orders_content_box = page.locator(
            '//h6[text()="New Orders"]//..//..//div[@class="position-relative card-body"]')
        self.see_new_orders_list_here_link = page.locator(
            '//a[text()="See New Orders List Here"]')
        self.awaiting_shipment_content_box = page.locator(
            '//h6[text()="Awaiting Shipment Orders"]//..//..//div[@class="position-relative card-body"]')
        self.awaiting_shipment_orders_link = page.locator(
            '//a[text()="See Awaiting Shipment Orders List Here"]')
        self.shipped_orders_content_box = page.locator(
            '//h6[text()="Shipped Orders"]//..//..//div[@class="position-relative card-body"]')
        self.see_shipped_orders_list_link = page.locator(
            '//a[text()="See Shipped Orders List Here"]')
        self.completed_orders_content_box = page.locator(
            '//h6[text()="Completed Orders"]//..//..//div[@class="position-relative card-body"]')
        self.see_completed_orders_list_link = page.locator(
            '//a[text()="See Completed Orders List Here"]')
        self.all_orders_content_box = page.locator(
            '//h6[text()="All Orders"]//..//..//div[@class="position-relative card-body"]')
        self.see_orders_list_link = page.locator(
            '//a[text()="See Orders List Here"]')
        self.approved_products_content_box = page.locator(
            '//h6[text()="Approved Products"]//..//..//div[@class="position-relative card-body"]')
        self.see_products_list_link = page.locator(
            '//a[text()="See Products List Here"]')
        self.orders_graph_box = page.locator('//div[text()="Orders"]//..//..//div[@class="card"]')
        self.orders_chart = page.locator('//div[text()="Orders"]//..//..//div[@class="echarts-for-react "]')
        self.most_ordered_products_content_box = page.locator(
            '//div[text()="Most Ordered Products"]//..//..//..//div[@class="ant-spin-container"]')
        self.top_adopted_products = page.locator("//button[@id='admin-dashboard-tab-tab-productsByPublish']")
        self.top_adopted_products_header = page.locator("//div[@class='vendor-dasboard-tabbed-table-wrapper']//tr[@class='text-center']")
        self.most_ordered_products = page.locator("//button[@id='admin-dashboard-tab-tab-mostOrderProducts']")
        self.most_ordered_products_header = page.locator("//div[@class='table-wrapper']//tr[@class='text-center']")

    @qase_screenshot
    @qase.step(
        title="click on user role dropdown and select role",
        expected="User should be able to change role successfully",
    )
    # def click_on_dropdown_and_change_user_role(self, role_to_change):
    #     """
    #     Change user role from dropdown
    #     """
    #     self.change_role_dropdown.click()
    #     self.page.locator(
    #         self.role_to_select.replace("<<role_to_change>>", role_to_change)
    #     ).click()
    #     print(f"User role changed to {role_to_change}")

    @qase_screenshot
    @qase.step(
        title="Verify dashboard tab",
        expected="User should be able to see dashboard icon and able to click on dashboard tab",
    )
    def verify_dashboard_tab(self):
        """
        Verify dashboard tab
        """
        # verify icon availability
        expect(self.dashboard_icon).to_be_visible()

    @qase_screenshot
    @qase.step(
        title="Verify dashboard page elements",
        expected="User should be able to see all elements on dashboard page",
    )
    def verify_dashboard_page_elements(self, most_sold_products_by_publish_table_headers,
                                       sold_products_this_week_table_headers):
        """
        Verify all key elements and headers on the dashboard page.
        """
        time.sleep(5)

        # Elements that should be visible
        elements_to_check = [
            self.company_information_content_box,
            self.company_logo,
            self.company_name,
            self.company_phone_number,
            self.company_email,
            self.most_ordered_products_content_box,
            self.most_ordered_products,
            self.top_adopted_products,
            self.orders_graph_box,
            self.orders_chart,
            self.approved_products_content_box,
            self.see_products_list_link,
            self.all_orders_content_box,
            self.see_orders_list_link,
            self.completed_orders_content_box,
            self.see_completed_orders_list_link,
            self.shipped_orders_content_box,
            self.see_shipped_orders_list_link,
            self.awaiting_shipment_orders_link,
            self.awaiting_shipment_content_box,
            self.new_orders_content_box,
            self.see_new_orders_list_here_link,
        ]

        for element in elements_to_check:
            expect(element).to_be_visible()

        # Check Most Ordered Products header
        self.most_ordered_products.click()
        time.sleep(2)
        products_headers = self.most_ordered_products_header.inner_text().strip()
        sold_products_this_week_table_headers = [header.strip() for header in sold_products_this_week_table_headers]
        assert any(header in products_headers for header in sold_products_this_week_table_headers), \
            f"Actual headers '{products_headers}' not found in expected headers {sold_products_this_week_table_headers}"

        # Click on Top Adopted Products and check header
        self.top_adopted_products.click()
        adopted_products_header = self.top_adopted_products_header.inner_text().strip()
        most_sold_products_by_publish_table_headers = [header.strip() for header in
                                                       most_sold_products_by_publish_table_headers]
        assert any(header in adopted_products_header for header in most_sold_products_by_publish_table_headers), \
            f"Actual headers '{adopted_products_header}' not found in expected headers {most_sold_products_by_publish_table_headers}"

        # Navigation and URL validation
        self.see_new_orders_list_here_link.click()
        time.sleep(2)
        assert 'dashboard/order-list' in self.page.url

        self.dashboard_tab.click()
        self.awaiting_shipment_orders_link.click()
        assert 'dashboard/order-list' in self.page.url

        self.dashboard_tab.click()
        self.see_shipped_orders_list_link.click()
        time.sleep(2)
        assert 'dashboard/order-list' in self.page.url

        self.dashboard_tab.click()
        self.see_completed_orders_list_link.click()
        time.sleep(2)
        assert 'dashboard/order-list' in self.page.url

        self.dashboard_tab.click()
        self.see_orders_list_link.click()
        time.sleep(2)
        assert 'dashboard/order-list' in self.page.url

        self.dashboard_tab.click()
        self.see_products_list_link.click()
        time.sleep(2)
        assert 'dashboard/product-list' in self.page.url
