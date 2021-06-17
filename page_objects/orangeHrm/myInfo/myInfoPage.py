from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.dataStrings import DataStrings
from locators.locators import Locator
from selenium import webdriver
import time


class LandingPage():

    driver = None
    firstName = None
    lastName = None
    middleName = None
    employeeId = None
    maritalStatus = None
    birthDate = None

    def __init__(self, driver: webdriver):

        self.driver = driver
        self.firstName = self.driver.find_element_by_id(Locator.firstName)
        self.lastName = self.driver.find_element_by_id(Locator.lastName)
        self.middleName = self.driver.find_element_by_id(Locator.middleName)
        self.employeeId = self.driver.find_element_by_id(Locator.employeeId)
        self.maritalStatus = self.driver.find_element_by_id(Locator.maritalStatus)
        self.birthDate = self.driver.find_element_by_id(Locator.birthDate)


    def firstNameValue(self, driver):
        
        print(self.firstName.get_attribute("value"))

    def middleNameValue(self, driver):
        
        print(self.middleName.get_attribute("value"))

    def lastNameValue(self, driver):
        
        print(self.lastName.get_attribute("value"))

    def employeeIdValue(self, driver):
        
        print(self.employeeId.get_attribute("value"))

    def maritalStatusSelected(self, driver):
        
        print(self.maritalStatus.get_attribute("selected")) # treba da poradim jos na ovome

    def birthDateValue(self, driver):
        
        print(self.birthDate.get_attribute("value"))
