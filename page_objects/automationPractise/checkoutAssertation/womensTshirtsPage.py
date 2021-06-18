from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import Locator
from selenium import webdriver
import time

class WomenTshirtSection():

    driver: webdriver = None
    fadedTshirt = None
    action = None
    webDriverWait = None

    def __init__(self, driver:webdriver):
        self.driver = driver
        self.action = ActionChains(driver)
        self.fadedTshirt = driver.find_element_by_xpath(Locator.fadedShortSleeveShirt)
        self.webDriverWait = WebDriverWait(driver, 10)

    def hoverOverNavigLink(self, driver):

        self.fadedTshirt.click()

        return
