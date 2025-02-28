import time

import bs4.builder
from appium.common import helper
from appium.webdriver import webdriver
from appium.webdriver.webdriver import webdriver


from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

from mobileChrome.Scroll_utils import ScrollUtil

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
#desired_caps['chromedriverExecutable'] = 'C:\\Program Files\\Python311\\Scripts\\chromedriver131.exe'
desired_caps['appPackage'] = 'com.sh.smart.caller'
desired_caps['appActivity'] = 'com.android.dialer.main.impl.MainActivity'


# capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
capabilities_options = UiAutomator2Options().load_capabilities(desired_cap)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id='com.sh.smart.caller:id/bottom_nav_item_text' "
                              "and @text='Contacts']").click()
driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id='com.sh.smart.caller:id/bottom_nav_item_text' "
                              "and @text='Recents']").click()
driver.find_element(By.ID, "com.sh.smart.caller:id/dialpad_hide").click()
time.sleep(2)
ScrollUtil.scrollUp(2, driver)
ScrollUtil.scrollDown(4, driver)
# driver.swipe(325, 941, 325, 436, 1000)
# driver.swipe(325, 941, 325, 436, 1000)
# driver.swipe(325, 436, 325, 941, 1000)
# driver.swipe(325, 436, 325, 941, 1000)
driver.find_element(By.XPATH, "//android.widget.ImageView[@resource-id='com.sh.smart.caller:id/fab']").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1,").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "5,JKL").click()
driver.find_element(AppiumBy.ID, "com.sh.smart.caller:id/nine").click()
driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc='0']").click()
driver.find_element(By.XPATH, "((//android.widget.RelativeLayout[@resource-id='com.sh.smart.caller:id/float_btn_root'])[1])").click()
driver.find_element(By.XPATH, "//android.widget.LinearLayout[@content-desc='Unmuted']/android.widget.ImageView").click()
driver.find_element(By.XPATH, "//android.widget.LinearLayout[@content-desc='Speaker, is Off']/android.widget.ImageView").click()
driver.find_element(By.XPATH, "//android.widget.LinearLayout[@content-desc='Muted']/android.widget.ImageView").click()
driver.find_element(By.XPATH, "//android.widget.LinearLayout[@content-desc='Keypad']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//android.widget.LinearLayout[@content-desc='Keypad']").click()
driver.find_element(By.ID, "com.sh.smart.caller:id/incall_end_call").click()
driver.find_element(By.XPATH, "((//android.widget.ImageView[@resource-id='com.sh.smart.caller:id/enter_call_details'])[1])").click()
driver.find_element(By.ID, "com.sh.smart.caller:id/call_detail_expand").click()
driver.back()
driver.find_element(By.ID, "com.sh.smart.caller:id/call_detail_add_or_edit").click()
driver.find_element(By.ID, "com.android.contacts:id/header_title").click() #android.widget.RelativeLayout -- classname, //android.widget.TextView[@resource-id="com.android.contacts:id/header_title"]

driver.find_element(By.ID, "com.android.contacts:id/account_header_container").click()
driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id='android:id/text2' and @text='asegema4christ3@gmail.com']").click()
driver.find_element(By.XPATH, "//android.widget.EditText[@text='First name']").send_keys("B S")
driver.find_element(By.XPATH, "//android.widget.EditText[@text='Last name']").send_keys("A A")
driver.find_element(By.ID, "com.android.contacts:id/menu_save").click()
driver.find_element(By.ID, "com.sh.smart.caller:id/img_back").click()
driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id='com.sh.smart.caller:id/bottom_nav_item_text' and @text='Contacts']").click()
driver.find_element(By.ID, "com.sh.smart.caller:id/call_log_search_icon").click()
time.sleep(2)
driver.find_element(By.ID, "com.sh.smart.caller:id/search_back_button").click()
print("im here")
#THIS WORKS
#driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("B S A A"))').click()
#driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("B S A A"))').click()
#driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("B S A A").instance(0))').click()
#driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id='com.sh.smart.caller:id/contact_name' and @text='A A A A']").click()
#ScrollUtil.scrollToTextByUIAutomator("B S A A")
#driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("B S A A"))').click()
ScrollUtil.scrollToTextByUIAutomatorclick("B S A A", driver)
driver.find_element(By.ID, "com.android.contacts:id/quick_contact_expand").click()
driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id='android:id/title' and @text='Delete contact']").click()
driver.find_element(By.ID, "com.android.contacts:id/btn_positive").click()
driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id='com.sh.smart.caller:id/bottom_nav_item_text' and @text='Recents']").click()
driver.press_keycode(4)
print("script end")
time.sleep(2)

driver.quit()


# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "key pad").click()
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1,").click()
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "5,JKL").click()
# driver.find_element(AppiumBy.ID, "com.google.android.dialer:id/nine").click()
# driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='0']").click()
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "dial").click()
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Unmuted").click()
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Hold call").click()
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Muted").click()
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Resume call").click()
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "End call").click()
#
# driver.find_element(By.ID, "com.google.android.dialer:id/call_log_tab").click()
# driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id='com.google.android.dialer:id/name' and @text='1590']").click()
# driver.find_element(By.XPATH, "//android.widget.TextView[@text='Call details']").click()
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Close").click()
# driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id='com.google.android.dialer:id/name' and @text='1590']").click()
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Quick contact for 1590").click()
# driver.find_element(By.ID, "com.android.contacts:id/menu_edit").click()
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Create new contact").click()
# driver.find_element(By.XPATH, "//android.widget.EditText[@text='First name']").send_keys("te")
# driver.find_element(By.XPATH, "//android.widget.EditText[@text='Last name']").send_keys("st")
# driver.find_element(By.CLASS_NAME, "android.widget.Button").click()
# driver.press_keycode(4)
# # driver.press_keycode(3), 66 -enter key, 3 - home, 187 - recent, 4 - Back
# print("codes")
#
# driver.find_element(By.ID, "com.google.android.dialer:id/contacts_tab").click()
# driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.google.android.dialer:id/contact_name' and @text='te st']").click()
# driver.find_element(By.CLASS_NAME, "android.widget.ImageButton").click()
# driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='android:id/title' and @text='Delete']").click()
# driver.find_element(By.ID, "android:id/button1").click()
# driver.find_element(By.ID, "com.google.android.dialer:id/call_log_tab").click()
# print("script end")

#driver.quit()
