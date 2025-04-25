#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install appium


# In[2]:


pip install appium python client


# In[3]:


pip install Appium-Python-Client


# In[4]:


from appium import webdriver


# In[8]:


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


# In[9]:


get_ipython().system('pip install -q openai')


# In[10]:


import openai


# In[22]:


import os
os.environ["OPENAI_API_KEY"] = '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'


# In[25]:


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


# In[28]:


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


# In[38]:


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


# Tracing XML page source layout for using click action in the current page

# In[5]:


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


# In[ ]:


Giving real time timestamp of the activities by tracking the current page source


# In[16]:


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


# In[8]:


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


# In[16]:


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


# In[19]:


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


# In[1]:


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


# In[12]:


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


# In[5]:


get_ipython().system('pip uninstall Appium-Python-Client')


# In[6]:


from appium.webdriver.common.actions.action_builder import ActionBuilder


# In[7]:


pip install Appium-Python-Client==2.11.1


# In[8]:


Appium-Python_client --version


# In[9]:


Appium-Python-client --version


# In[10]:


get_ipython().system('pip show Appium-Python-Client')


# In[11]:


from appium import webdriver
from appium.webdriver.common.actions.action_builder import ActionBuilder


# In[12]:


get_ipython().system('pip install -U selenium')


# In[13]:


import selenium
print(selenium.__version__)


# In[1]:


from appium import webdriver
from appium.webdriver.common.actions.action_builder import ActionBuilder


# In[2]:


from appium import webdriver
from appium.webdriver.common.actions.action_builder import ActionBuilder
from appium.webdriver.common.actions.pointer_input import PointerInput


# In[3]:


from appium import webdriver
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


# In[18]:


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


# In[20]:


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


# In[21]:


from appium.webdriver.common.touch_action import TouchAction


# one fault i find here in the code is that when i give the prompt it results accordingly making the new page source as now its current page source but when i give another prompt it only sticks to that page source not changing 

# In[1]:


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


# Multi Navigation Automated UI Elements

# In[2]:


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


# In[ ]:





# In[ ]:




