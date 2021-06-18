from webdriver_manager.driver import GeckoDriver
from page_objects.dynamicProp.basePage import PageStart
from selenium import webdriver
from page_objects.dynamicProp.elementsPage import ElementsPage
from page_objects.dynamicProp.dynamicPropertiesPage import DynamicPropPage
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest


#Fixture for Firefox
@pytest.fixture(scope="class")
def driver_init(request):
    ff_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = ff_driver
    yield
    ff_driver.close()

#Fixture for Chrome
@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()

@pytest.mark.usefixtures("driver_init")
class DynamicPropertiesFirefox():
    pass
class Test_DynamicPropertiesFirefox(DynamicPropertiesFirefox):
 

@pytest.mark.usefixtures("chrome_driver_init")
class DynamicPropertiesChrome():
    pass
class Test_DynamicPropertiesChrome(DynamicPropertiesChrome):
 

        dataStrings = DataStrings()

        self.driver.get(dataStrings.baseUrl)
        
        homePage = PageStart(self.driver)
        elementsPage = homePage.dynamicPropCardClick()
        dynamicPropPage = elementsPage.navigateToDynamicPropertiesPage()
        DynamicPropPage.assertRandomText()
        DynamicPropPage.visibleAfterException()
        DynamicPropPage.enableButtonFalse()
        DynamicPropPage.enableButtonTrue()
        DynamicPropPage.colorAssert()
        DynamicPropPage.visibleAfterTrue()





