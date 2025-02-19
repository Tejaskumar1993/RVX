import pytest
from qase.pytest import qase
from conftest import dictionary_parametrize
from data.deployment_admin_connects import DeploymentsConnectsData
from conftest import deployment_admin_connects_page


@dictionary_parametrize(
    {
        "Test_1": DeploymentsConnectsData.Test_1,
    }
)
@qase.title("Verify connects page elements")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all available fields on connects page",
    ),
)
def test_verify_connects_page_elements(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_connects_page,
    side_navigation_item,
    expected_title,
    filter_label,
    filter_default_value,
    headers_text,
    search_placeholder,
):
    """
    Regression test for connects page elements verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    # deployment_admin_connects_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=role_to_change
    # )
    # 3. Navigate to connects tab and check Title,filter,search elements

    deployment_admin_connects_page.verify_and_click_on_connects_tab(
        side_navigation_item=side_navigation_item )

    deployment_admin_connects_page.verify_connects_page__connect_table_elements(
        expected_title=expected_title,
        expected_filter_label=filter_label,
        expected_filter_value=filter_default_value,
        expected_search_placeholder=search_placeholder
    )
    # 4. Verify connects page elements availability
    deployment_admin_connects_page.verify_connects_page_elements(
        headers_text = headers_text
    )

@dictionary_parametrize(
    {
        "Test_2": DeploymentsConnectsData.Test_2,
    }
)
@qase.title("Apply filter on connects data and verify filtered data on connects")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Apply filter on connects data and verify filtered data on connects",
    ),
)
def test_apply_filter_on_connects_data(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    #role_to_change,
    deployment_admin_connects_page,
    side_navigation_item,
    available_filter_options,
    expected_statuses,
):
    """
    Regression test for connects filter functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )

    # deployment_admin_connects_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=role_to_change
    # )

    # 3. Navigate to connects tab
    deployment_admin_connects_page.verify_and_click_on_connects_tab(
        side_navigation_item=side_navigation_item
    )

    # 4. Apply filter on connects and verify filtered connects
    deployment_admin_connects_page.apply_filter_on_connects_and_verify_filtered_data(
        available_filter_options=available_filter_options,
        expected_statuses=expected_statuses,
    )

@dictionary_parametrize({
    "Test_3": DeploymentsConnectsData.Test_3})
@qase.title("Verify Connect Creation with E-Gift (Single Item) via email")
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    ("description", "Verify Connect creation with an e-gift single item via email."),
)
def test_send_egift_single_item_via_email(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    #role_to_change,
    menu_to_select,
    Select_Ontrack_Connect_Type,
    Internal_Connect_Name,
    Sender_Name,
    Connect_Description,
    Start_Date,
    End_Date,
    Days_expires,
    Assign_token,
    via_email,
    Success_message,
    deployment_admin_connects_page,
):
    """
       Regression test to verify Connects creation with e-gift (single item).
       """

    # 1. Navigate to OnTrack login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # deployment_admin_connects_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=role_to_change
    # )
    # 2. Navigate to Connects menu
    deployment_admin_connects_page.navigate_to_menu(
        menu_to_select =menu_to_select)

    deployment_admin_connects_page.verify_create_connect_with_e_gift_functionality_via_email(
        Select_Ontrack_Connect_Type= Select_Ontrack_Connect_Type,
        Internal_Connect_Name = Internal_Connect_Name,
        Sender_Name = Sender_Name,
        Connect_Description =Connect_Description,
        Start_Date = Start_Date,
        End_Date = End_Date,
        Days_expires =Days_expires,
        Assign_token =Assign_token,
        via_email=via_email,
        Success_message = Success_message)


@dictionary_parametrize({"Test_4": DeploymentsConnectsData.Test_4})
@qase.title("Verify Connect Creation with E-Gift (Single Item) via Shareable Link")
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    ("description", "Verify Connect creation with an e-gift single item via shareable link."),
)

def test_send_egift_single_item_via_shareable_link(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    menu_to_select,
    Select_Ontrack_Connect_Type,
    Internal_Connect_Name,
    Sender_Name,
    Connect_Description,
    Start_Date,
    End_Date,
    Days_expires,
    Assign_token,
    via_shareable_link,
    Success_message,
    deployment_admin_connects_page,
):
    """
       Regression test to verify Connects creation with e-gift (single item).
       """

    # 1. Navigate to OnTrack login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # deployment_admin_connects_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=role_to_change
    # )
    # 2. Navigate to Connects menu
    deployment_admin_connects_page.navigate_to_menu(
        menu_to_select =menu_to_select)

    deployment_admin_connects_page.verify_create_connect_with_e_gift_functionality_via_shareable_link(
        Select_Ontrack_Connect_Type= Select_Ontrack_Connect_Type,
        Internal_Connect_Name = Internal_Connect_Name,
        Sender_Name = Sender_Name,
        Connect_Description =Connect_Description,
        Start_Date = Start_Date,
        End_Date = End_Date,
        Days_expires =Days_expires,
        Assign_token =Assign_token,
        via_shareable_link=via_shareable_link,
        Success_message = Success_message)


