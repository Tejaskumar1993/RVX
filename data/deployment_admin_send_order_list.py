"""
Parameters for the deployment admin send order list page
"""


class DeploymentAdminSendOrderListParams:
    """
    Parameters for the deployment admin send order list page test-cases
    """

    Test_1 = {
        #"role_to_change": "Deployment Admin",
        "tab_to_navigate": "Send Order List",
        "headers_text": [
            'Thumbnail', 'ID', 'Sent To', 'Date Created', 'Date Sent', 'Status',
        ],
        "prospact_header":['Send Id','Send Name','Date Sent','Status']
    }
    Test_2 = {
        #"role_to_change": "Deployment Admin",
        "tab_to_navigate": "Send Order List",
        "available_filter_options": [
            ['All Orders', 'Created Orders', 'Acknowledged Orders', 'Processing Orders', 'Shipped Orders',
             'Completed Orders', 'Deleted Orders', 'Cancelled Orders', 'Custom'],],
            "expected_statuses": {
            "All Users": ["Created", "Shipped", "Processing", "Acknowledged"],
            "Created Orders": ["Created"],
            "Acknowledged Orders": ["Acknowledged"],
            "Processing Orders" : ["Processing"],
            "Shipped Orders": ["Shipped"],
            "Completed Orders": ["Completed"],
            "Deleted Orders":["Deleted"],
            "Cancelled Orders":["Cancelled"],
            "Custom":["Created"]
        }
    }
