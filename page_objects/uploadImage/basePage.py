from page_objects.uploadImage.elementsPage import ElementsPage
from selenium import webdriver
from locators.locators import Locator


class PageStart():

    findDynamicPropCard = None

    def __init__(self, driver: webdriver):

        self.findDynamicPropCard = driver.find_element_by_xpath(Locator.dynamicPropCard)

    
    def dynamicPropCardClick(self, driver):
        
        self.findDynamicPropCard.click()

        return ElementsPage(self, driver)