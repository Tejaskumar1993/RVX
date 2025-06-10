class VendorOrdersListParams:
    """
    Parameters for the vendor Orders List page test-cases
    """

    test_1 = {
        #"select_role": "Vendor",
        "tab_to_navigate": "Orders List",
        "users_table_headers": ['Order Number', 'Order Date', 'Item Name', 'Current Status', 'Actions']
    }

    Test_2 = {
        "tab_to_navigate": "Orders List",
        "available_filter_options": [
            "All Orders",
            "Created Orders",
            "Acknowledged Orders",
            "Processing Orders",
            "Shipped Orders",
            "Completed Orders",
            "Deleted Orders",
            "Cancelled Orders",
            "Custom",
        ],
        "expected_statuses": {
            "All Orders": ["Canceled","Shipped","Processing"],
            "Created Orders": ["Created"],
            "Acknowledged Orders": ["Acknowledged"],
            "Processing Orders": ["Processing"],
            "Shipped Orders": ["Shipped"],
            "Completed Orders":["Completed"],
            "Cancelled Orders":["Canceled"],
            "Custom" :["Processing","Shipped","Canceled","Shipped"]
        },
    }

