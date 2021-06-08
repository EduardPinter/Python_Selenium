from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class Screenshot():
    
    def test(self):
        baseUrl = "http://automationpractice.com/index.php"
        driver = webdriver.Chrome(executable_path='/home/edi/Downloads/Selenium/chromedriver')
        driver.implicitly_wait(2)

        driver.maximize_window()

        driver.get(baseUrl)

        driver.find_element_by_xpath("//div[@id='block_top_menu']/ul/li[3]/a[@title='T-shirts']").click()
        driver.find_element_by_xpath("//div[@id='center_column']/ul//div[@class='product-container']//h5/a[@title='Faded Short Sleeve T-shirts']").click()

        size = driver.find_element_by_id("group_1")
        sizeM = Select(size)
        sizeM.select_by_visible_text("M")

        driver.find_element_by_name("Blue").click()
        driver.find_element_by_id("quantity_wanted").clear()
        driver.find_element_by_id("quantity_wanted").send_keys(2)

        time.sleep(20)


        





ff = Screenshot()
ff.test()