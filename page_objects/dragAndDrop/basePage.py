
from page_objects.dragAndDrop.interactionsPage import InteractionsPage
from selenium import webdriver
from locators.locators import Locator


class PageStartInteractions():

    findInteractionsPropCard = None

    def __init__(self, driver: webdriver):

        self.findInteractionsPropCard = driver.find_element_by_xpath(Locator.interactionsPage)

    
    def InteractionsPropCardClick(self, driver):
        
        self.findInteractionsPropCard.click()

        return InteractionsPage(self, driver)