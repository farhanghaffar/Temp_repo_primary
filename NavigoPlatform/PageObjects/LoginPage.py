from NavigoPlatform.CommonBase.BasePage import BasePage
from selenium.webdriver.common.by import By
from NavigoPlatform.Configurations.Config import TestConfig


class LoginPage(BasePage):
    LocTxtUsername = (By.ID, "username")
    LocTxtPassword = (By.ID, "password")
    LocBtnLogin = (By.ID, "kc-login")
    LocMsgInvalidCreds = (By.CLASS_NAME, "kc-feedback-text")
    user = TestConfig.USERNAME
    pwd = TestConfig.PASSWORD

    def __init__(self, driver):
        super().__init__(driver)

    def enter_login_credentials(self):
        self.InputElement(self.LocTxtUsername, LoginPage.user)
        self.InputElement(self.LocTxtPassword, LoginPage.pwd)

    def enter_username(self, user):
        self.InputElement(self.LocTxtUsername, user)

    def enter_password(self, pwd):
        self.InputElement(self.LocTxtPassword, pwd)

    def enter_login(self):
        self.ClickElement(self.LocBtnLogin)

    def validateTitle(self):
        assert self.GetTitle() == "Navigo Platform"

    def validateInvalidCreds(self):
        assert self.GetElementText(self.LocMsgInvalidCreds) == "Invalid username or password."

    def validateEmptyUsername(self):
        assert self.GetElementText(self.LocMsgInvalidCreds) == "Invalid username or password."
    #
    # def validateEmptyPassword(self):
    #     assert self.get_element_text(self.MSG_INVALIDCREDS) == "Password cannot be empty"
