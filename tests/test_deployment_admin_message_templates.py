"""
test cases for deployment admin account balance page
"""

from qase.pytest import qase
from conftest import dictionary_parametrize
from data.deployment_admin_message_templates import (
    DeploymentAdminMessageTemplatesParams,
)
from conftest import deployment_admin_message_templates_page


@dictionary_parametrize(
    {
        "Test_1": DeploymentAdminMessageTemplatesParams.Test_1,
    }
)
@qase.title("Verify email templates page elements")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all available fields on email templates page",
    ),
)
def test_verify_email_templates_page_elements(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_message_templates_page,
    tab_to_navigate,
    templates_data_table_headers,
    available_filter_options,
    select_role,
):
    """
    Regression test for message templates page elements verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_message_templates_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to message templates tab
    deployment_admin_message_templates_page.verify_and_click_on_message_templates_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 3. Verify email templates page elements availability
    deployment_admin_message_templates_page.verify_email_templates_page_elements(
        templates_data_table_headers=templates_data_table_headers,
        available_filter_options=available_filter_options,
    )


@dictionary_parametrize(
    {
        "Test_2": DeploymentAdminMessageTemplatesParams.Test_2,
    }
)
@qase.title("Verify sms templates page elements")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all available fields on sms templates page",
    ),
)
def test_verify_sms_templates_page_elements(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_message_templates_page,
    tab_to_navigate,
    templates_data_table_headers,
    available_filter_options,
    select_role,
    templates_tab_to_change,
):
    """
    Regression test for sms templates page elements verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_message_templates_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to message templates tab
    deployment_admin_message_templates_page.verify_and_click_on_message_templates_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. Verify sms templates page elements availability
    deployment_admin_message_templates_page.verify_sms_templates_page_elements(
        templates_data_table_headers=templates_data_table_headers,
        available_filter_options=available_filter_options,
        tab_to_navigate=templates_tab_to_change,
    )


@dictionary_parametrize(
    {
        "Test_3": DeploymentAdminMessageTemplatesParams.Test_3,
    }
)
@qase.title("Verify d2p templates page elements")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all available fields on d2p templates page",
    ),
)
def test_verify_d2p_templates_page_elements(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    templates_tab_to_change,
    deployment_admin_message_templates_page,
    tab_to_navigate,
    templates_data_table_headers,
    available_filter_options,
    select_role,
):
    """
    Regression test for d2p templates page elements verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_message_templates_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to message templates tab
    deployment_admin_message_templates_page.verify_and_click_on_message_templates_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. Verify d2p templates page elements availability
    deployment_admin_message_templates_page.verify_d2p_templates_page_elements(
        templates_data_table_headers=templates_data_table_headers,
        available_filter_options=available_filter_options,
        tab_to_navigate=templates_tab_to_change,
    )


@dictionary_parametrize(
    {
        "Test_4": DeploymentAdminMessageTemplatesParams.Test_4,
    }
)
@qase.title("Verify email templates filter functionality")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all available filter options and check filtered data",
    ),
)
def test_verify_and_test_email_templates_filter_functionality(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_message_templates_page,
    tab_to_navigate,
    expected_statuses,
    available_filter_options,
    select_role,
):
    """
    Regression test for email templates filter functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_message_templates_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to message templates tab
    deployment_admin_message_templates_page.verify_and_click_on_message_templates_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. verify filter functionality
    deployment_admin_message_templates_page.verify_filter_functionality_of_email_templates(
        available_filter_options=available_filter_options,
        expected_statuses=expected_statuses,
    )


