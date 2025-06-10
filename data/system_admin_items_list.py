"""
Parameters for the system admin items list page
"""


class SystemAdminItemsListParams:
    """
    Parameters for the system admin items list page test-cases
    """

    Test_1 = {
        "tab_to_navigate": "Items List",
        "headers_text": [
            "Thumbnail",
            "ID",
            "Item Name",
            "Category",
            "Vendor Name",
            "Price",
            "Status",
            "Actions"
        ]
    }

    Test_2 = {
        "tab_to_navigate": "Items List",
    }
    Test_3 = {
        "tab_to_navigate": "Items List",
        "available_filter_options": ['All Items','Activated Items', 'On hold by Vendor', 'On hold by Admin', 'Custom'],
        "expected_statuses": {
            "All Items": ["Activated","On hold by Admin"],
            "Activated Items": ["Activated","On hold by Admin"],
            "On hold by Admin":["On hold by Admin"],
        },
    }
    Test_4 = {
        "tab_to_navigate": "Items List",
        "headers_text": [
            "Thumbnail",
            "ID",
            "Item Name",
            "Category",
            "Vendor Name",
            "Price",
            "Status",
            "Actions"],

        "deployments_header": [
            "ID",
            "Deployment Name",
            "Number of Sends",
            "Item Status",
        ],
        "item_price": "12",
        "item_fee": "2",
        "processing_time": "1",
        "item_status": "Active",
        "item_category": "eGift",
        "item_name": "test_item",
        "item_description": "this is test item description",
        "tab_to_change": "Send Orders",
        "deployment_tab": "Deployments",
        "add_item_success_message": "Item added successfully",
    }
    Test_5 = {
        "tab_to_navigate": "Items List",
        "orders_header": [
            "Order Number",
            "Batch ID",
            "Name",
            "Send Time",
            "Current Status",
        ],
        "products_header": ["ID", "Thumbnail", "Name", "Current Orders"],
        "users_header": ["ID", "Name", "username", "phonenumber", "Email"],
    }
