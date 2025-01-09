"""
test cases for deployment admin Dashboard page
"""

from qase.pytest import qase
from conftest import dictionary_parametrize
from data.deployment_admin_dashboard import DeploymentAdminDashboardParams
from conftest import deployment_admin_dashboard_page


@dictionary_parametrize(
    {
        "Test_1": DeploymentAdminDashboardParams.Test_1,
    }
)
@qase.title("Verify deployment admin Dashboard elements")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all fields of deployment admin Dashboard",
    ),
)
def test_verify_dashboard_page_elements(
    environment_to_run,
    ontrack_username,
    ontrack_password,
    ontrack_login_page,
    deployment_admin_dashboard_page,
    role_to_change,
    user_data_table_headers,
    item_data_table_headers,
    newest_sends_data_table_headers,
):
    """
    Regression test for items list page fields verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(
        environment_to_run, ontrack_username, ontrack_password
    )
    # 2. Change user role
    deployment_admin_dashboard_page.click_on_dropdown_and_change_user_role(
        role_to_change=role_to_change
    )
    # 3. Click and Verify items list tab
    deployment_admin_dashboard_page.verify_dashboard_tab()
    # 4. Verify daily updated chart
    deployment_admin_dashboard_page.verify_visual_graphs_component()
    # 5. Very user summary
    deployment_admin_dashboard_page.verify_order_summary_component(
        user_data_table_headers=user_data_table_headers,
        item_data_table_headers=item_data_table_headers,
        newest_sends_data_table_headers=newest_sends_data_table_headers,
    )
    # 6. send statistics data
    deployment_admin_dashboard_page.verify_send_statistic_component()
    # 7. User statistics data
    deployment_admin_dashboard_page.verify_user_statistics_component()
