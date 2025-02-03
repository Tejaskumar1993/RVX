"""
test cases for deployment admin account balance page
"""

from qase.pytest import qase
from conftest import dictionary_parametrize
from data.deployment_admin_account_balance import DeploymentAdminAccountBalanceParams


@dictionary_parametrize(
    {
        "Test_1": DeploymentAdminAccountBalanceParams.Test_1,
    }
)
@qase.title("Verify account balance page elements")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all available fields on deployments list page",
    ),
)
def test_verify_account_balance_page_elements(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_account_balance_page,
    tab_to_navigate,
    transaction_record_columns_title,
    available_filter_options,
    select_role,
):
    """
    Regression test for account balance page elements verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_account_balance_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to account balance tab
    deployment_admin_account_balance_page.verify_and_click_on_account_balance_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 3. Verify account balance page elements availability
    deployment_admin_account_balance_page.verify_account_balance_page_elements(
        transaction_record_columns_title=transaction_record_columns_title,
        available_filter_options=available_filter_options,
    )


@dictionary_parametrize(
    {
        "Test_2": DeploymentAdminAccountBalanceParams.Test_2,
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
def test_apply_filter_on_transactions_record_and_verify_data(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_account_balance_page,
    tab_to_navigate,
    available_filter_options,
    select_role,
):
    """
    Regression test for account balance  filter options verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_account_balance_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to account balance tab
    deployment_admin_account_balance_page.verify_and_click_on_account_balance_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. Apply filter and verify filtered data
    deployment_admin_account_balance_page.apply_filter_on_transaction_record__and_verify_it(
        filter_options=available_filter_options
    )


@dictionary_parametrize(
    {
        "Test_3": DeploymentAdminAccountBalanceParams.Test_3,
    }
)
@qase.title("Verify schedule deposits page elements")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify schedule deposits page elements",
    ),
)
def test_verify_schedule_deposits_page_elements(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_account_balance_page,
    tab_to_navigate,
    account_balance_page_tab,
    select_role,
):
    """
    Regression test for schedule deposits fields verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_account_balance_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to account balance tab
    deployment_admin_account_balance_page.verify_and_click_on_account_balance_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. Verify schedule deposits page elements
    deployment_admin_account_balance_page.verify_schedule_deposits_page_elements(
        tab_to_navigate=account_balance_page_tab
    )


@dictionary_parametrize(
    {
        "Test_4": DeploymentAdminAccountBalanceParams.Test_4,
    }
)
@qase.title("Verify minimum account balance functionality on schedule deposits page")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify that the minimum account balance is added and reflected in current auto refills on the schedule deposits page",
    ),
)
def test_add_minium_account_balance_and_verify_it_in_current_auto_refills(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_account_balance_page,
    tab_to_navigate,
    account_balance_page_tab,
    select_role,
    confirm_message,
    below_amount,
    auto_fund_amount,
    new_auto_fund_amount,
    confirm_message_of_auto_refill_deletion,
):
    """
    Regression test for the minium account balance
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_account_balance_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to account balance tab
    deployment_admin_account_balance_page.verify_and_click_on_account_balance_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. Verify schedule deposits page elements
    deployment_admin_account_balance_page.verify_schedule_deposits_page_elements(
        tab_to_navigate=account_balance_page_tab
    )
    # 5. Add and verify minium account balance
    deployment_admin_account_balance_page.add_and_verify_new_added_minimum_account_balance(
        confirm_message=confirm_message,
        below_amount=below_amount,
        auto_fund_amount=auto_fund_amount,
        confirm_message_of_auto_refill_deletion=confirm_message_of_auto_refill_deletion,
        new_auto_fund_amount=new_auto_fund_amount,
    )


@dictionary_parametrize(
    {
        "Test_5": DeploymentAdminAccountBalanceParams.Test_5,
    }
)
@qase.title("Verify set up new auto refill functionality on schedule deposits page")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify that the added new refill is added and reflected in current auto refills on the schedule deposits page",
    ),
)
def test_add_set_up_new_auto_refill_and_verify_it_in_current_auto_refills(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_account_balance_page,
    tab_to_navigate,
    account_balance_page_tab,
    select_role,
    confirm_message,
    below_amount,
    select_occurence,
    new_auto_fund_amount,
    confirm_message_of_auto_refill_deletion,
):
    """
    Regression test for the set up new auto refill
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_account_balance_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to account balance tab
    deployment_admin_account_balance_page.verify_and_click_on_account_balance_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. Verify schedule deposits page elements
    deployment_admin_account_balance_page.verify_schedule_deposits_page_elements(
        tab_to_navigate=account_balance_page_tab
    )
    # 5. Add and verify minium account balance
    deployment_admin_account_balance_page.add_and_verify_set_up_new_auto_refill(
        confirm_message=confirm_message,
        below_amount=below_amount,
        confirm_message_of_auto_refill_deletion=confirm_message_of_auto_refill_deletion,
        new_auto_fund_amount=new_auto_fund_amount,
        select_occurence=select_occurence,
    )


@dictionary_parametrize(
    {
        "Test_6": DeploymentAdminAccountBalanceParams.Test_6,
    }
)
@qase.title(
    "Verify add new card feature inside the payment method tab of account balance"
)
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify and add add new card feature inside the payment method tab of account balance",
    ),
)
def test_add_new_card_functionality(
    environment_to_run,
    ontrack_username,
    select_role,
    deployment_admin_account_balance_page,
    ontrack_password,
    tab_to_navigate,
    ontrack_login_page,
    account_balance_page_tab,
    card_number,
    cvv,
    expiry_date,
    name_on_card,
    name,
    addressline1,
    city,
    zip,
    delete_message_text,
    success_message_text,
    state_to_select,
):
    """
    Verify and test add new card feature inside the payment method
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_account_balance_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to account balance tab
    deployment_admin_account_balance_page.verify_and_click_on_account_balance_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. Verify and add new card inside payment method tab of account balance
    deployment_admin_account_balance_page.verify_payment_method_page_elements(
        tab_to_navigate=account_balance_page_tab,
        card_number=card_number,
        cvv=cvv,
        expiry_date=expiry_date,
        name_on_card=name_on_card,
        name=name,
        addressline1=addressline1,
        city=city,
        zip=zip,
        state_to_select=state_to_select,
        success_message_text=success_message_text,
        delete_message_text=delete_message_text,
    )


@dictionary_parametrize(
    {
        "Test_7": DeploymentAdminAccountBalanceParams.Test_7,
    }
)
@qase.title("Verify deposit funds functionality")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "deposit funds functionality should be working as expected and added funds get reflected in balance",
    ),
)
def test_deposit_funds_functionality(
    environment_to_run,
    ontrack_username,
    select_role,
    deployment_admin_account_balance_page,
    ontrack_password,
    ontrack_login_page,
    select_card,
    tab_to_navigate,
    amount_to_add,
):
    """
    Verify and test deposit funds functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_account_balance_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to account balance tab
    deployment_admin_account_balance_page.verify_and_click_on_account_balance_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. Add and verify deposit funds
    deployment_admin_account_balance_page.verify_deposit_funds_functionality(
        select_card=select_card, amount_to_add=amount_to_add
    )
