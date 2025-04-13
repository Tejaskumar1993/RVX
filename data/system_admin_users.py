"""
Parameters for the system admin users page
"""

import random
import string


class SystemAdminUsersParams:
    """
    Parameters for the system users list page test-cases
    """

    # Generate random firstname and lastname
    firstname = "".join(random.choices(string.ascii_lowercase, k=6)).capitalize()
    lastname = "".join(random.choices(string.ascii_lowercase, k=6)).capitalize()

    # Generate random email based on firstname and lastname
    domains = ["example.com", "testmail.com", "mail.com"]
    email = f"{firstname.lower()}.{lastname.lower()}@{random.choice(domains)}"

    Test_1 = {
        "tab_to_navigate": "Users",
        "headers_text": [
            "Profile Image",
            "ID",
            "User Type",
            "Username",
            "Email",
            "Phone Number",
            "Status",
            "Actions",
        ],
    }

    Test_2 = {
        "available_filter_options": ["All Users","Active Users","Inactive Users","Custom",],
        "tab_to_navigate": "Users",
        "expected_statuses": {
            "All Users": ["Active", "Inactive"],
            "Active Users": ["Active"],
            "Inactive Users": ["Inactive"],
        },
    }

    Test_3 = {
        "tab_to_navigate": "Users",
    }

    Test_4 = {
        "tab_to_navigate": "Users",
        "last_name": lastname,
        "first_name": firstname,
        "email": email,
        "user_type_select": ["System Admin", "Sender"],
    }

    Test_5 = {
        "tab_to_navigate": "Users",
        "last_name": lastname,
        "first_name": firstname,
        "email": email,
        "user_type_select": "Deployment Admin",
        "deployment_name": "Development Deployment",
    }

    Test_6 = {
        "tab_to_navigate": "Users",
        "last_name": lastname,
        "first_name": firstname,
        "email": email,
        "user_type_select": "Vendor",
        "vendor_to_select": "Tango E-Gift Provider",
    }
