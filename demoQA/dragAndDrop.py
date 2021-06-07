from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class DragAndDrop():
    
    def test(self):
        
        baseUrl = "https://demoqa.com"
        driver = webdriver.Chrome(executable_path='/home/edi/Downloads/Selenium/chromedriver')
        driver.implicitly_wait(2)
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
        action.drag_and_drop(draggableBox,droppableBox).perform()

        



        time.sleep(20)



ff = DragAndDrop()
ff.test()