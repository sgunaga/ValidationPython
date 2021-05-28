from selenium import webdriver
#this is used to select value from Dropdown
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys
import pytest

class Test_Login_Logout():
    @pytest.fixture()
    def test_setup(self):
        # we need to declare it global or else u see error outside this function if u use driver
        global driver
        driver = webdriver.Chrome("C:/Users/sgunaga/PycharmProjects/PRODTY/Drivers/chromedriver.exe")
        driver.get('https://www.thankyou.com/cms/thankyou/')
        driver.maximize_window()
        driver.implicitly_wait(5)
        # homescreen sign on
        time.sleep(5)
        signon = driver.find_element_by_link_text('Sign On')
        signon.click()
        # selecting other thankyou member from Dropdown using select class
        drop_down_value = driver.find_element_by_name('accountType')
        select_an_account = Select(drop_down_value)
        time.sleep(5)
        select_an_account.select_by_index(2)
        # Providing username and password and clicking sigon button
        user_id = driver.find_element_by_id('username').send_keys('epsilon123')
        password = driver.find_element_by_id('password').send_keys('Thankyu01')
        Signing_in = driver.find_element_by_id('signInBtn').click()
        time.sleep(5)
        yield
        driver.find_element_by_link_text("Sign Off").click()
        time.sleep(5)
        Log_off_Validation = driver.find_element_by_id("rememberUidLabel")
        if (Log_off_Validation.is_displayed()):
            print("Sign Off Sucessfull")
        else:
            print("Sign Off Failed")

        driver.close()

    def test_ValidationOfSignOffText(self,test_setup):
        Sign_Off = driver.find_element_by_link_text("Sign Off")
        time.sleep(5)
        if (Sign_Off.is_displayed()):
            print("Login Sucessfull")
        else:
            print("Login not sucessfull")

    @pytest.mark.search
    def test_SearchText(self,test_setup):
        # Search Functionality validation
        search_term = driver.find_element_by_name("search").send_keys("BestBuy")
        search_Icon = driver.find_element_by_name("search").send_keys(Keys.ENTER)
        Search_results = driver.find_elements_by_xpath(
            "//a//img[contains(@src,'https://content.blackhawknetwork.com/gcmimages/product/large/81998.png')]")
        driver.get_screenshot_as_file("screenshot.png")
        # driver.save_screenshot("BestBuy.png")


    # def test_teardown():



