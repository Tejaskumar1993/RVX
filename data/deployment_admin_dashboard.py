"""
Parameters for the deployment admin dashboard page
"""

class DeploymentAdminDashboardParams:
    """
    Parameters for the deployment admin dashboard page test-cases
    """

    Test_1 = {
        "role_to_change": "Deployment Admin",
        "user_data_table_headers": [
            "ID",
            "First Name",
            "Last Name",
            "Email",
            "Phone Number",
        ],
        "item_data_table_headers": ["ID", "Name", "Price", "Status"],
        "newest_sends_data_table_headers": [
            "Name",
            "Description",
            "Order Count",
            "Status",
        ],
    }
