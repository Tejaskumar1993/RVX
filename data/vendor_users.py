import random
import string


class VendorUsersListParams:
    """
    Parameters for the vendor Users List page test-cases
    """
    # Generate a random first name
    first_name = "".join(random.choices(string.ascii_uppercase, k=1)) + "".join(
        random.choices(string.ascii_lowercase, k=5)
    )
    # Generate a random last name
    last_name = "".join(random.choices(string.ascii_uppercase, k=1)) + "".join(
        random.choices(string.ascii_lowercase, k=5)
    )

    # Generate random email based on firstname and lastname
    domains = ["example.com", "testmail.com", "mail.com"]
    user_email = f"{first_name.lower()}.{last_name.lower()}@{random.choice(domains)}"

    test_1 = {
       # "select_role": "Vendor",
        "tab_to_navigate": "Users",
        "users_table_headers": ['Profile Image', 'ID', 'Username', 'Email', 'Phone Number', 'Status', 'Actions']
    }
    Test_2 = {
        "tab_to_navigate": "Users",
        "available_filter_options": [
            "All Users",
            "Activated",
            "Archived",
            "Deactivated",
            "Custom",
        ],
        "expected_statuses": {
            "All Users": ["Activated", "Deactivated"],
            "Activated": ["Activated"],
            "Archived": ["Activated", "Deactivated"],
            "Deactivated": ["Deactivated"],
            "Custom": ["Activated", "Deactivated"],
        },
    }
    Test_3 = {
       # "select_role": "Vendor",
        "tab_to_navigate": "Users",
    }
    Test_4 = {
        #"select_role": "Vendor",
        "tab_to_navigate": "Users",
        "user_name": first_name,
        "user_last_name": last_name,
        "user_email": user_email,
        "success_message": "Invitation Sent Successfully",
    }
