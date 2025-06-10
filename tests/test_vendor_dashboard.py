from pytest_playwright.pytest_playwright import page
from qase.pytest import qase
from conftest import dictionary_parametrize
from conftest import vendor_dashboard_page
from data.vendor_dashboard import VendorDashboardParams


@dictionary_parametrize(
    {
        "Test_1": VendorDashboardParams.Test_1,
    }
)
@qase.title("Verify vendor Dashboard elements")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "Verify all fields of vendor Dashboard",
    ),
)
def test_verify_vendor_dashboard_page_elements(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        vendor_dashboard_page,
        #role_to_change,
        most_sold_products_by_publish_table_headers,
        sold_products_this_week_table_headers,
):
    """
    Regression test for items list page fields verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role
    # vendor_dashboard_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=role_to_change
    # )
    # 3. Click and Verify items list tab
    vendor_dashboard_page.verify_dashboard_tab()
    # 4. Verify dashboard page functionality and elements
    vendor_dashboard_page.verify_dashboard_page_elements(
      most_sold_products_by_publish_table_headers =most_sold_products_by_publish_table_headers,
        sold_products_this_week_table_headers=sold_products_this_week_table_headers
      )
