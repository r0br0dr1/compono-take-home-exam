from behave import given, when, then
from POM.login_page import LoginPage
from POM.upload_cv_page import UploadCVPage
from POM.delete_details import SkillsExperienceHandler

import time
import allure

@given("the upload cv is available on the webpage")
def step_given_upload_cv_available(context):
    context.driver.get("https://candidate-qa-test.dev.platform.compono.dev/")
    context.login_page = LoginPage(context.driver)
    context.upload_page = UploadCVPage(context.driver)
    context.delete_details = SkillsExperienceHandler(context.driver)
    # context.login_page.login("yacesa3246@degcos.com", "Temp0rary")
    context.login_page.login("xiwera3361@ofionk.com", "Temp0rary")
    time.sleep(3)
    context.delete_details.handle_deletions()

@when("I upload a CV")
def step_when_upload_cv(context):
    context.upload_page.click_upload_cv_if_available()
    context.upload_page.upload_file(context.upload_folder)

@then("CV is uploaded successfully and data is captured")
def step_then_cv_uploaded_successfully(context):
    context.upload_page.wait_for_upload_success()
    context.upload_page.close_overlay()
    assert context.delete_details.check_experience_skills_is_filled
    with allure.step('CV is uploaded successfully and data is captured'):
        pass