@dictionary_parametrize(
    {
        "Test_5": DeploymentAdminMessageTemplatesParams.Test_5,
    }
)
@qase.title("Verify sms templates filter functionality")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all available filter options and check filtered data",
    ),
)
def test_verify_and_test_sms_templates_filter_functionality(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_message_templates_page,
    tab_to_navigate,
    expected_statuses,
    available_filter_options,
    select_role,
    templates_tab_to_change,
):
    """
    Regression test for sms templates filter functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_message_templates_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to message templates tab
    deployment_admin_message_templates_page.verify_and_click_on_message_templates_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. verify filter functionality
    deployment_admin_message_templates_page.verify_filter_functionality_of_sms_templates(
        available_filter_options=available_filter_options,
        expected_statuses=expected_statuses,
        tab_to_navigate=templates_tab_to_change,
    )


@dictionary_parametrize(
    {
        "Test_6": DeploymentAdminMessageTemplatesParams.Test_6,
    }
)
@qase.title("Verify d2p templates filter functionality")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all available filter options and check filtered data",
    ),
)
def test_verify_and_test_d2p_templates_filter_functionality(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_message_templates_page,
    tab_to_navigate,
    expected_statuses,
    available_filter_options,
    select_role,
    templates_tab_to_change,
):
    """
    Regression test for d2p templates filter functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_message_templates_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to message templates tab
    deployment_admin_message_templates_page.verify_and_click_on_message_templates_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. verify filter functionality
    deployment_admin_message_templates_page.verify_filter_functionality_of_d2p_templates(
        available_filter_options=available_filter_options,
        expected_statuses=expected_statuses,
        tab_to_navigate=templates_tab_to_change,
    )


@dictionary_parametrize(
    {
        "Test_7": DeploymentAdminMessageTemplatesParams.Test_7,
    }
)
@qase.title("Verify email templates search functionality")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify search functionality of email templates ",
    ),
)
def test_verify_and_test_email_templates_search_functionality(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_message_templates_page,
    tab_to_navigate,
    select_role,
):
    """
    Regression test for email templates search functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_message_templates_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to message templates tab
    deployment_admin_message_templates_page.verify_and_click_on_message_templates_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. verify search functionality
    deployment_admin_message_templates_page.verify_search_functionality_of_email_templates()


@dictionary_parametrize(
    {
        "Test_8": DeploymentAdminMessageTemplatesParams.Test_8,
    }
)
@qase.title("Verify sms templates search functionality")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify search functionality of sms templates ",
    ),
)
def test_verify_and_test_sms_templates_search_functionality(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_message_templates_page,
    tab_to_navigate,
    select_role,
    templates_tab_to_change,
):
    """
    Regression test for sms templates search functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_message_templates_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to message templates tab
    deployment_admin_message_templates_page.verify_and_click_on_message_templates_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. verify search functionality
    deployment_admin_message_templates_page.verify_search_functionality_of_sms_templates(
        tab_to_navigate=templates_tab_to_change,
    )


@dictionary_parametrize(
    {
        "Test_9": DeploymentAdminMessageTemplatesParams.Test_9,
    }
)
@qase.title("Verify d2p templates search functionality")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify search functionality of d2p templates ",
    ),
)
def test_verify_and_test_d2p_templates_search_functionality(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_message_templates_page,
    tab_to_navigate,
    select_role,
    templates_tab_to_change,
):
    """
    Regression test for d2p templates search functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_message_templates_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to message templates tab
    deployment_admin_message_templates_page.verify_and_click_on_message_templates_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. verify search functionality
    deployment_admin_message_templates_page.verify_search_functionality_of_d2p_templates(
        tab_to_navigate=templates_tab_to_change,
    )


@dictionary_parametrize(
    {
        "Test_10": DeploymentAdminMessageTemplatesParams.Test_10,
    }
)
@qase.title("Verify create new template functionality of email template")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify create new template functionality",
    ),
)
def test_verify_and_test_email_templates_create_new_template_functionality(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_message_templates_page,
    tab_to_navigate,
    select_role,
    template_name,
    enter_text_in_paragraph,
):
    """
    Regression test for create new template functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_message_templates_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to message templates tab
    deployment_admin_message_templates_page.verify_and_click_on_message_templates_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. verify create new template functionality
    deployment_admin_message_templates_page.verify_create_new_templates_of_email_templates(
        template_name=template_name, enter_text_in_paragraph=enter_text_in_paragraph
    )


