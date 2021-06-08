from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
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
class ToolTipFirefox():
    pass
class Test_ToolTipFirefox(ToolTipFirefox):
 
    def test_randomIdTxt(self):
        
        baseUrl = "https://demoqa.com"
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()

        self.driver.get(baseUrl)
        self.driver.find_element_by_xpath("//div[@id='app']/div[@class='body-height']/div[@class='home-content']/div[@class='home-body']/div/div[4]/div/div[@class='card-body']").click()
        toolTip = self.driver.find_element_by_xpath("//div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']/div[@class='row']//div[@class='accordion']/div[4]/div/ul[@class='menu-list']/li[7]")
        toolTip.location_once_scrolled_into_view
        toolTip.click()


    def test_hoverButton(self):
        button = self.driver.find_element_by_id("toolTipButton")
        action = ActionChains(self.driver)
        action.move_to_element(button).perform()
        time.sleep(2)
        buttonMessage = self.driver.find_element_by_id("buttonToolTip")
        assert buttonMessage.text == "You hovered over the Button"

    def test_hoverInputField(self):
        inputField = self.driver.find_element_by_id("toolTipTextField")
        ActionChains(self.driver).move_to_element(inputField).perform()
        time.sleep(2)
        inputFieldMessage = self.driver.find_element_by_id("textFieldToolTip")
        assert inputFieldMessage.text == "You hovered over the text field"
        


       


@pytest.mark.usefixtures("chrome_driver_init")
class ToolTipChrome():
    pass
class Test_ToolTipChrome(ToolTipChrome):
 
    def test_randomIdTxt(self):

        baseUrl = "https://demoqa.com"
        self.driver.implicitly_wait(2)
        action = ActionChains(self.driver)
        self.driver.maximize_window()

        self.driver.get(baseUrl)
        self.driver.find_element_by_xpath("//div[@id='app']/div[@class='body-height']/div[@class='home-content']/div[@class='home-body']/div/div[4]/div/div[@class='card-body']").click()
        toolTip = self.driver.find_element_by_xpath("//div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']/div[@class='row']//div[@class='accordion']/div[4]/div/ul[@class='menu-list']/li[7]")
        toolTip.location_once_scrolled_into_view
        toolTip.click()

    def test_hoverButton(self):

        button = self.driver.find_element_by_id("toolTipButton")
        action = ActionChains(self.driver)
        action.move_to_element(button).perform()
        time.sleep(2)
        buttonMessage = self.driver.find_element_by_id("buttonToolTip")
        assert buttonMessage.text == "You hovered over the Button"

    def test_hoverInputField(self):
        inputField = self.driver.find_element_by_id("toolTipTextField")
        ActionChains(self.driver).move_to_element(inputField).perform()
        time.sleep(2)
        inputFieldMessage = self.driver.find_element_by_id("textFieldToolTip")
        assert inputFieldMessage.text == "You hovered over the text field"


       




