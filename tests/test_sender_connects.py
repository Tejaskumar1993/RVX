"""
test cases for sender connects page
"""

from qase.pytest import qase
from conftest import dictionary_parametrize
from data.sender_connects import SenderConnectsParams
from conftest import sender_connects_page


@dictionary_parametrize(
    {
        "Test_1": SenderConnectsParams.Test_1,
    }
)
@qase.title("Verify connects page elements")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all available fields on connects all gifts type tab page",
    ),
)
def test_verify_connects_all_gifts_type_page_elements(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    sender_connects_page,
    available_filter_options,
):
    """
    Regression test for connects all gifts tab page elements verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # # 2. Change user role to deployment admin
    # sender_connects_page.verify_and_change_user_role(select_role=select_role)
    # 3. verify connects tab
    sender_connects_page.verify_connects_tab()
    # 3. Verify all gift type page elements availability
    sender_connects_page.verify_all_gifts_page_elements(
        available_filter_options=available_filter_options,
    )


@dictionary_parametrize(
    {
        "Test_1": SenderConnectsParams.Test_1,
    }
)
@qase.title("Verify connects page elements")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all available fields on connects egifts type tab page",
    ),
)
def test_verify_connects_egifts_type_page_elements(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    sender_connects_page,
    available_filter_options,
):
    """
    Regression test for connects egifts tab page elements verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # # 2. Change user role to deployment admin
    # sender_connects_page.verify_and_change_user_role(select_role=select_role)
    # 3. verify connects tab
    sender_connects_page.verify_connects_tab()
    # 3. Verify egifts page elements availability
    sender_connects_page.verify_egifts_page_elements(
        available_filter_options=available_filter_options,
    )


@dictionary_parametrize(
    {
        "Test_2": SenderConnectsParams.Test_2,
    }
)
@qase.title("Verify and send item via email")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "verify and send item to the user via email",
    ),
)
def test_verify_and_send_item_via_email(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    email_subject,
    sender_connects_page,
    recipient_email,
    item_category_to_select,
    email_message,
):
    """
    Regression test for send item via email
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # # 2. Change user role to deployment admin
    # sender_connects_page.verify_and_change_user_role(select_role=select_role)
    # 3. verify connects tab
    sender_connects_page.verify_connects_tab()
    # 4. Verify send connects via email
    sender_connects_page.verify_and_send_gifts_via_email(
        item_category_to_select=item_category_to_select,
        recipient_email=recipient_email,
        email_subject=email_subject,
        email_message=email_message,
    )


@dictionary_parametrize(
    {
        "Test_3": SenderConnectsParams.Test_3,
    }
)
@qase.title("Verify and send item via shareable link")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify and send item to the user via shareable link",
    ),
)
def test_verify_and_send_item_via_shareable_link(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    sender_connects_page,
    recipient_email,
    item_category_to_select,
):
    """
    Regression test for send item via shareable link
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # # 2. Change user role to deployment admin
    # sender_connects_page.verify_and_change_user_role(select_role=select_role)
    # 3. verify connects tab
    sender_connects_page.verify_connects_tab()
    # 4. Verify send connects via shareable link
    sender_connects_page.verify_and_send_gifts_via_shareable_link(
        item_category_to_select=item_category_to_select,
        recipient_email=recipient_email,
    )


@dictionary_parametrize(
    {
        "Test_4": SenderConnectsParams.Test_4,
    }
)
@qase.title("verify and send item via sms")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "verify and send item to the user via sms",
    ),
)
def test_verify_and_send_item_via_sms(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    sender_connects_page,
    item_category_to_select,
    recipient_phone_number,
    text_message,
    success_message,
):
    """
    Regression test for send item via sms
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # # 2. Change user role to deployment admin
    # sender_connects_page.verify_and_change_user_role(select_role=select_role)
    # 3. verify connects tab
    sender_connects_page.verify_connects_tab()
    # 4. Verify and send connects via sms
    sender_connects_page.verify_and_send_gifts_via_sms(
        item_category_to_select=item_category_to_select,
        recipient_phone_number=recipient_phone_number,
        text_message=text_message,
        success_message=success_message,
    )


@dictionary_parametrize(
    {
        "Test_5": SenderConnectsParams.Test_5,
    }
)
@qase.title("navigate to egifts tab and send item via sms")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Navigate to egifts tab and send item to the user via email",
    ),
)
def test_navigate_to_egifts_tab_and_send_item_via_email(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    sender_connects_page,
    item_category_to_select,
    recipient_email,
    email_subject,
    email_message,
    available_filter_options,
):
    """
    Regression test for navigate to egifts tab send item via sms
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # # 2. Change user role to deployment admin
    # sender_connects_page.verify_and_change_user_role(select_role=select_role)
    # 3. verify connects tab
    sender_connects_page.verify_connects_tab()
    # 4. Verify egifts page elements availability
    sender_connects_page.verify_egifts_page_elements(
        available_filter_options=available_filter_options,
    )
    # 5. Verify and send connects via sms
    sender_connects_page.verify_and_send_gifts_via_email(
        item_category_to_select=item_category_to_select,
        recipient_email=recipient_email,
        email_subject=email_subject,
        email_message=email_message,
    )


