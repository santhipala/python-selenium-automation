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
driver.get("https://www.target.com/")
# Find Element By Xpath
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
sleep(1)
driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()
sleep(1)
# verification
# expected_result = 'Sign into your Target account'
actual_result = driver.find_element(By.XPATH,"//span[contains(text(),'Sign into your Target account')]")
print("Text found:",actual_result.is_displayed())
# driver.back()
sleep(2)
sign_in_button_visible = driver.find_element(By.XPATH,"//span[contains(text(),'Sign in with password')]")
print("SignIn button visible:", sign_in_button_visible.is_displayed())
sleep(2)
driver.quit()



