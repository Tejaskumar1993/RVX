"""
Parameters for the deployment admin message templates page
"""


class DeploymentAdminMessageTemplatesParams:
    """
    Parameters for the deployment admin message templates page test-cases
    """

    Test_1 = {
        "tab_to_navigate": "Message Templates",
        "templates_data_table_headers": ["Name", "Visibility", "Actions"],
        "available_filter_options": [
            "All Templates",
            "Public Templates",
            "Private Templates",
        ],
        "select_role": "Deployment Admin",
    }
    Test_2 = {
        "tab_to_navigate": "Message Templates",
        "templates_data_table_headers": ["Name", "Visibility", "Actions"],
        "available_filter_options": [
            "All Templates",
            "Public Templates",
            "Private Templates",
        ],
        "select_role": "Deployment Admin",
        "templates_tab_to_change": "SMS Templates",
    }
    Test_3 = {
        "tab_to_navigate": "Message Templates",
        "templates_data_table_headers": ["Name", "Visibility", "Actions"],
        "available_filter_options": [
            "All Templates",
            "Public Templates",
            "Private Templates",
        ],
        "select_role": "Deployment Admin",
        "templates_tab_to_change": "D2P Templates",
    }
    Test_4 = {
        "tab_to_navigate": "Message Templates",
        "available_filter_options": [
            "All Templates",
            "Public Templates",
            "Private Templates",
        ],
        "select_role": "Deployment Admin",
        "expected_statuses": {
            "All Templates": ["Public", "Private"],
            "Public Templates": ["Public"],
            "Private Templates": ["Private"],
        },
    }
    Test_5 = {
        "tab_to_navigate": "Message Templates",
        "available_filter_options": [
            "All Templates",
            "Public Templates",
            "Private Templates",
        ],
        "select_role": "Deployment Admin",
        "expected_statuses": {
            "All Templates": ["Public", "Private"],
            "Public Templates": ["Public"],
            "Private Templates": ["Private"],
        },
        "templates_tab_to_change": "SMS Templates",
    }
    Test_6 = {
        "tab_to_navigate": "Message Templates",
        "available_filter_options": [
            "All Templates",
            "Public Templates",
            "Private Templates",
        ],
        "select_role": "Deployment Admin",
        "expected_statuses": {
            "All Templates": ["Public", "Private"],
            "Public Templates": ["Public"],
            "Private Templates": ["Private"],
        },
        "templates_tab_to_change": "D2P Templates",
    }
    Test_7 = {
        "tab_to_navigate": "Message Templates",
        "select_role": "Deployment Admin",
    }
    Test_8 = {
        "tab_to_navigate": "Message Templates",
        "select_role": "Deployment Admin",
        "templates_tab_to_change": "SMS Templates",
    }
    Test_9 = {
        "tab_to_navigate": "Message Templates",
        "select_role": "Deployment Admin",
        "templates_tab_to_change": "D2P Templates",
    }
    Test_10 = {
        "tab_to_navigate": "Message Templates",
        #"select_role": "Deployment Admin",
        "template_name": "Test33",
        "enter_text_in_paragraph": "this is test template description",
    }
    Test_11 = {
        "tab_to_navigate": "Message Templates",
        "select_role": "Deployment Admin",
        "template_name": "test template",
        "enter_text_in_paragraph": "this is test template description",
        "templates_tab_to_change": "D2P Templates",
    }
    Test_12 = {
        "tab_to_navigate": "Message Templates",
        "select_role": "Deployment Admin",
        "template_name": "test template",
        "enter_text_in_paragraph": "this is test template description",
        "templates_tab_to_change": "SMS Templates",
    }
