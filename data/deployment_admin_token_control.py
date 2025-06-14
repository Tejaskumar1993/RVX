"""
Parameters for the deployment admin token control page
"""
import random
import string

bucket_description = "".join(
    random.choices(string.ascii_letters + string.digits + " ", k=20)
).strip()
bucket_name = "".join(random.choices(string.ascii_letters + string.digits, k=10))


class DeploymentAdminTokenControlParams:
    """
    Parameters for the deployment admin token control page test-cases
    """

    Test_1 = {
        "tab_to_navigate": "Token Control",
        "token_bucket_table_headers": [
            "Bucket Id",
            "Buckets",
            "Token",
            "Token Limit",
            "Status",
            "Actions",
        ],
        "available_filter_options": [
            'All Buckets','Activated Buckets','Deactivated Buckets','Custom'
        ],

        "select_role": "Deployment Admin",
    }

    Test_2 = {
        "tab_to_navigate": "Token Control",
        "available_filter_options": [
            'All Buckets', 'Activated Buckets', 'Deactivated Buckets', 'Custom'
        ],
        "expected_statuses": {
            "All Buckets": ["Activated", "Deactivated"],
            "Activated Buckets": ["Activated"],
            "Deactivated Buckets": ["Deactivated"],
        },
    }
    Test_3 = {
        "tab_to_navigate": "Token Control",
        #"select_role": "Deployment Admin",
        "enable_message_text": "Token Controls Enabled  Successfully",
        "disable_message_text":"Token Controls Disabled Successfully",
    }
    Test_4 = {
        "tab_to_navigate": "Token Control",
        "select_role": "Deployment Admin",
        "tokens_count": "3",
        "max_token": "2",
        "total_limit": "4",
        "bucket_description": bucket_description,
        "bucket_name": bucket_name,
        "new_description": "this is test description",
    }
