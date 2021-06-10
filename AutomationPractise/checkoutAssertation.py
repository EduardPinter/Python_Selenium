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

        hoverElement = driver.find_element_by_xpath("//div[@id='block_top_menu']/ul//a[@title='Women']")
        ActionChains(driver).move_to_element(hoverElement).perform()
        time.sleep(1)

        driver.find_element_by_xpath("//div[@id='block_top_menu']/ul/li[1]/ul/li[1]/ul//a[@title='T-shirts']").click()
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.XPATH, "//div[@id='center_column']/ul//div[@class='product-container']//h5/a[@title='Faded Short Sleeve T-shirts']"))
        driver.find_element_by_xpath("//div[@id='center_column']/ul//div[@class='product-container']//h5/a[@title='Faded Short Sleeve T-shirts']").click()

    def test_shirtRequirements(self):
        
        size = driver.find_element_by_id("group_1")
        sizeM = Select(size)
        sizeM.select_by_visible_text("M")

        driver.find_element_by_name("Blue").click()
        driver.find_element_by_id("quantity_wanted").clear()
        driver.find_element_by_id("quantity_wanted").send_keys(2)

    def test_AddToCart(self):

        driver.find_element_by_xpath("//p[@id='add_to_cart']//span[.='Add to cart']").click()
        time.sleep(2)

    def test_assertCartTitle(self):
        global shoppingCartTitle 
        shoppingCartTitle = "Faded Short Sleeve T-shirts"
        shoppingCartTitleId = driver.find_element_by_id("layer_cart_product_title")
        assert shoppingCartTitleId.text == shoppingCartTitle

    def test_assertCartAttr(self):

        global shoppingCartAttr 
        shoppingCartAttr = "Blue, M"
        shoppingCartAttrId = driver.find_element_by_id("layer_cart_product_attributes")
        assert shoppingCartAttrId.text == shoppingCartAttr

    def test_assertCartQuantity(self):

        global shoppingCartQuantity 
        shoppingCartQuantity = "2"
        shoppingCartQuantityId = driver.find_element_by_id("layer_cart_product_quantity")
        assert shoppingCartQuantityId.text == shoppingCartQuantity

    def test_assertCartCost(self):

        global shoppingCartCost 
        shoppingCartCost = "$33.02"
        shoppingCartCostId = driver.find_element_by_id("layer_cart_product_price")
        assert shoppingCartCostId.text == shoppingCartCost

    #def test_proceedToCheckout(self):

        #driver.find_element_by_xpath("/html//div[@id='layer_cart']//a[@title='Proceed to checkout']/span").click()
        #time.sleep(10)
    
    #def test_assertCheckout(self):
        #descriptionTitle = driver.find_element_by_link_text("Faded Short Sleeve T-shirts")
        #assert descriptionTitle.text == shoppingCartTitle
        #descriptionColorSize = driver.find_element_by_link_text("Color : Blue, Size : M")
        #assert descriptionColorSize.text == "Color : Blue, Size : M"
        #totalPrice = driver.find_element_by_id("total_product")
        #assert totalPrice.text == "$33.02"

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

        hoverElement = driver.find_element_by_xpath("//div[@id='block_top_menu']/ul//a[@title='Women']")
        ActionChains(driver).move_to_element(hoverElement).perform()
        time.sleep(1)

        driver.find_element_by_xpath("//div[@id='block_top_menu']/ul/li[1]/ul/li[1]/ul//a[@title='T-shirts']").click()
        driver.find_element_by_xpath("//div[@id='center_column']/ul//div[@class='product-container']//h5/a[@title='Faded Short Sleeve T-shirts']").click()

    def test_shirtRequirements(self):

        size = driver.find_element_by_id("group_1")
        sizeM = Select(size)
        sizeM.select_by_visible_text("M")

        driver.find_element_by_name("Blue").click()
        driver.find_element_by_id("quantity_wanted").clear()
        driver.find_element_by_id("quantity_wanted").send_keys(2)

    def test_AddToCart(self):

        driver.find_element_by_xpath("//p[@id='add_to_cart']//span[.='Add to cart']").click()
        time.sleep(2)

    def test_assertCartTitle(self):
        global shoppingCartTitle 
        shoppingCartTitle = "Faded Short Sleeve T-shirts"
        shoppingCartTitleId = driver.find_element_by_id("layer_cart_product_title")
        assert shoppingCartTitleId.text == shoppingCartTitle

    def test_assertCartAttr(self):

        global shoppingCartAttr 
        shoppingCartAttr = "Blue, M"
        shoppingCartAttrId = driver.find_element_by_id("layer_cart_product_attributes")
        assert shoppingCartAttrId.text == shoppingCartAttr

    def test_assertCartQuantity(self):

        global shoppingCartQuantity 
        shoppingCartQuantity = "2"
        shoppingCartQuantityId = driver.find_element_by_id("layer_cart_product_quantity")
        assert shoppingCartQuantityId.text == shoppingCartQuantity

    def test_assertCartCost(self):

        global shoppingCartCost 
        shoppingCartCost = "$33.02"
        shoppingCartCostId = driver.find_element_by_id("layer_cart_product_price")
        assert shoppingCartCostId.text == shoppingCartCost

    #def test_proceedToCheckout(self):

        #driver.find_element_by_xpath("/html//div[@id='layer_cart']//a[@title='Proceed to checkout']/span").click()
        #time.sleep(10)
    
    #def test_assertCheckout(self):
        #descriptionTitle = driver.find_element_by_link_text("Faded Short Sleeve T-shirts")
        #assert descriptionTitle.text == shoppingCartTitle
        #descriptionColorSize = driver.find_element_by_link_text("Color : Blue, Size : M")
        #assert descriptionColorSize.text == "Color : Blue, Size : M"
        #totalPrice = driver.find_element_by_id("total_product")
        #assert totalPrice.text == "$33.02"