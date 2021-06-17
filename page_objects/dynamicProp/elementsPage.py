from page_objects.dynamicProp.dynamicPropertiesPage import DynamicPropPage
from selenium import webdriver
from locators.locators import Locator



class ElementsPage():
    driver: webdriver = None
    dynamicPropClick = None

    def __init__(self, driver: webdriver):

        self.driver = driver
        self.dynamicPropClick = driver.find_element_by_xpath(Locator.dynamicPropSection)

    def findAndScroll(self, driver, webElement):

        webElement.location_once_scrolled_into_view

    def ClickElement(self, driver):

        self.dynamicPropClick.click()

        return DynamicPropPage(self, driver)