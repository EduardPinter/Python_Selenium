from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.dataStrings import DataStrings
from locators.locators import Locator
from selenium import webdriver
import time


class LandingPage():

    driver = None
    menuLinkAdminModule = None
    menuLinkUserManag = None
    menuLinkSystemUsers = None
    menuLinkMyInfo = None

    def __init__(self, driver: webdriver):

        self.driver = driver
        self.menuLinkAdminModule = self.driver.find_element_by_id(Locator.menuLinkAdminModule)
        self.menuLinkUserManag = self.driver.find_element_by_id(Locator.menuLinkUserManag)
        self.menuLinkSystemUsers = self.driver.find_element_by_id(Locator.menuLinkSystemUsers)
        self.menuLinkMyInfo = self.driver.find_element_by_id(Locator.menuLinkMyInfo)

    def navigationToSystemUsers(self, driver):

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locator.menuLinkAdminModule)))
        ActionChains(driver).move_to_element(self.menuLinkAdminModule).perform()
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "menu_admin_UserManagement")))
        ActionChains(driver).move_to_element(self.menuLinkUserManag).perform()
        self.menuLinkSystemUsers.click()

        return

    def myInfoLink(self, driver):

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "menu_pim_viewMyDetails")))
        self.menuLinkMyInfo.click()



