"""
Parameters for the deployment admin send order list page
"""


class DeploymentAdminSendOrderListParams:
    """
    Parameters for the deployment admin send order list page test-cases
    """

    Test_1 = {
        "role_to_change": "Deployment Admin",
        "tab_to_navigate": "Send Order List",
    }
    Test_2 = {
        "role_to_change": "Deployment Admin",
        "tab_to_navigate": "Send Order List",
        "filter_options": [
            "All Orders",
            "Created Orders",
            "Acknowledged Orders",
            "Shipped Orders",
            "Completed Orders",
            "Custom",
        ],
        "expected_statuses": {
            "All Orders": [
                "Created",
                "Acknowledged",
                "Shipped",
                "Processing",
                "completed",
            ],
        },
    }
