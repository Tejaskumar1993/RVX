"""
Parameters for the Deployment admin Account Balance page
"""


class DeploymentAdminAccountBalanceParams:
    """
    Parameters for the deployment deployments Account Balance page test-cases
    """

    Test_1 = {
        "tab_to_navigate": "Account Balance",
        "transaction_record_columns_title": [
            "Username",
            "Account",
            "Type",
            "Previous Balance",
            "Amount",
            "New Balance",
            "Time Stamp",
        ],
        "available_filter_options": [
            "All Items",
            "Previous Month",
            "Previous Week",
            "Quarter-1 : Jan-March",
            "Quarter-2 : April-June",
            "Quarter-3 : July-September",
            "Quarter-4 : October-December",
        ],
        "select_role": "Deployment Admin",
    }

    Test_2 = {
        "tab_to_navigate": "Account Balance",
        "select_role": "Deployment Admin",
        "available_filter_options": [
            "All Items",
            "Previous Month",
            "Previous Week",
            "Quarter-1 : Jan-March",
            "Quarter-2 : April-June",
            "Quarter-3 : July-September",
            "Quarter-4 : October-December",
        ],
    }
    Test_3 = {
        "tab_to_navigate": "Account Balance",
        "select_role": "Deployment Admin",
        "account_balance_page_tab": "Schedule Deposits",
    }
    Test_4 = {
        "tab_to_navigate": "Account Balance",
        "select_role": "Deployment Admin",
        "account_balance_page_tab": "Schedule Deposits",
        "confirm_message": "Are you sure you would like to submit this change?",
        "below_amount": "1",
        "auto_fund_amount": "1",
        "confirm_message_of_auto_refill_deletion": "Are you sure you want to cancel this Auto refill?",
        "new_auto_fund_amount": "2",
    }
    Test_5 = {
        "tab_to_navigate": "Account Balance",
        "select_role": "Deployment Admin",
        "account_balance_page_tab": "Schedule Deposits",
        "confirm_message": "Are you sure you would like to submit this change?",
        "below_amount": "1",
        "select_occurence": "Monthly",
        "confirm_message_of_auto_refill_deletion": "Are you sure you want to cancel this Auto refill?",
        "new_auto_fund_amount": "2",
    }
