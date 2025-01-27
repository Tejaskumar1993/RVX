from qase.pytest import qase
from conftest import dictionary_parametrize
from conftest import vendor_orders_list_page
from data.vendor_orders_list import VendorOrdersListParams


@dictionary_parametrize(
    {
        "Test_1": VendorOrdersListParams.test_1,
    }
)
@qase.title("Verify vendor orders list page elements")
# @qase.id(1)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all available fields on vendor orders list page",
    ),
)
def test_verify_vendor_orders_list_page_elements(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    vendor_orders_list_page,
    select_role,
    tab_to_navigate,
):
    # Log in to the application
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to vendor
    # vendor_orders_list_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=select_role
    # u
    # )
    # 3. Navigate to order list tab
    vendor_orders_list_page.verify_and_click_on_orders_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. Verify send order list page elements availability
    vendor_orders_list_page.verify_vendor_order_list_page_elements()
