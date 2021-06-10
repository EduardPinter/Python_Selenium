from selenium import webdriver
import time
import pytest


#Fixture for Firefox
@pytest.fixture(scope="class")
def driver_init(request):
    ff_driver = webdriver.Firefox(executable_path='/home/edi/Downloads/Selenium/geckodriver')
    request.cls.driver = ff_driver
    yield
    ff_driver.close()

#Fixture for Chrome
@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome(executable_path='/home/edi/Downloads/Selenium/chromedriver')
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()

@pytest.mark.usefixtures("driver_init")
class UploadFirefox():
    pass
class Test_UploadFirefox(UploadFirefox):
 
    def test_randomIdTxt(self):

        baseUrl = "https://demoqa.com"
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()

        self.driver.get(baseUrl)
        self.driver.find_element_by_xpath("//div[@id='app']/div[@class='body-height']/div[@class='home-content']//div[@class='category-cards']/div[1]").click()
        uploadLi = self.driver.find_element_by_xpath("//div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']//div[@class='accordion']/div[1]/div/ul[@class='menu-list']/li[8]/span[@class='text']")
        uploadLi.location_once_scrolled_into_view
        uploadLi.click()

        time.sleep(2)
        filePath = "/home/edi/Desktop/image.png"
        self.driver.find_element_by_id("uploadFile").send_keys(filePath)
        alertMessage = self.driver.find_element_by_id("uploadedFilePath")
        assert alertMessage.text == "Thanks, you have selected {} file to Upload".format(filePath)

        time.sleep(5)

@pytest.mark.usefixtures("chrome_driver_init")
class UploadChrome():
    pass
class Test_UploadChrome(UploadChrome):
 
    def test_uploadNavigation(self):

        baseUrl = "https://demoqa.com"
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()

        self.driver.get(baseUrl)
        self.driver.find_element_by_xpath("//div[@id='app']/div[@class='body-height']/div[@class='home-content']//div[@class='category-cards']/div[1]").click()
        uploadLi = self.driver.find_element_by_xpath("//div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']//div[@class='accordion']/div[1]/div/ul[@class='menu-list']/li[8]/span[@class='text']")
        uploadLi.location_once_scrolled_into_view
        uploadLi.click()

        time.sleep(2)
        filePath = "/home/edi/Desktop/image.png"
        self.driver.find_element_by_id("uploadFile").send_keys(filePath)
        alertMessage = self.driver.find_element_by_id("uploadedFilePath")
        assert alertMessage.text == "Thanks, you have selected {} file to Upload".format(filePath)

        time.sleep(5)




