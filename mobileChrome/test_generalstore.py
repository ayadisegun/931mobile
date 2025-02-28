import time
from _ast import Assert

import bs4.builder
from appium.common import helper
from appium.webdriver import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.webdriver import webdriver
from appium.options.android import UiAutomator2Options
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.action_chains import KeyInput
from selenium.webdriver.common.actions.key_actions import KeyActions
from selenium.webdriver.support import expected_conditions as EC
# from mobileChrome.Scroll_utils import ScrollUtil
from Scroll_utils import ScrollUtil


def setup_function():
    global appium_service
    appium_service = AppiumService()
    appium_service.start()

    desired_caps = dict(
        deviceName='Rapt',
        platformName='Android',
        browserName='Chrome',
        automationName='UiAutomator2',
        chromedriverExecutable='C:\\Program Files\\Python311\\Scripts\\chromedriver131.exe',
    )

    desired_cap = {}
    desired_caps['deviceName'] = 'Android'
    desired_caps['platformName'] = 'Android'
    desired_caps['browserName'] = 'Chrome'
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps['chromedriverExecutable'] = 'C:\\Program Files\\Python311\\Scripts\\chromedriver131.exe'
    desired_caps['appPackage'] = 'com.androidsample.generalstore'
    desired_caps['appActivity'] = 'com.androidsample.generalstore.SplashActivity'
    desired_caps['noReset'] = True


    # capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    capabilities_options = UiAutomator2Options().load_capabilities(desired_cap)
    global driver
    driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
    driver.implicitly_wait(10)
    touch_actions = ActionChains(driver)
    global wait
    wait = WebDriverWait(driver, 10)


def teardown():
    driver.quit()
    appium_service.stop()


def test_login_toast():
    driver.set_clipboard_text("Rapture")
    driver.find_element(AppiumBy.ID, "com.androidsample.generalstore:id/radioFemale").click()
    driver.find_element(AppiumBy.ID, "com.androidsample.generalstore:id/spinnerCountry").click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiScrollable(new UiSelector()).scrollIntoView(text(\"Bolivia\"))")
    driver.find_element(By.XPATH, "//android.widget.TextView[@text='Bolivia']").click()
    driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button").click()
    # Toast_message capture
    toast_msg = driver.find_element(By.XPATH, "//android.widget.Toast").get_attribute("name")
    assert toast_msg == "Please enter your name", f"Expected 'Please enter your name' but found '{toast_msg}'"
    print("toast message test successful")


def test_login_page():
    driver.find_element(AppiumBy.ID, "com.androidsample.generalstore:id/nameField").send_keys(driver.get_clipboard_text())
    driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button").click()
    print("login successful")


# Adding item to cart
def test_shopping_page():
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiScrollable(new UiSelector()).scrollIntoView(text(\"Jordan 6 Rings\"))")
    products = driver.find_elements(By.ID, "com.androidsample.generalstore:id/productName")
    itemscount = len(products)
    # Iterate through the product list
    for i in range(itemscount):
        product_name = products[i].text
        if product_name.lower() == "jordan 6 rings":
            add_to_cart_buttons = driver.find_elements(By.ID, "com.androidsample.generalstore:id/productAddCart")
            add_to_cart_buttons[i].click()
        break
    ScrollUtil.scrollUp(2, driver)
    driver.find_element(AppiumBy.ID, "com.androidsample.generalstore:id/appbar_btn_cart").click()
    time.sleep(2)


def test_cart_page():
    cart_label = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.androidsample.generalstore:id/toolbar_title"))).get_attribute("text")
    assert cart_label == "Cart", f"Expected 'Cart' but found '{cart_label}'"
    wait.until(EC.text_to_be_present_in_element((AppiumBy.ID, "com.androidsample.generalstore:id/toolbar_title"), "Cart"))
    cart_product_name = driver.find_element(By.ID, "com.androidsample.generalstore:id/productName").text
    assert cart_product_name == "Jordan 6 Rings", f"Expected 'Jordan 6 Rings' but found '{cart_product_name}'"
    print("Test passed")
    # verify total amount
    amount_total = driver.find_element(By.ID, "com.androidsample.generalstore:id/totalAmountLbl").text
    strip_amount = amount_total.lstrip(" $")
    print("stripped amount is: " + strip_amount)
    driver.find_element(By.CLASS_NAME, "android.widget.CheckBox").click()
    tandc = driver.find_element(By.ID, "com.androidsample.generalstore:id/termsButton")
    tandc_text = tandc.get_attribute("text")
    assert tandc_text == "Please read our terms of conditions", f"Expect 'Please read our terms of conditions' but found '{tandc}'"
    # ScrollUtil.longPress(tandc)
    # driver.find_element(By.ID, "android:id/button1").click()
    driver.find_element(By.ID, "com.androidsample.generalstore:id/btnProceed").click()
    # contexts = driver.contexts
    # for content in contexts:
    #     print(content)
    # driver.switch_to.context(contexts[0]) #OR


def test_web_login():
    contexts = driver.contexts
    driver.switch_to.context(contexts[0])
    # webview = driver.switch_to.context(contexts[0])
    editbox = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "android.widget.EditText")))
    editbox.send_keys("Sauce demo")
    editbox.click()
    driver.press_keycode(66)
    time.sleep(5)
    driver.find_element(By.XPATH, "//android.view.View[@text='Swag Labs']").click()
    username = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@resource-id='user-name']")))
    username.send_keys("standard_user")
    driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@resource-id='password']").send_keys("secret_sauce")
    driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@resource-id='login-button']").click()
    time.sleep(2)
    print("thank you, web login successful")


