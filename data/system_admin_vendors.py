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
        'All Vendors', 'Activated Vendors', 'Deactivated Vendors', 'Custom'],
        "tab_to_navigate": "Vendors",
        "expected_statuses": {
            "All Vendors": ["Activated","Deactivated"],
            "Activated Vendors": ["Activated"],
            "Deactivated Vendors":["Deactivated"],
        },
    }
    Test_3 = {
        "tab_to_navigate": "Vendors",
        "success_message_text": ["Vendor Active", "Vendor Inactive"],
    }
    Test_4 = {
        "tab_to_navigate": "Vendors",
        "success_message_text": "Vendor Created Successfully",
        "vendor_name": fake.name(),
        "vendor_email": fake.email(),
        "vendor_addressline_1": fake.street_address(),
        "vendor_addressline_2": fake.secondary_address(),
        "vendor_city": fake.city(),
        "state_to_select": "Alabama",
        "zipcode": fake.zipcode(),
        "phone_number": "1234567890",
        "select_vendor": "Tango Card Providor",
        "image_path":"C:\\Playwright\\qa-automation-scripts\\resources\\download.jpg"
    }
    Test_5 = {
        "tab_to_navigate": "Vendors",
        "updated_vendor_message_text": ["Vendor Activated", "Vendor Deactivated"],
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
