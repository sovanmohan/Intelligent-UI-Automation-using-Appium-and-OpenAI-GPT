import re
from appium.webdriver.common.appiumby import AppiumBy

def parse_actions(response_text):
    lines = response_text.strip().split("\n")
    steps = []
    for line in lines:
        match = re.search(r"'(.*?)'", line)
        if "tap" in line.lower() and match:
            steps.append({"action": "tap", "target_text": match.group(1)})
    return steps

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
