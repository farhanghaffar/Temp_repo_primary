import random
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotVisibleException, TimeoutException, \
    NoSuchElementException, ElementNotInteractableException, InvalidElementStateException, \
    InvalidSelectorException as EX
from NavigoPlatform.Configurations.Config import TestConfig

"""This class is the parent of all the page classes"""
"""It contains all the common action methods and utilities for all the pageObjects"""


class BasePage:

    def __init__(self, Driver):
        self.Driver = Driver

    def WaitTime(self, WaitTime):
        wait.WebDriverWait(self.Driver, WaitTime)

    def ClickOnRandomLocation(self, ByLocator):
        Element = WebDriverWait(self.Driver, 10).until(EC.element_to_be_clickable(ByLocator))
        Element.click()
        # js_code = """
        # var mapElement = document.getElementsByTagName('canvas');
        # var clickEvent = new MouseEvent('click', {
        #     clientX: 30,  // Replace with the desired X coordinate
        #     clientY: 130   // Replace with the desired Y coordinate
        #     });
        #     mapElement[0].dispatchEvent(clickEvent);
        #     """

        # Execute the JavaScript code
        # self.driver.execute_script(js_code)

    def ClickElement(self, ByLocator):
        try:
            Element = WebDriverWait(self.Driver, 10).until(EC.visibility_of_element_located(ByLocator))
            self.Driver.execute_script("arguments[0].click();", Element)
        except EX as e:
            print("Exception! Can't click on the element")

    def Click(self, ByLocator):
        WebDriverWait(self.Driver, 10).until(EC.element_to_be_clickable(ByLocator)).click()

    def InputElement(self, ByLocator, Text):
        try:
            WebDriverWait(self.Driver, 10).until(EC.visibility_of_element_located(ByLocator)).send_keys(Text)
        except EX as e:
            print("Exception! Can't click on the element")

    def GetElementText(self, ByLocator):
        Element = WebDriverWait(self.Driver, 10).until(EC.visibility_of_element_located(ByLocator))
        return Element.text

    def GetText(self, ByLocator, Text):
        Element = WebDriverWait(self.Driver, 10).until(EC.text_to_be_present_in_element(ByLocator, Text))
        return Element

    def GetTitle(self):
        return self.Driver.title

    def GetElementAttribute(self, ByLocator, AttributeName):
        Element = WebDriverWait(self.Driver, 10).until(EC.visibility_of_element_located(ByLocator))
        return Element.get_attribute(AttributeName)

    def VerifyElementDisplayed(self, ByLocator):
        try:
            Element = WebDriverWait(self.Driver, 10).until(EC.visibility_of_element_located(ByLocator))
            return Element.is_displayed()
        except:
            return False

    def SelectCnFromDropDown(self, ByLocator):
        Element = WebDriverWait(self.Driver, 10).until(EC.visibility_of_element_located(ByLocator))
        DropdownElement = Element
        select = Select(DropdownElement)
        print("dropdown selected object", select)
        TestConfig.logger.info(select)
        Options = select.options
        SelectedOption = random.choice(Options)
        SelectedCountry = SelectedOption.text
        select.select_by_visible_text(SelectedCountry)
        print("selected country: ", SelectedCountry)
        TestConfig.logger.info(SelectedCountry)
        return SelectedCountry

    def SelectFromDropDown(self, ByLocator):
        Element = WebDriverWait(self.Driver, 10).until(EC.visibility_of_element_located(ByLocator))
        DropdownElement = Element
        select = Select(DropdownElement)
        TestConfig.logger.info(select)
        options = select.options
        SelectedOption = random.choice(options)
        SelectedChoice = SelectedOption.text
        select.select_by_visible_text(SelectedChoice)
        print("Selected flight model and make: ", SelectedChoice)
        TestConfig.logger.info(SelectedChoice)
        return SelectedChoice

    def UploadFile(self, ByLocator, PathToFile):
        FileUpload = WebDriverWait(self.Driver, 10).until(EC.presence_of_element_located(ByLocator))
        FileUpload.send_keys(PathToFile)

    def GenerateRandomNumber(self):
        # Generate a random 4-digit number
        RandomNumber = random.randint(1000, 9999)
        print(RandomNumber)
        return RandomNumber
