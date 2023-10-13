from NavigoPlatform.CommonBase.BasePage import BasePage
from selenium.webdriver.common.by import By


class CreateAirCraftPage(BasePage):
    LOCAircraftTab = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[1]/div[3]")
    LOCAvailableAircraftTab = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[2]/div/div/div[1]/div[2]")
    LOCCreateNewAircraftBtn = (
        By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/button")
    LOCAircraftMake = (By.ID, "make")
    LOCAircraftModel = (By.ID, "model")
    LOCAircraftTitle = (By.ID, "title")
    LOCAircraftTail = (By.ID, "tail_number")
    LOCAircraftWeight = (By.ID, "weight")
    LOCAircraftLength = (By.ID, "length")
    LOCAircraftSeatsTotal = (By.ID, "seats_total")
    LOCAircraftNumberOfEngines = (By.ID, "number_of_engines")
    LOCAircraftEngineType = (By.ID, "engine_type")
    LOCAircraftMaxSpeed = (By.ID, "max_speed")
    LOCAircraftMaxPayload = (By.ID, "maximum_payload")
    LOCAirSchematicsBrowseFiles = (By.ID, "file-input")
    LOCSeatAvailabiltyTab = (By.XPATH, "//*[@id='navigo.modal']/div/div[2]/div/div[1]/div[2]")
    LOCBrowseSeatSelection = (By.ID, "file-input")
    LOCSaveAircraftBtn = (By.XPATH, "//*[@id='navigo.modal']/div/div[3]/div[2]/button/span")
    LOCVerifyAircraftName = (By.XPATH, "//*[@id='root']/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[1]/span")
    #LOCVerifyAircraftName = (By.XPATH, "(//td[contains(@class,'px-3 py-3')]//span)[1]")
    #LOCVerifyAircraftName = (By.XPATH, "(//span[contains(@class,'text-font font-roboto')])[2]")

    Aircraft_title_name = " "

    def __init__(self, driver):
        super().__init__(driver)

    def Click_on_Aircraft_Tab(self):
        self.ClickElement(self.LOCAircraftTab)

    def Click_on_Available_Aircraft_Tab(self):
        self.ClickElement(self.LOCAvailableAircraftTab)

    def Click_on_Create_New_Aircraft_Btn(self):
        self.ClickElement(self.LOCCreateNewAircraftBtn)

    def Fill_aircraft_details(self):
        selected_aircraft_make = self.SelectFromDropDown(self.LOCAircraftMake)
        selected_aircraft_model = self.SelectFromDropDown(self.LOCAircraftModel)
        CreateAirCraftPage.Aircraft_title_name = f'{selected_aircraft_make}+{selected_aircraft_model}+automode'
        print(f'{CreateAirCraftPage.Aircraft_title_name}')
        self.InputElement(self.LOCAircraftTitle, f'{CreateAirCraftPage.Aircraft_title_name}')
        tail_number = self.GenerateRandomNumber()
        self.InputElement(self.LOCAircraftTail, tail_number)
        self.InputElement(self.LOCAircraftWeight, "88888")
        self.InputElement(self.LOCAircraftLength, "66666")
        self.InputElement(self.LOCAircraftSeatsTotal, "450")
        self.InputElement(self.LOCAircraftNumberOfEngines, "4")
        self.InputElement(self.LOCAircraftEngineType, "automode dual type")
        self.InputElement(self.LOCAircraftMaxSpeed, "555")
        #self.InputElement(self.LOCAircraftMaxPayload, "999999")

    def Upload_seat_schematics(self):
        path_to_file = '/Users/harshithkumar/navigo-automate/NavigoPlatform/TestData/Seat_schematics.png'
        self.UploadFile(self.LOCAirSchematicsBrowseFiles, path_to_file)

    def Upload_seats(self):
        path_to_file = '/Users/harshithkumar/navigo-automate/NavigoPlatform/TestData/75_seats.txt'
        self.ClickElement(self.LOCSeatAvailabiltyTab)
        self.UploadFile(self.LOCBrowseSeatSelection, path_to_file)

    def Click_on_Save_Aircraft(self):
        self.ClickElement(self.LOCSaveAircraftBtn)

    def Verify_Created_aircraft(self):
        if self.GetText(self.LOCVerifyAircraftName, CreateAirCraftPage.Aircraft_title_name):
            expected_aircraft_name = self.GetElementText(self.LOCVerifyAircraftName)
            print("Created this aircraft: ", CreateAirCraftPage.Aircraft_title_name)
            print("Verifying this aircraft: ", expected_aircraft_name)
            assert expected_aircraft_name == CreateAirCraftPage.Aircraft_title_name
        else:
            print(f'Created {CreateAirCraftPage.Aircraft_title_name} is not present')