def test_web_add_items():
    web_products = driver.find_elements(AppiumBy.XPATH, "(//android.view.View[@resource-id='inventory_container'])")
    product_counts = len(web_products)
    # target_items = ["sauce labs backpack", "sauce labs bolt t-shirt"]
    found_items = 0
    for i in range(product_counts):
        name = web_products[i].text
        if name == "Sauce Labs Backpack" or "Sauce Labs Bolt T-Shirt":
            web_addButton = driver.find_elements(AppiumBy.XPATH, "(//android.widget.Button[@text='ADD TO CART'])")
            web_addButton[i].click()
            found_items += 1  # Increment the counter
            if found_items == 2:  # Stop the loop if both items have been found
                break

        break
    print("Found item is: " + format(found_items))
    print("found item is: " + str(found_items))
    print("2 done")
    ScrollUtil.scrollToTextByUIAutomator('Sauce Labs Onesie', driver)

    time.sleep(3)
    web_products1 = driver.find_elements(AppiumBy.XPATH, "(//android.view.View[@resource-id='inventory_container'])")
    product_counts1 = len(web_products1)
    found_items1 = 0
    for i in range(product_counts1):
        name = web_products1[i].text
        if name == "Sauce Labs Onesie" or "Sauce Labs Fleece Jacket":
            web_addButton1 = driver.find_elements(AppiumBy.XPATH, "(//android.widget.Button[@text='ADD TO CART'])")
            web_addButton1[i].click()
            found_items1 += 1  # Increment the counter
            if found_items1 == 2:  # Stop the loop if both items have been found
                break

        break

    # web_products = driver.find_elements(AppiumBy.XPATH, "(//android.view.View[@resource-id='inventory_container'])")
    # product_counts = len(web_products)
    # target_items = ["sauce labs backpack", "sauce labs bolt t-shirt"]  # List of items to look for
    # found_items = 0  # Counter to track how many items have been found
    # for i in range(product_counts):
    #     name = web_products[i].text.lower()  # Convert to lowercase for case-insensitive comparison
    #     if name in target_items:   # Check if the current product is one of the target items
    #         web_addButton = driver.find_elements(AppiumBy.XPATH, "(//android.widget.Button[@text='ADD TO CART'])")
    #         web_addButton[i].click()
    #         found_items += 1  # Increment the counter
    #         if found_items == 2:  # Stop the loop if both items have been found
    #             break


    # web_products1 = driver.find_elements(AppiumBy.XPATH, "(//android.view.View[@resource-id='inventory_container'])")
    # product_counts1 = len(web_products)
    # target_items1 = ["Sauce Labs Onesie", "Sauce Labs Fleece Jacket"]  # List of items to look for
    # found_items1 = 0  # Counter to track how many items have been found
    # for i in range(product_counts1):
    #     name = web_products1[i].text.lower()  # Convert to lowercase for case-insensitive comparison
    #     if name in target_items1:   # Check if the current product is one of the target items
    #         web_addButton = driver.find_elements(AppiumBy.XPATH, "(//android.widget.Button[@text='ADD TO CART'])")
    #         web_addButton[i].click()
    #         found_items1 += 1  # Increment the counter
    #         if found_items1 == 2:  # Stop the loop if both items have been found
    #             break

    ScrollUtil.scrollUp(3, driver)

    # # Menu icon -
    # driver.find_element(AppiumBy.XPATH, "//*[@class='bm-burger-button']").click() #- //button[@id='react-burger-menu-btn' and contains(text(), 'Open-Menu')]
    # All_Items = driver.find_element(By.XPATH, "//*[@id='inventory_sidebar_link']").text
    # print("sidebar label list is: " + All_Items)
    # driver.find_element(By.XPATH, "//*[contains(text(),'Close Menu')] ").click() #//*[@class='btn_secondary' and @name='Continue Shopping']


def test_web_cart():
    driver.find_element(AppiumBy.XPATH, "//*[@resource-id='shopping_cart_container']").click()
    ScrollUtil.scrollDown(2, driver)
    time.sleep(2)
    # driver.find_element(AppiumBy.XPATH, "//*[@text='CONTINUE SHOPPING']").click()
    # time.sleep(2)
    # driver.find_element(AppiumBy.XPATH, "//*[@resource-id='shopping_cart_container']").click()
    # ScrollUtil.scrollDown(2, driver)
    # driver.find_element(AppiumBy.XPATH, "//*[@text='CHECKOUT']").click()  #//button[@id='checkout' and contains(text(), 'Checkout')]


# driver.quit()

