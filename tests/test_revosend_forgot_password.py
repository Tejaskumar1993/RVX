"""
test cases for login page
"""
from qase.pytest import qase
from conftest import dictionary_parametrize
from data.revosend_forgot_password import ForgotPasswordParams
from conftest import revosend_forgot_password



@qase.title("User should be able to see all available fields on vendors list page")
# @qase.id(2)
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all available fields on vendors list page",
    ),
)
def test_revosend_forgot_password_elements(
        environment_to_run,
        revosend_forgot_password,

   ):
    revosend_forgot_password.open_revosend(environment_to_run)
    revosend_forgot_password.verify_forgot_password_page_elements()


@dictionary_parametrize(
    {
        "Test_1": ForgotPasswordParams.Test_1,
    }
)
@qase.title("User should be able to see all available fields on vendors list page")
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
            "description",
            "Verify all available fields on vendors list page",
    ),
    )
def test_revosend_forgot_password(
        environment_to_run,
        revosend_forgot_password,
        email,
        answer1,
   ):
   revosend_forgot_password.open_revosend(environment_to_run)
   revosend_forgot_password.verify_forgot_password_page_elements()
   revosend_forgot_password.verify_forgot_password_email(
       email=email)
   revosend_forgot_password.verify_forgot_password_questions_form_elements()
   revosend_forgot_password.verify_forgot_password_question_answer(answer1=answer1)







