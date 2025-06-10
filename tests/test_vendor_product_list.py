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
        #select_role,
        tab_to_navigate,
        headers_text
):
    # Log in to the application
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )

    #2. Navigate to product list tab
    vendor_product_list_page.navigate_to_product_list(
        tab_to_navigate=tab_to_navigate
    )
    #4. Verify product list page elements availability
    vendor_product_list_page.verify_vendor_product_list_page_elements(
        tab_to_navigate=tab_to_navigate,
         headers_text=headers_text)


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
        #select_role,
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
    # vendor_product_list_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=select_role
    # )
    # 3. Navigate to product list tab
    vendor_product_list_page.navigate_to_product_list(
        tab_to_navigate=tab_to_navigate

    )
    # 4. Apply filter on products list and verify filtered item list
    vendor_product_list_page.apply_filter_and_verify_statuses(
        available_filter_options=available_filter_options,
        expected_statuses=expected_statuses,
    )


@qase.title("Add Product Request and Verify Element Visibility & Values")
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    ("description",
     "Verify that the elements are visible and contain correct values in the Add Product Request process."),
)
@dictionary_parametrize(
    {
        "Test_0": VendorProductListParams.Test_0,  # Fetching parameters from VendorProductListParams
    }
)
def test_add_product_request_element_verification(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        vendor_product_list_page,
        tab_to_navigate,
):
    """
    Test case to add a product request and verify the element visibility and values.
    """

    # Step 1: Open and verify the Ontrack login page with provided credentials
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )

    # Step 2: Navigate to the Product List tab
    vendor_product_list_page.navigate_to_product_list(
        tab_to_navigate=tab_to_navigate
    )

    # Step 3: Verify visibility and correctness of elements on the 'New Product Request' page
    vendor_product_list_page.verify_new_product_request_page_elements()



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
    vendor_product_list_page,
    tab_to_navigate,
    product_name,
    category,
    product_price,
    product_shipping_rate,
    product_type,
    description,
    image_path,
    success_message_text
):
    """
    Regression test for add product functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to vendor
    # vendor_product_list_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=select_role
    # )
    # 3. Navigate to product list tab
    vendor_product_list_page.navigate_to_product_list(
        tab_to_navigate=tab_to_navigate
    )
    # 4. add item to the list
    vendor_product_list_page.verify_and_fill_add_product_request_form(
        product_name,
        product_price,
        product_shipping_rate,
        description,
        category,
        product_type,
        image_path,
        success_message_text
    )
    print(f"Product request for '{product_name}' has been successfully submitted.")


@dictionary_parametrize(
    {
        "Test_Update_1": VendorProductListParams.Test_3,
    }
)
@qase.title("Verify product list update product functionality")
# @qase.id(3)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "Updating existing product and sending updated request to system admin",
    ),
)
def test_update_product_flow(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        vendor_product_list_page,
        tab_to_navigate,
        product_name,
        category,
        product_price,
        product_shipping_rate,
        product_type,
        description,
        image_path,
        success_message_text
):
    """
    Regression test for update product functionality
    """
    # 1. Navigate to ontrack login page and verify all elements of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to vendor
    # vendor_product_list_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=select_role
    # )
    # 3. Navigate to product list tab
    vendor_product_list_page.navigate_to_product_list(
        tab_to_navigate=tab_to_navigate
    )
    # 4. Update existing product
    vendor_product_list_page.verify_and_fill_update_product_form(
        product_name,
        product_price,
        product_shipping_rate,
        description,
        category,
        product_type,
        image_path,
        success_message_text
    )
    print(f"Product '{product_name}' has been successfully updated.")


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
        #select_role,
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
    # vendor_product_list_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=select_role
    # )
    # 3. Navigate to product list tab
    vendor_product_list_page.navigate_to_product_list(
        tab_to_navigate=tab_to_navigate
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


@dictionary_parametrize(
    {
        "Test_Update_1": VendorProductListParams.Test_6,
    }
)
@qase.title("Verify product list update product functionality")
# @qase.id(3)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "Updating existing product and sending updated request to system admin",
    ),
)
def test_change_order_product_flow(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        vendor_product_list_page,
        tab_to_navigate,
        available_filter_options,
        expected_statuses,
        product_name,
        category,
        product_price,
        product_shipping_rate,
        description,
        image_path,
        success_message_text
):
    """
    Regression test for update product functionality
    """
    # 1. Navigate to ontrack login page and verify all elements of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to vendor
    # vendor_product_list_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=select_role
    # )
    # 3. Navigate to product list tab
    vendor_product_list_page.navigate_to_product_list(
        tab_to_navigate=tab_to_navigate
    )
    vendor_product_list_page.verify_approved_product(
        available_filter_options = available_filter_options,
        expected_statuses = expected_statuses)

    vendor_product_list_page.verify_submit_change_order_flow_and_elements(
        product_name,
        product_price,
        product_shipping_rate,
        description,
        category,
        image_path,
        success_message_text
    )

@dictionary_parametrize(
    {
        "Test_Update_1": VendorProductListParams.Test_7,
    }
)
@qase.title("Verify Edit product disable functionality")
# @qase.id(3)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "Edit product disable functionality",
    ),
)

def test_enable_disable_and_edit_actions(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        vendor_product_list_page,
        tab_to_navigate,
        available_filter_options,
        expected_statuses,
):
    """
    Regression test for enable/disable and edit action
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to vendor
    # vendor_product_list_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=select_role
    # )
    # 3. Navigate to product list tab
    vendor_product_list_page.navigate_to_product_list(
        tab_to_navigate=tab_to_navigate
    )

    vendor_product_list_page.verify_approved_product(
        available_filter_options=available_filter_options,
        expected_statuses=expected_statuses
    )
    # 4. perform enable/disable and edit action
    vendor_product_list_page.verify_vendor_edit_product_disable_functionality()


@dictionary_parametrize(
    {
        "Test_Update_1": VendorProductListParams.Test_8,
    }
)
@qase.title("Verify batch action Deleted item")
# @qase.id(3)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    ("description", "Verify batch action Deleted item"),
)
def test_batch_action_delete_product_item(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        vendor_product_list_page,
        tab_to_navigate,
        available_filter_options,
        expected_statuses,
        success_message_text
):
    """
    Test for verifying the edit product disable functionality in the vendor product list.
    """
    # 1. Navigate to Ontrack login page and verify all elements on the login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and verify the Product list tab
    vendor_product_list_page.navigate_to_product_list(
        tab_to_navigate=tab_to_navigate
    )
    # 3. Verify that batch action functionality works correctly
    vendor_product_list_page.verify_batch_action_delete_product_item(
        available_filter_options=available_filter_options,
        expected_statuses=expected_statuses,
        success_message_text= success_message_text
    )

