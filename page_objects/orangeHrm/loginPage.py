from data.dataStrings import DataStrings
from locators.locators import Locator
from selenium import webdriver
import time


class LoginPage():

    # gde da postavljam implicit wait i get(url) deo unutar POM-a, maxim.window ..

    driver = None
    btnLogin = None
    userNameField = None
    passwordField = None

    def __init__(self, driver: webdriver):

        self.driver = driver
        self.btnLogin = self.driver.find_element_by_id(Locator.btnLogin)
        self.userNameField = self.driver.find_element_by_id(Locator.userNameInput)
        self.passwordField = self.driver.find_element_by_id(Locator.passwordInput)

    def loginPage(self, driver):

        self.userNameField.send_keys(DataStrings.username)
        self.passwordField.send_keys(DataStrings.password)
        self.btnLogin.click()

        return

