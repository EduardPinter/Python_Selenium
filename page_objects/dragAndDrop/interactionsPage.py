
from page_objects.dragAndDrop.dragDrop import DroppablePage
from selenium import webdriver
from locators.locators import Locator



class InteractionsPage():

    droppableClick = None

    def __init__(self, driver: webdriver):
        
        self.droppableClick = driver.find_element_by_xpath(Locator.droppablePage)
    
    def findAndScroll(self, driver):

        self.droppableClick.location_once_scrolled_into_view

        return DroppablePage(self, driver)

    def ClickElement(self, driver):

        self.droppableClick.click()

        return DroppablePage(self, driver)