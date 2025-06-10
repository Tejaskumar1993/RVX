import random
import string


class VendorProductListParams:
    """
    Parameters for the vendor products List page test-cases
    """
    # Generate product details
    product_name = "Product " + "".join(random.choices(string.ascii_uppercase, k=8))
    product_price = round(random.uniform(10, 500), 2)  # Random price between $10 and $500
    product_shipping_rate = round(random.uniform(5, 50), 2)  # Random shipping rate between $5 and $50
    product_description = " ".join(
        f"{''.join(random.choices(string.ascii_uppercase, k=5))} "
        f"{''.join(random.choices(string.ascii_lowercase, k=4))} "
        f"{''.join(random.choices(string.ascii_lowercase, k=6))}."
        for _ in range(5)
    )
    subjects = [
        "Unable to access account",
        "Payment issue",
        "Feature request",
        "Bug report",
        "Login problem",
        "Shipping delay",
        "Request for refund",
        "Technical support required",
    ]

    # Generate a random description
    description = " ".join(
        f"{''.join(random.choices(string.ascii_uppercase, k=1))}{''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))}"
        for _ in range(random.randint(10, 20))
    ) + "."

    Test_0 ={
        "tab_to_navigate": "Product List"
        }

    # Select a random subject
    subject = random.choice(subjects)
    test_1 = {
        #"select_role": "Vendor",
        "tab_to_navigate": "Product List",
        "headers_text": [[
            "Thumbnail",
            "Name",
            "Status",
            "Actions"]]
    }
    Test_2 = {
        #"select_role": "Vendor",
        "tab_to_navigate": "Product List",
        "available_filter_options": [
            "All Products",
            "Pending Products",
            "Approved Products",
            "Declined Products",
        ],
        "expected_statuses": {
            "All Products": ["Approved","On Hold By Admin"],
            "Pending Products": ["Pending"],
            "Approved Products": ["Approved","On Hold By Admin"],
            "Declined Products": ["Declined"],
        },
    }
    Test_3 = {
        #"select_role": "Vendor",
        "tab_to_navigate": "Product List",
        "product_name": product_name,
        "category":"Customer appreciation",
        "product_price": str(product_price),
        "product_type":"eGift",
        "product_shipping_rate": str(product_shipping_rate),
        "description": product_description,
        "image_path": 'resources/download.jpg',
        "success_message_text": "Product Request is sent"
    }
    Test_4 = {
        #"select_role": "Vendor",
        "tab_to_navigate": "Product List",
        "request_description": description,
        "request_subject": subject,
        "success_message_text": "Your request for support from the system administrators has been sent successfully"
    }
    Test_5 = {
        #"select_role": "Vendor",
        "tab_to_navigate": "Product List",
    }

    Test_6 = {
        #"tab_to_navigate": "Product List",
        "available_filter_options": [
            "Approved Products",
        ],
        "expected_statuses": {
            "Approved Products": ["Approved", "On Hold By Admin"],},
        "product_name": product_name,
        "category": "Customer appreciation",
        "product_price": str(product_price),
        "product_shipping_rate": str(product_shipping_rate),
        "description": product_description,
        "image_path": 'resources/download.jpg',
        "success_message_text": "Product Request is sent"
    }

    Test_7 = {
        "tab_to_navigate": "Product List",
        "available_filter_options": [
            "Approved Products",
        ],
        "expected_statuses": {
            "Approved Products": ["Approved", "On Hold By Admin"], },
    }

    Test_8 = {"tab_to_navigate": "Product List",
        "available_filter_options": [
            "Pending Products",
            "Declined Products"],
              "expected_statuses": {
                  "Pending Products": ["Pending"],
                  "Declined Products": ["Declined"],
              },
              "success_message_text": "Product Deleted Successfully"
            }

