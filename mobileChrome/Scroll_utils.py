from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from appium import webdriver


class ScrollUtil:
    @staticmethod
    def draganddrop(source, drop):
        ActionChains.drag_and_drop(source, drop).perform()

    @staticmethod
    def longPress(element):
        ActionChains.click_and_hold(element).perform()

    @staticmethod
    def scrollToTextByUIAutomatorclick(text, driver):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                            "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new "
                            "UiSelector().textContains(\"" + text + "\").instance(0))").click()

    # @staticmethod
    # def scrollToTextByAccessibilityIdclick(text, driver):
    #     driver.find_element(AppiumBy.ACCESSIBILITY_ID,
    #                         "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new "
    #                         "UiSelector().text(\"" + text + "\").instance(0))").click()

    @staticmethod
    def scrollToTextByUIAutomator(text, driver):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                            "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new "
                            "UiSelector().textContains(\"" + text + "\").instance(0))")

    @staticmethod
    def scrollDown(numberOfswipes, driver):
        for i in range(1, numberOfswipes+1):
            driver.swipe(325, 941, 325, 436, 1000)

    @staticmethod
    def scrollUp(numberOfswipes, driver):
        for i in range(1, numberOfswipes + 1):
            driver.swipe(325, 436, 325, 941, 1000)

    @staticmethod
    def swipeRight(numberOfswipes, driver):
        for i in range(1, numberOfswipes + 1):
            driver.swipe(40, 277, 390, 277, 1000)

    @staticmethod
    def swipeLeft(numberOfswipes, driver):
        for i in range(1, numberOfswipes + 1):
            driver.swipe(347, 280, 40, 280, 500)

    @staticmethod
    def swipeUpawaiting(howManySwipes, driver):
        action = ActionChains(driver)
        for i in range(1, howManySwipes + 1):
            action.w3c_actions.pointer_action.move_to_location(514, 600)
            action.w3c_actions.pointer_action.pointer_down()
            action.w3c_actions.pointer_action.move_to_location(514, 200)
            action.w3c_actions.pointer_action.pointer_up()
            action.perform()
            action.reset_actions()

    @staticmethod
    def swipeDownawaitingc(howManySwipes, driver):
        action = ActionChains(driver)
        for i in range(1, howManySwipes + 1):
            action.w3c_actions.pointer_action.move_to_location(514, 500)
            action.w3c_actions.pointer_action.pointer_down()
            action.w3c_actions.pointer_action.move_to_location(514, 800)
            action.w3c_actions.pointer_action.pointer_up()
            action.perform()
            action.reset_actions()

    @staticmethod
    def swipeLefta(howManySwipes, driver):
        action = ActionChains(driver)
        for i in range(1, howManySwipes + 1):
            action.w3c_actions.pointer_action.move_to_location(900, 600)
            action.w3c_actions.pointer_action.pointer_down()
            action.w3c_actions.pointer_action.move_to_location(200, 600)
            action.w3c_actions.pointer_action.pointer_up()
            action.perform()
            action.reset_actions()

    @staticmethod
    def swipeRighta(howManySwipes, driver):
        action = ActionChains(driver)
        for i in range(1, howManySwipes + 1):
            action.w3c_actions.pointer_action.move_to_location(200, 600)
            action.w3c_actions.pointer_action.pointer_down()
            action.w3c_actions.pointer_action.move_to_location(900, 600)
            action.w3c_actions.pointer_action.pointer_up()
            action.perform()
            action.reset_actions()


# Android Keycodes
# 0 - 7
# 1 - 8
# 2 - 9
# 3 - 10
# 4 - 11
# 5 - 12
# 6 - 13
# 7 - 14
# 8 - 15
# 9 -16
# 10 -
# 11 - 227
# 12 - 228