class SystemAdminNotificationSettingsParams:
    """
    Parameters for the system admin notification setting page test-cases
    """

    test_1 = {
        "change_to_notification": "Notification Settings",
        "success_message_text": "Notification updated successfully",
        "vendor_notification": [
            "Select All",
            "Unacknowledged orders",
            "Unfulfilled orders",
            "Orders created",
        ],
        "sender_notification": [
            "Select All",
            "Password reset",
            "Balance notifications",
            "Order status updates",
            "Unclaimed eGift",
        ],
        "deployment_admin_notification": [
            "Select All",
            "New order created",
            "Automatic funds adjusted",
            "Funds depleted",
            "Automatic refill updated",
            "Deposit receipt",
            "Unacknowledged orders",
        ],
    }
