# %%
pip install appium

# %%
pip install appium python client

# %%
pip install Appium-Python-Client==0.24

# %%
from appium import webdriver

# %%
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

capabilities:Dict[str,Any]={
    'platformName':'Android',
    'automationName':'uiautomator2',
    'deviceName':'Android',
    "appPackage": "com.amazon.mShop.android.shopping",  # Example: Amazon app
    "appActivity": "com.amazon.mShop.home.HomeActivity",
    'language':'en',
    'locale':'US',
    "noReset": True }

url = 'http://localhost:4723'

driver=webdriver.Remote(url,options=AppiumOptions().load_capabilities(capabilities))
driver.quit()

# %%
!pip install -q openai

# %%
import openai

# %%
import os
os.environ["OPENAI_API_KEY"] = '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'

# %%
import xml.etree.ElementTree as ET
import openai
import time

# XML File Path
xml_file_path = "C:/Users/lenovo/Downloads/app-source-2025-03-28T03_54_46.626Z.xml"

# Function to extract UI elements
def extract_ui_elements(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    ui_elements = []
    
    for element in root.iter():
        content_desc = element.attrib.get("content-desc", "")
        resource_id = element.attrib.get("resource-id", "")
        class_name = element.attrib.get("class", "")

        if content_desc or resource_id:
            ui_elements.append({
                "content-desc": content_desc,
                "resource-id": resource_id,
                "class": class_name
            })
    
    return ui_elements

# Load UI elements from XML
ui_elements = extract_ui_elements(xml_file_path)

if not ui_elements:
    print("No UI elements found in the page source.")
    exit()

messages = [{"role": "system", "content": "You are a UI testing assistant. Answer based on the given page source."}]

while True:
    user_input = input("User: ")
    
    if user_input.lower() == "exit":
        print("Exiting chat...")
        break
    
    # Adding UI elements context to user input
    context = "Relevant UI elements: " + str(ui_elements[:5])  # Limiting to 5 elements for brevity
    full_prompt = f"{user_input}\n\n{context}"
    
    messages.append({"role": "user", "content": full_prompt})
    
    # AI Response
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    
    reply = response.choices[0].message.content
    print(f"ChatGPT: {reply}")
    
    messages.append({"role": "assistant", "content": reply})


# %%
import xml.etree.ElementTree as ET
import openai
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Initialize Appium driver
capabilities = {
    "platformName": "Android",
    "deviceName": "emulator-5554",  # Change as per your device
    "appPackage": "com.android.chrome",  # Change if using another app
    "appActivity": "com.google.android.apps.chrome.Main",
    "automationName": "UiAutomator2"
}
url = 'http://localhost:4723'

driver=webdriver.Remote(url,options=AppiumOptions().load_capabilities(capabilities))

def extract_ui_elements(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    ui_elements = []
    
    for element in root.iter():
        content_desc = element.attrib.get("content-desc", "")
        resource_id = element.attrib.get("resource-id", "")
        class_name = element.attrib.get("class", "")

        if content_desc or resource_id:
            ui_elements.append({
                "content-desc": content_desc,
                "resource-id": resource_id,
                "class": class_name
            })
    
    return ui_elements

# XML File Path
xml_file_path = "C:/Users/lenovo/Downloads/app-source-2025-03-28T03_54_46.626Z.xml"
ui_elements = extract_ui_elements(xml_file_path)

if not ui_elements:
    print("No UI elements found in the page source.")
    exit()

messages = [{"role": "system", "content": "You are a UI testing assistant. Answer based on the given page source."}]

while True:
    user_input = input("User: ")
    
    if user_input.lower() == "exit":
        print("Exiting chat...")
        break
    
    context = "Relevant UI elements: " + str(ui_elements[:5])
    full_prompt = f"{user_input}\n\n{context}"
    messages.append({"role": "user", "content": full_prompt})
    
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    
    reply = response.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
    
    # Extract actions from the response and perform them in Appium
    if "click on" in reply.lower():
        for element in ui_elements:
            if element["content-desc"] in reply or element["resource-id"] in reply:
                try:
                    element_to_click = driver.find_element(AppiumBy.ACCESSIBILITY_ID, element["content-desc"])
                    element_to_click.click()
                    print(f"Clicked on {element['content-desc']}")
                    break
                except:
                    pass
    
    if "search" in reply.lower():
        search_bar = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
        search_bar.send_keys("Trending books")
        search_bar.submit()
        print("Searched for trending books.")


# %%
import xml.etree.ElementTree as ET
import openai
from appium import webdriver
import time

# OpenAI API Key
OPENAI_API_KEY = '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'

# Appium Server and Device Capabilities
capabilities = {
    "platformName": "Android",
    "deviceName": "emulator-5554",  # Change this if needed
    "appPackage": "com.android.settings",  # Change this to target the desired app
    "appActivity": ".Settings",
    "automationName": "UiAutomator2"
}

# Initialize Appium Driver
url = 'http://localhost:4723'

driver=webdriver.Remote(url,options=AppiumOptions().load_capabilities(capabilities))

def get_current_page_source():
    """Fetch the current UI XML source from the running AVD."""
    page_source = driver.page_source
    return page_source

def extract_ui_elements(xml_source):
    """Parse XML and extract relevant UI elements."""
    root = ET.fromstring(xml_source)
    ui_elements = []

    for element in root.iter():
        content_desc = element.attrib.get("content-desc", "")
        resource_id = element.attrib.get("resource-id", "")
        class_name = element.attrib.get("class", "")

        if content_desc or resource_id:
            ui_elements.append({
                "content-desc": content_desc,
                "resource-id": resource_id,
                "class": class_name
            })
    
    return ui_elements

# OpenAI Prompt Setup
messages = [
    {"role": "system", "content": "You are a UI testing assistant. Answer based on the given page source."}
]

# Infinite Loop for Continuous Interaction
while True:
    # Fetch and process page source
    xml_source = get_current_page_source()
    ui_elements = extract_ui_elements(xml_source)

    if not ui_elements:
        print("No UI elements found on the current screen.")
        continue

    user_input = input("User: ")

    if user_input.lower() == "exit":
        print("Exiting chat...")
        break

    # Adding UI elements context to user input
    context = "Relevant UI elements: " + str(ui_elements[:5])  # Limiting to 5 elements for brevity
    full_prompt = f"{user_input}\n\n{context}"

    messages.append({"role": "user", "content": full_prompt})

    # AI Response
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    reply = response.choices[0].message.content
    print(f"ChatGPT: {reply}")

    messages.append({"role": "assistant", "content": reply})

# Quit Appium Driver
driver.quit()


# %%
"""
Tracing XML page source layout for using click action in the current page
"""

# %%
import xml.etree.ElementTree as ET
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import openai
import time
OPENAI_API_KEY = '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'
# Initialize Appium Driver (Change as per your AVD setup)
capabilities = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.android.settings",  # Default app (change as needed)
    "appActivity": ".Settings",
    "automationName": "UiAutomator2"
}

url = 'http://localhost:4723'

driver=webdriver.Remote(url,options=AppiumOptions().load_capabilities(capabilities))
# Function to get XML page source dynamically
def get_page_source():
    xml_source = driver.page_source
    return xml_source

# Function to extract UI elements dynamically
def extract_ui_elements(xml_source):
    root = ET.fromstring(xml_source)
    ui_elements = []

    for element in root.iter():
        content_desc = element.attrib.get("content-desc", "")
        resource_id = element.attrib.get("resource-id", "")
        class_name = element.attrib.get("class", "")
        text = element.attrib.get("text", "")

        if content_desc or resource_id or text:
            ui_elements.append({
                "content-desc": content_desc,
                "resource-id": resource_id,
                "text": text,
                "class": class_name
            })
    
    return ui_elements

# Function to perform action based on the user's prompt
def perform_navigation(prompt):
    # Get the latest XML page source
    xml_source = get_page_source()
    ui_elements = extract_ui_elements(xml_source)

    # Add the extracted UI elements as context
    context = f"Current UI Elements: {ui_elements[:5]}"  # Limit to 5 elements for brevity

    full_prompt = f"User Instruction: {prompt}\n\n{context}"

    # Send prompt to OpenAI
    messages = [{"role": "system", "content": "You are a UI automation assistant."},
                {"role": "user", "content": full_prompt}]

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    action = response.choices[0].message.content
    print(f"ChatGPT: {action}")

    # Find the UI element to interact with
    #mobile controller  code
    for element in ui_elements:
        if element["text"] and element["text"].lower() in action.lower():
            try:
                el = driver.find_element(AppiumBy.XPATH, f"//*[@text='{element['text']}']")
                el.click()
                print(f"✅ Navigated to: {element['text']}")
                return
            except Exception as e:
                print(f"⚠️ Unable to click: {element['text']} - {e}")

    print("⚠️ No matching UI element found for navigation.")

# Infinite loop for user prompts and navigation
while True:
    user_input = input("User: ")
    
    if user_input.lower() == "exit":
        print("Exiting...")
        break

    perform_navigation(user_input)
    time.sleep(2)  # Wait for the UI to update


# %%
Giving real time timestamp of the activities by tracking the current page source

# %%
import time
import json
from appium import webdriver
import openai
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions

# Initialize OpenAI API
openai.api_key = "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"

# Appium Desired Capabilities
capabilities = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.android.settings",  # Default app (change as needed)
    "appActivity": ".Settings",
    "automationName": "UiAutomator2"
}


url = 'http://localhost:4723'

driver=webdriver.Remote(url,options=AppiumOptions().load_capabilities(capabilities))

# Action logs storage
action_logs = []

def log_action(action):
    """Logs an action and saves it to a file."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {"time": timestamp, "action": action}
    action_logs.append(log_entry)

    # Save logs to a file
    with open("action_log.txt", "a") as log_file:
        log_file.write(json.dumps(log_entry) + "\n")
    
    print(f"[LOG] {timestamp} - {action}")

while True:
    # Get the current page source (XML)
    page_source = driver.page_source
    
    # User Prompt
    message = input("User: ")
    
    if message.lower() == "exit":
        break
    
    # Send prompt + XML to OpenAI
    messages = [
        {"role": "system", "content": "You are an assistant that guides Appium automation."},
        {"role": "user", "content": f"Current XML page source:\n{page_source}\n\nUser request: {message}"}
    ]
    
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    
    action_steps = response.choices[0].message.content
    
    # Log OpenAI's suggestion
    log_action(f"AI Suggested Steps: {action_steps}")
    
    # Simulate actions based on AI suggestion (example for clicking)
    if "click on" in action_steps.lower():
        element_id = "android:id/title"  # Example: Extracting an ID dynamically
        try:
            element = driver.find_element_by_id(element_id)
            element.click()
            log_action(f"Clicked on {element_id}")
        except Exception as e:
            log_action(f"Error: {str(e)}")
    
    time.sleep(2)  # Allow some time before fetching the new page source
    if message.lower() == "go back":
        driver.back()  # Simulate Android back button
        log_action("Navigated back")
        time.sleep(2)
        continue  # Skip OpenAI processing and go to the next input


print("Session Ended. Logs saved in action_log.txt.")
driver.quit()


# %%
import time
import json
from appium import webdriver
import openai
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
import os

capabilities = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.android.settings",  # Can be any package you navigate to
    "appActivity": ".Settings",
    "automationName": "UiAutomator2"
}

url = 'http://localhost:4723'

driver=webdriver.Remote(url,options=AppiumOptions().load_capabilities(capabilities))


# Ensure the emulator starts from the home screen
os.system("adb shell input keyevent 3")  # Press the Home button

# Now, Appium can begin navigation from the home screen
openai.api_key = "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"
action_logs = []

def log_action(action):
    """Logs an action and saves it to a file."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {"time": timestamp, "action": action}
    action_logs.append(log_entry)

    # Save logs to a file
    with open("navigation_log.txt", "a") as log_file:
        log_file.write(json.dumps(log_entry) + "\n")
    
    print(f"[LOG] {timestamp} - {action}")

