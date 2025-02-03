"""
Parameters for the system admin send order list page
"""


class SystemAdminSendOrderListParams:
    """
    Parameters for the deployment admin send order list page test-cases
    """

    Test_1 = {
        "tab_to_navigate": "Send Order List",
    }

    Test_2 = {
        "tab_to_navigate": "Send Order List",
        "available_filter_options": [
            "All Orders",
            "Created",
            "Acknowledged",
            "Shipped",
            "Completed",
            "Custom",
        ],
        "expected_statuses": {
            "All Users": ["Created"],
            "Created": ["Created"],
            "Acknowledged": ["Acknowledged"],
            "Shipped": ["Processing"],
            "Completed": ["Created", "Shipped"],
        },
    }
