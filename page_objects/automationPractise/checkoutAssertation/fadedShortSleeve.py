from typing import Sized
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import Locator
from selenium import webdriver
import time

class WomenTshirtSection():

    driver: webdriver = None
    sizeOfShirt = None
    quantity = None
    addToCartBtn = None
    shoppingCartTitleId = None
    shopptingCartAttr = None
    shoppingCartQuantity = None
    shoppingCartCost = None
    action = None
    webDriverWait = None

    def __init__(self, driver:webdriver):
        self.driver = driver
        self.action = ActionChains(driver)
        self.sizeOfShirt = self.driver.find_element_by_id(Locator.sizeSelectField)
        self.quantity = self.driver.find_element_by_id(Locator.shirtQuantity)
        self.addToCartBtn = self.driver.find_element_by_id(Locator.addToCartButton)
        self.shoppingCartTitleId = self.driver.find_element_by_id(Locator)
        self.shopptingCartAttr = self.driver.find_element_by_id(Locator)
        self.shoppingCartQuantity = self.driver.find_element_by_id(Locator)
        self.shoppingCartCost = self.driver.find_element_by_id(Locator)

        self.webDriverWait = WebDriverWait(driver, 10)

    def hoverOverNavigLink(self, driver):

        self.fadedTshirt.click()

        return
