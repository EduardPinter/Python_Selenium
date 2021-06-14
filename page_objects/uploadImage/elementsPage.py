from page_objects.uploadImage.uploadImage import UploadImage
from page_objects.dynamicProp.dynamicPropertiesPage import DynamicPropPage
from selenium import webdriver
from locators.locators import Locator



class ElementsPage():
    uploadClick = None

    def __init__(self, driver: webdriver):

        self.uploadClick = driver.find_element_by_xpath(Locator.uploadLi)
    
    def findAndScroll(self, driver):

        self.uploadClick
        self.uploadClick.location_once_scrolled_into_view

        return UploadImage(self, driver)

    def ClickElement(self, driver):

        self.dynamicPropClick.click()

        return UploadImage(self, driver)