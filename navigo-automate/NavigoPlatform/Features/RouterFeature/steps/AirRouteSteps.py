from behave import *
from NavigoPlatform.Configurations.Config import TestConfig
from NavigoPlatform.PageObjects.LoginPage import LoginPage
from NavigoPlatform.PageObjects.AirRoutesPage import AirRoutesPage


@then(u'Click on Create New Route button')
def ClickOnCreateNewBtn(Context):
    try:
        Context.loginPage = LoginPage(Context.driver)
        Context.airRoutePage = AirRoutesPage(Context.driver)
        Context.airRoutePage.ClickOnCreateNewRouteBtn()
        TestConfig.logger.info("Clicked on Create New btn")
    except:
        assert False, "Not able to click on Create New button"


@then(u'Enter all the details of Origin Airport')
def OriginAirportDetails(Context):
    Context.airRoutePage.FillAllOriginDetails()
    TestConfig.logger.info("filling origin Details")


@then(u'Enter all the details of Destination Airport')
def DestinationAirportDetails(Context):
    Context.airRoutePage.Fill_all_destination_details()
    TestConfig.logger.info("filling Destination Details")
    Context.airRoutePage.Enter_Price_Details()
    Context.airRoutePage.click_on_create_air_route_btn()
    TestConfig.logger.info("Created NEw Air Route")