@dictionary_parametrize(
    {
        "Test_6": SenderConnectsParams.Test_6,
    }
)
@qase.title("navigate to egifts and send item via shareable link")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Navigate to egifts tab and send item to the user via shareable link",
    ),
)
def test_navigate_to_egifts_tab_and_send_item_via_shareable_link(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    sender_connects_page,
    item_category_to_select,
    recipient_email,
    available_filter_options,
):
    """
    Regression test for navigate to egifts tab and send item via shareable link
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # # 2. Change user role to deployment admin
    # sender_connects_page.verify_and_change_user_role(select_role=select_role)
    # 4. Verify egifts page elements availability
    sender_connects_page.verify_egifts_page_elements(
        available_filter_options=available_filter_options,
    )
    # 5. Verify and send connects via sms
    sender_connects_page.verify_and_send_gifts_via_shareable_link(
        item_category_to_select=item_category_to_select,
        recipient_email=recipient_email,
    )


@dictionary_parametrize(
    {
        "Test_7": SenderConnectsParams.Test_7,
    }
)
@qase.title("navigate to egifts tab and send item via sms")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Navigate to egifts tab and send item to the user via SMS",
    ),
)
def test_navigate_to_egifts_tab_and_send_item_via_sms(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    sender_connects_page,
    item_category_to_select,
    recipient_phone_number,
    text_message,
    success_message,
    available_filter_options,
):
    """
    Regression test for navigate to egifts and tab item via sms
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # # 2. Change user role to deployment admin
    # sender_connects_page.verify_and_change_user_role(select_role=select_role)
    # 4. Verify egifts page elements availability
    sender_connects_page.verify_egifts_page_elements(
        available_filter_options=available_filter_options,
    )
    # 5. Verify and send connects via sms
    sender_connects_page.verify_and_send_gifts_via_sms(
        item_category_to_select=item_category_to_select,
        recipient_phone_number=recipient_phone_number,
        text_message=text_message,
        success_message=success_message,
    )


@dictionary_parametrize(
    {
        "Test_8": SenderConnectsParams.Test_8,
    }
)
@qase.title(
    "Navigate to ontrack d2p tab, verify page elements and send gift with address details"
)
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Navigate to ontrack d2p tab, verify page elements and send gift with known address details",
    ),
)
def test_navigate_to_ontrack_d2p_tab_and_send_gift_on_known_address(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    sender_connects_page,
    item_category_to_select,
    state,
    email_message,
    user_address,
    user_name,
    user_city,
    email_subject,
    zip_code,
    country,
    available_filter_options,
    recipient_email,
):
    """
    Regression test for navigate to ontrack d2p tab, verify page elements and send gift with address details
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # # 2. Change user role to deployment admin
    # sender_connects_page.verify_and_change_user_role(select_role=select_role)
    # 4. Verify egifts page elements availability
    sender_connects_page.verify_ontrack_d2p_page_elements(
        available_filter_options=available_filter_options,
    )
    # 5. Verify and send connects via sms
    sender_connects_page.navigate_to_ontrack_d2p_tab_and_send_a_gift_with_address(
        item_category_to_select=item_category_to_select,
        state=state,
        email_message=email_message,
        user_address=user_address,
        user_name=user_name,
        user_city=user_city,
        email_subject=email_subject,
        zip_code=zip_code,
        country=country,
        recipient_email=recipient_email,
    )


@dictionary_parametrize(
    {
        "Test_9": SenderConnectsParams.Test_9,
    }
)
@qase.title(
    "Navigate to ontrack d2p tab, verify page elements and send gift with unknown address details"
)
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Navigate to ontrack d2p tab, verify page elements and send gift with unknown address details",
    ),
)
def test_navigate_to_ontrack_d2p_tab_and_send_gift_on_unknown_address(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    sender_connects_page,
    item_category_to_select,
    email_message,
    user_name,
    email_subject,
    recipient_email,
    available_filter_options,
):
    """
    Regression test for navigate to ontrack d2p tab, verify page elements and send gift with unknown address details
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # # 2. Change user role to deployment admin
    # sender_connects_page.verify_and_change_user_role(select_role=select_role)
    # 4. Verify egifts page elements availability
    sender_connects_page.verify_ontrack_d2p_page_elements(
        available_filter_options=available_filter_options,
    )
    # 5. Verify and send connects via sms
    sender_connects_page.navigate_to_ontrack_d2p_tab_and_send_a_gift_without_address(
        item_category_to_select=item_category_to_select,
        email_message=email_message,
        user_name=user_name,
        email_subject=email_subject,
        recipient_email=recipient_email,
    )
