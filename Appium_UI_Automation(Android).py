# %%
pip install Appium-Python-Client

# %%
!pip install -q openai

# %%
import xml.etree.ElementTree as ET
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import openai
import time
import re
from appium.options.common import AppiumOptions
from appium.webdriver.common.touch_action import TouchAction

openai.api_key = "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"  # Replace with your API key

# --- Init Appium Driver ---
capabilities = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.android.settings",
    "appActivity": ".Settings",
    "automationName": "UiAutomator2"
}

driver = webdriver.Remote('http://localhost:4723', options=AppiumOptions().load_capabilities(capabilities))

# --- Helper Functions ---
def get_page_source():
    return driver.page_source

def extract_ui_elements(xml_source):
    root = ET.fromstring(xml_source)
    ui_elements = []
    for element in root.iter():
        text = element.attrib.get("text", "")
        resource_id = element.attrib.get("resource-id", "")
        content_desc = element.attrib.get("content-desc", "")
        class_name = element.attrib.get("class", "")
        if text or resource_id or content_desc:
            ui_elements.append({
                "text": text,
                "resource-id": resource_id,
                "content-desc": content_desc,
                "class": class_name
            })
    return ui_elements[:5]

def parse_actions(response_text):
    lines = response_text.strip().split("\n")
    steps = []
    for line in lines:
        match = re.search(r"'(.*?)'", line)
        if "tap" in line.lower() and match:
            steps.append({"action": "tap", "target_text": match.group(1)})
    return steps

def perform_action(plan):
    target_text = plan["target_text"]
    if plan["action"] == "tap":
        try:
            el = driver.find_element(AppiumBy.XPATH, f"//*[@text='{target_text}']")
            el.click()
            print(f"✅ Tapped: {target_text}")
        except Exception as e:
            print(f"❌ Tap failed, trying scroll: {e}")
            scroll_and_tap(target_text)

def scroll_and_tap(text):
    try:
        scrollable = 'new UiScrollable(new UiSelector().scrollable(true))'
        scroll_cmd = f'{scrollable}.scrollIntoView(new UiSelector().text("{text}"))'
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scroll_cmd).click()
        print(f"✅ Scrolled and tapped: {text}")
    except Exception as e:
        print(f"❌ Scroll and tap failed: {e}")

# --- Multi-Step Controller ---
def execute_ui_navigation(user_prompt):
    xml = get_page_source()
    ui_elements = extract_ui_elements(xml)

    context = f"Current screen elements:\n" + "\n".join(
        [f"{el['text']} - {el['resource-id']} - {el['content-desc']}" for el in ui_elements]
    )

    full_prompt = (
        f"You are a mobile UI automation assistant. Based on the current screen and user request, list the steps needed "
        f"to complete the task, one per line, like: Tap on 'Connected Devices', Tap on 'Connection Preferences', etc.\n\n"
        f"User Task: {user_prompt}\n\n{context}"
    )

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": full_prompt}]
    )

    instructions = response.choices[0].message.content.strip()
    print(f"Sovan GPT says:\n{instructions}")

    steps = parse_actions(instructions)
    for step in steps:
        perform_action(step)
        time.sleep(2)  # wait between steps

# --- Prompt Loop ---
while True:
    user_prompt = input("Your Task (or 'exit'): ")
    if user_prompt.lower() == "exit":
        break
    execute_ui_navigation(user_prompt)
    time.sleep(2)
