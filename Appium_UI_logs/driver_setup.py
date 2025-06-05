from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.touch_action import TouchAction

def initialize_driver():
    capabilities = {
        "platformName": "Android",
        "deviceName": "RZCX61TM8AJ",
        "appPackage": "com.android.settings",
        "appActivity": ".Settings",
        "automationName": "UiAutomator2"
    }
    driver = webdriver.Remote('http://localhost:4723', options=AppiumOptions().load_capabilities(capabilities))
    action = TouchAction(driver)
    return driver, action
