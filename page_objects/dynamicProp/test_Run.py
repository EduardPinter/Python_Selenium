from page_objects.dynamicProp.basePage import PageStart
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from data.dataStrings import DataStrings
from locators.locators import Locator
from selenium.common.exceptions import NoSuchElementException

class TestBase():
    

    def __init__(self, driver: webdriver):
        self.driver = driver




    def test_Run(self):


        self.driver.implicitly_wait(2)
        action = ActionChains(self.driver)
        self.driver.maximize_window()

        dataStrings = DataStrings()
        locator = Locator()

        self.driver.get(dataStrings.baseUrl)
        time.sleep(2)
        randomTextId = "This text has random Id"
        PageStart.dynamicPropCardClick()
        dynamicProp = self.driver.find_element_by_xpath(locator.dynamicPropSection)
        dynamicProp.location_once_scrolled_into_view
        dynamicProp.click()
        textOfElement = self.driver.find_element_by_xpath(locator.randomTextId1)
        assert textOfElement.text == dataStrings.randomTextId

        try:

            self.driver.find_element_by_id(locator.visibleAfter)

        except NoSuchElementException:
            pass

        enableButton = self.driver.find_element_by_id(locator.enableButton).is_enabled()
        assert enableButton == False

        time.sleep(5)
        enableButton = self.driver.find_element_by_id(locator.enableButton).is_enabled()
        assert enableButton == True

        #colorChange = self.driver.find_element_by_id(locator.colorChange)
        #color = colorChange.value_of_css_property(dataStrings.color)
        #assert color == dataStrings.colorAsserting

        visibleAfter = self.driver.find_element_by_id(locator.visibleAfter)
        assert visibleAfter.is_displayed() == True

        time.sleep(2)

        