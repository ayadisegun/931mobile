import time
from _ast import Assert

import bs4.builder
from appium.common import helper
from appium.webdriver import webdriver
from appium.webdriver.webdriver import webdriver
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.action_chains import KeyInput
from selenium.webdriver.common.actions.key_actions import KeyActions



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
desired_caps['appPackage'] = 'io.appium.android.apis'
desired_caps['appActivity'] = '.ApiDemos'
desired_caps['noReset'] = True


# capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
capabilities_options = UiAutomator2Options().load_capabilities(desired_cap)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
driver.implicitly_wait(10)
touch_actions = ActionChains(driver)

# #Scrolling and Tabs
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()
# ScrollUtil.scrollUp(2, driver)
# ScrollUtil.scrollDown(4, driver)
# ScrollUtil.scrollToTextByUIAutomator("Visibility", driver)
# time.sleep(2)
# ScrollUtil.scrollDown(2, driver)
# print("I got here")
# ScrollUtil.scrollToTextByUIAutomatorclick("Tabs", driver)
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1. Content By Id").click()
# driver.find_element(By.XPATH, "//android.widget.LinearLayout[@index='1']").click()
# time.sleep(3)
# print("script completed")

# swiping, - view --> gallery --> photos
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Gallery").click()
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1. Photos").click()
# ScrollUtil.swipeLeft(1, driver)
# print("complete")
# img = driver.find_elements(AppiumBy.CLASS_NAME, "((android.widget.ImageView)[0])")

#Alert, Handle clipboard, checkbox
# driver.set_clipboard_text("Raptures Wifi")  # to save a text on clipboard
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Preference").click()
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "3. Preference dependencies").click()
# driver.find_element(By.ID, "android:id/checkbox").click()
# driver.find_element(By.XPATH, "(//android.widget.RelativeLayout)[2]").click()
# driver.find_element(By.ID, "android:id/edit").send_keys(driver.get_clipboard_text())
# driver.find_element(By.ID, "android:id/button1").click()
# print("complete")

# #drag and drop, - view - drag & drop
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Drag and Drop").click()#x1 484, y1 460, x2 152, y2 771
# source = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/drag_dot_1")
# drop = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/drag_dot_2")
# touch_actions.click_and_hold(source).perform()
# time.sleep(1)
# touch_actions.drag_and_drop_by_offset(source, 466, 454).perform()  #OR
# touch_actions.drag_and_drop(source, drop).perform()
# driver.press_keycode(4)  # 66 -enter key, 3 - home, 187 - recent, 4 - Back

print("----------")
# Tap and long press expandable list --> custom adapter -->people names
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Expandable Lists").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1. Custom Adapter").click()
lngPress = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='People Names']")  #longpress this
touch_actions.click_and_hold(lngPress).perform()
txt = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sample menu']").get_attribute("text")
print(txt)
assert txt == "Sample menu"

# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "2. People")
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "new UiSelector().className('android.widget.ImageView').instance(0)")
# driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Expandable Lists")

#Switching to webview
contexts = driver.contexts
for context in contexts:
    print(context)
driver.switch_to.context('WEBVIEW_chrome')  #OR
webview = driver.contexts[1]
driver.switch_to.context(webview)

driver.start_activity('package name', 'activity name')

driver.activate_app("package name")

driver.find_elements('com.android.mms:id/subject')[0].click()  #clicks the first contact message
messages = driver.find_elements('com.android.mms:id/text_view')
text = messages[len(messages) - 1].text
print(text[83:89])
otp = text[83:89]





driver.quit()

