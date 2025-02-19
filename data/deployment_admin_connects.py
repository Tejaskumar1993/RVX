import datetime
import random
import string

def generate_random_name(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_random_description(length=20):
    words = [
        "automated", "seamless", "user-friendly", "scalable", "innovative",
        "high-performance", "intuitive", "flexible", "reliable", "secure",
        "real-time", "next-gen", "cloud-based", "adaptive", "enterprise-grade"
    ]
    description = ' '.join(random.choices(words, k=length))
    return description

def generate_random_date(start_date=datetime.datetime.today(), days_range=30):
    random_days = random.randint(0, days_range)
    random_date = start_date + datetime.timedelta(days=random_days)
    return random_date.strftime('%Y-%m-%d')

class DeploymentsConnectsData:
    """
    Contains test data for verifying Deployment Admin Connects Page.
    """
    Test_1 = {
        "side_navigation_item": "Connects",
        "expected_title": "Connects",
        "filter_label": "Filter:",
        "filter_default_value": "all_connects",
        "search_placeholder": "Input Search Text",
        "headers_text": ["Name", "Desc.", "Start Date", "End Date", "Gift Type", "Status", "Actions"],
    }

    Test_2 = {
        "side_navigation_item": "Connects",
        "available_filter_options": [
            "All Connects",
            "Active Connects",
            "Inactive Connects",
            "Custom",
        ],
        "expected_statuses": {
            "All Users": ["Active", "Inactive"],
            "Active Users": ["Active"],
            "Suspended Users": ["Inactive"],
        },
    }

    # Fixing the key: Using "Select_Ontrack_Connect_Type" consistently
    Test_3 = {
        "menu_to_select": "Connects",
        "Select_Ontrack_Connect_Type": "On Track eGift",
        "Internal_Connect_Name": generate_random_name(),
        "Sender_Name": generate_random_name(),
        "Connect_Description": generate_random_description(),
        "Start_Date": generate_random_date(),
        "End_Date": generate_random_date(start_date=datetime.datetime.today() + datetime.timedelta(days=7), days_range=30),
        "Days_expires": "7 Days",
        "Assign_token": "TestName",
        "via_email": "Email",
        "Success_message": "Activate Connect Successfully"
    }

    Test_4 = {
        "menu_to_select": "Connects",
        "Select_Ontrack_Connect_Type": "On Track eGift",
        "Internal_Connect_Name": generate_random_name(),
        "Sender_Name": generate_random_name(),
        "Connect_Description": generate_random_description(),
        "Start_Date": generate_random_date(),
        "End_Date": generate_random_date(start_date=datetime.datetime.today() + datetime.timedelta(days=7), days_range=30),
        "Days_expires": "7 Days",
        "Assign_token": "TestName",
        "via_shareable_link": "Shareable Link",
        "Success_message": "Activate Connect Successfully"
    }

    Test_5 = {
        "menu_to_select": "Connects",
        "Select_Ontrack_Connect_Type": "On Track eGift",
        "Internal_Connect_Name": generate_random_name(),
        "Sender_Name": generate_random_name(),
        "Connect_Description": generate_random_description(),
        "Start_Date": generate_random_date(),
        "End_Date": generate_random_date(start_date=datetime.datetime.today() + datetime.timedelta(days=7), days_range=30),
        "Days_expires": "7 Days",
        "Assign_token": "TestName",
        "via_sms": "SMS",
        "Success_message": "Activate Connect Successfully"
    }

    Test_6 = {
        "menu_to_select": "Connects",
        "Select_Ontrack_Connect_Type": "On Track eGift",
        "Internal_Connect_Name": generate_random_name(),
        "Sender_Name": generate_random_name(),
        "Connect_Description": generate_random_description(),
        "Start_Date": generate_random_date(),
        "End_Date": generate_random_date(start_date=datetime.datetime.today() + datetime.timedelta(days=7), days_range=30),
        "Days_expires": "7 Days",
        "Assign_token": "TestName",
        "via_sender_Choice": "Sender's Choice",
        "Success_message": "Activate Connect Successfully"
    }

    Test_7 = {
        "menu_to_select": "Connects",
        "Select_Ontrack_Connect_Type": "On Track eGift",
        "Custom_Value": f"{random.randint(11, 99)}",
        "Internal_Connect_Name": generate_random_name(),
        "Sender_Name": generate_random_name(),
        "Connect_Description": generate_random_description(),
        "Start_Date": generate_random_date(),
        "End_Date": generate_random_date(start_date=datetime.datetime.today() + datetime.timedelta(days=7), days_range=30),
        "Days_expires": "7 Days",
        "Assign_token": "TestName",
        "Success_message": "Activate Connect Successfully"
    }

    Test_8 = {
        "menu_to_select": "Connects",
        "Select_Ontrack_Connect_Type":"Marketplace",
        "Internal_Connect_Name": generate_random_name(),
        "Sender_Name": generate_random_name(),
        "Connect_Description": generate_random_description(),
        "Start_Date": generate_random_date(),
        "End_Date": generate_random_date(start_date=datetime.datetime.today() + datetime.timedelta(days=7),
                                         days_range=30),
        "Days_expires": "7 Days",
        "Assign_token": "TestName",
        "Success_message": "Activate Connect Successfully"
    }

    Test_9 = {
        "menu_to_select": "Connects",
        "success_message_text": "Edit Connect Successfully"
    }

    Test_10 = {
        "menu_to_select": "Connects",
        "Custom_Value": f"{random.randint(11, 99)}",
        "success_message_text": "Edit Connect Successfully"
    }
