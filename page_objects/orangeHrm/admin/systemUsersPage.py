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
    lengthOfTable = None
    names = None

    def __init__(self, driver: webdriver):

        self.driver = driver
        self.lengthOfTable = self.driver.find_elements_by_css_selector(Locator.lengthOfTable)
        self.names = self.driver.find_elements_by_css_selector(Locator.names)

    def countLengthOfTable(self, driver):

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, Locator.lengthOfTable)))
        counter = 0

        for element in self.lengthOfTable:
            counter += 1
        print(counter)

    def printTableNames(self, driver):

        for element in self.names:
            print(element.text)



