from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest
from selenium.common.exceptions import NoSuchElementException

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
class DynamicPropertiesFirefox():
    pass
class Test_DynamicPropertiesFirefox(DynamicPropertiesFirefox):
 
    def test_randomIdTxt(self):

        baseUrl = "https://demoqa.com"
        self.driver.implicitly_wait(2)
        action = ActionChains(self.driver)
        self.driver.maximize_window()

        self.driver.get(baseUrl)
        self.driver.find_element_by_xpath("//div[@id='app']/div[@class='body-height']/div[@class='home-content']//div[@class='category-cards']/div[1]").click()
        dynamicProp = self.driver.find_element_by_xpath("//div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']/div[@class='row']//div[@class='accordion']/div[1]/div/ul[@class='menu-list']/li[9]/span[@class='text']")
        dynamicProp.location_once_scrolled_into_view
        dynamicProp.click()

        randomIdText = self.driver.find_element_by_xpath("//div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']//p[.='This text has random Id']")
        textAssert = "This text has random Id"
        assert textAssert == randomIdText.text

    def test_notVisibleAfterButton(self):

        try:

            visibleAfter = self.driver.find_element_by_id("visibleAfter")

        except NoSuchElementException:
            pass
       

    def test_enabledBefore(self):

        
            enableButton = self.driver.find_element_by_id("enableAfter").is_enabled()
            assert enableButton == False
    
    def test_enabledAfter(self):

        enableButton = self.driver.find_element_by_id("enableAfter")
        time.sleep(5)
        assert enableButton.is_enabled() == True

    def test_colorButton(self):

        colorRed = "red"
        colorChange = self.driver.find_element_by_id("colorChange")
        color = colorChange.value_of_css_property("color")
        assert color == colorRed

    def test_isVisible(self):

        visibleAfter = self.driver.find_element_by_id("visibleAfter")
        assert visibleAfter.is_displayed() == True

@pytest.mark.usefixtures("chrome_driver_init")
class DynamicPropertiesChrome():
    pass
class Test_DynamicPropertiesChrome(DynamicPropertiesChrome):
 
    def test_randomIdTxt(self):

        baseUrl = "https://demoqa.com"
        self.driver.implicitly_wait(2)
        action = ActionChains(self.driver)
        self.driver.maximize_window()

        self.driver.get(baseUrl)
        self.driver.find_element_by_xpath("//div[@id='app']/div[@class='body-height']/div[@class='home-content']//div[@class='category-cards']/div[1]").click()
        dynamicProp = self.driver.find_element_by_xpath("//div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']/div[@class='row']//div[@class='accordion']/div[1]/div/ul[@class='menu-list']/li[9]/span[@class='text']")
        dynamicProp.location_once_scrolled_into_view
        dynamicProp.click()

        randomIdText = self.driver.find_element_by_xpath("//div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']//p[.='This text has random Id']")
        textAssert = "This text has random Id"
        assert textAssert == randomIdText.text

    def test_notVisibleAfterButton(self):

        try:

            visibleAfter = self.driver.find_element_by_id("visibleAfter")

        except NoSuchElementException:
            pass
       

    def test_enabledBefore(self):

        
            enableButton = self.driver.find_element_by_id("enableAfter").is_enabled()
            assert enableButton == False
    
    def test_enabledAfter(self):

        enableButton = self.driver.find_element_by_id("enableAfter")
        time.sleep(5)
        assert enableButton.is_enabled() == True

    def test_colorButton(self):

        colorRed = "red"
        colorChange = self.driver.find_element_by_id("colorChange")
        color = colorChange.value_of_css_property("color")
        assert color == colorRed

    def test_isVisible(self):

        visibleAfter = self.driver.find_element_by_id("visibleAfter")
        assert visibleAfter.is_displayed() == True



