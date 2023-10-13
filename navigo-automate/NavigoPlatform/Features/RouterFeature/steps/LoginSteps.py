import os

from behave import *
from NavigoPlatform.Configurations.Config import TestConfig
from NavigoPlatform.Configurations import Config
from NavigoPlatform.PageObjects.LoginPage import LoginPage
from NavigoPlatform.PageObjects.DashboardPage import DashboardPage


@given(u'Launch the browser')
def LaunchBrowser(context):
    # Config.HeadlessChromeBrowser(context)
    # Config.ChromeBrowser(context)
    # this is the logoic to access whether we want to execute chrome with non-headless or headless by running first
    # By Default it runs in headless and running export HEADLESS=false before behave cmd will run in non-headless mode
    headless_mode = os.environ.get("HEADLESS", "false").lower() == "true"
    Config.ChromeWithParamBrowser(context, headless_mode)


@when(u'Open the router app https://qa2-platform.navigo.global/apps/router/')
def OpenLoginPage(context):
    TestConfig.logger.info("Opening login page")
    context.loginPage = LoginPage(context.driver)


@then(u'The login portal has been opened')
def ValidateLoginPage(Context):
    try:
        Context.loginPage.validateTitle()
        TestConfig.logger.info("Validating the title page")
    except:
        assert False, "Test is failed in validate login page title"


@then(u'Provide valid username and password')
def EnterLoginCreds(Context):
    Context.loginPage.enter_login_credentials()
    TestConfig.logger.info("Login creds are entered")


@then(u'Click on the Login button')
def EnterLogin(Context):
    try:
        Context.loginPage.enter_login()
        TestConfig.logger.info("Login button is clicked")
    except:
        assert False, "Test is failed in enter login"


@then(u'Login is successful and dashboard is opened')
def validate_dashboard_page(context):
    context.DashboardPage = DashboardPage(context.driver)
    context.DashboardPage.Validate_Router_PageLoaded()
    TestConfig.logger.info("Login is successful and dashboard is opened")


@then(u'Provide the username "{User}" and password "{Pwd}"')
def ValidateMultipleLoginCreds(Context, User, Pwd):
    try:
        Context.loginPage.enter_username(User)
        Context.loginPage.enter_password(Pwd)
    except:
        TestConfig.logger.critical("Login is Failed")
        assert False, "Test is failed in validating invalid login"


@then(u'Login is failed and invalid credential error is displayed')
def ValidateInvalidLogin(Context):
    try:
        Context.loginPage.validateInvalidCreds()
    except:
        TestConfig.logger.critical("Login is Failed")
        assert False, "Test is failed in validating invalid login"


@then(u'Provide the password "{Pwd}"')
def EnterLoginCreds(Context, Pwd):
    try:
        Context.loginPage.enter_password(Pwd)
    except:
        assert False, "Test is failed in enter password"


#
# @then(u'Provide the username "{user}"')
# def enter_login_creds(context, user):
#     try:
#         context.loginPage.enter_username(user)
#     except:
#         context.driver.close()
#         assert False, "Test is failed in enter username"
#
#
@then(u'Login is failed and empty username error is displayed')
def validate_empty_username(context):
    try:
        print("well done ")
        context.loginPage.validateEmptyUsername()
    except:
        print("failed ")
        context.driver.close()
        assert False, "Test is failed in validate empty username"
#
#
# @then(u'Login is failed and empty password error is displayed')
# def validate_empty_passeword(context):
#     try:
#         context.loginPage.validateEmptyPassword()
#     except:
#         context.driver.close()
#         assert False, "Test is failed in validate empty password"


@then(u'Close the browser')
def StepImpl(Context):
    Context.driver.close()
