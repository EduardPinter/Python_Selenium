from page_objects.dynamicProp.dynamicPropertiesPage import DynamicPropPage
from selenium import webdriver
from locators.locators import Locator



class ElementsPage():
    dynamicPropClick = None

    def __init__(self, driver: webdriver):
        self.dynamicPropClick = driver.find_element_by_xpath(Locator.dynamicPropSection)
    
    def findAndScroll(self, driver):
        self.dynamicPropClick
        self.dynamicPropClick.location_once_scrolled_into_view

        return DynamicPropPage(self, driver)

    def ClickElement(self, driver):
        self.dynamicPropClick.click()

        return DynamicPropPage(self, driver)