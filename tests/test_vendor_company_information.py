"""
test cases for vendor company information page
"""

from qase.pytest import qase
from conftest import dictionary_parametrize
from data.vendor_company_information import VendorCompanyInformationParams
from conftest import vendor_company_information_page


@dictionary_parametrize(
    {
        "Test_1": VendorCompanyInformationParams.test_1,
    }
)
@qase.title("Verify vendor company information page elements")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all available fields on vendor company information page",
    ),
)
def test_verify_vendor_company_information_page_elements(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    vendor_company_information_page,
    tab_to_navigate,
    #select_role,
):
    """
    Regression test for vendor company information page elements verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # # 2. Change user role to vendor
    # vendor_company_information_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=select_role
    # )
    # 3. Navigate to company information tab
    vendor_company_information_page.verify_and_click_on_company_information_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. Verify company information page elements availability
    vendor_company_information_page.verify_company_information_page_elements()


@dictionary_parametrize(
    {
        "Test_2": VendorCompanyInformationParams.test_2,
    }
)
@qase.title("Verify and edit vendor company information ")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify and edit company information",
    ),
)
def test_verify_and_edit_vendor_company_information(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    vendor_company_information_page,
    tab_to_navigate,
    success_message_text,
    #select_role,
    updated_email,
):
    """
    Regression test for edit vendor company information
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role to vendor
    # vendor_company_information_page.click_on_dropdown_and_change_user_role(
    #     role_to_change=select_role
    # )
    # # 3. Navigate to company information tab
    vendor_company_information_page.verify_and_click_on_company_information_tab(
        side_navigation_item=tab_to_navigate
    )
    # 4. Verify edit company information
    vendor_company_information_page.verify_edit_functionality(
        updated_email=updated_email,
        success_message_text=success_message_text,
    )
