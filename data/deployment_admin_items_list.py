"""
Parameters for the deployment admin items list page
"""


class DeploymentAdminItemsListParams:
    """
    Parameters for the deployment admin items list page test-cases
    """

    Test_1 = {
        "role_to_change": "Deployment Admin",
        "tab_to_navigate": "Items List",
        "headers_text": [
            "Thumbnail",
            "ID",
            "Display Name",
            "Price",
            "Status",
            "Actions",
        ],
    }
    Test_2 = {
        "role_to_change": "Deployment Admin",
        "tab_to_navigate": "Items List",
        "available_filter_options": [
            "All Items",
            "Active Items",
            "Inactive Items",
            "Custom",
        ],
        "expected_statuses": {
            "All Users": ["Active", "Inactive"],
            "Active Users": ["Active"],
            "Suspended Users": ["Inactive"],
        },
    }
    Test_3 = {"role_to_change": "Deployment Admin", "tab_to_navigate": "Items List"}
    Test_4 = {
        "role_to_change": "Deployment Admin",
        "tab_to_navigate": "Items List",
        "headers_text": [
            "ID",
            "Thumbnail",
            "Item Name",
            "Description",
            "Price",
            "Status",
        ],
        "headers_text_of_summary": [
            "ID",
            "Item Name",
            "Description",
            "Price",
            "Status",
        ],
    }
    Test_5 = {
        "role_to_change": "Deployment Admin",
        "tab_to_navigate": "Items List",
        "tab_to_change": "Send Orders",
        "headers_text": [
            "ID",
            "Batch ID",
            "Campaign",
            "Item Sent",
            "Date Sent",
            "Status",
        ],
    }
    Test_6 = {
        "role_to_change": "Deployment Admin",
        "tab_to_navigate": "Items List",
        "available_filter_options": [
            "All Items",
            "Active Items",
            "Custom",
        ],
        "expected_statuses": {"All Users": ["Active"], "Active Users": ["Active"]},
    }