@dictionary_parametrize({
    "Test_5": DeploymentsConnectsData.Test_5})
@qase.title("Verify Connect Creation with E-Gift (Single Item) via shareable sms")
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    ("description", "Verify Connect creation with an e-gift single item via shareable sms."),
)
def test_send_egift_single_item_via_shareable_sms(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    #role_to_change,
    menu_to_select,
    Select_Ontrack_Connect_Type,
    Internal_Connect_Name,
    Sender_Name,
    Connect_Description,
    Start_Date,
    End_Date,
    Days_expires,
    Assign_token,
    via_sms,
    Success_message,
    deployment_admin_connects_page,
):
    """
       Regression test to verify Connects creation with e-gift (single item).
       """

    # 1. Navigate to OnTrack login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # deployment_admin_connects_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=role_to_change
    # )
    # 2. Navigate to Connects menu
    deployment_admin_connects_page.navigate_to_menu(
        menu_to_select =menu_to_select)

    deployment_admin_connects_page.verify_create_connect_with_e_gift_functionality_via_sms(
        Select_Ontrack_Connect_Type= Select_Ontrack_Connect_Type,
        Internal_Connect_Name = Internal_Connect_Name,
        Sender_Name = Sender_Name,
        Connect_Description =Connect_Description,
        Start_Date = Start_Date,
        End_Date = End_Date,
        Days_expires =Days_expires,
        Assign_token =Assign_token,
        via_sms =via_sms,
        Success_message = Success_message)


@dictionary_parametrize({
    "Test_6": DeploymentsConnectsData.Test_6})
@qase.title("Verify Connect Creation with E-Gift (Single Item) via sender choice")
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    ("description", "Verify Connect creation with an e-gift single item via sender choice."),
)
def test_send_egift_single_item_via_sender_choice(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        # role_to_change,
        menu_to_select,
        Select_Ontrack_Connect_Type,
        Internal_Connect_Name,
        Sender_Name,
        Connect_Description,
        Start_Date,
        End_Date,
        Days_expires,
        Assign_token,
        via_sender_Choice,
        Success_message,
        deployment_admin_connects_page,
):
    """
       Regression test to verify Connects creation with e-gift (single item).
       """

    # 1. Navigate to OnTrack login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # deployment_admin_connects_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=role_to_change
    # )
    # 2. Navigate to Connects menu
    deployment_admin_connects_page.navigate_to_menu(
        menu_to_select=menu_to_select)

    deployment_admin_connects_page.verify_create_connect_with_e_gift_functionality_via_Sender_Choice(
        Select_Ontrack_Connect_Type=Select_Ontrack_Connect_Type,
        Internal_Connect_Name=Internal_Connect_Name,
        Sender_Name=Sender_Name,
        Connect_Description=Connect_Description,
        Start_Date=Start_Date,
        End_Date=End_Date,
        Days_expires=Days_expires,
        Assign_token=Assign_token,
        via_sender_Choice =via_sender_Choice,
        Success_message=Success_message)


# @dictionary_parametrize({
#     "Test_3": DeploymentsConnectsData.Test_3})
# @qase.title("Verify Connect Creation with E-Gift (Single Item)")
# @qase.fields(
#     ("severity", "major"),
#     ("priority", "high"),
#     ("description", "Verify Connect creation with an e-gift single item."),
# )
# def test_verify_connects_with_egift_single_item_functionality(
#     environment_to_run,
#     ontrack_username,
#     ontrack_password,
#     ontrack_login_page,
#     #role_to_change,
#     menu_to_select,
#     Select_Ontrack_Connect_Type,
#     Internal_Connect_Name,
#     Sender_Name,
#     Connect_Description,
#     Start_Date,
#     End_Date,
#     Days_expires,
#     Assign_token,
#     Success_message,
#     deployment_admin_connects_page,
# ):
#     """
#        Regression test to verify Connects creation with e-gift (single item).
#        """
#
#     # 1. Navigate to OnTrack login page
#     ontrack_login_page.open_and_verify_ontrack_login_page(
#         environment_to_run, ontrack_username, ontrack_password
#     )
#     # deployment_admin_connects_page.click_on_dropdown_and_change_user_role(
#     #     role_to_change=role_to_change
#     # )
#     # 2. Navigate to Connects menu
#     deployment_admin_connects_page.navigate_to_menu(
#         menu_to_select =menu_to_select)
#
#     deployment_admin_connects_page.verify_create_connect_with_e_gift_functionality(
#         Select_Ontrack_Connect_Type= Select_Ontrack_Connect_Type,
#         Internal_Connect_Name = Internal_Connect_Name,
#         Sender_Name = Sender_Name,
#         Connect_Description =Connect_Description,
#         Start_Date = Start_Date,
#         End_Date = End_Date,
#         Days_expires =Days_expires,
#         Assign_token =Assign_token,
#         Success_message = Success_message)
#
#

