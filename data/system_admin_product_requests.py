"""
Parameters for the System Admin product request page
"""


class SystemAdminProductRequestParams:
    """
    Parameters for the System Admin product request page test-cases
    """

    Test_1 = {
        "tab_to_navigate": "Product Requests",
    }

    Test_2 = {
        "tab_to_navigate": "Product Requests",
    }
    Test_3 = {
        "tab_to_navigate": "Product Requests",
        "available_filter_options": [
            "All Products",
            "Pending Products",
            "Approved Products",
            "Declined Products",
        ],
        "expected_statuses": {
            "All Products": ["Pending", "Approved", "Declined"],
            "Pending Products": ["Pending"],
            "Approved Products": ["Approved"],
            "Declined Products": ["Declined"],
        },
    }
