"""
Parameters for the sender connection list page
"""


class SenderConnectionListParams:
    """
    Parameters for the sender connection list page test-cases
    """

    Test_1 = {
        #"select_role": "Sender",
        "tab_to_navigate": "Connection List",
        "headers_text": [
            "Recipient",
            "Items",
            "Sender",
            "Delivery Method",
            "Date",
            "Status",
        ],
        "available_filter_options": [
            "All Sends",
            "Custom",
        ],
        "expected_statuses": {
            "All Sends": [
                "Acknowledged",
                "Processing",
                "Shipped",
                "Created",
                "Completed",
            ],
            "expected_custom_filter": {
                "Custom": [
                    "Recipient",
                    "Items",
                    "Sender",
                    "Delivery Method",
                    "Date",
                    "Status",
                ]
            },
        },
    }
