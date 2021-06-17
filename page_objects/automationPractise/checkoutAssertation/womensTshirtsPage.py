from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import Locator
from selenium import webdriver
import time

class WomenTshirtSection():

    driver: webdriver = None
    hoverNavigationWomen = None
    tshirtsSection = None
    action = None
    webDriverWait = None

    def __init__(self, driver:webdriver):
        self.driver = driver
        self.hoverNavigationWomen = driver.find_element_by_xpath(Locator.hoverNavigationWomen)
        self.action = ActionChains(driver)
        self.tshirtsSection = driver.find_element_by_xpath(Locator.tshirtsNavSection)
        self.webDriverWait = WebDriverWait(driver, 10)

    def hoverOverNavigLink(self, driver):

        self.action.move_to_element(self.hoverNavigationWomen).perform()
        time.sleep(1)

        return

    def clickTshirtsSection(self, driver):

        self.tshirtsSection.click()

        return