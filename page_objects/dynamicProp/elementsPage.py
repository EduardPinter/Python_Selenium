from page_objects.dynamicProp.dynamicPropertiesPage import DynamicPropPage
from selenium import webdriver
from locators.locators import Locator



class ElementsPage():
    driver: webdriver = None
    dynamicPropClick = None

    def __init__(self, driver: webdriver):

        self.driver = driver
        self.dynamicPropClick = driver.find_element_by_xpath(Locator.dynamicPropSection)
    
    def navigateToDynamicPropertiesPage(self):

        self.dynamicPropClick.location_once_scrolled_into_view
        self.dynamicPropClick.click()

        return DynamicPropPage(self.driver)