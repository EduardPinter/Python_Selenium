import time
from selenium.common.exceptions import NoSuchElementException
from page_objects.dynamicProp.test_Run import TestBase
from data.dataStrings import DataStrings
from locators.locators import Locator
from selenium import webdriver

class DynamicPropPage():
    driver: webdriver = None
    randomText = None
    visibleAfter = None
    enableButton = None
    colorChange = None

    def __init__(self, driver: webdriver):

        self.driver = driver
        self.randomText = driver.find_element_by_xpath(Locator.randomTextId1)
        self.visibleAfter = driver.find_element_by_id(Locator.visibleAfter)
        self.enableButton = driver.find_element_by_id(Locator.enableButton)
        self.colorChange = driver.find_element_by_id(Locator.colorChange)

    def assertRandomText(self, driver):

        assert self.randomText.text == DataStrings.randomTextId

        return TestBase(self, driver)

    def visibleAfterException(self, driver):

        try:

            self.visibleAfter

        except NoSuchElementException:
            pass

        return TestBase(self,driver)

    def enableButtonFalse(self, driver):

        assert self.enableButton.is_enabled() == False

        return TestBase(self,driver)

    def enableButtonTrue(self, driver):

        
        assert self.enableButton.is_enabled() == True

        return TestBase(self,driver)

    def colorAssert(self, driver):

        color = self.colorChange.value_of_css_property(DataStrings.color)
        assert color == DataStrings.colorAsserting

        return TestBase(self, driver)

    def visibleAfterTrue(self, driver):

        assert self.visibleAfter.is_displayed() == True

        return TestBase(self, driver)




