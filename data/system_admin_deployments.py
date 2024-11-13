"""
Parameters for the system admin deployments page
"""


class SystemAdminDeploymentsParams:
    """
    Parameters for the system deployments list page test-cases
    """

    Test_1 = {
        "tab_to_navigate": "Deployments",
        "headers_text": ["ID", "Name", "Server Name", "Database Name", "Actions"],
    }
    Test_2 = {
        "tab_to_navigate": "Deployments",
        "success_message": "Deployment Deleted Successfully",
    }
    Test_3 = {
        "tab_to_navigate": "Deployments",
    }
    Test_4 = {
        "tab_to_navigate": "Deployments",
        "available_filter_options": [
            "All Users",
            "Active Users",
            "Suspended Users",
            "Custom",
        ],
        "expected_statuses": {
            "All Users": ["Active", "Suspended"],
            "Active Users": ["Active"],
            "Suspended Users": ["Suspended"],
        },
    }
    Test_5 = {
        "tab_to_navigate": "Deployments",
        "headers_text": [
            "Profile Image",
            "ID",
            "First Name",
            "Last Name",
            "Email",
            "Phone Number",
            "Status",
            "Actions",
        ],
    }
    Test_6 = {
        "tab_to_navigate": "Deployments",
        "deployment_summary_tab_navigation": "Published Items",
        "headers_text": ["ID", "Name", "Description", "Price", "Status"],
    }
    Test_7 = {
        "tab_to_navigate": "Deployments",
        "deployment_summary_tab_navigation": "Sends",
        "headers_text": [
            "Thumbnail",
            "ID",
            "Item ID",
            "Deployment ID",
            "Deployment Name",
            "Send Time",
            "Date Created",
            "Status",
        ],
    }
    Test_8 = {
        "tab_to_navigate": "Deployments",
        "deployment_summary_tab_navigation": "Account Balance",
        "account_balance_title": "Balance",
    }
    Test_9 = {
        "tab_to_navigate": "Deployments",
        "available_filter_options": [
            "All Groups",
            "Active Groups",
            "Inactive Groups",
            "Custom",
        ],
        "error_message": "User Suspended",
        "success_message": "User Activated",
        "expected_statuses": {
            "All Users": ["Active", "Inactive"],
            "Active Users": ["Active"],
            "Suspended Users": ["Inactive"],
        },
    }
