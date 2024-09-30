def test_add_notice_message(
    ontrack_login_page,
):
    """
    P1 Regression test for login page element verification
    """
    # 1. Navigate to ontrack login page and verify all element of login page
    ontrack_login_page.open_and_verify_ontrack_login_page()