while True:
    # Get the current page source (XML)
    page_source = driver.page_source
    log_action(f"Current Page Source: {page_source[:500]}...")  # Log truncated source
    
    # User Prompt
    message = input("User: ")
    
    if message.lower() == "exit":
        log_action("Session Ended by User")
        break
    
    # Send prompt + XML to OpenAI
    messages = [
        {"role": "system", "content": "You are an assistant that guides Appium automation."},
        {"role": "user", "content": f"Current XML page source:\n{page_source}\n\nUser request: {message}"}
    ]
    
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    
    action_steps = response.choices[0].message.content
    
    # Log OpenAI's suggestion
    log_action(f"AI Suggested Steps: {action_steps}")
    
    # Execute actions based on AI suggestion
    if "click on" in action_steps.lower():
        element_id = "android:id/title"  # Example: Extracting an ID dynamically
        try:
            element = driver.find_element_by_id(element_id)
            element.click()
            log_action(f"Clicked on {element_id}")
        except Exception as e:
            log_action(f"Error: {str(e)}")
    
    elif "go back" in action_steps.lower():
        try:
            driver.back()
            log_action("Navigated Back")
        except Exception as e:
            log_action(f"Error going back: {str(e)}")
    
    time.sleep(2)  # Allow some time before fetching the new page source

print("Session Ended. Logs saved in navigation_log.txt.")
driver.quit()


# %%
import time
import json
from appium import webdriver
import openai
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
# Initialize OpenAI API
openai.api_key = "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"

# Ensure the device starts from the home screen
import os
os.system("adb shell input keyevent 3")  # Press Home button

# Appium Desired Capabilities
capabilities = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.android.settings",  # Open Settings App
    "appActivity": ".Settings",
    "automationName": "UiAutomator2"  # Ensure the app doesn't reset every time
}

url = 'http://localhost:4723'

driver=webdriver.Remote(url,options=AppiumOptions().load_capabilities(capabilities))

# Action logs storage
action_logs = []

