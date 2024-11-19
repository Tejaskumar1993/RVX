"""
Parameters for the vendor company information page
"""

import random
import string


class VendorCompanyInformationParams:
    """
    Parameters for the vendor company information page test-cases
    """

    # Generate random email
    random_email = f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=8))}@{random.choice(['example.com', 'test.com', 'demo.com'])}"

    test_1 = {
        "tab_to_navigate": "Company Information",
        "select_role": "Vendor",
    }
    test_2 = {
        "tab_to_navigate": "Company Information",
        "select_role": "Vendor",
        "updated_email": random_email,
        "success_message_text": "Updated Company Information Successfully",
    }
