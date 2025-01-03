"""
Parameters for the sender connects page
"""

import random
import string

domains = ["example.com", "testmail.com", "mailinator.com", "randommail.com"]
random_name = "".join(random.choices(string.ascii_lowercase, k=8))
recipient_email = f"{random_name}@{random.choice(domains)}"

# Generate random city
cities = [
    "Toronto",
    "Vancouver",
    "Montreal",
    "Calgary",
    "Edmonton",
    "Ottawa",
    "Winnipeg",
    "Quebec City",
]
random_city = random.choice(cities)

# Generate random Canadian postal code
random_postal_code = (
    random.choice(string.ascii_uppercase)
    + random.choice(string.digits)
    + random.choice(string.ascii_uppercase)
    + " "
    + random.choice(string.digits)
    + random.choice(string.ascii_uppercase)
    + random.choice(string.digits)
)

# Generate random address
street_numbers = range(1, 9999)
street_names = [
    "Maple St",
    "Pine Ave",
    "Main St",
    "Elm Dr",
    "Cedar Rd",
    "Oak Blvd",
    "Birch Ct",
    "Spruce Ln",
]
random_address = f"{random.choice(street_numbers)} {random.choice(street_names)}, {random_city}, Canada"

# Generate random subject
subjects = [
    "Meeting Reminder",
    "Urgent Update Required",
    "Welcome to Our Service",
    "Weekly Newsletter",
    "Action Required",
]
email_subject = random.choice(subjects)
# Generate random phone number
recipient_phone_number = "+1" + "".join(random.choices(string.digits, k=10))

# Generate random text message
messages = [
    "Hello! Your package is on the way.",
    "Reminder: Your appointment is scheduled for tomorrow.",
    "Thank you for choosing our service. Let us know how we did!",
    "Your verification code is 123456.",
    "Your subscription has been successfully renewed.",
]
text_message = random.choice(messages)


class SenderConnectsParams:
    """
    Parameters for the sender connects  page test-cases
    """

    Test_1 = {
        # "role_to_change": "Sender",
        "available_filter_options": [
            "Customer appreciation",
            "Employee appreciation",
            "Luxury",
            "Meeting followup",
            "Door opener",
            "Specialty",
        ],
    }
    Test_2 = {
        # "role_to_change": "Sender",
        "item_category_to_select": "Door opener",
        "recipient_email": recipient_email,
        "email_subject": email_subject,
        "email_message": email_subject,
    }
    Test_3 = {
        # "role_to_change": "Sender",
        "item_category_to_select": "Door opener",
        "recipient_email": recipient_email,
    }
    Test_4 = {
        # "role_to_change": "Sender",
        "item_category_to_select": "Door opener",
        "recipient_phone_number": recipient_phone_number,
        "text_message": text_message,
        "success_message": "Connection Send Via SMS Successfully",
    }
    Test_5 = {
        # "role_to_change": "Sender",
        "item_category_to_select": "Door opener",
        "recipient_email": recipient_email,
        "email_subject": email_subject,
        "email_message": email_subject,
        "available_filter_options": [
            "Customer appreciation",
            "Employee appreciation",
            "Luxury",
            "Meeting followup",
            "Door opener",
            "Specialty",
        ],
    }
    Test_6 = {
        # "role_to_change": "Sender",
        "item_category_to_select": "Door opener",
        "recipient_email": recipient_email,
        "available_filter_options": [
            "Customer appreciation",
            "Employee appreciation",
            "Luxury",
            "Meeting followup",
            "Door opener",
            "Specialty",
        ],
    }
    Test_7 = {
        # "role_to_change": "Sender",
        "item_category_to_select": "Door opener",
        "recipient_phone_number": recipient_phone_number,
        "text_message": text_message,
        "success_message": "Connection Send Via SMS Successfully",
        "available_filter_options": [
            "Customer appreciation",
            "Employee appreciation",
            "Luxury",
            "Meeting followup",
            "Door opener",
            "Specialty",
        ],
    }
    Test_8 = {
        # "role_to_change": "Sender",
        "item_category_to_select": "Meeting followup",
        "state": "Colorado",
        "email_message": text_message,
        "user_address": random_address,
        "user_name": random_name,
        "user_city": random_city,
        "email_subject": email_subject,
        "recipient_email": recipient_email,
        "zip_code": random_postal_code,
        "country": "Canada",
        "available_filter_options": [
            "Customer appreciation",
            "Employee appreciation",
            "Luxury",
            "Meeting followup",
            "Door opener",
            "Specialty",
        ],
    }
    Test_9 = {
        # "role_to_change": "Sender",
        "item_category_to_select": "Meeting followup",
        "email_message": text_message,
        "user_name": random_name,
        "email_subject": email_subject,
        "recipient_email": recipient_email,
        "available_filter_options": [
            "Customer appreciation",
            "Employee appreciation",
            "Luxury",
            "Meeting followup",
            "Door opener",
            "Specialty",
        ],
    }
