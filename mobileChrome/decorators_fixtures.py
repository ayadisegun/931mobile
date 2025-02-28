import time

import pytest
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium import webdriver

# class setup:
#     @staticmethod
#     def setup_module(module):
#         print(connect DB")
#
#     @staticmethod
#     def teardown_module(module):
#         print("closing DB")
#
#     @staticmethod
#     def setup_function(function):
#         print("setup function - launching browser")
#
#     @staticmethod
#     def teardown_function(function):
#         print("teardown - quitting driver")

# @pytest.fixture(scope='module')
# def setup_module():
#     print("connect Appium")
#
#     yield
#     print("closing Appium")
#
#
# @pytest.fixture(scope='function')
# def setup_function():
#     print("launching App")
#
#     yield
#     print("closing App")

# @pytest.mark.functional
# @pytest.mark.usefixtures("setup_module", "setup_function")
# def test_login():
#     print("testing login")
#
#
# @pytest.mark.regression
# @pytest.mark.usefixtures("setup_module", "setup_function")
# def test_cart():
#     print("cart")
#
#
# @pytest.mark.functional
# @pytest.mark.usefixtures("setup_module", "setup_function")
# def test_logout():
#     print("logout")

# Parameterising

# def get_data():
#     return[
#         ("trainer", "3476fhf"),
#         ("nayou", "82742"),
#         ("cejd", "96489")
#     ]

# @pytest.mark.parametrize("username, password", get_data())
# def test_params(username, password):
#     print(username, "-----", password)


def get_data():
    return [
        ["Delhi"],
        ["Dubai"],
    ]

# def setup_function():
#     global appium_service
#     appium_service = AppiumService()
#     appium_service.start()
#
#     desired_caps = {}
#     desired_caps['platformName'] = 'Android'
#     desired_caps['deviceName'] = 'Android'
#     desired_caps['appPackage'] = 'com.goibibo'
#     desired_caps['appActivity'] = '.common.HomeActivity'
#     desired_caps['noReset'] = True
#     global driver
#     capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
#     driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
#     # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#     driver.implicitly_wait(10)
#
# def teardown_function():
#     time.sleep(2)
#     driver.quit()
#     appium_service.stop()


@pytest.mark.parametrize("city", get_data())
def test_login(city):
    print(city)

