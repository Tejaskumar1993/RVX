"""
test cases for Vendors list page
"""

from qase.pytest import qase
from conftest import dictionary_parametrize
from data.system_admin_vendors import SystemAdminVendorsParams
from conftest import system_admin_vendors_page


@dictionary_parametrize(
    {
        "Test_1": SystemAdminVendorsParams.Test_1,
    }
)
@qase.title("User should be able to see all available fields on vendors list page")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all available fields on vendors list page",
    ),
)
def test_verify_vendors_page_fields(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    system_admin_vendors_page,
    tab_to_navigate,
    headers_text,
):
    """
    Regression test for users page fields verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify users tab
    system_admin_vendors_page.verify_and_click_on_vendors_tab(
        side_navigation_item=tab_to_navigate
    )
    # 3. Verify users page elements availability
    system_admin_vendors_page.verify_vendors_page_elements(headers_text=headers_text)


@dictionary_parametrize(
    {
        "Test_2": SystemAdminVendorsParams.Test_2,
    }
)
@qase.title("system admin should be able filter vendors list data")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "system admin should be able filter vendors list data",
    ),
)
def test_vendors_list_filters(
    environment_to_run,
    system_admin_vendors_page,
    available_filter_options,
    expected_statuses,
    ontrack_login_page,
    ontrack_password,
    ontrack_username,
    tab_to_navigate,
):
    """
    Regression test for vendors lists filters
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify vendors tab
    system_admin_vendors_page.verify_and_click_on_vendors_tab(
        side_navigation_item=tab_to_navigate
    )
    # 3. Verify filter title and options
    system_admin_vendors_page.verify_filters_field_and_filter_options(
        available_filter_options=available_filter_options
    )
    # 4. Apply all available filters and verify filtered data
    system_admin_vendors_page.apply_filters_and_verify_filtered_data(
        available_filter_options, expected_statuses
    )


@dictionary_parametrize(
    {
        "Test_3": SystemAdminVendorsParams.Test_3,
    }
)
@qase.title("system admin should be able perform batch action on vendors list")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "system admin should be able apply batch actions to vendors list(delete item, suspended, activate)",
    ),
)
def test_batch_action_on_vendors_list(
    environment_to_run,
    system_admin_vendors_page,
    ontrack_login_page,
    ontrack_password,
    ontrack_username,
    tab_to_navigate,
    success_message_text,
):
    """
    Regression test for vendors lists Batch action
    """
    # 1. Navigate to ontrack log, in page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify vendors tab
    system_admin_vendors_page.verify_and_click_on_vendors_tab(
        side_navigation_item=tab_to_navigate
    )
    # 3. Verify Batch action functionality
    system_admin_vendors_page.apply_batch_actions_to_vendors_list(
        success_message_text=success_message_text
    )


@dictionary_parametrize(
    {
        "Test_4": SystemAdminVendorsParams.Test_4,
    }
)
@qase.title("system admin should be able add new vendor on vendor list")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "system admin should be able to add new vendor via vendors list page",
    ),
)
def test_add_vendor_functionality_on_vendors_list(
    environment_to_run,
    system_admin_vendors_page,
    ontrack_login_page,
    ontrack_password,
    ontrack_username,
    tab_to_navigate,
    success_message_text,
    vendor_name,
    vendor_email,
    vendor_addressline_1,
    vendor_addressline_2,
    vendor_city,
    state_to_select,
    zipcode,
    phone_number,
    select_vendor,
):
    """
    Regression test for vendors lists add vendor feature
    """
    # 1. Navigate to ontrack log, in page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify vendors tab
    system_admin_vendors_page.verify_and_click_on_vendors_tab(
        side_navigation_item=tab_to_navigate
    )
    # 3. verify and add new vendor
    system_admin_vendors_page.add_new_vendor_in_vendors_list(
        success_message_text,
        vendor_name=vendor_name,
        vendor_email=vendor_email,
        vendor_addressline_1=vendor_addressline_1,
        vendor_addressline_2=vendor_addressline_2,
        vendor_city=vendor_city,
        state_to_select=state_to_select,
        zipcode=zipcode,
        phone_number=phone_number,
        select_vendor=select_vendor,
    )


@dictionary_parametrize({"Test_5": SystemAdminVendorsParams.Test_5})
@qase.title("system should be able active or inactive any vendor from the actions")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "system should be able active or inactive any vendor from the actions",
    ),
)
def test_active_inactive_vendor_functionality_on_vendors_list(
    environment_to_run,
    system_admin_vendors_page,
    ontrack_login_page,
    ontrack_password,
    ontrack_username,
    tab_to_navigate,
    updated_vendor_message_text,
):
    """
    Regression test for vendors lists add vendor feature
    """
    # 1. Navigate to ontrack log, in page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify vendors tab
    system_admin_vendors_page.verify_and_click_on_vendors_tab(
        side_navigation_item=tab_to_navigate
    )
    # 3. verify active and inactive feature from the actions
    system_admin_vendors_page.verify_active_and_inactive_functionality_from_action(
        updated_vendor_message_text=updated_vendor_message_text
    )


@dictionary_parametrize({"Test_6": SystemAdminVendorsParams.Test_6})
@qase.title("system admin should be able manage and delete any vendor from the actions")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "system admin should be able manage and delete any vendor from the actions",
    ),
)
def test_more_info_actions_functionality_on_vendors_list(
    environment_to_run,
    system_admin_vendors_page,
    ontrack_login_page,
    ontrack_password,
    ontrack_username,
    tab_to_navigate,
    orders_headers_text,
    products_headers_text,
    users_headers_text,
):
    """
    Regression test for vendors lists add vendor feature
    """
    # 1. Navigate to ontrack log, in page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Click and Verify vendors tab
    system_admin_vendors_page.verify_and_click_on_vendors_tab(
        side_navigation_item=tab_to_navigate
    )
    # 3. verify and test manage and delete functionality
    system_admin_vendors_page.verify_manage_and_delete_functionality_from_action(
        orders_headers_text=orders_headers_text,
        products_headers_text=products_headers_text,
        users_headers_text=users_headers_text,
    )
