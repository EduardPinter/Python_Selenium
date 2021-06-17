from page_objects.hoverElements.widgetsPage import WidgetsPage
from selenium import webdriver
from locators.locators import Locator


class PageStartWidgets():

    findWidgetsPropCard = None

    def __init__(self, driver: webdriver):

        self.findWidgetsPropCard = driver.find_element_by_xpath(Locator.widgetsPropCard)

    
    def widgetsPropCardClick(self, driver):
        
        self.findDynamicPropCard.click()

        return WidgetsPage(self, driver)