def log_action(action):
    """Logs an action and saves it to a file."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {"time": timestamp, "action": action}
    action_logs.append(log_entry)

    # Save logs to a file
    with open("navigation_log.txt", "a") as log_file:
        log_file.write(json.dumps(log_entry) + "\n")

    print(f"[LOG] {timestamp} - {action}")

while True:
    # Get the current page source (XML)
    page_source = driver.page_source
    log_action(f"Current Page Source: {page_source[:500]}...")  # Log truncated source

    # User Prompt
    message = input("User: ")

    if message.lower() == "exit":
        log_action("Session Ended by User")
        break

    # Send prompt + XML to OpenAI
    messages = [
        {"role": "system", "content": "You are an assistant that guides Appium automation."},
        {"role": "user", "content": f"Current XML page source:\n{page_source}\n\nUser request: {message}"}
    ]

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    action_steps =  response.choices[0].message.content

    # Log OpenAI's suggestion
    log_action(f"AI Suggested Steps: {action_steps}")

    # Execute actions dynamically based on AI suggestion
    if "click on" in action_steps.lower():
        try:
            # Extract element text from AI response
            element_text = action_steps.split("click on")[-1].strip().split("\n")[0]

            # Find the element using partial match for text
            element = driver.find_element(AppiumBy.XPATH, f"//android.widget.TextView[contains(@text, '{element_text}')]")
            element.click()
            log_action(f"Clicked on '{element_text}'")
        
        except Exception as e:
            log_action(f"Error: {str(e)}")

    elif "go back" in action_steps.lower():
        try:
            driver.back()
            log_action("Navigated Back")
        except Exception as e:
            log_action(f"Error going back: {str(e)}")

    elif "open home screen" in action_steps.lower():
        try:
            os.system("adb shell input keyevent 3")  # Press Home button
            log_action("Navigated to Home Screen")
        except Exception as e:
            log_action(f"Error going to home screen: {str(e)}")

    time.sleep(2)  # Allow some time before fetching the new page source

print("Session Ended. Logs saved in navigation_log.txt.")
driver.quit()


# %%
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import openai
import time
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
openai.api_key = "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"
capabilities= {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": "com.android.settings",  # Example for Settings app
        "appActivity": ".Settings",
        "automationName": "UiAutomator2"
    }
url = 'http://localhost:4723'

driver=webdriver.Remote(url,options=AppiumOptions().load_capabilities(capabilities))
def get_openai_response(prompt):
    response = openai.chat.completion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "You are a mobile UI assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def perform_touch_action(driver, action_type, element):
    touch = TouchAction(driver)
    if action_type == "tap":
        touch.tap(element).perform()
    elif action_type == "long_press":
        touch.long_press(element).release().perform()
    elif action_type == "swipe":
        driver.swipe(start_x=element.location["x"], start_y=element.location["y"],
                     end_x=element.location["x"] + 100, end_y=element.location["y"], duration=500)

def execute_prompt(driver, prompt):
    page_source = driver.page_source
    response = get_openai_response(f"Based on this page source: {page_source}, what action should I take for: {prompt}")
    
    if "tap" in response.lower():
        elements = driver.find_elements_by_xpath("//*[contains(@text, '" + prompt.split()[-1] + "')]")
        if elements:
            perform_touch_action(driver, "tap", elements[0])
    elif "swipe" in response.lower():
        perform_touch_action(driver, "swipe", driver.find_element_by_xpath("//*[contains(@text, 'Battery')]") )
    elif "long press" in response.lower():
        elements = driver.find_elements_by_xpath("//*[contains(@text, '" + prompt.split()[-1] + "')]")
        if elements:
            perform_touch_action(driver, "long_press", elements[0])
    else:
        print("No direct action found. Instruction: ", response)

if __name__ == "__main__":
    driver = initialize_driver()
    time.sleep(2)
    
    while True:
        user_input = input("Enter command: ")
        if user_input.lower() == "exit":
            break
        execute_prompt(driver, user_input)
    
    driver.quit()


# %%
from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
import openai
import time
from appium.options.common import AppiumOptions
openai.api_key = "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"
def initialize_driver():
    capabilities = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": "com.android.settings",  # Example for Settings app
        "appActivity": ".Settings",
        "automationName": "UiAutomator2"
    }
    url = 'http://localhost:4723'

    return webdriver.Remote(url,options=AppiumOptions().load_capabilities(capabilities))
def get_openai_response(prompt):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "You are a mobile UI assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def perform_action_chain(driver, action_type, element):
    actions = ActionChains(driver)
    pointer = PointerInput(PointerInput.INTERACTION_TOUCH, "touch")
    actions.w3c_actions.add_pointer_input(pointer)
    
    if action_type == "tap":
        actions.w3c_actions.pointer_action.move_to(element).pointer_down().pointer_up()
    elif action_type == "long_press":
        actions.w3c_actions.pointer_action.move_to(element).pointer_down()
        time.sleep(1)
        actions.w3c_actions.pointer_action.pointer_up()
    elif action_type == "swipe":
        start_x = element.location["x"]
        start_y = element.location["y"]
        end_x = start_x + 100  # Example swipe distance
        end_y = start_y
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        actions.w3c_actions.pointer_action.pointer_up()
    
    actions.perform()

def execute_prompt(driver, prompt):
    page_source = driver.page_source
    response = get_openai_response(f"Based on this page source: {page_source}, what action should I take for: {prompt}")
    
    if "tap" in response.lower():
        elements = driver.find_elements_by_xpath("//*[contains(@text, '" + prompt.split()[-1] + "')]")
        if elements:
            perform_action_chain(driver, "tap", elements[0])
    elif "swipe" in response.lower():
        perform_action_chain(driver, "swipe", driver.find_element_by_xpath("//*[contains(@text, 'Battery')]") )
    elif "long press" in response.lower():
        elements = driver.find_elements_by_xpath("//*[contains(@text, '" + prompt.split()[-1] + "')]")
        if elements:
            perform_action_chain(driver, "long_press", elements[0])
    else:
        print("No direct action found. Instruction: ", response)

if __name__ == "__main__":
    driver = initialize_driver()
    time.sleep(2)
    
    while True:
        user_input = input("Enter command: ")
        if user_input.lower() == "exit":
            break
        execute_prompt(driver, user_input)
    
    driver.quit()


# %%
from appium import webdriver
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import openai
import time
from appium.options.common import AppiumOptions
openai.api_key = "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"
# Initialize Appium driver
def initialize_driver():
    capabilities= {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": "com.android.settings",  # Change to launcher if you want home screen
        "appActivity": ".Settings",
        "automationName": "UiAutomator2"
    }
    url = 'http://localhost:4723'

    return webdriver.Remote(url,options=AppiumOptions().load_capabilities(capabilities))

# Use OpenAI to analyze the current page and suggest UI behavior
def get_llm_response(page_source, prompt):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You help automate mobile UI navigation. Based on the current XML page source, guide which UI gesture (swipe or tap) is needed to reach the destination."},
            {"role": "user", "content": f"Page source: {page_source[:4000]} \n\nUser wants to: {prompt}\n\nWhat gesture is needed (swipe down, tap 'Settings', etc.)?"}
        ]
    )
    return response.choices[0].message.content

# Perform swipe gesture using ActionChains
def swipe(driver, start_x, start_y, end_x, end_y, duration=500):
    finger = PointerInput(PointerInput.TOUCH, "finger")
    actions = ActionBuilder(driver, pointer_inputs=[finger])

    actions.pointer_action.move_to_location(start_x, start_y)
    actions.pointer_action.pointer_down()
    actions.pointer_action.pause(duration / 1000)
    actions.pointer_action.move_to_location(end_x, end_y)
    actions.pointer_action.pointer_up()

    actions.perform()
# Try tapping the closest matching element
def tap_on_text(driver, text):
    elements = driver.find_elements("xpath", f"//*[contains(@text, '{text}')]")
    if elements:
        elements[0].click()
        return True
    return False

# Main logic to parse and perform actions
def execute_prompt(driver, prompt):
    page_source = driver.page_source
    action = prompt.split()[0].lower()
    destination = prompt.split()[-1].capitalize()

    llm_reply = get_llm_response(page_source, prompt)
    print(f"LLM Suggestion: {llm_reply}")

    # If swipe is needed
    if "swipe down" in llm_reply.lower():
        size = driver.get_window_size()
        swipe(driver, size["width"] // 2, size["height"] // 3,
              size["width"] // 2, size["height"] * 3 // 4)

    # Then try tapping the element
    success = tap_on_text(driver, destination)
    if not success:
        print(f"[❌] Could not tap on '{destination}' after trying.")

# --- Run the system ---
if __name__ == "__main__":
    driver = initialize_driver()
    time.sleep(3)

    try:
        while True:
            user_input = input("🔎 Enter command (or 'exit'): ")
            if user_input.lower() == "exit":
                break
            execute_prompt(driver, user_input)
    finally:
        driver.quit()


# %%
!pip uninstall Appium-Python-Client


# %%
from appium.webdriver.common.actions.action_builder import ActionBuilder


# %%
pip install Appium-Python-Client==2.11.1

# %%
Appium-Python_client --version

# %%
Appium-Python-client --version

# %%
!pip show Appium-Python-Client

# %%
from appium import webdriver
from appium.webdriver.common.actions.action_builder import ActionBuilder

# %%
!pip install -U selenium

# %%
import selenium
print(selenium.__version__)


# %%
from appium import webdriver
from appium.webdriver.common.actions.action_builder import ActionBuilder

# %%
from appium import webdriver
from appium.webdriver.common.actions.action_builder import ActionBuilder
from appium.webdriver.common.actions.pointer_input import PointerInput


# %%
from appium import webdriver
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


# %%
from appium import webdriver
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import openai
import time
import os
import re
from appium.options.common import AppiumOptions
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
# Initialize Appium driver
def initialize_driver():
    capabilities= {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": "com.android.settings",  # Change to launcher if you want home screen
        "appActivity": ".Settings",
        "automationName": "UiAutomator2"
    }
    url = 'http://localhost:4723'

    return webdriver.Remote(url,options=AppiumOptions().load_capabilities(capabilities))
# Use OpenAI to analyze the current page and suggest UI behavior
def get_llm_response(page_source, prompt):
    try:
        # Get API key from environment variable or set it directly
        api_key = os.environ.get("OPENAI_API_KEY") or "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"
        openai.api_key = api_key
        
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # Updated to use valid model name
            messages=[
                {"role": "system", "content": "You help automate mobile UI navigation. Based on the current XML page source, guide which UI gesture (swipe or tap) is needed to reach the destination."},
                {"role": "user", "content": f"Page source: {page_source[:4000]} \n\nUser wants to: {prompt}\n\nWhat gesture is needed (swipe down, tap 'Settings', etc.)?"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error getting LLM response: {e}")
        return "Error communicating with LLM service"

# Perform swipe gesture using ActionBuilder
def swipe(driver, start_x, start_y, end_x, end_y, duration=500):
    finger = PointerInput(POINTER_TOUCH, "finger") 
    actions = ActionBuilder(driver, pointer_inputs=[finger])
    actions.pointer_action.move_to_location(start_x, start_y)
    actions.pointer_action.pointer_down()
    actions.pointer_action.pause(duration / 1000)
    actions.pointer_action.move_to_location(end_x, end_y)
    actions.pointer_action.pointer_up()
    actions.perform()

# Try tapping the closest matching element with multiple strategies
def tap_on_text(driver, text):
    # Try exact match
    elements = driver.find_elements("xpath", f"//*[@text='{text}']")
    if elements:
        elements[0].click()
        print(f"[✓] Tapped exact match: '{text}'")
        return True

    # Try contains match
    elements = driver.find_elements("xpath", f"//*[contains(@text, '{text}')]")
    if elements:
        elements[0].click()
        print(f"[✓] Tapped partial match: '{elements[0].text}'")
        return True

    # Try case-insensitive match
    elements = driver.find_elements("xpath", f"//*[translate(@text, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')=translate('{text}', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')]")
    if elements:
        elements[0].click()
        print(f"[✓] Tapped case-insensitive match: '{elements[0].text}'")
        return True

    # Try resource-id containing the text
    elements = driver.find_elements("xpath", f"//*[contains(@resource-id, '{text.lower()}')]")
    if elements:
        elements[0].click()
        print(f"[✓] Tapped element with matching resource-id")
        return True

    print(f"[❌] Could not find any element matching '{text}'")
    return False

# Main logic to parse and perform actions
def execute_prompt(driver, prompt):
    try:
        page_source = driver.page_source
        llm_reply = get_llm_response(page_source, prompt)
        print(f"LLM Suggestion: {llm_reply}")
        
        # Extract destination from prompt or LLM response
        destination_match = re.search(r'tap [\'"]?([^\'"]+)[\'"]?', llm_reply, re.IGNORECASE)
        destination = destination_match.group(1) if destination_match else prompt.split()[-1]
        
        # Check if swipe is needed based on LLM response
        if "swipe down" in llm_reply.lower() or "scroll down" in llm_reply.lower():
            print("Performing swipe down gesture")
            size = driver.get_window_size()
            # Corrected swipe direction (bottom to top = scroll down)
            swipe(driver, size["width"] // 2, size["height"] * 3 // 4,
                  size["width"] // 2, size["height"] // 3)
            time.sleep(1)  # Wait for scroll to complete
        
        if "swipe up" in llm_reply.lower() or "scroll up" in llm_reply.lower():
            print("Performing swipe up gesture")
            size = driver.get_window_size()
            # Top to bottom = scroll up
            swipe(driver, size["width"] // 2, size["height"] // 3,
                  size["width"] // 2, size["height"] * 3 // 4)
            time.sleep(1)  # Wait for scroll to complete
        
        # Try tapping the element
        if "tap" in llm_reply.lower():
            success = tap_on_text(driver, destination)
            if not success:
                print(f"Trying alternative tap strategies for '{destination}'")
                # If direct tap failed, try other approaches based on LLM response
                if not tap_on_text(driver, destination.capitalize()) and not tap_on_text(driver, destination.lower()):
                    print(f"[❌] All tap strategies failed for '{destination}'")
    except Exception as e:
        print(f"Error executing prompt: {e}")

# --- Run the system ---
if __name__ == "__main__":
    driver = None
    try:
        print("Initializing Appium driver...")
        driver = initialize_driver()
        time.sleep(3)
        print("Ready for commands!")
        
        while True:
            user_input = input("🔎 Enter command (or 'exit'): ")
            if user_input.lower() == "exit":
                break
            execute_prompt(driver, user_input)
    except Exception as e:
        print(f"Unhandled error: {e}")
    finally:
        if driver:
            print("Closing driver...")
            driver.quit()

# %%
from appium import webdriver
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import openai
import time
import os
import re
from appium.options.common import AppiumOptions
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
# Initialize Appium driver
def initialize_driver():
    capabilities= {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": "com.android.settings",  # Change to launcher if you want home screen
        "appActivity": ".Settings",
        "automationName": "UiAutomator2"
    }
    url = 'http://localhost:4723'

    return webdriver.Remote(url, options=AppiumOptions().load_capabilities(capabilities))
# Use OpenAI to analyze the current page and suggest UI behavior
def get_llm_response(page_source, prompt):
    try:
        # Get API key from environment variable or set it directly
        api_key = os.environ.get("OPENAI_API_KEY") or "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"
        openai.api_key = api_key
        
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # Updated to use valid model name
            messages=[
                {"role": "system", "content": "You help automate mobile UI navigation. Based on the current XML page source, guide which UI gesture (swipe or tap) is needed to reach the destination."},
                {"role": "user", "content": f"Page source: {page_source[:4000]} \n\nUser wants to: {prompt}\n\nWhat gesture is needed (swipe down, tap 'Settings', etc.)?"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error getting LLM response: {e}")
        return "Error communicating with LLM service"

# Perform swipe gesture using ActionBuilder
def swipe(driver, start_x, start_y, end_x, end_y, duration=500):
    try:
        # Method 1: Using ActionBuilder with POINTER_TOUCH
        finger = PointerInput(POINTER_TOUCH, "finger") 
        actions = ActionBuilder(driver, pointer_inputs=[finger])
        actions.pointer_action.move_to_location(start_x, start_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pause(duration / 1000)
        actions.pointer_action.move_to_location(end_x, end_y)
        actions.pointer_action.pointer_up()
        actions.perform()
    except Exception as e:
        print(f"Error with ActionBuilder swipe: {e}")
        try:
            # Method 2: Using Appium's mobile command
            if end_y < start_y:
                direction = 'up'  # Swipe up (scroll down)
            else:
                direction = 'down'  # Swipe down (scroll up)
            driver.execute_script('mobile: swipe', {'direction': direction})
        except Exception as e2:
            print(f"Error with mobile: swipe command: {e2}")
            try:
                # Method 3: Using TouchAction (legacy but sometimes works)
                from appium.webdriver.common.touch_action import TouchAction
                actions = TouchAction(driver)
                actions.press(x=start_x, y=start_y).wait(duration).move_to(x=end_x, y=end_y).release().perform()
            except Exception as e3:
                print(f"All swipe methods failed: {e3}")

# Try tapping the closest matching element with multiple strategies
def tap_on_text(driver, text):
    # Try exact match
    elements = driver.find_elements("xpath", f"//*[@text='{text}']")
    if elements:
        elements[0].click()
        print(f"[✓] Tapped exact match: '{text}'")
        return True

    # Try contains match
    elements = driver.find_elements("xpath", f"//*[contains(@text, '{text}')]")
    if elements:
        elements[0].click()
        print(f"[✓] Tapped partial match: '{elements[0].text}'")
        return True

    # Try case-insensitive match
    elements = driver.find_elements("xpath", f"//*[translate(@text, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')=translate('{text}', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')]")
    if elements:
        elements[0].click()
        print(f"[✓] Tapped case-insensitive match: '{elements[0].text}'")
        return True

    # Try resource-id containing the text
    elements = driver.find_elements("xpath", f"//*[contains(@resource-id, '{text.lower()}')]")
    if elements:
        elements[0].click()
        print(f"[✓] Tapped element with matching resource-id")
        return True

    print(f"[❌] Could not find any element matching '{text}'")
    return False

# Main logic to parse and perform actions
def execute_prompt(driver, prompt):
    try:
        page_source = driver.page_source
        llm_reply = get_llm_response(page_source, prompt)
        print(f"LLM Suggestion: {llm_reply}")
        
        # Extract destination from prompt or LLM response
        destination_match = re.search(r'tap [\'"]?([^\'"]+)[\'"]?', llm_reply, re.IGNORECASE)
        destination = destination_match.group(1) if destination_match else prompt.split()[-1]
        
        # Check if swipe is needed based on LLM response
        if "swipe down" in llm_reply.lower() or "scroll down" in llm_reply.lower():
            print("Performing swipe down gesture")
            size = driver.get_window_size()
            # Corrected swipe direction (bottom to top = scroll down)
            swipe(driver, size["width"] // 2, size["height"] * 3 // 4,
                  size["width"] // 2, size["height"] // 3)
            time.sleep(1)  # Wait for scroll to complete
        
        if "swipe up" in llm_reply.lower() or "scroll up" in llm_reply.lower():
            print("Performing swipe up gesture")
            size = driver.get_window_size()
            # Top to bottom = scroll up
            swipe(driver, size["width"] // 2, size["height"] // 3,
                  size["width"] // 2, size["height"] * 3 // 4)
            time.sleep(1)  # Wait for scroll to complete
        
        # Try tapping the element
        if "tap" in llm_reply.lower():
            success = tap_on_text(driver, destination)
            if not success:
                print(f"Trying alternative tap strategies for '{destination}'")
                # If direct tap failed, try other approaches based on LLM response
                if not tap_on_text(driver, destination.capitalize()) and not tap_on_text(driver, destination.lower()):
                    print(f"[❌] All tap strategies failed for '{destination}'")
    except Exception as e:
        print(f"Error executing prompt: {e}")

# --- Run the system ---
if __name__ == "__main__":
    driver = None
    try:
        print("Initializing Appium driver...")
        driver = initialize_driver()
        time.sleep(3)
        print("Ready for commands!")
        
        while True:
            user_input = input("🔎 Enter command (or 'exit'): ")
            if user_input.lower() == "exit":
                break
            execute_prompt(driver, user_input)
    except Exception as e:
        print(f"Unhandled error: {e}")
    finally:
        if driver:
            print("Closing driver...")
            driver.quit()

# %%
from appium.webdriver.common.touch_action import TouchAction

# %%
"""
one fault i find here in the code is that when i give the prompt it results accordingly making the new page source as now its current page source but when i give another prompt it only sticks to that page source not changing 
"""

# %%
import xml.etree.ElementTree as ET
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import openai
import time
import re
from appium.options.common import AppiumOptions
from appium.webdriver.common.touch_action import TouchAction
openai.api_key = "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"
# --- Init Appium Driver ---
capabilities = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.android.settings",
    "appActivity": ".Settings",
    "automationName": "UiAutomator2"
}

url = 'http://localhost:4723'

driver=webdriver.Remote(url, options=AppiumOptions().load_capabilities(capabilities))

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
    return ui_elements[:5]  # Limit context

def parse_action(response_text):
    if "tap" in response_text.lower():
        match = re.search(r"'(.*?)'", response_text)
        if match:
            return {"action": "tap", "target_text": match.group(1)}
    elif "scroll" in response_text.lower():
        match = re.search(r"'(.*?)'", response_text)
        if match:
            return {"action": "scroll_and_tap", "target_text": match.group(1)}
    return None

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

    elif plan["action"] == "scroll_and_tap":
        scroll_and_tap(target_text)

def scroll_and_tap(text):
    try:
        scrollable = 'new UiScrollable(new UiSelector().scrollable(true))'
        scroll_cmd = f'{scrollable}.scrollIntoView(new UiSelector().text("{text}"))'
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scroll_cmd).click()
        print(f"✅ Scrolled and tapped: {text}")
    except Exception as e:
        print(f"❌ Scroll and tap failed: {e}")

# --- Main Controller Logic ---

def execute_ui_navigation(user_prompt):
    xml = get_page_source()
    ui_elements = extract_ui_elements(xml)

    context = f"Current screen elements:\n" + "\n".join(
        [f"{el['text']} - {el['resource-id']} - {el['content-desc']}" for el in ui_elements]
    )

    full_prompt = (
        f"You are a UI automation assistant. Based on the user's task, "
        f"respond with the action to perform on the mobile UI.\n"
        f"Example response: Tap on 'Wi-Fi'\n\n"
        f"User Task: {user_prompt}\n\n{context}"
    )

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": full_prompt}] # Replace with your valid key
    )

    instruction = response.choices[0].message.content.strip()
    print(f"Sovan GPT says: {instruction}")

    plan = parse_action(instruction)
    if plan:
        perform_action(plan)
    else:
        print("⚠️ Could not parse action plan.")

# --- Prompt Loop ---
while True:
    user_prompt = input("Your Task (or 'exit'): ")
    if user_prompt.lower() == "exit":
        break
    execute_ui_navigation(user_prompt)
    time.sleep(2)


# %%
"""
Multi Navigation Automated UI Elements
"""

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


# %%
!pip install -q openai

# %%
pip install Appium-Python-Client==0.24

# %%
pip install selenium==3.5.0

# %%
import openai
from appium import webdriver
import time
import re
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
openai.api_key = "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"  # Replace with your OpenAI API key

# Start WinAppDriver if not already running
os.system('start "" "C:\\Program Files (x86)\\Windows Application Driver\\WinAppDriver.exe"')

# WinAppDriver capabilities (e.g., Notepad)
caps = {
    "platformName": "Windows",
    "deviceName": "WindowsPC",
    "app": "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"  # Or "Root" to attach to any open app
}

driver = webdriver.Remote("http://127.0.0.1:4723", caps)

# Helper: Parse actions from GPT response
def parse_windows_action(response_text):
    match = re.search(r"(click|type|select|press|close)\s+['\"](.*?)['\"]", response_text, re.IGNORECASE)
    if match:
        return {
            "action": match.group(1).lower(),
            "target_text": match.group(2)
        }
    return None

# Perform actions on Windows UI
def perform_windows_action(plan):
    try:
        if plan["action"] == "click":
            el = driver.find_element("name", plan["target_text"])
            el.click()
            print(f"✅ Clicked: {plan['target_text']}")

        elif plan["action"] == "type":
                    try:
                        el = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CLASS_NAME, "Edit"))
                        )
                        el.send_keys(plan["target_text"])
                        print(f"✅ Typed into edit field: {plan['target_text']}")
                    except Exception as e:
                        print(f"❌ Typing failed: {e}")


        elif plan["action"] == "close":
            driver.quit()
            print("✅ Application closed")

    except Exception as e:
        print(f"❌ Failed to perform action: {e}")

# Main controller
def execute_windows_prompt(user_prompt):
    page_source = driver.page_source  # Not used directly but gives structure

    # Prompt OpenAI
    prompt = (
        f"You are a Windows desktop automation assistant. A user has launched Windows Calculator and says: {user_prompt}.\n"
        f"Respond with an instruction like: click 'numbers and functions as seen in the calculator', or close 'Calculator'."
    )

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    instruction = response.choices[0].message.content.strip()
    print(f"Sovan GPT says:\n{instruction}")

    plan = parse_windows_action(instruction)
    if plan:
        perform_windows_action(plan)
    else:
        print("⚠️ No actionable step found.")

# Infinite loop for user interaction
while True:
    cmd = input("🧠 Your Windows command (or 'exit'): ")
    if cmd.lower() == "exit":
        driver.quit()
        break
    execute_windows_prompt(cmd)
    time.sleep(2)


# %%
import openai
from appium import webdriver
from appium.webdriver.common.actions.action_builder import ActionBuilder
from appium.webdriver.common.actions.key_input import KeyInput
import time
import re
import os

# 🔐 Set OpenAI API Key
openai.api_key = "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"  # Replace with your actual key

# 🚀 Start WinAppDriver
os.system('start "" "C:\\Program Files (x86)\\Windows Application Driver\\WinAppDriver.exe"')
time.sleep(3)

# 📲 Desired Capabilities for Notepad
caps = {
    "platformName": "Windows",
    "deviceName": "WindowsPC",
    "app": "C:\\Windows\\System32\\notepad.exe"
}

driver = webdriver.Remote("http://127.0.0.1:4723", caps)

# 🧠 Parse action instruction from GPT
def parse_windows_action(response_text):
    match = re.search(r"(click|type|select|press|close)\s+['\"](.*?)['\"]", response_text, re.IGNORECASE)
    if match:
        return {
            "action": match.group(1).lower(),
            "target_text": match.group(2)
        }
    return None

# 🛠 Perform the action
def perform_windows_action(plan):
    try:
        if plan["action"] == "click":
            el = driver.find_element("name", plan["target_text"])
            el.click()
            print(f"✅ Clicked: {plan['target_text']}")

        elif plan["action"] == "type":
            keyboard = KeyInput("keyboard")
            actions = ActionBuilder(driver)
            actions.add_key_input(keyboard)

            for char in plan["target_text"]:
                actions.key_action.key_down(char).key_up(char)
            actions.perform()

            print(f"✅ Typed using keys: {plan['target_text']}")

        elif plan["action"] == "close":
            driver.quit()
            print("✅ Application closed")

    except Exception as e:
        print(f"❌ Failed to perform action: {e}")

# 💬 Main control loop
def execute_windows_prompt(user_prompt):
    prompt = (
        f"You are a Windows desktop automation assistant. The user says: {user_prompt}. "
        f"Respond with an instruction like: click 'File', type 'Hello world', or close 'Notepad'."
    )

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    instruction = response.choices[0].message.content.strip()
    print(f"\n🤖 Sovan GPT says: {instruction}")

    plan = parse_windows_action(instruction)
    if plan:
        perform_windows_action(plan)
    else:
        print("⚠️ Could not interpret any actionable command.")

# 🧠 Start assistant
while True:
    cmd = input("\n🧠 Your Windows command (or 'exit'): ")
    if cmd.lower() == "exit":
        driver.quit()
        break
    execute_windows_prompt(cmd)
    time.sleep(2)


# %%
import openai
from appium import webdriver
import time
import re
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

# ─── Configuration ─────────────────────────────────────────────────────────────

# 1) Your OpenAI key
openai.api_key = "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"

# 2) WinAppDriver executable path
WINAPPDRIVER_PATH = r"C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe"

# 3) Timeout for element waits
DEFAULT_TIMEOUT = 10


# ─── Startup ───────────────────────────────────────────────────────────────────

# Launch WinAppDriver (if not already running)
os.system(f'start "" "{WINAPPDRIVER_PATH}"')
time.sleep(2)

# Start a "Root" session to discover all top-level windows
caps_root = {
    "platformName": "Windows",
    "deviceName": "WindowsPC",
    "app": "Root"
}
driver = webdriver.Remote("http://127.0.0.1:4723", caps_root)


# ─── Helper Functions ──────────────────────────────────────────────────────────

def list_windows():
    """Return list of (handle, title) for each open window."""
    handles = driver.window_handles
    windows = []
    for h in handles:
        driver.switch_to.window(h)
        windows.append((h, driver.title))
    driver.switch_to.window(handles[0])
    return windows

def attach_to_window(name_substr: str) -> bool:
    """
    Attach the driver to the first window whose title contains name_substr.
    Returns True if found, False otherwise.
    """
    for handle, title in list_windows():
        if name_substr.lower() in title.lower():
            driver.switch_to.window(handle)
            time.sleep(1)  # allow UI to settle
            return True
    return False

def parse_windows_action(text: str):
    """
    From GPT’s reply extract {"action": "...", "target": "..."}.
    Supports click/type/close.
    """
    match = re.search(r"(click|type|close)\s+['\"](.+?)['\"]", text, re.IGNORECASE)
    if not match:
        return None
    return {"action": match.group(1).lower(), "target": match.group(2)}

def perform_windows_action(plan: dict):
    """Execute the parsed action on the currently attached window."""
    action = plan["action"]
    targ   = plan["target"]

    try:
        if action == "click":
            el = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                EC.element_to_be_clickable((By.NAME, targ))
            )
            el.click()
            print(f"✅ Clicked '{targ}'")

        elif action == "type":
            # Try an Edit control first
            try:
                edit = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "Edit"))
                )
                edit.send_keys(targ)
                print(f"✅ Typed via send_keys: '{targ}'")
            except:
                # Fallback to system keyboard
                time.sleep(0.5)
                pyautogui.write(targ)
                print(f"✅ Typed via pyautogui: '{targ}'")

        elif action == "close":
            driver.close()
            print("✅ Closed current window")

    except Exception as e:
        print(f"❌ Action '{action}' on '{targ}' failed: {e}")


# ─── Main Controller ──────────────────────────────────────────────────────────

print("🧠 Windows Automation Assistant (type 'exit' to quit)\n")

while True:
    cmd = input("Command (e.g. open notepad, click 'OK', type 'Hello', close app): ").strip()
    if cmd.lower() == "exit":
        driver.quit()
        break

    # 1) If user says "open X" → attach to that window
    m = re.match(r"open\s+(.+)", cmd, re.IGNORECASE)
    if m:
        app_name = m.group(1)
        if attach_to_window(app_name):
            print(f"✅ Attached to window containing '{app_name}'")
        else:
            print(f"⚠️ No window found for '{app_name}'")
        continue

    # 2) Otherwise, send to GPT for click/type/close planning
    prompt = (
        f"You are a Windows automation assistant. The user says: {cmd}. "
        f"Respond with 'click \"Name\"', 'type \"text\"', or 'close \"app\"'."
    )
    resp =openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    instruction = resp.choices[0].message.content.strip()
    print(f"GPT → {instruction}")

    plan = parse_windows_action(instruction)
    if plan:
        perform_windows_action(plan)
    else:
        print("⚠️ Could not parse any actionable instruction.")

    time.sleep(1)


# %%
!pip install pyautogui

# %%
import openai
from appium import webdriver
import time
import re
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ─── Configuration ─────────────────────────────────────────────────────────────

# 1) Your OpenAI key
openai.api_key = "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"

# 2) WinAppDriver path (adjust if necessary)
WINAPPDRIVER_PATH = r"C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe"

# 3) How long to wait for element lookups
DEFAULT_TIMEOUT = 10

# ─── Startup ───────────────────────────────────────────────────────────────────

# Launch WinAppDriver if not running
os.system(f'start "" "{WINAPPDRIVER_PATH}"')
time.sleep(2)

# Start a "Root" session that allows discovering any top-level window
caps_root = {
    "platformName": "Windows",
    "deviceName": "WindowsPC",
    "app": "Root",
}
driver = webdriver.Remote("http://127.0.0.1:4723", caps_root)

# ─── Helpers ──────────────────────────────────────────────────────────────────

def list_windows():
    """Return a list of tuples (handle, name) of all top-level windows."""
    handles = driver.window_handles
    windows = []
    for h in handles:
        driver.switch_to.window(h)
        name = driver.title or driver.current_window_handle
        windows.append((h, name))
    # switch back to root
    driver.switch_to.window(handles[0])
    return windows

def attach_to_window(name_substring):
    """
    Switch the driver to the first top-level window whose title contains
    name_substring (case-insensitive). Returns True on success.
    """
    for handle, title in list_windows():
        if name_substring.lower() in title.lower():
            driver.switch_to.window(handle)
            time.sleep(1)
            return True
    return False

def parse_action(text):
    """
    Extract an action dict from GPT’s response, e.g.
    "click 'OK'" → {action:'click', target:'OK'}
    """
    m = re.search(r"(click|type|close)\s+['\"](.+?)['\"]", text, re.IGNORECASE)
    if not m:
        return None
    return { "action": m.group(1).lower(), "target": m.group(2) }

def click(name):
    # wait then click by its Name attribute
    el = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable((By.NAME, name))
    )
    el.click()

def type_text(text):
    # fallback: try sending to a class-name Edit control
    try:
        el = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Edit"))
        )
        el.send_keys(text)
    except:
        # last-resort: use pyautogui for system-wide typing
        import pyautogui
        time.sleep(0.5)
        pyautogui.write(text)

def close_app():
    driver.close()  # closes current window
    time.sleep(0.5)

# ─── Main Loop ────────────────────────────────────────────────────────────────

print("🤖 Desktop Automation Assistant (type 'exit' to quit)")
while True:
    cmd = input("\nEnter command (e.g. \"open notepad\", \"click 'OK'\", \"type 'Hello'\", \"close app\"): ").strip()
    if cmd.lower() == "exit":
        driver.quit()
        break

    # If the user says "open X", we attach to that window
    m_open = re.match(r"open\s+(.+)", cmd, re.IGNORECASE)
    if m_open:
        app_name = m_open.group(1).strip()
        success = attach_to_window(app_name)
        print("✅ Attached to:", app_name if success else f"No window found matching '{app_name}'")
        continue

    # Otherwise, parse it as an in-app action
    action = parse_action(cmd)
    if not action:
        print("⚠️ Could not parse action. Try: click 'OK', type 'Hello', or close 'app'.")
        continue

    # Execute action on the currently attached window
    if action["action"] == "click":
        click(action["target"])
        print(f"✅ Clicked '{action['target']}'")
    elif action["action"] == "type":
        type_text(action["target"])
        print(f"✅ Typed '{action['target']}'")
    elif action["action"] == "close":
        close_app()
        print("✅ Closed current app")



# %%
"""
import xml.etree.ElementTree as ET
import openai
import time
import re
import os
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

