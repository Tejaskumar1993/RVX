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
        "select_role": "Vendor",
        "tab_to_navigate": "Users",
        "users_table_headers": ['Profile Image', 'ID', 'Username', 'Email', 'Phone Number', 'Status', 'Actions']
    }
    Test_2 = {
        "select_role": "Vendor",
        "tab_to_navigate": "Users",
        "available_filter_options": [
            "All Users",
            "Active Users",
            "Inactive Users",
            "Custom",
        ],
        "expected_statuses": {
            "All Users": ["Active", "Inactive"],
            "Active Users": ["Active"],
            "Inactive Users Users": ["Inactive"],
        },
    }
    Test_3 = {
        "select_role": "Vendor",
        "tab_to_navigate": "Users",
    }
    Test_4 = {
        "select_role": "Vendor",
        "tab_to_navigate": "Users",
        "user_name": first_name,
        "user_last_name": last_name,
        "user_email": user_email,
        "available_filter_options": ["Deployment Admin", "Sender"],
        "user_type_to_select": "Deployment Admin",
        "success_message": "Invitation sent successfully",
    }
