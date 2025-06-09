from playwright.sync_api import expect
from qase.pytest import qase
from conftest import dictionary_parametrize
from data.revosend_admin_signup import SystemAdminSignupParams
from pages.revosend_admin_signup_page import SystemAdminSignupPage
from conftest import revosend_signup

@dictionary_parametrize({
    "Test_1": SystemAdminSignupParams.Test_1,
})
@qase.title("Verify system admin signup contact page elements")
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all elements on the system admin signup contact page are visible and functional",
    ),
)
def test_verify_system_admin_signup_contact_page(
    environment_to_run,
    revosend_signup,
    firstname,
    lastname,
    business_name,
    business_address1,
    business_address2,
    city,
    zipcode,
    state,
    image_path,
):
    """
    Regression test for verifying system admin signup contact page elements.
    """
    revosend_signup.open_revosend(environment_to_run)
    revosend_signup.verify_sign_up_contact_page_elements()
    revosend_signup.fill_signup_form(
        firstname=firstname,
        lastname=lastname,
        business_name=business_name,
        business_address1=business_address1,
        business_address2=business_address2,
        city=city,
        zipcode=zipcode,
        state=state,
        image_path=image_path
    )
    #expect(revosend_signup.success_message).to_be_visible(timeout=5000)  # Added assertion

@dictionary_parametrize({
    "Test_Combined": {**SystemAdminSignupParams.Test_1, **SystemAdminSignupParams.Test_2}
})
@qase.title("Verify system admin signup login page elements and form submission")
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all elements on the system admin signup login page and successful form submission",
    ),
)
def test_verify_system_admin_signup_login_page(
    environment_to_run,
    revosend_signup,
    firstname,
    lastname,
    business_name,
    business_address1,
    business_address2,
    city,
    zipcode,
    state,
    image_path,
    username,
    email,
    phone_number,
    password,
):
    """
    Regression test for verifying system admin signup login page elements and form submission.
    """
    revosend_signup.open_revosend(environment_to_run)
    revosend_signup.verify_sign_up_contact_page_elements()
    revosend_signup.fill_signup_form(
        firstname=firstname,
        lastname=lastname,
        business_name=business_name,
        business_address1=business_address1,
        business_address2=business_address2,
        city=city,
        zipcode=zipcode,
        state=state,
        image_path=image_path
    )
    revosend_signup.verify_sign_up_login_page_elements()
    revosend_signup.fill_signup_login_form(
        username=username,
        email=email,
        phone_number=phone_number,
        password=password
    )
    #expect(revosend_signup.success_message).to_be_visible(timeout=5000)  # Added assertion

@dictionary_parametrize({
    "Test_Full": SystemAdminSignupParams.Test_Full
})
@qase.title("Verify system admin signup security questions page elements and form submission")
@qase.fields(
    ("severity", "major"),
    ("priority", "high"),
    (
        "description",
        "Verify all elements on the system admin signup security questions page and successful form submission",
    ),
)
def test_verify_system_admin_signup_security_page(
    environment_to_run,
    revosend_signup,
    firstname,
    lastname,
    business_name,
    business_address1,
    business_address2,
    city,
    zipcode,
    state,
    image_path,
    username,
    email,
    phone_number,
    password,
    answer1,
    answer2,
    answer3,
):
    """
    Regression test for verifying system admin signup security questions page elements and form submission.
    """
    revosend_signup.open_revosend(environment_to_run)
    revosend_signup.verify_sign_up_contact_page_elements()
    revosend_signup.fill_signup_form(
        firstname=firstname,
        lastname=lastname,
        business_name=business_name,
        business_address1=business_address1,
        business_address2=business_address2,
        city=city,
        zipcode=zipcode,
        state=state,
        image_path=image_path
    )
    revosend_signup.verify_sign_up_login_page_elements()
    revosend_signup.fill_signup_login_form(
        username=username,
        email=email,
        phone_number=phone_number,
        password=password
    )
    revosend_signup.verify_sign_up_security_question_page_elements()
    revosend_signup.fill_signup_security_form(
        answer1=answer1,
        answer2=answer2,
        answer3=answer3
    )
    #expect(revosend_signup.success_message).to_be_visible(timeout=5000)  # Added assertion

@qase.title("Verify full system admin signup flow")
@qase.fields(
    ("severity", "critical"),
    ("priority", "high"),
    (
        "description",
        "Verify the complete system admin signup flow from contact to security questions",
    ),
)
@dictionary_parametrize({
    "Test_Full": SystemAdminSignupParams.Test_Full
})
def test_full_system_admin_signup_flow(
    environment_to_run,
    revosend_signup,
    firstname,
    lastname,
    business_name,
    business_address1,
    business_address2,
    city,
    zipcode,
    state,
    image_path,
    username,
    email,
    phone_number,
    password,
    answer1,
    answer2,
    answer3,
):
    """
    Regression test for the complete system admin signup flow.
    """
    revosend_signup.open_revosend(environment_to_run)
    revosend_signup.verify_sign_up_contact_page_elements()
    revosend_signup.fill_signup_form(
        firstname=firstname,
        lastname=lastname,
        business_name=business_name,
        business_address1=business_address1,
        business_address2=business_address2,
        city=city,
        zipcode=zipcode,
        state=state,
        image_path=image_path
    )
    revosend_signup.verify_sign_up_login_page_elements()
    revosend_signup.fill_signup_login_form(
        username=username,
        email=email,
        phone_number=phone_number,
        password=password
    )
    revosend_signup.verify_sign_up_security_question_page_elements()
    revosend_signup.fill_signup_security_form(
        answer1=answer1,
        answer2=answer2,
        answer3=answer3
    )
    expect(revosend_signup.next_button).to_be_visible(timeout=5000)
    revosend_signup.next_button.click()
    expect(revosend_signup.complete_tab).to_be_visible(timeout=5000)
    print("Full signup flow completed successfully")
