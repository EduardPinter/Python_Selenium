
from page_objects.uploadImage.uploadImage import UploadImage
from page_objects.uploadImage.elementsPage import ElementsPageUpload
from page_objects.uploadImage.basePage import PageStartUpload
from selenium import webdriver
import time
from data.dataStrings import DataStrings
from locators.locators import Locator

class TestBaseUpload():
    

    def __init__(self, driver: webdriver):
        self.driver = driver




    def test_Run(self):


        self.driver.implicitly_wait(2)
        self.driver.maximize_window()

        dataStrings = DataStrings()
        locator = Locator()

        self.driver.get(dataStrings.baseUrl)
        time.sleep(2)
        PageStartUpload.elementsPropCardClick()
        ElementsPageUpload.findAndScroll()
        ElementsPageUpload.ClickElement()
        UploadImage.sendFilePath()

        

        