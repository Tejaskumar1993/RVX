"""
test cases for deployments page
"""

from qase.pytest import qase
from conftest import dictionary_parametrize
from data.system_admin_items_list import SystemAdminItemsListParams
from conftest import system_admin_items_list_page


@dictionary_parametrize(
    {
        "Test_1": SystemAdminItemsListParams.Test_1,
    }
)
@qase.title("Verify element visibility on system admin items list")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all available fields on system admin items list",
    ),
)
def test_verify_system_admin_items_list_page_elements(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    system_admin_items_list_page,
    tab_to_navigate,
    headers_text,
):
    """
    Regression test for system admin items list fields verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify items list tab
    system_admin_items_list_page.verify_and_click_on_items_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 3. Verify items list page elements availability
    system_admin_items_list_page.verify_items_list_page_elements(
        headers_text=headers_text
    )


@dictionary_parametrize(
    {
        "Test_2": SystemAdminItemsListParams.Test_2,
    }
)
@qase.title("system admin should be able performe batch action on users list")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "system admin should be able apply batch actions to users list(suspended, activate)",
    ),
)
def test_batch_action_on_items_list(
    environment_to_run,
    system_admin_items_list_page,
    ontrack_login_page,
    ontrack_password,
    ontrack_username,
    tab_to_navigate,
):
    """
    Regression test for items lists Batch action
    """
    # 1. Navigate to ontrack log, in page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify users tab
    system_admin_items_list_page.verify_and_click_on_items_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 3. Verify Batch action functionality
    system_admin_items_list_page.apply_batch_actions_to_items_list()


@dictionary_parametrize(
    {
        "Test_3": SystemAdminItemsListParams.Test_3,
    }
)
@qase.title("Verify filters functionality on items list")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify filter functionality on items list",
    ),
)
def test_filter_functionality_on_item_list(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    available_filter_options,
    system_admin_items_list_page,
    tab_to_navigate,
    expected_statuses,
):
    """
    Regression test for filter functionality of items list
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify items list tab
    system_admin_items_list_page.verify_and_click_on_items_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 3. verify filter functionality
    system_admin_items_list_page.apply_filter_on_items_list_and_verify_filtered_data(
        available_filter_options=available_filter_options,
        expected_statuses=expected_statuses,
    )


@dictionary_parametrize(
    {
        "Test_4": SystemAdminItemsListParams.Test_4,
    }
)
@qase.title(
    "verify and add new item, verify added item details on item list and check item information in item information box and perform action on added item"
)
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify and Add a New Item, Validate Item Details on the Items List, Check Item Information in the Information Box, and Perform Actions on the Added Item",
    ),
)
def test_verify_filtering_functionality_on_item_list_based_on_applied_criteria(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    system_admin_items_list_page,
    tab_to_navigate,
    item_price,
    item_fee,
    processing_time,
    item_status,
    item_category,
    item_name,
    item_description,
    tab_to_change,
    headers_text,
    deployment_tab,
    deployments_header,
    add_item_success_message,
):
    """
    Regression test for Verify and Add a New Item, Validate Item Details on the Items List, Check Item Information in the Information Box, and Perform Actions on the Added Item
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify items list tab
    system_admin_items_list_page.verify_and_click_on_items_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 3. Verify and Add a New Item, Validate Item Details on the Items List, Check Item Information in the Information Box, and Perform Actions on the Added Item
    system_admin_items_list_page.verify_and_add_new_item_and_check_added_item_information_and_perform_action_on_added_item(
        item_price=item_price,
        item_fee=item_fee,
        processing_time=processing_time,
        item_status=item_status,
        item_category=item_category,
        item_name=item_name,
        item_description=item_description,
        tab_to_change=tab_to_change,
        headers_text=headers_text,
        deployment_tab=deployment_tab,
        deployments_header=deployments_header,
        add_item_success_message=add_item_success_message,
    )


@dictionary_parametrize(
    {
        "Test_5": SystemAdminItemsListParams.Test_5,
    }
)
@qase.title("Verify and check vendor more info inside item information")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "verify and check vendor more information",
    ),
)
def test_vendor_more_info_inside_item_information(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    system_admin_items_list_page,
    tab_to_navigate,
    orders_header,
    products_header,
    users_header,
):
    """
    Regression test for verify vendor information
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify items list tab
    system_admin_items_list_page.verify_and_click_on_items_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 3. Verify and test vendor more information
    system_admin_items_list_page.verify_vendor_more_info_inside_item_information(
        orders_header=orders_header,
        products_header=products_header,
        users_header=users_header,
    )
