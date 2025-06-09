import string
import random
import os
from faker import Faker

faker = Faker()

def generate_password(length=10):
    """Generate a random password with at least one uppercase, lowercase, digit, and special character"""
    characters = string.ascii_letters + string.digits + "!@#$"
    password = (
        random.choice(string.ascii_uppercase) +
        random.choice(string.ascii_lowercase) +
        random.choice(string.digits) +
        random.choice("!@#$") +
        ''.join(random.choice(characters) for _ in range(length - 4))
    )
    return ''.join(random.sample(password, len(password)))  # Shuffle for randomness

class SystemAdminSignupParams:
    """
    Parameters for the deployment admin send order list page test-cases
    """
    # Base directory for resources
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    IMAGE_PATH = os.path.join(BASE_DIR, "resources", "download.jpg")

    Test_1 = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "business_name": faker.company(),
        "business_address1": faker.street_address(),
        "business_address2": faker.secondary_address(),
        "city": faker.city(),
        "state": "Alaska",
        "zipcode": faker.zipcode(),
        "image_path": r"C:\Playwright\qa-automation-scripts\resources\download.jpg"
    }

    Test_2 = {
        "username": faker.user_name(),
        "email": faker.email(),
        "phone_number": faker.phone_number(),
        "password": generate_password(),
    }

    Test_3 = {
        "answer1": "Test",
        "answer2": "Test",
        "answer3": "Test",
    }

    # Combined data for full flow
    Test_Full = {**Test_1, **Test_2, **Test_3}