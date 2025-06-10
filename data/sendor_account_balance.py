"""
Parameters for the sender account balance page
"""


class SenderAccountBalanceParams:
    """
    Parameters for the sender account balance page test-cases
    """

    Test_1 = {
       # "select_role": "Sender",
        "tab_to_navigate": "Account Balance",
        "history_table_headers": [
            "Name",
            "Date",
            "Transaction Type",
            "Previous Balance",
            "Change",
            "New Balance",
        ],
    }
    Test_2 = {
      # "select_role": "Sender",
        "tab_to_navigate": "Account Balance",
        "available_filter_options": [
            "All Transactions",
            "Previous Month",
            "Previous Week",
            "Quarter-1 : Jan-March",
            "Quarter-2 : April-June",
            "Quarter-3 : July-September",
            "Quarter-4 : October-December",
        ],
    }