# ─── CONFIG ────────────────────────────────────────────────────────────────
openai.api_key = "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"
WINAPPDRIVER_PATH = r"C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe"
DEFAULT_TIMEOUT = 10

# ─── STARTUP ────────────────────────────────────────────────────────────────
os.system(f'start "" "{WINAPPDRIVER_PATH}"')
time.sleep(2)

# Launch “Root” session so we can attach to any window
caps = {
    "platformName": "Windows",
    "deviceName": "WindowsPC",
    "app": "Root"
}
driver = webdriver.Remote("http://127.0.0.1:4723", caps)

# ─── HELPERS ────────────────────────────────────────────────────────────────

def get_page_source():
    """Fetch live XML of the current window."""
    return driver.page_source

def extract_ui_elements(xml_source, limit=5):
    """Parse XML and return up to `limit` element names/AutomationIds."""
    root = ET.fromstring(xml_source)
    elems = []
    for el in root.iter():
        name = el.attrib.get("Name") or el.attrib.get("AutomationId")
        if name and name.strip():
            elems.append(name.strip())
        if len(elems) >= limit:
            break
    return elems

def parse_steps(gpt_reply):
    """
    Extract actions like click 'X' or type 'Y' from GPT reply.
    Returns list of dicts: [{"action":"click","target":"X"}, ...]
    """
    steps = []
    for line in gpt_reply.splitlines():
        m = re.search(r"(click|type)\s+'(.+?)'", line, re.IGNORECASE)
        if m:
            steps.append({"action": m.group(1).lower(), "target": m.group(2)})
    return steps

