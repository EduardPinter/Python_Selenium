from selenium.webdriver.support.wait import WebDriverWait
from page_objects.dynamicProp.dynamicPropertiesPage import DynamicPropPage
from page_objects.dynamicProp.elementsPage import ElementsPage
from page_objects.dynamicProp.basePage import PageStart
from selenium import webdriver
import time
from data.dataStrings import DataStrings

class TestBase():
    

    def __init__(self, driver: webdriver):
        self.driver = driver




    def test_Run(self):


        self.driver.implicitly_wait(2)
        self.driver.maximize_window()

        dataStrings = DataStrings()

        self.driver.get(dataStrings.baseUrl)
        
        homePage = PageStart(self.driver)
        elementsPage = homePage.dynamicPropCardClick()
        ElementsPage.findAndScroll(self.driver)
        ElementsPage.ClickElement()
        DynamicPropPage.assertRandomText()
        DynamicPropPage.visibleAfterException()
        DynamicPropPage.enableButtonFalse()
        DynamicPropPage.enableButtonTrue()
        DynamicPropPage.colorAssert()
        DynamicPropPage.visibleAfterTrue()
        

        