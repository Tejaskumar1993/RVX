from qase.pytest import qase
from conftest import dictionary_parametrize
from conftest import vendor_product_list_page
from data.vendor_product_list import VendorProductListParams


@dictionary_parametrize(
    {
        "Test_1": VendorProductListParams.test_1,
    }
)
@qase.title("Verify vendor product list page elements")
# @qase.id(1)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "Verify all available fields on vendor product list page",
    ),
)
def test_verify_vendor_product_list_page_elements(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        vendor_product_list_page,
        select_role,
        tab_to_navigate,
        headers_text
):
    # Log in to the application
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to vendor
    vendor_product_list_page.click_on_dropdown_and_change_user_role(
        role_to_change=select_role
    )
    # 3. Navigate to product list tab
    vendor_product_list_page.verify_and_click_on_product_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. Verify product list page elements availability
    vendor_product_list_page.verify_product_list_page_elements(
        headers_text=headers_text
    )


@dictionary_parametrize(
    {
        "Test_2": VendorProductListParams.Test_2,
    }
)
@qase.title("Apply filter on products list data and verify filtered data on products list")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "Apply filter on products list data and verify filtered data on products list",
    ),
)
def test_apply_filter_on_products_list_data(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        select_role,
        vendor_product_list_page,
        tab_to_navigate,
        available_filter_options,
        expected_statuses,
):
    """
    Regression test for products list filter functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to vendor
    vendor_product_list_page.click_on_dropdown_and_change_user_role(
        role_to_change=select_role
    )
    # 3. Navigate to product list tab
    vendor_product_list_page.verify_and_click_on_product_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. Apply filter on products list and verify filtered item list
    vendor_product_list_page.verify_filter_functionality_of_product_list(
        available_filter_options=available_filter_options,
        expected_statuses=expected_statuses,
    )


@dictionary_parametrize(
    {
        "Test_3": VendorProductListParams.Test_3,
    }
)
@qase.title("Verify product list add product functionality")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "adding new product and send product request to system admin",
    ),
)
def test_add_product_flow(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        select_role,
        vendor_product_list_page,
        tab_to_navigate,
        product_name, product_price, product_shipping_rate,
        description, image_path, success_message_text
):
    """
    Regression test for add product functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to vendor
    vendor_product_list_page.click_on_dropdown_and_change_user_role(
        role_to_change=select_role
    )
    # 3. Navigate to product list tab
    vendor_product_list_page.verify_and_click_on_product_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. add item to the list
    vendor_product_list_page.verify_add_product_component_and_add_new_product(product_name=product_name,
                                                                              product_price=product_price,
                                                                              product_shipping_rate=product_shipping_rate,
                                                                              description=description,
                                                                              image_path=image_path,
                                                                              success_message_text=success_message_text)


@dictionary_parametrize(
    {
        "Test_4": VendorProductListParams.Test_4,
    }
)
@qase.title("Verify request support functionality and sent request")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "test request support functionality",
    ),
)
def test_request_support_flow(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        select_role,
        vendor_product_list_page,
        tab_to_navigate,
        request_subject,
        request_description, success_message_text
):
    """
    Regression test for request support functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to vendor
    vendor_product_list_page.click_on_dropdown_and_change_user_role(
        role_to_change=select_role
    )
    # 3. Navigate to product list tab
    vendor_product_list_page.verify_and_click_on_product_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. sent request support
    vendor_product_list_page.verify_request_support_flow_and_elements(request_subject=request_subject,
                                                                      request_description=request_description,
                                                                      success_message_text=success_message_text)


@dictionary_parametrize(
    {
        "Test_5": VendorProductListParams.Test_5,
    }
)
@qase.title("Verify enable/disable and edit action")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "enable/disable product and edit product on product list page",
    ),
)
def test_enable_disable_and_edit_actions(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        select_role,
        vendor_product_list_page,
        tab_to_navigate
):
    """
    Regression test for enable/disable and edit action
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to vendor
    vendor_product_list_page.click_on_dropdown_and_change_user_role(
        role_to_change=select_role
    )
    # 3. Navigate to product list tab
    vendor_product_list_page.verify_and_click_on_product_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. perform enable/disable and edit action
    vendor_product_list_page.verify_active_inactive_and_edit_action()
