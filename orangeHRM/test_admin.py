from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
class AdminFirefox():
    pass
class Test_AdminFirefox(AdminFirefox):
 
    def test_admin(self):

        global driver
        driver = self.driver
        driver.implicitly_wait(3)
        baseUrl = "https://s2.demo.opensourcecms.com/orangehrm/symfony/web/index.php/auth/login"
        driver.maximize_window()

        driver.get(baseUrl)
        driver.find_element_by_id("txtUsername").send_keys("opensourcecms")
        driver.find_element_by_id("txtPassword").send_keys("opensourcecms")
        driver.find_element_by_id("btnLogin").click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "menu_admin_viewAdminModule")))
        adminPanel = driver.find_element_by_id("menu_admin_viewAdminModule")
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "menu_admin_UserManagement")))
        adminUserMan = driver.find_element_by_id("menu_admin_UserManagement")
        ActionChains(driver).move_to_element(adminPanel).perform()
        ActionChains(driver).move_to_element(adminUserMan).perform()
        driver.find_element_by_id("menu_admin_viewSystemUsers").click()
        time.sleep(5)

        lengthOfTable = driver.find_elements_by_css_selector('#resultTable > tbody > tr')
        counter = 0

        for element in lengthOfTable:
            counter += 1
        print(counter)

        names = driver.find_elements_by_css_selector('#resultTable > tbody > tr > td:nth-child(2) > a')
        for element in names:
            print(element.text)


@pytest.mark.usefixtures("chrome_driver_init")
class AdminChrome():
    pass
class Test_AdminChrome(AdminChrome):
 
    def test_adminChrome(self):
        global driver
        driver = self.driver
        driver.implicitly_wait(3)
        baseUrl = "https://s2.demo.opensourcecms.com/orangehrm/symfony/web/index.php/auth/login"
        driver.maximize_window()

        driver.get(baseUrl)
        driver.find_element_by_id("txtUsername").send_keys("opensourcecms")
        driver.find_element_by_id("txtPassword").send_keys("opensourcecms")
        driver.find_element_by_id("btnLogin").click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "menu_admin_viewAdminModule")))
        adminPanel = driver.find_element_by_id("menu_admin_viewAdminModule")
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "menu_admin_UserManagement")))
        adminUserMan = driver.find_element_by_id("menu_admin_UserManagement")
        ActionChains(driver).move_to_element(adminPanel).perform()
        ActionChains(driver).move_to_element(adminUserMan).perform()
        driver.find_element_by_id("menu_admin_viewSystemUsers").click()
        time.sleep(5)

        lengthOfTable = driver.find_elements_by_css_selector('#resultTable > tbody > tr')
        counter = 0

        for element in lengthOfTable:
            counter += 1
        print(counter)

        names = driver.find_elements_by_css_selector('#resultTable > tbody > tr > td:nth-child(2) > a')
        for element in names:
            print(element.text)



