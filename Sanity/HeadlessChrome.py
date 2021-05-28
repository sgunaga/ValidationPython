from selenium import webdriver
#this is used to select value from Dropdown
from selenium.webdriver.support.ui import Select
#this is used to run test in headless chrome
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options,executable_path="../Drivers/chromedriver.exe")
driver.get('https://www.thankyou.com/cms/thankyou/')
driver.maximize_window()

time.sleep(5)
#homescreen sign on
signon=driver.find_element_by_link_text('Sign On')
signon.click()

time.sleep(5)
#selecting other thankyou member from Dropdown using select class
drop_down_value=driver.find_element_by_name('accountType')
select_an_account = Select(drop_down_value)
select_an_account.select_by_index(2)

time.sleep(5)
#Providing username and password and clicking sigon button
user_id=driver.find_element_by_id('username').send_keys('epsilon123')
password=driver.find_element_by_id('password').send_keys('Thankyu01')
Signing_in=driver.find_element_by_id('signInBtn').click()