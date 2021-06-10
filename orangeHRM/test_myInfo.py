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




@pytest.mark.usefixtures("chrome_driver_init")
class MyInfoChrome():
    pass
class Test_MyInfoChrome(MyInfoChrome):
 
    def test_MyInfoChrome(self):
        global driver
        driver = self.driver
        driver.implicitly_wait(3)
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver.maximize_window()

        driver.get(baseUrl)
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "menu_pim_viewMyDetails")))
        driver.find_element_by_id("menu_pim_viewMyDetails").click()
        firstName = driver.find_element_by_id("personal_txtEmpFirstName")
        print(firstName.get_attribute("value"))
        middleName = driver.find_element_by_id("personal_txtEmpMiddleName")
        print(middleName.get_attribute("value"))
        lastName = driver.find_element_by_id("personal_txtEmpLastName")
        print(lastName.get_attribute("value"))
        employeeId = driver.find_element_by_id("personal_txtEmployeeId")
        print(employeeId.get_attribute("value"))
        maritalStatus = driver.find_element_by_id("personal_cmbMarital")
        print(maritalStatus.get_attribute("selected"))  # na ovome jos poraditi da dobijemo vrednost
        birthDate = driver.find_element_by_id("personal_DOB")
        print(birthDate.get_attribute("value"))




