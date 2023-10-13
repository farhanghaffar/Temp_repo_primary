import time
# from NavigoPlatform.PageObjects.BasePage import BasePage

from NavigoPlatform.CommonBase.BasePage import BasePage

from selenium.webdriver.common.by import By
from NavigoPlatform.CommonBase.BasePage import BasePage


class AirRoutesPage(BasePage):
    LOCCreateNewRouteBtn = (By.XPATH, "//span[text()='Create New Route']")
    LOCOriginCNDropDown = (By.XPATH, "(//select[contains(@class,'text-sm w-full')])[1]")
    LOCOriginAirportName = (By.ID, "origin_airport_name")
    LOCOriginAirportCode = (By.ID, "origin_airport_code")
    LOCOriginAirportMapPoint = (By.XPATH, "//*[@id='DestinationFormMap']/div[2]/canvas[1]")
    LOCOriginAirportCoordinates = (By.ID, "origin_airport_coorinates")
    LOCOriginAirportStartTime = (By.ID, "origin_time")
    LOCStartTimeZone = (By.XPATH, "//div[contains(@class,'px-2 py-[6px]')]//select)[2]")
    LOCStartNextBtn = (By.XPATH, "//span[text()='Next']")

    LOCDestCnDropDown = (
        By.XPATH, "//*[@id='navigo.modal']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/select[1]")
    LOCDestAirportName = (By.ID, "destination_airport_name")
    LOCDestAirportCode = (By.ID, "destination_airport_code")
    LOCDestAirportCoordinates = (By.ID, "destination_airport_coorinates")
    LOCDestAirportEndTime = (By.ID, "destination_time")
    LOCDestEndTimeZone = (
        By.XPATH, "//*[@id='navigo.modal']/div[1]/div[2]/div[1]/div[2]/div[1]/div[6]/div[1]/select[1]")
    LOCDestNextBtn = (By.XPATH, "//span[text()='Next']")

    LOCPriceText = (By.ID, "cost")
    LOCCreateAirRouteBtn = (By.XPATH, "//*[@id='navigo.modal']/div/div[2]/div/div[3]/button[2]/span")

    LOCVerifyRoute = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[2]/div/div[1]/table/tbody/tr[1]/td[8]")

    def __init__(self, driver):
        super().__init__(driver)

    def ClickOnCreateNewRouteBtn(self):
        self.ClickElement(self.LOCCreateNewRouteBtn)

    def FillAllOriginDetails(self):
        origin_cn_name = self.SelectCnFromDropDown(self.LOCOriginCNDropDown)
        self.InputElement(self.LOCOriginAirportName, f'{origin_cn_name}+automation')
        self.InputElement(self.LOCOriginAirportCode, f'{origin_cn_name}+auto123')
        time.sleep(5)
        self.ClickOnRandomLocation(self.LOCOriginAirportMapPoint)
        self.InputElement(self.LOCOriginAirportStartTime, "14:30 PM")
        self.ClickElement(self.LOCStartNextBtn)

    def Fill_all_destination_details(self):
        dest_cn_name = self.SelectCnFromDropDown(self.LOCDestCnDropDown)
        self.InputElement(self.LOCDestAirportName, f'{dest_cn_name}+automation')
        self.InputElement(self.LOCDestAirportCode, f'{dest_cn_name}+auto789')
        time.sleep(5)
        self.ClickOnRandomLocation(self.LOCOriginAirportMapPoint)
        self.InputElement(self.LOCDestAirportEndTime, "19:30 PM")
        self.ClickElement(self.LOCDestNextBtn)

    def Enter_Price_Details(self):
        time.sleep(5)
        self.InputElement(self.LOCPriceText, "2222")

    def click_on_create_air_route_btn(self):
        self.InputElement(self.LOCCreateAirRouteBtn)