@dictionary_parametrize({
    "Test_7": DeploymentsConnectsData.Test_7})
@qase.title("Verify Connect Creation with E-Gift (Range Item)")
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    ("description", "Verify Connect creation with an e-gift range item."),
)
def test_verify_connects_with_egift_range_item_functionality(
        environment_to_run,
        ontrack_username,
        ontrack_password,
        ontrack_login_page,
        #role_to_change,
        menu_to_select,
        Custom_Value,
        Select_Ontrack_Connect_Type,
        Internal_Connect_Name,
        Sender_Name,
        Connect_Description,
        Start_Date,
        End_Date,
        Days_expires,
        Assign_token,
        Success_message,
        deployment_admin_connects_page):
    """
       Regression test to verify Connects creation with e-gift (Range item).
       """

    # 1. Navigate to OnTrack login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # deployment_admin_connects_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=role_to_change
    # )
    # 2. Navigate to Connects menu
    deployment_admin_connects_page.navigate_to_menu(
        menu_to_select=menu_to_select)

    deployment_admin_connects_page.verify_create_connect_with_e_gift_range_item_functionality(
        Select_Ontrack_Connect_Type=Select_Ontrack_Connect_Type,
        Custom_Value = Custom_Value,
        Internal_Connect_Name=Internal_Connect_Name,
        Sender_Name=Sender_Name,
        Connect_Description=Connect_Description,
        Start_Date=Start_Date,
        End_Date=End_Date,
        Days_expires=Days_expires,
        Assign_token=Assign_token,
        Success_message=Success_message)


@dictionary_parametrize({
    "Test_8": DeploymentsConnectsData.Test_8
})
@qase.title("Verify Connect Creation with Direct to Prospect")
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    ("description", "Verify Connect creation using Direct to Prospect functionality."),
)
def test_verify_connects_with_direct_2_prospect_functionality(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    menu_to_select,
    Select_Ontrack_Connect_Type,
    Internal_Connect_Name,
    Sender_Name,
    Connect_Description,
    Start_Date,
    End_Date,
    Days_expires,
    Assign_token,
    Success_message,
    deployment_admin_connects_page,
):
    """
       Regression test to verify Connects creation with Direct to Prospect.
    """

    # 1. Navigate to OnTrack login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )

    # 2. Navigate to Connects menu
    deployment_admin_connects_page.navigate_to_menu(
        menu_to_select=menu_to_select
    )

    deployment_admin_connects_page.verify_create_connect_Direct_2_Prospect_functionality(
        Select_Ontrack_Connect_Type=Select_Ontrack_Connect_Type,
        Internal_Connect_Name=Internal_Connect_Name,
        Sender_Name=Sender_Name,
        Connect_Description=Connect_Description,
        Start_Date=Start_Date,
        End_Date=End_Date,
        Days_expires=Days_expires,
        Assign_token=Assign_token,
        Success_message=Success_message)

@dictionary_parametrize({
    "Test_9": DeploymentsConnectsData.Test_9})
@qase.title("Verify Edit Connect Page Elements - Single Item Add")
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    ("description", "Verify the edit connect page elements when adding a single item."),
)
def test_verify_edit_connect_page_elements_single_item_add(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    menu_to_select,
    success_message_text,
    deployment_admin_connects_page,
):
    """
    Test to verify the edit connect page elements when adding a single item.
    """
    # 1. Navigate to OnTrack login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # deployment_admin_connects_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=role_to_change
    # )
    # 2. Navigate to Connects menu
    deployment_admin_connects_page.navigate_to_menu(menu_to_select=menu_to_select)

    # 3. Verify Edit connect page Element for single item add
    deployment_admin_connects_page.verify_edit_connect_page_elements_single_item_add(
        success_message_text=success_message_text
    )

@dictionary_parametrize({
    "Test_10": DeploymentsConnectsData.Test_10})
@qase.title("Verify Edit Connect Page Elements - Range Item Add")
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    ("description", "Verify the edit connect page elements when adding a range of items."),
)
def test_verify_edit_connect_page_elements_range_item_add(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    menu_to_select,
    Custom_Value,
    success_message_text,
    deployment_admin_connects_page,
    ):
    """
    Test to verify the  edit connect page elements when adding a range of items.
    """
    # 1. Navigate to OnTrack login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # deployment_admin_connects_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=role_to_change
    # )
    # 2. Navigate to Connects menu
    deployment_admin_connects_page.navigate_to_menu(menu_to_select=menu_to_select)

    # 3. Verify Edit connect page Element for range item add
    deployment_admin_connects_page.verify_edit_connect_page_elements_range_item_add(
        Custom_Value=Custom_Value,
        success_message_text=success_message_text)

