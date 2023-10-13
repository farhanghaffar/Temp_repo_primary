from behave import *
from NavigoPlatform.Configurations.Config import TestConfig
from NavigoPlatform.PageObjects.AirRoutesPage import AirRoutesPage
from NavigoPlatform.PageObjects.LoginPage import LoginPage
from NavigoPlatform.PageObjects.CreateAircraftPage import CreateAirCraftPage


@then(u'Click on Tabs Aircraft and Available Aircraft')
def ClickOnTabAircraftAndAvailableAircraft(Context):
    Context.airCraftPage = CreateAirCraftPage(Context.driver)
    Context.airCraftPage.Click_on_Aircraft_Tab()
    Context.airCraftPage.Click_on_Available_Aircraft_Tab()
    TestConfig.logger.info("Clicked on Tabs Aircraft")


@then(u'Click on Create New Aircraft Btn')
def ClickOnCreateNewAircraftBtn(Context):
    Context.airCraftPage.Click_on_Create_New_Aircraft_Btn()
    TestConfig.logger.info("Clicked on Create New Aircraft Btn")


@then(u'Enter all Aircraft Details')
def FillAircraftData(Context):
    Context.airCraftPage.Fill_aircraft_details()
    TestConfig.logger.info("Filled all the details of the aircraft")


@then(u'Upload Seat Schematics file')
def UploadSeatSchematicsFile(Context):
    Context.airCraftPage.Upload_seat_schematics()
    TestConfig.logger.info("Uploaded the Seat Schematics")


@then(u'Goto Seat Availability Tab and upload Seat which is less than total number of available Seats')
def UploadSeatsFile(Context):
    Context.airCraftPage.Upload_seats()
    TestConfig.logger.info("Uploaded the Seats txt file")


@then(u'Save Aircraft')
def SaveAircraftBtn(Context):
    Context.airCraftPage.Click_on_Save_Aircraft()
    TestConfig.logger.info("Uploaded the Seats txt file")


@then(u'Verify its been Create or not')
def VerifyCreatedAircraft(Context):
    Context.airCraftPage.Verify_Created_aircraft()
    TestConfig.logger.info("Verified that the aircraft has created")

