from page_objects.dragAndDrop.dragDrop import DroppablePage
from page_objects.dragAndDrop.interactionsPage import InteractionsPage
from page_objects.dragAndDrop.basePage import PageStartInteractions
from selenium import webdriver
import time
from data.dataStrings import DataStrings
from locators.locators import Locator

class TestBaseHover():
    

    def __init__(self, driver: webdriver):
        self.driver = driver




    def test_Run(self):


        self.driver.implicitly_wait(2)
        self.driver.maximize_window()

        dataStrings = DataStrings()
        locator = Locator()

        self.driver.get(dataStrings.baseUrl)
        time.sleep(2)
        PageStartInteractions.InteractionsPropCardClick()
        InteractionsPage.findAndScroll()
        InteractionsPage.ClickElement()
        DroppablePage.dragDrop()