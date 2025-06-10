"""
test cases for sender connection list page
"""

from qase.pytest import qase
from conftest import dictionary_parametrize
from data.sender_connection_list import SenderConnectionListParams
from conftest import sender_connection_list_page


@dictionary_parametrize(
    {
        "Test_1": SenderConnectionListParams.Test_1,
    }
)
@qase.title("Verify sender connection list page elements")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify sender connection list page elements",
    ),
)
def test_verify_sender_connection_list_tab(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    sender_connection_list_page,
    #select_role,
    tab_to_navigate,
    headers_text,
    available_filter_options,
    expected_statuses,
):
    """
    Regression test for sender connection list page elements verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to sender
   # sender_connection_list_page.verify_and_change_user_of_role(select_role=select_role)
    # 3. Navigate to connection list tab
    sender_connection_list_page.verify_and_click_on_connection_list_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. Verify connection list page elements availability
    sender_connection_list_page.verify_connection_list_page_elements(
        headers_text=headers_text
    )
    # 5. verify filter functionality
    sender_connection_list_page.apply_filter_on_connection_list_and_verify_filtered_data(
        available_filter_options=available_filter_options,
        expected_statuses=expected_statuses,
    )
