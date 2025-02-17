"""
test cases for deployment admin Dashboard page
"""

from qase.pytest import qase
from conftest import dictionary_parametrize
from data.system_admin_dashboard import SystemAdminDashboardParams
from conftest import system_admin_dashboard_page


@dictionary_parametrize(
    {
        "Test_1": SystemAdminDashboardParams.Test_1,
    }
)
@qase.title("Verify system admin Dashboard elements")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all fields of system admin Dashboard",
    ),
)
def test_verify_system_admin_dashboard_page_elements(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    system_admin_dashboard_page,
):
    """
    Regression test for items list page fields verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Navigate to System admin page and verify all elements
    system_admin_dashboard_page.verify_all_elements()
