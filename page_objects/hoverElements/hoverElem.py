from time import time
from selenium.webdriver.common.action_chains import ActionChains
from data.dataStrings import DataStrings
from selenium import webdriver
from locators.locators import Locator
import time

class ToolTipPage():

    btn = None
    txtField = None
    btnMessage = None
    txtFieldMessage = None
    action = None

    def __init__(self, driver:webdriver):
        
        self.btn = driver.find_element_by_id(Locator.toolTipBtn)
        self.txtField = driver.find_element_by_id(Locator.textfield)
        self.btnMessage = driver.find_element_by_id(Locator.buttonMessage)
        self.txtFieldMessage = driver.find_element_by_id(Locator.textfieldMessage)
        self.action = ActionChains(self.driver)

    def hoverButton(self, driver):

        self.action.move_to_element(self.btn).perform()
        time.sleep(2)
        assert self.btnMessage.text == DataStrings.buttonMessageHover

    def hoverTextField(self, driver):

        self.action.move_to_element(self.txtField).perform()
        time.sleep(2)
        assert self.txtFieldMessage.text == DataStrings.inputFieldMessage
