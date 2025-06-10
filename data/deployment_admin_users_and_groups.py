"""
Parameters for the deployment admin users & groups page
"""

import random
import string


class DeploymentAdminUsersAndGroupsParams:
    """
    Parameters for the deployment admin users & groups page test-cases
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
    user_name = f"{first_name} {last_name}"

    # Generate random email based on firstname and lastname
    domains = ["example.com", "testmail.com", "mail.com"]
    user_email = f"{first_name.lower()}.{last_name.lower()}@{random.choice(domains)}"

    Test_1 = {
        "select_role": "Deployment Admin",
        "tab_to_navigate": "Users & Groups",
        "users_table_headers": [
            'Profile Image', 'Username', 'ID', 'First Name', 'Last Name', 'Email', 'Phone Number', 'Status', 'Actions'],
    }
    Test_2 = {
        "select_role": "Deployment Admin",
        "tab_to_navigate": "Users & Groups",
        "available_filter_options": [
            'All Users', 'Activated', 'Deactivated', 'Custom',
        ],
        "expected_statuses": {
            "All Users": ["Activated"],
            "Active Users": ["Activated"],
            "Suspended Users": ["Deactivated"],
        },
    }
    Test_3 = {
        "select_role": "Deployment Admin",
        "tab_to_navigate": "Users & Groups",
    }
    Test_4 = {
        "select_role": "Deployment Admin",
        "tab_to_navigate": "Users & Groups",
        "user_name": user_name,
        "user_email": user_email,
        "available_filter_options": ["Deployment Admin", "Sender"],
        "user_type_to_select": "Deployment Admin",
        "success_message": "Invitation sent successfully",
    }
    Test_5 = {
        "select_role": "Deployment Admin",
        "tab_to_navigate": "Users & Groups",
    }
    Test_6 = {
        "select_role": "Deployment Admin",
        "tab_to_navigate": "Users & Groups",
        "headers": ["ID", "Name", "description", "Status"],
        "success_message": "Groups assigned to user",
    }
