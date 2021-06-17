from time import time
from selenium.webdriver.common.action_chains import ActionChains
from data.dataStrings import DataStrings
from selenium import webdriver
from locators.locators import Locator
import time

class DroppablePage():

    draggable = None
    droppable = None
    action = None

    def __init__(self, driver:webdriver):
        
        self.draggable = driver.find_element_by_css_selector(Locator.draggableBox)
        self.droppable = driver.find_element_by_css_selector(Locator.droppableBox)
        self.action = ActionChains(self,driver)


    def dragDrop(self, driver):

        self.action.drag_and_drop(self.draggable, self.droppable).perform()