def perform_step(step):
    """Execute a single click or type action."""
    act, tgt = step["action"], step["target"]
    try:
        if act == "click":
            el = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                EC.element_to_be_clickable((By.NAME, tgt))
            )
            el.click()
            print(f"✅ Clicked '{tgt}'")

        elif act == "type":
            # try a text box
            try:
                tb = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "Edit"))
                )
                tb.send_keys(tgt)
                print(f"✅ Typed '{tgt}' via send_keys")
            except:
                # fallback
                time.sleep(0.5)
                pyautogui.write(tgt)
                print(f"✅ Typed '{tgt}' via pyautogui")

    except Exception as e:
        print(f"❌ Failed {act} '{tgt}': {e}")

# ─── MAIN CONTROLLER ────────────────────────────────────────────────────────

print("🔹 Windows NLP UI Automation (type 'exit' to quit)\n")

while True:
    user_cmd = input("Your Task: ").strip()
    if user_cmd.lower() == "exit":
        driver.quit()
        break

    # 1) Get current UI context
    xml = get_page_source()
    sample = extract_ui_elements(xml)

    # 2) Build GPT prompt
    prompt = (
        f"You are a Windows automation assistant. The current window has these elements:\n"
        f"{sample}\n\n"
        f"User request: {user_cmd}\n"
        f"List each action as `click 'Name'` or `type 'Text'`, one per line."
    )

    # 3) Call GPT
    resp = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user", "content":prompt}]
    )
    instructions = resp.choices[0].message.content.strip()
    print(f"\nGPT suggests:\n{instructions}\n")

    # 4) Parse & execute
    steps = parse_steps(instructions)
    if not steps:
        print("⚠️ No actionable steps parsed.\n")
        continue

    for step in steps:
        perform_step(step)
        time.sleep(1)  # pause between steps

    print()  # blank line before next prompt

"""

# %%
import xml.etree.ElementTree as ET
import openai
import time
import re
import os
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

# ─── CONFIG ────────────────────────────────────────────────────────────────
openai.api_key = "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"
WINAPPDRIVER_PATH = r"C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe"
DEFAULT_TIMEOUT = 10

# ─── STARTUP ────────────────────────────────────────────────────────────────
os.system(f'start "" "{WINAPPDRIVER_PATH}"')
time.sleep(2)

# Launch “Root” session so we can attach to any window
caps = {
    "platformName": "Windows",
    "deviceName": "WindowsPC",
    "app": "Root"
}
driver = webdriver.Remote("http://127.0.0.1:4723", caps)

# ─── HELPERS ────────────────────────────────────────────────────────────────

def get_page_source():
    """Fetch live XML of the current window."""
    return driver.page_source

def extract_ui_elements(xml_source, limit=5):
    """Parse XML and return up to `limit` element names/AutomationIds."""
    root = ET.fromstring(xml_source)
    elems = []
    for el in root.iter():
        name = el.attrib.get("Name") or el.attrib.get("AutomationId")
        if name and name.strip():
            elems.append(name.strip())
        if len(elems) >= limit:
            break
    return elems

def parse_steps(gpt_reply):
    """
    Extract actions like click 'X' or type 'Y' from GPT reply.
    Returns list of dicts: [{"action":"click","target":"X"}, ...]
    """
    steps = []
    for line in gpt_reply.splitlines():
        m = re.search(r"(click|type)\s+'(.+?)'", line, re.IGNORECASE)
        if m:
            steps.append({"action": m.group(1).lower(), "target": m.group(2)})
    return steps

def perform_step(step):
    """Execute a single click or type action."""
    act, tgt = step["action"], step["target"]
    try:
        if act == "click":
            el = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                EC.element_to_be_clickable((By.NAME, tgt))
            )
            el.click()
            print(f"✅ Clicked '{tgt}'")

        elif act == "type":
            # try a text box
            try:
                tb = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "Edit"))
                )
                tb.send_keys(tgt)
                print(f"✅ Typed '{tgt}' via send_keys")
            except:
                # fallback
                time.sleep(0.5)
                pyautogui.write(tgt)
                print(f"✅ Typed '{tgt}' via pyautogui")

    except Exception as e:
        print(f"❌ Failed {act} '{tgt}': {e}")

# ─── MAIN CONTROLLER ────────────────────────────────────────────────────────

print("🔹 Windows NLP UI Automation (type 'exit' to quit)\n")

while True:
    user_cmd = input("Your Task: ").strip()
    if user_cmd.lower() == "exit":
        driver.quit()
        break

    # 1) Get current UI context
    xml = get_page_source()
    sample = extract_ui_elements(xml)

    # 2) Build GPT prompt
    prompt = (
        f"You are a Windows automation assistant. The current window has these elements:\n"
        f"{sample}\n\n"
        f"User request: {user_cmd}\n"
        f"List each action as `click 'Name'` or `type 'Text'`, one per line."
    )

    # 3) Call GPT
    resp = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user", "content":prompt}]
    )
    instructions = resp.choices[0].message.content.strip()
    print(f"\nGPT suggests:\n{instructions}\n")

    # 4) Parse & execute
    steps = parse_steps(instructions)
    if not steps:
        print("⚠️ No actionable steps parsed.\n")2+3
        continue

    for step in steps:
        perform_step(step)
        time.sleep(1)  # pause between steps

    print()  # blank line before next prompt


# %%
import xml.etree.ElementTree as ET
import openai
import time
import re
import os
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

# ─── CONFIG ────────────────────────────────────────────────────────────────
openai.api_key = "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"
WINAPPDRIVER_PATH = r"C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe"
DEFAULT_TIMEOUT = 10

# ─── STARTUP ────────────────────────────────────────────────────────────────
os.system(f'start "" "{WINAPPDRIVER_PATH}"')
time.sleep(2)

# Launch “Root” session so we can attach to any window
caps = {"platformName": "Windows", "deviceName": "WindowsPC", "app": "Root"}
driver = webdriver.Remote("http://127.0.0.1:4723", caps)

# ─── HELPERS ────────────────────────────────────────────────────────────────

def get_page_source():
    return driver.page_source

def extract_ui_elements(xml_source, limit=5):
    root = ET.fromstring(xml_source)
    elems = []
    for el in root.iter():
        name = el.attrib.get("Name") or el.attrib.get("AutomationId")
        if name and name.strip():
            elems.append(name.strip())
        if len(elems) >= limit:
            break
    return elems

def parse_steps(gpt_reply):
    steps = []
    for line in gpt_reply.splitlines():
        m = re.search(r"(click|type)\s+'(.+?)'", line, re.IGNORECASE)
        if m:
            steps.append({"action": m.group(1).lower(), "target": m.group(2)})
    return steps

def perform_step(step):
    act, tgt = step["action"], step["target"]
    try:
        if act == "click":
            el = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                EC.element_to_be_clickable((By.NAME, tgt))
            )
            el.click(); print(f"✅ Clicked '{tgt}'")
        elif act == "type":
            try:
                tb = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "Edit"))
                )
                tb.send_keys(tgt); print(f"✅ Typed '{tgt}' via send_keys")
            except:
                time.sleep(0.5); pyautogui.write(tgt)
                print(f"✅ Typed '{tgt}' via pyautogui")
    except Exception as e:
        print(f"❌ Failed {act} '{tgt}': {e}")

def launch_via_start(app_name: str, timeout=5) -> bool:
    """Press Win, type app_name, Enter, wait for a new window."""
    pyautogui.press('win'); time.sleep(0.5)
    pyautogui.write(app_name, interval=0.05); time.sleep(0.5)
    pyautogui.press('enter')
    # wait for a new window handle
    start = time.time()
    while time.time() - start < timeout:
        if len(driver.window_handles) > 1:
            # switch to the newest window
            driver.switch_to.window(driver.window_handles[-1])
            return True
        time.sleep(0.5)
    return False

# ─── MAIN CONTROLLER ────────────────────────────────────────────────────────

print("🔹 Windows NLP UI Automation (type 'exit' to quit)\n")

while True:
    user_cmd = input("Your Task: ").strip()
    if user_cmd.lower() == "exit":
        driver.quit()
        break

    # ⌨️ 1) Launch via Start-menu if asked
    m = re.match(r"open\s+(.+)", user_cmd, re.IGNORECASE)
    if m:
        app = m.group(1).strip()
        print(f"🚀 Launching '{app}' via Start menu...")
        if launch_via_start(app):
            print(f"✅ Launched & attached to '{app}'.\n")
        else:
            print(f"⚠️ Could not launch or find window for '{app}'.\n")
        continue

    # 🔍 2) Fetch context & ask GPT
    xml = get_page_source()
    sample = extract_ui_elements(xml)

    prompt = (
        f"You are a Windows automation assistant. Current window elements:\n"
        f"{sample}\n\nUser request: {user_cmd}\n"
        f"List each action as `click 'Name'` or `type 'Text'`, one per line."
    )
    resp = openai.chat.completions.create(
        model="gpt-4o-mini", messages=[{"role":"user","content":prompt}]
    )
    instructions = resp.choices[0].message.content.strip()
    print(f"\nGPT suggests:\n{instructions}\n")

    # ⚙️ 3) Execute steps
    steps = parse_steps(instructions)
    if not steps:
        print("⚠️ No actionable steps parsed.\n")
        continue

    for step in steps:
        perform_step(step)
        time.sleep(1)
    print()  # blank line for readability


# %%
"""
##### import xml.etree.ElementTree as ET
import openai
import time
import re
import os
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

