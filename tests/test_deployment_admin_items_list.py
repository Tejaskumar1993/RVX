"""
test cases for deployment admin items list page
"""

from qase.pytest import qase
from conftest import dictionary_parametrize
from data.deployment_admin_items_list import DeploymentAdminItemsListParams
from conftest import deployment_admin_items_list_page


@dictionary_parametrize(
    {
        "Test_1": DeploymentAdminItemsListParams.Test_1,
    }
)
@qase.title("Verify deployment admin items list page elements")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "Verify all fields of deployment admin items list page",
    ),
)
def test_verify_items_list_page_elements(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        deployment_admin_items_list_page,
        tab_to_navigate,
        role_to_change,
        headers_text,
):
    """
    Regression test for items list page fields verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role
    deployment_admin_items_list_page.click_on_dropdown_and_change_user_role(
        role_to_change=role_to_change
    )
    # 3. Click and Verify items list tab
    deployment_admin_items_list_page.verify_and_click_on_items_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. Verify items list page elements availability
    deployment_admin_items_list_page.verify_items_list_page_elements(
        headers_text=headers_text
    )

@dictionary_parametrize(
    {
        "Test_2": DeploymentAdminItemsListParams.Test_2,
    }
)
@qase.title("Apply filter on items list data and verify filtered data on items list")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "Apply filter on items list data and verify filtered data on items list",
    ),
)
def test_apply_filter_on_items_list_data(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        #role_to_change,
        deployment_admin_items_list_page,
        tab_to_navigate,
        available_filter_options,
        expected_statuses,
):
    """
    Regression test for items list filter functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role
    # deployment_admin_items_list_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=role_to_change
    # )
    # 3. Click and Verify users tab
    deployment_admin_items_list_page.verify_and_click_on_items_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. Apply filter on items list and verify filtered item list
    deployment_admin_items_list_page.apply_filter_on_items_list_and_verify_filtered_data(
        available_filter_options=available_filter_options,
        expected_statuses=expected_statuses,
    )


@dictionary_parametrize(
    {
        "Test_3": DeploymentAdminItemsListParams.Test_3,
    }
)
@qase.title("Apply batch action on item to change status of items")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "apply batch action on multiple items at time to change status",
    ),
)
def test_apply_batch_action_on_items_to_changes_current_status_in_bulk(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        role_to_change,
        deployment_admin_items_list_page,
        tab_to_navigate,
):
    """
    Regression test for batch action functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role
    deployment_admin_items_list_page.click_on_dropdown_and_change_user_role(
        role_to_change=role_to_change
    )
    # 3. Click and Verify users tab
    deployment_admin_items_list_page.verify_and_click_on_items_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. Apply batch action on item to change status
    deployment_admin_items_list_page.apply_batch_action_to_items()


@dictionary_parametrize(
    {
        "Test_4": DeploymentAdminItemsListParams.Test_4,
    }
)
@qase.title("Verify items list add item functionality")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "using add item functionality, Add item to the user list",
    ),
)
def test_add_item_flow(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        role_to_change,
        headers_text_of_summary,
        deployment_admin_items_list_page,
        tab_to_navigate,
        headers_text,
):
    """
    Regression test for add item functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role
    deployment_admin_items_list_page.click_on_dropdown_and_change_user_role(
        role_to_change=role_to_change
    )
    # 3. Click and Verify users tab
    deployment_admin_items_list_page.verify_and_click_on_items_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. add item to the list
    deployment_admin_items_list_page.add_item_to_user_list_and_make_it_ready_to_send(
        headers_text=headers_text, headers_text_of_summary=headers_text_of_summary
    )


@dictionary_parametrize(
    {
        "Test_5": DeploymentAdminItemsListParams.Test_5,
    }
)
@qase.title("Verify items information pop-up details")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "Verify item information both tabs fields",
    ),
)
def test_item_information_component_and_tabs(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        role_to_change,
        tab_to_change,
        deployment_admin_items_list_page,
        tab_to_navigate,
        headers_text,
):
    """
    Regression test for item information
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role
    deployment_admin_items_list_page.click_on_dropdown_and_change_user_role(
        role_to_change=role_to_change
    )
    # 3. Click and Verify users tab
    deployment_admin_items_list_page.verify_and_click_on_items_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. verify item information
    deployment_admin_items_list_page.verify_item_information_modal_content(
        tab_to_change=tab_to_change, headers_text=headers_text
    )

@dictionary_parametrize(
    {
        "Test_6": DeploymentAdminItemsListParams.Test_6,
    }
)
@qase.title("Verify add items filters functionality")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "Verify add item filter functionality",
    ),
)
def test_filter_functionality_inside_add_item_feature(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        #role_to_change,
        available_filter_options,
        deployment_admin_items_list_page,
        tab_to_navigate,
        expected_statuses,
):
    """
    Regression test for filter functionality of add item page
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role
    # deployment_admin_items_list_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=role_to_change
    # )
    # 3. Click and Verify users tab
    deployment_admin_items_list_page.verify_and_click_on_items_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. verify filter functionality
    deployment_admin_items_list_page.verify_filter_functionality_of_add_item(
        available_filter_options=available_filter_options,
        expected_statuses=expected_statuses,
    )


@dictionary_parametrize(
    {
        "Test_7": DeploymentAdminItemsListParams.Test_5,
    }
)
@qase.title("Verify actions functionality on items list")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "Verify and perform actions functionality on items list",
    ),
)
def test_actions_on_the_items_list(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        role_to_change,
        deployment_admin_items_list_page,
        tab_to_navigate,
        tab_to_change,
        headers_text,
):
    """
    Regression test for actions functionality of add item page
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role
    deployment_admin_items_list_page.click_on_dropdown_and_change_user_role(
        role_to_change=role_to_change
    )
    # 3. Click and Verify users tab
    deployment_admin_items_list_page.verify_and_click_on_items_list_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. Test edit delete and status activity on items list
    deployment_admin_items_list_page.verify_and_perform_edit_status_and_delete_actions_functionality_from_actions(
        tab_to_change=tab_to_change, headers_text=headers_text
    )
