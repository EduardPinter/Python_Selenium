from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import Locator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class BasePageShop():

    driver: webdriver = None
    hoverNavigationWomen = None
    tshirtsSection = None
    action = None

    def __init__(self, driver:webdriver):

        self.driver = driver
        self.hoverNavigationWomen = driver.find_element_by_xpath(Locator.hoverNavigationWomen)
        self.action = ActionChains(driver)
        self.tshirtsSection = driver.find_element_by_xpath(Locator.tshirtsNavSection)

    def hoverOverNavigLink(self, driver):

        self.action.move_to_element(self.hoverNavigationWomen).perform()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.XPATH, Locator.tshirtsNavSection))

        return

    def clickTshirtsSection(self, driver):

        self.tshirtsSection.click()
        
        return