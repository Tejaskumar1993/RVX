"""
Parameters for the Deployment admin Account Balance page
"""

import random
import string
from datetime import datetime, timedelta


class DeploymentAdminAccountBalanceParams:
    """
    Parameters for the deployment deployments Account Balance page test-cases
    """

    # Generate a random first name
    first_name = "".join(random.choices(string.ascii_uppercase, k=1)) + "".join(
        random.choices(string.ascii_lowercase, k=5)
    )
    # Generate a random last name
    last_name = "".join(random.choices(string.ascii_uppercase, k=1)) + "".join(
        random.choices(string.ascii_lowercase, k=5)
    )
    # Combine the first and last name
    name_on_card = f"{first_name} {last_name}"
    # Output the generated name
    print(f"Generated Name on Card: {name_on_card}")
    # Generate expiry date for a future month in MM/YY format
    current_date = datetime.now()
    # Adding a random number of months (between 1 and 24 months) to the current date
    future_date = current_date + timedelta(days=random.randint(30, 730))
    expiry_date = future_date.strftime("%m/%y")
    print(f"Generated Expiry Date: {expiry_date}")
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
            "All Transactions",
            "Previous Month",
            "Previous Week",
            "Quarter-1 : Jan-March",
            "Quarter-2 : April-June",
            "Quarter-3 : July-September",
            "Quarter-4 : October-December",
            "Custom"
        ],
        "select_role": "Deployment Admin",
    }

    Test_2 = {
        "tab_to_navigate": "Account Balance",
        "select_role": "Deployment Admin",
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
    Test_6 = {
        "tab_to_navigate": "Account Balance",
        "select_role": "Deployment Admin",
        "account_balance_page_tab": "Payment Method",
        "card_number": "5063516945005047",
        "cvv": "234",
        "expiry_date": expiry_date,
        "name_on_card": name_on_card,
        "name": first_name,
        "addressline1": "1306 E Belt Line Rd",
        "city": "Richardson",
        "zip": "75081",
        "state_to_select": "Texas",
        "success_message_text": "New card added successfully!",
        "delete_message_text": "Card deleted successfully",
    }
    Test_7 = {
        "tab_to_navigate": "Account Balance",
        "select_role": "Deployment Admin",
        "select_card": "DINERS - 0004",
        "amount_to_add": "5",
    }