# ─── CONFIG ────────────────────────────────────────────────────────────────
openai.api_key = "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"
WINAPPDRIVER_PATH = r"C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe"
DEFAULT_TIMEOUT = 10

# ─── STARTUP ────────────────────────────────────────────────────────────────
os.system(f'start "" "{WINAPPDRIVER_PATH}"')
time.sleep(2)

# Launch “Root” session so we can attach to any window
caps = {"platformName": "Windows", "deviceName": "WindowsPC", "app": "Root"}
driver = webdriver.Remote("http://127.0.0.1:4723", caps)

# ─── HELPERS ────────────────────────────────────────────────────────────────

def get_page_source():
    return driver.page_source

def extract_ui_elements(xml_source, limit=5):
    root = ET.fromstring(xml_source)
    elems = []
    for el in root.iter():
        name = el.attrib.get("Name") or el.attrib.get("AutomationId")
        if name and name.strip():
            elems.append(name.strip())
        if len(elems) >= limit:
            break
    return elems

def parse_steps(gpt_reply):
    steps = []
    for line in gpt_reply.splitlines():
        m = re.search(r"(click|type)\s+'(.+?)'", line, re.IGNORECASE)
        if m:
            steps.append({"action": m.group(1).lower(), "target": m.group(2)})
    return steps

def perform_step(step):
    act, tgt = step["action"], step["target"]
    try:
        if act == "click":
            el = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                EC.element_to_be_clickable((By.NAME, tgt))
            )
            el.click()
            print(f"✅ Clicked '{tgt}'")
        elif act == "type":
            try:
                tb = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "Edit"))
                )
                tb.send_keys(tgt)
                print(f"✅ Typed '{tgt}' via send_keys")
            except:
                time.sleep(0.5)
                pyautogui.write(tgt)
                print(f"✅ Typed '{tgt}' via pyautogui")
    except Exception as e:
        print(f"❌ Failed {act} '{tgt}': {e}")

def launch_via_start(app_name: str, timeout=5) -> bool:
    """Press Win, type app_name, Enter, wait for a new window."""
    pyautogui.press('win')
    time.sleep(0.5)
    pyautogui.write(app_name, interval=0.05)
    time.sleep(0.5)
    pyautogui.press('enter')
    start = time.time()
    while time.time() - start < timeout:
        # new handle appears when app launches
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])
            return True
        time.sleep(0.5)
    return False

# ─── MAIN CONTROLLER ────────────────────────────────────────────────────────

print("🔹 Windows NLP UI Automation (type 'exit' to quit)\n")

while True:
    user_cmd = input("Your Task: ").strip()
    if user_cmd.lower() == "exit":
        driver.quit()
        break

    # 1) If user said "open XYZ", go via Start-menu
    m = re.match(r"open\s+(.+)", user_cmd, re.IGNORECASE)
    if m:
        app = m.group(1).strip()
        print(f"🚀 Launching '{app}' via Start menu...")
        if launch_via_start(app):
            print(f"✅ Launched & attached to '{app}'.\n")
        else:
            print(f"⚠️ Could not launch or find window for '{app}'.\n")
        continue

    # 2) Otherwise, treat it as in-app navigation
    xml = get_page_source()
    sample = extract_ui_elements(xml)

    prompt = (
        f"You are a Windows automation assistant. Current window elements:\n"
        f"{sample}\n\n"
        f"User request: {user_cmd}\n"
        f"List each action as `click 'Name'` or `type 'Text'`, one per line."
    )
    resp = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )
    instructions = resp.choices[0].message.content.strip()
    print(f"\nGPT suggests:\n{instructions}\n")

    steps = parse_steps(instructions)
    if not steps:
        print("⚠️ No actionable steps parsed.\n")
        continue
45
    for step in steps:
        perform_step(step)
        time.sleep(1)

    print()  # blank line for readability

"""

# %%
import xml.etree.ElementTree as ET
import openai
import time
import re
import os
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

# ─── CONFIG ────────────────────────────────────────────────────────────────
openai.api_key = "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"
WINAPPDRIVER_PATH = r"C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe"
DEFAULT_TIMEOUT = 10

# ─── STARTUP ────────────────────────────────────────────────────────────────
os.system(f'start "" "{WINAPPDRIVER_PATH}"')
time.sleep(2)

# Launch “Root” session so we can attach to any window
caps = {"platformName": "Windows", "deviceName": "WindowsPC", "app": "Root"}
driver = webdriver.Remote("http://127.0.0.1:4723", caps)

# ─── HELPERS ────────────────────────────────────────────────────────────────

def get_page_source():
    return driver.page_source

def extract_ui_elements(xml_source, limit=5):
    root = ET.fromstring(xml_source)
    elems = []
    for el in root.iter():
        name = el.attrib.get("Name") or el.attrib.get("AutomationId")
        if name and name.strip():
            elems.append(name.strip())
        if len(elems) >= limit:
            break
    return elems

def parse_steps(gpt_reply):
    steps = []
    for line in gpt_reply.splitlines():
        m = re.search(r"(click|type)\s+'(.+?)'", line, re.IGNORECASE)
        if m:
            steps.append({"action": m.group(1).lower(), "target": m.group(2)})
    return steps

def perform_step(step):
    act, tgt = step["action"], step["target"]
    try:
        if act == "click":
            el = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                EC.element_to_be_clickable((By.NAME, tgt))
            )
            el.click()
            print(f"✅ Clicked '{tgt}'")
        elif act == "type":
            try:
                tb = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "Edit"))
                )
                tb.send_keys(tgt)
                print(f"✅ Typed '{tgt}' via send_keys")
            except:
                time.sleep(0.5)
                pyautogui.write(tgt)
                print(f"✅ Typed '{tgt}' via pyautogui")
    except Exception as e:
        print(f"❌ Failed {act} '{tgt}': {e}")

def launch_via_start(app_name: str, timeout=5) -> bool:
    """Press Win, type app_name, Enter, wait for a new window."""
    pyautogui.press('win')
    time.sleep(0.5)
    pyautogui.write(app_name, interval=0.05)
    time.sleep(0.5)
    pyautogui.press('enter')
    start = time.time()
    while time.time() - start < timeout:
        # new handle appears when app launches
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])
            return True
        time.sleep(0.5)
    return False

# ─── MAIN CONTROLLER ────────────────────────────────────────────────────────

print("🔹 Windows NLP UI Automation (type 'exit' to quit)\n")

while True:
    user_cmd = input("Your Task: ").strip()
    if user_cmd.lower() == "exit":
        driver.quit()
        break

    # 1) If user said "open XYZ", go via Start-menu
    m = re.match(r"open\s+(.+)", user_cmd, re.IGNORECASE)
    if m:
        app = m.group(1).strip()
        print(f"🚀 Launching '{app}' via Start menu...")
        if launch_via_start(app):
            print(f"✅ Launched & attached to '{app}'.\n")
        else:
            print(f"⚠️ Could not launch or find window for '{app}'.\n")
        continue

    # 2) Otherwise, treat it as in-app navigation
    xml = get_page_source()
    sample = extract_ui_elements(xml)

    prompt = (
        f"You are a Windows automation assistant. Current window elements:\n"
        f"{sample}\n\n"
        f"User request: {user_cmd}\n"
        f"List each action as `click 'Name'` or `type 'Text'`, one per line."
    )
    resp = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )
    instructions = resp.choices[0].message.content.strip()
    print(f"\nGPT suggests:\n{instructions}\n")

    steps = parse_steps(instructions)
    if not steps:
        print("⚠️ No actionable steps parsed.\n")
        continue

    for step in steps:
        perform_step(step)
        time.sleep(1)

    print()  # blank line for readability


# %%
"""
## import xml.etree.ElementTree as ET
import openai
import time
import re
import os
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

# ─── CONFIG ────────────────────────────────────────────────────────────────
openai.api_key = "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"
WINAPPDRIVER_PATH = r"C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe"
DEFAULT_TIMEOUT = 10

# ─── STARTUP ────────────────────────────────────────────────────────────────
os.system(f'start "" "{WINAPPDRIVER_PATH}"')
time.sleep(2)
caps = {"platformName": "Windows", "deviceName": "WindowsPC", "app": "Root"}
driver = webdriver.Remote("http://127.0.0.1:4723", caps)

# ─── HELPERS ────────────────────────────────────────────────────────────────
def get_page_source():
    return driver.page_source

def extract_ui_elements(xml_source, limit=5):
    root = ET.fromstring(xml_source)
    elems = []
    for el in root.iter():
        name = el.attrib.get("Name") or el.attrib.get("AutomationId")
        if name and name.strip():
            elems.append(name.strip())
        if len(elems) >= limit:
            break
    return elems

def parse_steps(gpt_reply):
    steps = []
    for line in gpt_reply.splitlines():
        m = re.search(r"(click|type)\s+'(.+?)'", line, re.IGNORECASE)
        if m:
            steps.append({"action": m.group(1).lower(), "target": m.group(2)})
    return steps

def perform_step(step):
    act, tgt = step["action"], step["target"]
    try:
        if act == "click":
            el = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                EC.element_to_be_clickable((By.NAME, tgt))
            )
            el.click()
            print(f"✅ Clicked '{tgt}'")
        elif act == "type":
            try:
                tb = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "Edit"))
                )
                tb.send_keys(tgt)
                print(f"✅ Typed '{tgt}' via send_keys")
            except:
                time.sleep(0.5)
                pyautogui.write(tgt)
                print(f"✅ Typed '{tgt}' via pyautogui")
    except Exception as e:
        print(f"❌ Failed {act} '{tgt}': {e}")

