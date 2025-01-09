"""
Parameters for the system admin Vendors page
"""

from faker import Faker
import random

# Initialize the Faker instance
fake = Faker()


class SystemAdminVendorsParams:
    """
    Parameters for the system admin vendors list page test-cases
    """

    Test_1 = {
        "tab_to_navigate": "Vendors",
        "headers_text": ["Logo", "ID", "Name", "Address", "Phone", "Status", "Actions"],
    }
    Test_2 = {
        "available_filter_options": [
            "All Vendors",
            "Active Vendors",
            "Suspended Vendors",
            "Custom",
        ],
        "tab_to_navigate": "Vendors",
        "expected_statuses": {
            "All Users": ["Active", "Inactive"],
            "Active Users": ["Active"],
            "Suspended Users": ["Inactive"],
        },
    }
    Test_3 = {
        "tab_to_navigate": "Vendors",
        "success_message_text": ["Vendor Active", "Vendor Inactive"],
    }
    Test_4 = {
        "tab_to_navigate": "Vendors",
        "success_message_text": "Vendor Created Successfully",
        "vendor_name": fake.company(),
        "vendor_email": fake.email(),
        "vendor_addressline_1": fake.street_address(),
        "vendor_addressline_2": fake.secondary_address(),
        "vendor_city": fake.city(),
        "state_to_select": "Alabama",
        "zipcode": fake.zipcode(),
        "phone_number": fake.phone_number(),
        "select_vendor": "AlexDoe",
    }
    Test_5 = {
        "tab_to_navigate": "Vendors",
        "updated_vendor_message_text": ["Vendor Active", "Vendor Inactive"],
    }
    Test_6 = {
        "tab_to_navigate": "Vendors",
        "orders_headers_text": [
            "Order Number",
            "Batch ID",
            "Name",
            "Send Time",
            "Current Status",
        ],
        "products_headers_text": ["ID", "Thumbnail", "Name", "Current Orders"],
        "users_headers_text": ["ID", "Name", "username", "phonenumber", "Email"],
    }
