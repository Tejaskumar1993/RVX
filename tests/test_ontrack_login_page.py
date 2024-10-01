"""
test cases for login page
"""

from qase.pytest import qase


@qase.title("User should be able see all the required elements on login page")
@qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "User should be able see all the required elements on login page",
    ),
)
def test_login_page_elements(
    environment_to_run,
    ontrack_login_page,
):
    """
    P1 Regression test for login page element verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page(environment_to_run)
