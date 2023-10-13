from NavigoPlatform.CommonBase.BasePage import BasePage
from selenium.webdriver.common.by import By


class DashboardPage(BasePage):
    TXTRouterDashboard = (By.XPATH, "//*[@id='root']/div[1]/div[1]/div[2]/div[1]/button/span/div/span")

    def __init__(self, driver):
        super().__init__(driver)

    def Validate_Router_PageLoaded(self):
        assert self.GetElementText(self.TXTRouterDashboard) == "Router"
