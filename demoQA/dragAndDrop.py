from demoQA.conftest import printBefore
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
from seleniumbase import BaseCase
import pytest
import os

#Fixture for Chrome
#@pytest.fixture(scope="class")
#def chrome_driver_init(request):
    #chrome_driver = webdriver.Chrome(ChromeDriverManager().install())
    #request.cls.driver = chrome_driver
    #yield
    #chrome_driver.close()



#@pytest.mark.usefixtures("chrome_driver_init")
class DragAndDropChrome():
    pass
class Test_DragAndDrop(BaseCase):
    
    def test_dragDrop(self):

        
        baseUrl = "https://demoqa.com"
        driver = self.driver
        action = ActionChains(driver)

        driver.maximize_window()

        driver.get(baseUrl)
        driver.find_element_by_xpath("//div[@id='app']/div[@class='body-height']/div[@class='home-content']//div[@class='category-cards']/div[5]/div").click()
        time.sleep(2)
        droppableVar = driver.find_element_by_xpath("//div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']/div[@class='row']//div[@class='accordion']/div[5]/div/ul[@class='menu-list']/li[4]/span[@class='text']")
        droppableVar.location_once_scrolled_into_view
        droppableVar.click()

        draggableBox = driver.find_element_by_css_selector("div#draggable")
        droppableBox = driver.find_element_by_css_selector("#simpleDropContainer #droppable")
        action.drag_and_drop(draggableBox, droppableBox).perform()
        


