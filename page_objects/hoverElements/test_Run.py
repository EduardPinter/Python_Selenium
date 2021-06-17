from page_objects.hoverElements.hoverElem import ToolTipPage
from page_objects.hoverElements.widgetsPage import WidgetsPageToolTip
from page_objects.hoverElements.basePage import PageStartWidgets
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
        PageStartWidgets.widgetsPropCardClick()
        WidgetsPageToolTip.findAndScroll()
        WidgetsPageToolTip.ClickElement()
        ToolTipPage.hoverButton()
        ToolTipPage.hoverTextField()

        

        