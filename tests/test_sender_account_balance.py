"""
test cases for sender account balance page
"""

from qase.pytest import qase
from conftest import dictionary_parametrize
from data.sendor_account_balance import SenderAccountBalanceParams
from conftest import sender_account_balance_page


@dictionary_parametrize(
    {
        "Test_1": SenderAccountBalanceParams.Test_1,
    }
)
@qase.title("Verify sender account balance page elements")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify sender account balance page elements",
    ),
)
def test_verify_users_and_account_balance_tab(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    sender_account_balance_page,
    tab_to_navigate,
    history_table_headers,
    #select_role,
):
    """
    Regression test for sender account balance page elements verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to sender
    #sender_account_balance_page.verify_and_change_user_of_role(select_role=select_role)
    # 3. Navigate to account balance tab
    sender_account_balance_page.verify_and_click_on_account_balance_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. Verify account balance page elements availability
    sender_account_balance_page.verify_account_balance_page_elements(
        history_table_headers=history_table_headers,
    )


@dictionary_parametrize(
    {
        "Test_2": SenderAccountBalanceParams.Test_2,
    }
)
@qase.title(
    "Verify and apply all available filter on transaction record of account balance page"
)
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify filtered data",
    ),
)
def test_apply_filter_on_transactions_record_and_verify_data_of_sender_account(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    sender_account_balance_page,
    tab_to_navigate,
    available_filter_options,
    #select_role,
):
    """
    Regression test for account balance  filter options verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to sender
    #sender_account_balance_page.verify_and_change_user_of_role(select_role=select_role)
    # 3. Navigate to account balance tab
    sender_account_balance_page.verify_and_click_on_account_balance_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. Apply filter and verify filtered data
    sender_account_balance_page.apply_filter_on_transaction_record_and_verify_it(
        filter_options=available_filter_options
    )