@dictionary_parametrize(
    {
        "Test_10": DeploymentAdminMessageTemplatesParams.Test_10,
    }
)
@qase.title("Verify actions(edit, delete) functionality of email templates")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify and perform actions on email templates",
    ),
)
def test_verify_and_test_actions_on_email_templates(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_message_templates_page,
    tab_to_navigate,
    select_role,
    template_name,
    enter_text_in_paragraph,
):
    """
    Regression test for actions of email templates
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_message_templates_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to message templates tab
    deployment_admin_message_templates_page.verify_and_click_on_message_templates_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. verify actions functionality
    deployment_admin_message_templates_page.verify_actions_functionality_of_email_templates(
        template_name, enter_text_in_paragraph
    )


@dictionary_parametrize(
    {
        "Test_11": DeploymentAdminMessageTemplatesParams.Test_11,
    }
)
@qase.title("Verify create new template functionality of d2p template")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify create new template functionality",
    ),
)
def test_verify_and_test_d2p_templates_create_new_template_functionality(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_message_templates_page,
    tab_to_navigate,
    select_role,
    template_name,
    templates_tab_to_change,
    enter_text_in_paragraph,
):
    """
    Regression test for create new template functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_message_templates_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to message templates tab
    deployment_admin_message_templates_page.verify_and_click_on_message_templates_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. verify create new template functionality
    deployment_admin_message_templates_page.verify_create_new_templates_of_d2p_templates(
        template_name=template_name,
        enter_text_in_paragraph=enter_text_in_paragraph,
        tab_to_navigate=templates_tab_to_change,
    )


@dictionary_parametrize(
    {
        "Test_11": DeploymentAdminMessageTemplatesParams.Test_11,
    }
)
@qase.title("Verify actions(edit, delete) functionality of d2p templates")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify and perform actions on d2p templates",
    ),
)
def test_verify_and_test_actions_on_d2p_templates(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_message_templates_page,
    tab_to_navigate,
    select_role,
    template_name,
    templates_tab_to_change,
    enter_text_in_paragraph,
):
    """
    Regression test for actions of d2p templates
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_message_templates_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to message templates tab
    deployment_admin_message_templates_page.verify_and_click_on_message_templates_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. verify actions functionality
    deployment_admin_message_templates_page.verify_actions_functionality_of_d2p_templates(
        template_name=template_name,
        enter_text_in_paragraph=enter_text_in_paragraph,
        tab_to_navigate=templates_tab_to_change,
    )


@dictionary_parametrize(
    {
        "Test_12": DeploymentAdminMessageTemplatesParams.Test_12,
    }
)
@qase.title("Verify create new template functionality of sms template")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify create new template functionality",
    ),
)
def test_verify_and_test_sms_templates_create_new_template_functionality(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_message_templates_page,
    tab_to_navigate,
    select_role,
    template_name,
    templates_tab_to_change,
    enter_text_in_paragraph,
):
    """
    Regression test for create new template functionality
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_message_templates_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to message templates tab
    deployment_admin_message_templates_page.verify_and_click_on_message_templates_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. verify create new template functionality
    deployment_admin_message_templates_page.verify_create_new_templates_of_sms_templates(
        template_name=template_name,
        enter_text_in_paragraph=enter_text_in_paragraph,
        tab_to_navigate=templates_tab_to_change,
    )


@dictionary_parametrize(
    {
        "Test_12": DeploymentAdminMessageTemplatesParams.Test_12,
    }
)
@qase.title("Verify actions(edit, delete) functionality of sms templates")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify and perform actions on d2p templates",
    ),
)
def test_verify_and_test_actions_on_sms_templates(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_message_templates_page,
    tab_to_navigate,
    select_role,
    template_name,
    templates_tab_to_change,
    enter_text_in_paragraph,
):
    """
    Regression test for actions of sms templates
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to deployment admin
    deployment_admin_message_templates_page.verify_and_change_user_role(
        select_role=select_role
    )
    # 3. Navigate to message templates tab
    deployment_admin_message_templates_page.verify_and_click_on_message_templates_tab(
        tab_to_navigate=tab_to_navigate
    )
    # 4. verify actions functionality
    deployment_admin_message_templates_page.verify_actions_functionality_of_sms_templates(
        template_name=template_name,
        enter_text_in_paragraph=enter_text_in_paragraph,
        tab_to_navigate=templates_tab_to_change,
    )
