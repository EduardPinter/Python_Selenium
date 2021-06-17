from page_objects.hoverElements.hoverElem import ToolTipPage
from selenium import webdriver
from locators.locators import Locator



class WidgetsPageToolTip():

    toolTipClick = None

    def __init__(self, driver: webdriver):
        self.toolTipClick = driver.find_element_by_xpath(Locator.toolTip)
    
    def findAndScroll(self, driver):

        self.toolTipClick.location_once_scrolled_into_view

        return ToolTipPage(self, driver)

    def ClickElement(self, driver):

        self.toolTipClick.click()

        return ToolTipPage(self, driver)