from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
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
class CheckoutFirefox():
    pass
class Test_Checkout(CheckoutFirefox):
    
    def test_findShirt(self):
        global driver
        driver = self.driver
        baseUrl = "http://automationpractice.com/index.php"
        driver.implicitly_wait(3)

        driver.maximize_window()

        driver.get(baseUrl)



@pytest.mark.usefixtures("chrome_driver_init")
class CheckoutChrome():
    pass
class Test_Checkout2(CheckoutChrome):

    def test_findShirt(self):
        global driver
        driver = self.driver
        baseUrl = "http://automationpractice.com/index.php"
        driver.implicitly_wait(3)

        driver.maximize_window()

        driver.get(baseUrl)
        