def launch_via_start(app_name: str, timeout=5) -> bool:
    pyautogui.press('win')
    time.sleep(0.5)
    pyautogui.write(app_name, interval=0.05)
    time.sleep(0.5)
    pyautogui.press('enter')
    start = time.time()
    while time.time() - start < timeout:
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])
            return True
        time.sleep(0.5)
    return False

# ─── MAIN CONTROLLER ────────────────────────────────────────────────────────
print("🔹 Windows NLP UI Automation (type 'exit' to quit)\n")

settings_keywords = ["bluetooth", "wifi", "brightness", "display", "sound", "battery"]

while True:
    user_cmd = input("Your Task: ").strip()
    if user_cmd.lower() == "exit":
        driver.quit()
        break

    # ── 0) Math calculation?
    calc_match = re.match(r"calculate\s+(.+)", user_cmd, re.IGNORECASE)
    if calc_match:
        expr = calc_match.group(1).strip()
        print("🧮 Calculation detected → launching Calculator…")
        if launch_via_start("Calculator"):
            print("✅ Calculator launched. Now fetching the Calculator UI…")
            time.sleep(1)

            # grab a larger sample of buttons
            xml_calc = get_page_source()
            sample_calc = extract_ui_elements(xml_calc, limit=20)

            # ask GPT which buttons to click
            prompt_calc = (
                "You are a Windows automation assistant inside Calculator.\n"
                f"Current buttons: {sample_calc}\n"
                f"User request: calculate {expr}\n"
                "List each action as `click 'Name'` one per line."
            )
            resp_calc = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role":"user","content":prompt_calc}]
            )
            instr_calc = resp_calc.choices[0].message.content.strip()
            print(f"\nGPT suggests (Calculator):\n{instr_calc}\n")

            # parse & execute
            steps = parse_steps(instr_calc)
            for step in steps:
                perform_step(step)
                time.sleep(0.5)
            print()
            continue
        else:
            print("⚠️ Couldn't open Calculator; continuing in current window.\n")

    # ── 1) System settings?
    if any(kw in user_cmd.lower() for kw in settings_keywords):
        print("🔧 System command detected—launching Settings…")
        if launch_via_start("Settings"):
            print("✅ Settings launched. Now navigating inside Settings…\n")
            time.sleep(2)
        else:
            print("⚠️ Couldn't open Settings; will continue with the current window.\n")

    # ── 2) Explicit “open X”
    m = re.match(r"open\s+(.+)", user_cmd, re.IGNORECASE)
    if m:
        app = m.group(1).strip()
        print(f"🚀 Launching '{app}' via Start menu…")
        if launch_via_start(app):
            print(f"✅ Launched & attached to '{app}'.\n")
        else:
            print(f"⚠️ Could not launch or find window for '{app}'.\n")
        continue

    # ── 3) Otherwise, generic GPT UI navigation
    xml = get_page_source()
    sample = extract_ui_elements(xml)
    prompt = (
        f"You are a Windows automation assistant. Current window elements:\n"
        f"{sample}\n\n"
        f"User request: {user_cmd}\n"
        "List each action as `click 'Name'` or `type 'Text'`, one per line."
    )
    resp = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )
    instructions = resp.choices[0].message.content.strip()
    print(f"\nGPT suggests:\n{instructions}\n")

    # ── 4) Parse & execute
    steps = parse_steps(instructions)
    if not steps:
        print("⚠️ No actionable steps parsed.\n")
        continue

    for step in steps:
        perform_step(step)
        time.sleep(1)

    print()  # blank line for readability

