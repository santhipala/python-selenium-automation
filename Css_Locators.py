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
driver.get("https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&webAuthnChallengeIdForAutofill=-57tJLHNRKyoOub1RA3TcbhtEObl_xnJ%3ANA&webAuthnGetParametersForAutofill=eyJycElkIjoiYW1hem9uLmNvbSIsImNoYWxsZW5nZSI6Ii01N3RKTEhOUkt5b091YjFSQTNUY2JodEVPYmxfeG5KIiwidGltZW91dCI6MzI0NDQxLCJhbGxvd0NyZWRlbnRpYWxzIjpudWxsLCJtZWRpYXRpb24iOiJjb25kaXRpb25hbCIsInVzZXJWZXJpZmljYXRpb24iOiJwcmVmZXJyZWQifQ%3D%3D&pageId=usflex&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Ftag%3Damazusnavi-20%26hvadid%3D675149237887%26hvpos%3D%26hvnetw%3Dg%26hvrand%3D8659164597735424148%26hvpone%3D%26hvptwo%3D%26hvqmt%3De%26hvdev%3Dc%26hvdvcmdl%3D%26hvlocint%3D%26hvlocphy%3D9030021%26hvtargid%3Dkwd-10573980%26ref%3Dnav_ya_signin%26hydadcr%3D28883_14649097&prevRID=W7J7ZRHMWVJMPR5PAEK1&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
# Find Element By CSS Selectors class - Amazon Logo
driver.find_element(By.CSS_SELECTOR,".a-icon.a-icon-logo")
sleep(2)
# Find Element By CSS Selectors class and tag - Create Account
driver.find_element(By.CSS_SELECTOR,"h1.a-spacing-small")
sleep(2)
# Find Element By CSS by ID - Your Name
driver.find_element(By.CSS_SELECTOR,"#ap_customer_name")
sleep(2)
# Find Element By CSS tag and ID - Mobile Number E-Mail
driver.find_element(By.CSS_SELECTOR,"input#ap_email")
sleep(2)
# Find Element By CSS tag and ID - Password
driver.find_element(By.CSS_SELECTOR,"input#ap_password")
sleep(2)
# Find Element By CSS tag and ID - At least 6 characters
driver.find_element(By.CSS_SELECTOR,"input[placeholder='At least 6 characters']")
sleep(2)
# Find Element By CSS tag and ID - Re-enter Password
driver.find_element(By.CSS_SELECTOR,"input#ap_password_check")
sleep(2)
# Find Element By CSS tag and ID - Continue
driver.find_element(By.CSS_SELECTOR,"input[type='submit']")
sleep(2)
# Find Element By CSS tag and Attribute - Conditions of Use
driver.find_element(By.CSS_SELECTOR,"a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")
sleep(2)
# Find Element By CSS tag and Attribute partial match - Privacy Notice
driver.find_element(By.CSS_SELECTOR,"a[href*='/gp/help/customer/display.html/ref=ap_register_notification_privacy']")
sleep(2)
# Find Element By CSS class - Signin
driver.find_element(By.CSS_SELECTOR,".a-link-emphasis")
sleep(2)