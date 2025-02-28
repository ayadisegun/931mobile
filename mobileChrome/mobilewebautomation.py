import time

from appium.webdriver import webdriver
from appium.webdriver.webdriver import webdriver

from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

desired_caps = dict(
    deviceName='Rapt',
    platformName='Android',
    browserName='Chrome',
    automationName='UiAutomator2',
    chromedriverExecutable='C:\\Program Files\\Python311\\Scripts\\chromedriver131.exe',

)

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
driver.implicitly_wait(10)


# driver.get("https://google.com")
# driver.find_element(AppiumBy.XPATH, "//textarea[@class='gLFyf']").send_keys("Hello")
# # driver.find_element().send_Keys("Hello")
# print(driver.title)
# time.sleep(3)

driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
time.sleep(2)

act_title = driver.title
exp_title = "Swag Labs"

if act_title == exp_title:
    print("title correct")
else:
    print("wrong title")

act_url = driver.current_url
exp_url = "https://www.saucedemo.com/"
if act_url == exp_url:
    print("Login Successful")
else:
    print("login failed")

print(driver.current_url)
print("The current url is:"+str(act_url))

# driver.find_element()
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH, "//*[@id='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH, "//input[@id='login-button']").click()

time.sleep(10)

driver.close()
driver.quit()

# #add five items to cart
# driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-onesie']").click()
# time.sleep(2)
#
# #removing 2 of the added items
# driver.find_element(By.XPATH, "//*[@id='remove-sauce-labs-backpack']").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@id='remove-sauce-labs-bolt-t-shirt']").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@id='remove-sauce-labs-onesie']").click()
# time.sleep(2)
#
# #adding two more item
# driver.find_element(By.XPATH, "//*[@id='add-to-cart-test_files.allthethings()-t-shirt-(red)']").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']").click()
# time.sleep(2)
#
# #checkout
# driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@id='checkout']").click()
# time.sleep(2)
#
# #Logout
# driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@id='logout_sidebar_link']").click()
# time.sleep(2)
#
# #app='C:\\Program Files\\Python311\\Scripts\\Chrome_131.0.6778.104_APKPure.apk'
#     # app='C:\\Program Files\\Python311\\Scripts\\General-Store.apk'
# driver.quit()