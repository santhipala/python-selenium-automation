from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Selenium commands to get url
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
# Find Element By Xpath - Amazon Logo
#driver.find_element(By.XPATH,"//*[@aria-label='Amazon']")
driver.find_element(By.XPATH, "//a[@href='/ref=ap_frn_logo']").click()
sleep(3)
driver.back()
# Get Element By ID - E-Mail Field
driver.find_element(By.ID,'ap_email').send_keys('partisanship')
sleep(1)
# Select element by tag and multiple attributes
driver.find_element(By.XPATH,"//input[@id='continue' and @type='submit']").click()
sleep(1)
driver.find_element(By.XPATH,"//a[text()='Conditions of Use']").click()
sleep(1)
driver.back()
driver.find_element(By.XPATH,"//a[text()='Privacy Notice']").click()
sleep(1)
driver.back()
driver.find_element(By.XPATH,"//span[contains(text(),'Need help?')]").click()
sleep(1)

driver.find_element(By.XPATH,"//a[contains(text(),'Forgot your password?')]").click()
sleep(1)
driver.back()
driver.find_element(By.XPATH,"//span[contains(text(),'Need help?')]").click()
sleep(1)
driver.find_element(By.XPATH,"//a[contains(text(),'More ways to get support')]").click()
sleep(3)
driver.back()
driver.find_element(By.ID,'createAccountSubmit').click()
sleep(3)
driver.back()