"""

# %%
import xml.etree.ElementTree as ET
import openai
import time
import re
import os
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

# ─── CONFIG ────────────────────────────────────────────────────────────────
openai.api_key = "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"
WINAPPDRIVER_PATH = r"C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe"
DEFAULT_TIMEOUT = 10

# ─── STARTUP ────────────────────────────────────────────────────────────────
os.system(f'start "" "{WINAPPDRIVER_PATH}"')
time.sleep(2)
caps = {"platformName": "Windows", "deviceName": "WindowsPC", "app": "Root"}
driver = webdriver.Remote("http://127.0.0.1:4723", caps)

# ─── HELPERS ────────────────────────────────────────────────────────────────
def get_page_source():
    return driver.page_source

def extract_ui_elements(xml_source, limit=5):
    root = ET.fromstring(xml_source)
    elems = []
    for el in root.iter():
        name = el.attrib.get("Name") or el.attrib.get("AutomationId")
        if name and name.strip():
            elems.append(name.strip())
        if len(elems) >= limit:
            break
    return elems

def parse_steps(gpt_reply):
    steps = []
    for line in gpt_reply.splitlines():
        m = re.search(r"(click|type)\s+'(.+?)'", line, re.IGNORECASE)
        if m:
            steps.append({"action": m.group(1).lower(), "target": m.group(2)})
    return steps

def perform_step(step):
    act, tgt = step["action"], step["target"]
    try:
        if act == "click":
            el = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                EC.element_to_be_clickable((By.NAME, tgt))
            )
            el.click()
            print(f"✅ Clicked '{tgt}'")
        elif act == "type":
            try:
                tb = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "Edit"))
                )
                tb.send_keys(tgt)
                print(f"✅ Typed '{tgt}' via send_keys")
            except:
                time.sleep(0.5)
                pyautogui.write(tgt)
                print(f"✅ Typed '{tgt}' via pyautogui")
    except Exception as e:
        print(f"❌ Failed {act} '{tgt}': {e}")

def launch_via_start(app_name: str, timeout=5) -> bool:
    pyautogui.press('win')
    time.sleep(0.5)
    pyautogui.write(app_name, interval=0.05)
    time.sleep(0.5)
    pyautogui.press('enter')
    start = time.time()
    while time.time() - start < timeout:
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])
            return True
        time.sleep(0.5)
    return False

# ─── MAIN CONTROLLER ────────────────────────────────────────────────────────
print("🔹 Windows NLP UI Automation (type 'exit' to quit)\n")

settings_keywords = ["bluetooth", "wifi", "brightness", "display", "sound", "battery"]

while True:
    user_cmd = input("Your Task: ").strip()
    if user_cmd.lower() == "exit":
        driver.quit()
        break

    # ── 0) Math calculation?
    calc_match = re.match(r"calculate\s+(.+)", user_cmd, re.IGNORECASE)
    if calc_match:
        expr = calc_match.group(1).strip()
        print("🧮 Calculation detected → launching Calculator…")
        if launch_via_start("Calculator"):
            print("✅ Calculator launched. Now fetching the Calculator UI…")
            time.sleep(1)

            # grab a larger sample of buttons
            xml_calc = get_page_source()
            sample_calc = extract_ui_elements(xml_calc, limit=20)

            # ask GPT which buttons to click
            prompt_calc = (
                "You are a Windows automation assistant inside Calculator.\n"
                f"Current buttons: {sample_calc}\n"
                f"User request: calculate {expr}\n"
                "List each action as `click 'Name'` one per line."
            )
            resp_calc = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role":"user","content":prompt_calc}]
            )
            instr_calc = resp_calc.choices[0].message.content.strip()
            print(f"\nGPT suggests (Calculator):\n{instr_calc}\n")

            # parse & execute
            steps = parse_steps(instr_calc)
            for step in steps:
                perform_step(step)
                time.sleep(0.5)
            print()
            continue
        else:
            print("⚠️ Couldn't open Calculator; continuing in current window.\n")

    # ── 1) System settings?
    if any(kw in user_cmd.lower() for kw in settings_keywords):
        print("🔧 System command detected—launching Settings…")
        if launch_via_start("Settings"):
            print("✅ Settings launched. Now navigating inside Settings…\n")
            time.sleep(2)
        else:
            print("⚠️ Couldn't open Settings; will continue with the current window.\n")

    # ── 2) Explicit “open X”
    m = re.match(r"open\s+(.+)", user_cmd, re.IGNORECASE)
    if m:
        app = m.group(1).strip()
        print(f"🚀 Launching '{app}' via Start menu…")
        if launch_via_start(app):
            print(f"✅ Launched & attached to '{app}'.\n")
        else:
            print(f"⚠️ Could not launch or find window for '{app}'.\n")
        continue

    # ── 3) Otherwise, generic GPT UI navigation
    xml = get_page_source()
    sample = extract_ui_elements(xml)
    prompt = (
        f"You are a Windows automation assistant. Current window elements:\n"
        f"{sample}\n\n"
        f"User request: {user_cmd}\n"
        "List each action as `click 'Name'` or `type 'Text'`, one per line."
    )
    resp = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )
    instructions = resp.choices[0].message.content.strip()
    print(f"\nGPT suggests:\n{instructions}\n")

    # ── 4) Parse & execute
    steps = parse_steps(instructions)
    if not steps:
        print("⚠️ No actionable steps parsed.\n")
        continue

    for step in steps:
        perform_step(step)
        time.sleep(1)

    print()  # blank line for readability


# %%
import time
import re
import os
import openai
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import xml.etree.ElementTree as ET

# ─── CONFIG ────────────────────────────────────────────────────────────────
openai.api_key    = "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"
WINAPPDRIVER_PATH = r"C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe"
DEFAULT_TIMEOUT   = 10

# ─── STARTUP ────────────────────────────────────────────────────────────────
os.system(f'start "" "{WINAPPDRIVER_PATH}"')
time.sleep(2)
caps   = {"platformName":"Windows","deviceName":"WindowsPC","app":"Root"}
driver = webdriver.Remote("http://127.0.0.1:4723", caps)

# ─── HELPERS ────────────────────────────────────────────────────────────────
def launch_via_start(app_name: str, timeout=5) -> bool:
    pyautogui.press('win'); time.sleep(0.3)
    pyautogui.write(app_name, interval=0.05); time.sleep(0.3)
    pyautogui.press('enter')
    start = time.time()
    while time.time() - start < timeout:
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])
            return True
        time.sleep(0.3)
    return False

def click_button(name: str):
    el = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable((By.NAME, name))
    )
    el.click()
    print(f"  • clicked '{name}'")

def parse_calc(expr: str):
    tokens = re.findall(r"\d+|[+\-*/]", expr)
    return tokens + ["="]

def get_page_source():
    return driver.page_source

def extract_ui_elements(xml_source, limit=10):
    root = ET.fromstring(xml_source)
    elems = []
    for el in root.iter():
        name = el.attrib.get("Name") or el.attrib.get("AutomationId")
        if name and name.strip():
            elems.append(name.strip())
        if len(elems) >= limit:
            break
    return elems

def ask_gpt_to_navigate(sample, user_cmd):
    prompt = (
        "You are a Windows UI automation assistant.\n"
        f"Current elements: {sample}\n"
        f"User request: {user_cmd}\n"
        "List each action as `click 'Name'` or `type 'Text'`, one per line."
    )
    resp = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )
    return resp.choices[0].message.content.strip()

def parse_steps(gpt_reply):
    steps = []
    for line in gpt_reply.splitlines():
        m = re.search(r"(click|type)\s+'(.+?)'", line, re.IGNORECASE)
        if m:
            steps.append({"action":m.group(1).lower(),"target":m.group(2)})
    return steps

def perform_step(step):
    act, tgt = step["action"], step["target"]
    try:
        if act=="click":
            click_button(tgt)
        elif act=="type":
            # try direct send_keys, else fall back to pyautogui
            try:
                tb = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                    EC.presence_of_element_located((By.CLASS_NAME,"Edit"))
                )
                tb.send_keys(tgt)
                print(f"  • typed '{tgt}' via send_keys")
            except:
                pyautogui.write(tgt)
                print(f"  • typed '{tgt}' via pyautogui")
    except Exception as e:
        print(f"❌ Failed {act} '{tgt}': {e}")

# ─── MAIN LOOP ─────────────────────────────────────────────────────────────
print("🔹 Windows NLP UI Automation  (type ‘exit’ to quit)\n")
attached_app = None

while True:
    cmd = input(f"{'['+attached_app+'] ' if attached_app else ''}Your command: ").strip()
    if cmd.lower()=="exit":
        driver.quit()
        break

    # 1) “open X”
    m = re.match(r"open\s+(.+)", cmd, re.IGNORECASE)
    if m:
        app = m.group(1).strip()
        print(f"🔎 Launching '{app}'…")
        if launch_via_start(app):
            attached_app = app
            print(f"✅ Attached to '{app}'.\n")
        continue

    # 2) If Calculator is attached
    if attached_app and attached_app.lower()=="calculator":
        expr = re.sub(r"^calculate\s+","", cmd, flags=re.IGNORECASE)
        print(f"🧮 Calculator: performing {expr}")
        for tok in parse_calc(expr):
            btn = {"+" :"Plus","-":"Minus","*":"Multiply by","/":"Divide by","=":"Equals"}.get(tok, tok)
            click_button(btn)
            time.sleep(0.3)
        print()
        continue

    # 3) If any other app is attached, use GPT to navigate its UI
    if attached_app:
        xml    = get_page_source()
        sample = extract_ui_elements(xml, limit=15)
        print(f"🤖 Asking GPT how to do “{cmd}” in {attached_app}…")
        instr = ask_gpt_to_navigate(sample, cmd)
        print(f"\nGPT suggests:\n{instr}\n")
        steps = parse_steps(instr)
        if not steps:
            print("⚠️ No actionable steps parsed.\n")
            continue

        for step in steps:
            perform_step(step)
            time.sleep(0.8)
        print()
        continue

    # 4) No app attached
    print("⚠️ Start by typing “open <AppName>” to attach to an application.\n")


# %%
import time
import re
import os
import openai
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import xml.etree.ElementTree as ET

# ─── CONFIG ────────────────────────────────────────────────────────────────
openai.api_key    = "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"
WINAPPDRIVER_PATH = r"C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe"
DEFAULT_TIMEOUT   = 10

# ─── STARTUP ────────────────────────────────────────────────────────────────
os.system(f'start "" "{WINAPPDRIVER_PATH}"')
time.sleep(2)
caps   = {"platformName":"Windows","deviceName":"WindowsPC","app":"Root"}
driver = webdriver.Remote("http://127.0.0.1:4723", caps)

# ─── HELPERS ────────────────────────────────────────────────────────────────
def launch_via_start(app_name: str, timeout=5) -> bool:
    pyautogui.press('win'); time.sleep(0.3)
    pyautogui.write(app_name, interval=0.05); time.sleep(0.3)
    pyautogui.press('enter')
    start = time.time()
    while time.time() - start < timeout:
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])
            return True
        time.sleep(0.3)
    return False

def click_button(name: str):
    el = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable((By.NAME, name))
    )
    el.click()
    print(f"  • clicked '{name}'")

def parse_calc(expr: str):
    tokens = re.findall(r"\d+|[+\-*/]", expr)
    return tokens + ["="]

def get_page_source():
    return driver.page_source

def extract_ui_elements(xml_source, limit=15):
    root = ET.fromstring(xml_source)
    elems = []
    for el in root.iter():
        name = el.attrib.get("Name") or el.attrib.get("AutomationId")
        if name and name.strip():
            elems.append(name.strip())
        if len(elems) >= limit:
            break
    return elems

def ask_gpt_to_navigate(sample, user_cmd):
    prompt = (
        "You are a Windows UI automation assistant.\n"
        f"Current elements: {sample}\n"
        f"User request: {user_cmd}\n"
        "List each action as `click 'Name'` or `type 'Text'`, one per line."
    )
    resp =  openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )
    return resp.choices[0].message.content.strip()

def parse_steps(gpt_reply):
    steps = []
    for line in gpt_reply.splitlines():
        m = re.search(r"(click|type)\s+'(.+?)'", line, re.IGNORECASE)
        if m:
            steps.append({"action":m.group(1).lower(),"target":m.group(2)})
    return steps

def perform_step(step):
    act, tgt = step["action"], step["target"]
    try:
        if act=="click":
            click_button(tgt)
        elif act=="type":
            try:
                tb = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                    EC.presence_of_element_located((By.CLASS_NAME,"Edit"))
                )
                tb.send_keys(tgt)
                print(f"  • typed '{tgt}' via send_keys")
            except:
                pyautogui.write(tgt)
                print(f"  • typed '{tgt}' via pyautogui")
    except Exception as e:
        print(f"❌ Failed {act} '{tgt}': {e}")

# ─── MAIN LOOP ─────────────────────────────────────────────────────────────
print("🔹 Windows NLP UI Automation  (type ‘exit’ to quit)\n")
attached_app = None

while True:
    prompt = f"[{attached_app}] Your command: " if attached_app else "Your command: "
    cmd = input(prompt).strip()
    if cmd.lower()=="exit":
        driver.quit()
        break

    # ── 1) “open X” → attach to new app
    m = re.match(r"open\s+(.+)", cmd, re.IGNORECASE)
    if m:
        app = m.group(1).strip()
        print(f"🔎 Launching '{app}'…")
        if launch_via_start(app):
            attached_app = app
            print(f"✅ Attached to '{app}'.\n")
        else:
            print(f"❌ Could not open '{app}'.\n")
        continue

    # ── 2) If Calculator is attached → token‐by‐token clicks
    if attached_app and attached_app.lower()=="calculator":
        expr = re.sub(r"^calculate\s+","", cmd, flags=re.IGNORECASE)
        print(f"🧮 Calculator: performing {expr}")
        for tok in parse_calc(expr):
            btn = {
                "+":"Plus", "-":"Minus",
                "*":"Multiply by", "/":"Divide by",
                "=":"Equals"
            }.get(tok, tok)
            click_button(btn)
            time.sleep(0.3)
        print()
        continue

    # ── 3) Any other app attached → GPT‐driven navigation
    if attached_app:
        xml    = get_page_source()
        sample = extract_ui_elements(xml)
        print(f"🤖 Asking GPT how to do “{cmd}” in {attached_app}…")
        instr = ask_gpt_to_navigate(sample, cmd)
        print(f"\nGPT suggests:\n{instr}\n")
        steps = parse_steps(instr)
        if not steps:
            print("⚠️ No actionable steps parsed.\n")
            continue
        for step in steps:
            perform_step(step)
            time.sleep(0.8)
        print()
        continue

    # ── 4) No app attached yet
    print("⚠️ Please start with `open <AppName>` to attach to an application.\n")


# %%
import time
import re
import os
import openai
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import xml.etree.ElementTree as ET
from selenium.common.exceptions import TimeoutException

# ─── CONFIG ────────────────────────────────────────────────────────────────
openai.api_key    = "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"
WINAPPDRIVER_PATH = r"C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe"
DEFAULT_TIMEOUT   = 10

# ─── STARTUP ────────────────────────────────────────────────────────────────
os.system(f'start "" "{WINAPPDRIVER_PATH}"')
time.sleep(2)
caps   = {"platformName":"Windows","deviceName":"WindowsPC","app":"Root"}
driver = webdriver.Remote("http://127.0.0.1:4723", caps)

# ─── HELPERS ────────────────────────────────────────────────────────────────

def launch_via_start(app_name: str, timeout=10) -> bool:
    """
    Opens `app_name` via Windows Start, then waits until a new window handle
    appears before returning True.
    """
    pyautogui.press('win'); time.sleep(0.2)
    pyautogui.write(app_name, interval=0.05); time.sleep(0.2)
    pyautogui.press('enter')

    # record original handles
    original_handles = set(driver.window_handles)
    start = time.time()
    while time.time() - start < timeout:
        current_handles = set(driver.window_handles)
        new_handles = current_handles - original_handles
        if new_handles:
            # switch to the first new handle
            new_handle = new_handles.pop()
            driver.switch_to.window(new_handle)
            return True
        time.sleep(0.3)
    return False


def click_button(name: str):
    el = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable((By.NAME, name))
    )
    el.click()
    print(f"  • clicked '{name}'")


def parse_calc(expr: str):
    tokens = re.findall(r"\d+|[+\-*/]", expr)
    return tokens + ['=']


def get_page_source():
    return driver.page_source


def extract_ui_elements(xml_source, limit=15):
    root = ET.fromstring(xml_source)
    elems = []
    for el in root.iter():
        name = el.attrib.get("Name") or el.attrib.get("AutomationId")
        if name and name.strip():
            elems.append(name.strip())
        if len(elems) >= limit:
            break
    return elems


def ask_gpt_to_navigate(sample, user_cmd):
    prompt = (
        "You are a Windows UI automation assistant.\n"
        f"Current elements: {sample}\n"
        f"User request: {user_cmd}\n"
        "List each action as `click 'Name'` or `type 'Text'`, one per line."
    )
    resp =  openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )
    return resp.choices[0].message.content.strip()


def parse_steps(gpt_reply):
    steps = []
    for line in gpt_reply.splitlines():
        m = re.search(r"(click|type)\s+'(.+?)'", line, re.IGNORECASE)
        if m:
            steps.append({"action":m.group(1).lower(),"target":m.group(2)})
    return steps


def perform_step(step):
    act, tgt = step["action"], step["target"]
    try:
        if act=="click":
            click_button(tgt)
        elif act=="type":
            try:
                tb = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
                    EC.presence_of_element_located((By.CLASS_NAME,"Edit"))
                )
                tb.send_keys(tgt)
                print(f"  • typed '{tgt}' via send_keys")
            except:
                pyautogui.write(tgt)
                print(f"  • typed '{tgt}' via pyautogui")
    except Exception as e:
        print(f"❌ Failed {act} '{tgt}': {e}")

# ─── MAIN LOOP ─────────────────────────────────────────────────────────────

print("🔹 Windows NLP UI Automation  (type ‘exit’ to quit)\n")
attached_app = None

while True:
    prompt = f"[{attached_app}] Your command: " if attached_app else "Your command: "
    cmd = input(prompt).strip()
    if cmd.lower()=="exit":
        driver.quit()
        break

    # ── 1) “open X” → attach to new app
    m = re.match(r"open\s+(.+)", cmd, re.IGNORECASE)
    if m:
        app = m.group(1).strip()
        print(f"🔎 Launching '{app}'…")
        if launch_via_start(app):
            attached_app = app
            print(f"✅ Attached to '{app}'.\n")
        else:
            print(f"❌ Could not open '{app}'.\n")
        continue

    # ── 2) If Calculator is attached → token‐by‐token clicks
    if attached_app and attached_app.lower()=="calculator":
        expr = re.sub(r"^calculate\s+","", cmd, flags=re.IGNORECASE)
        print(f"🧮 Calculator: performing {expr}")
        for tok in parse_calc(expr):
            btn = {
                "+":"Plus", "-":"Minus",
                "*":"Multiply by", "/":"Divide by",
                "=":"Equals"
            }.get(tok, tok)
            click_button(btn)
            time.sleep(0.3)
        print()
        continue

    # ── 3) Any other app attached → GPT‐driven navigation
    if attached_app:
        xml    = get_page_source()
        sample = extract_ui_elements(xml)
        print(f"🤖 Asking GPT how to do “{cmd}” in {attached_app}…")
        instr = ask_gpt_to_navigate(sample, cmd)
        print(f"\nGPT suggests:\n{instr}\n")
        steps = parse_steps(instr)
        if not steps:
            print("⚠️ No actionable steps parsed.\n")
            continue
        for step in steps:
            perform_step(step)
            time.sleep(0.8)
        print()
        continue

    # ── 4) No app attached yet
    print("⚠️ Please start with `open <AppName>` to attach to an application.\n")


# %%
