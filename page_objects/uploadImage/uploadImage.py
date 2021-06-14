from data.dataStrings import DataStrings
from selenium import webdriver
from locators.locators import Locator

class UploadImage():

    uploadFile = None
    alertMessage = None

    def __init__(self, driver:webdriver):
        
        self.uploadFile = driver.find_element_by_id(Locator.uploadFileId)
        self.alertMessage = driver.find_element_by_id(Locator.alertMessageId)

    def sendFilePath(self, driver):

        self.uploadFile.send_keys(DataStrings.filePath)
        assert self.alertMessage.text == DataStrings.alertMessage
