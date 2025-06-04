from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium.options.common import AppiumOptions

def setup_driver():
    capabilities = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": "com.android.settings",
        "appActivity": ".Settings",
        "automationName": "UiAutomator2"
    }
    driver = webdriver.Remote('http://localhost:4723',options=AppiumOptions().load_capabilities(capabilities))
    return driver, TouchAction(driver)

def perform_action(driver, plan):
    target_text = plan["target_text"]
    if plan["action"] == "tap":
        try:
            el = driver.find_element(AppiumBy.XPATH, f"//*[@text='{target_text}']")
            el.click()
            return f"✅ Tapped: {target_text}"
        except Exception:
            return scroll_and_tap(driver, target_text)

def scroll_and_tap(driver, text):
    try:
        scrollable = 'new UiScrollable(new UiSelector().scrollable(true))'
        scroll_cmd = f'{scrollable}.scrollIntoView(new UiSelector().text("{text}"))'
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scroll_cmd).click()
        return f"✅ Scrolled and tapped: {text}"
    except Exception as e:
        return f"❌ Scroll and tap failed: {e}"
