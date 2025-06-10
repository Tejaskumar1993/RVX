class DeploymentAdminNotificationSettingsParams:
    """
    Parameters for the system admin notification setting page test-cases
    """

    test_1 = {
        "change_to_notification": "Settings",
        "success_message_text": "Notification updated successfully",
        "deployment_admin_notification": [
            "Select All",
            "Password reset",
            "User created",
            "Order created",
            "Funds depleted",
            "Deposit receipt",
            "Order status updates",
            "New account login",
            "Unclaimed eGift",
            "Automatic refill updated",
            "Automatic refill updated",
        ],
        "select_role": "Deployment Admin",
    }
