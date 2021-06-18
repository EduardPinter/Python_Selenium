from page_objects.dynamicProp.elementsPage import ElementsPage
from selenium import webdriver
from locators.locators import Locator


class PageStart():
    
    driver: webdriver = None
    findDynamicPropCard = None

    def __init__(self, driver: webdriver):
        
        self.driver = driver
        self.findDynamicPropCard = self.driver.find_element_by_xpath(Locator.elementsPropCard)

    def goToWebsite(self, driver, url):

        self.driver.implicitly_wait(3)

        self.driver.get(url)
        self.driver.maximize_window()


    
    def dynamicPropCardClick(self):
        self.findDynamicPropCard.click()

        return ElementsPage(self.driver)


