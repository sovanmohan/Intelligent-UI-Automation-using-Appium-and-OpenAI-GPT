# Intelligent UI Automation with Appium & OpenAI GPT-4o-mini

This document captures the end-to-end progress, architecture, and implementation details of a project designed to enable natural language-driven UI automation for both Android and Windows desktop platforms using OpenAI's GPT-4o-mini model and Appium automation frameworks.

---

## Project Overview

The primary goal of this project is to provide seamless automation of mobile and desktop applications through natural language commands. The system uses OpenAI GPT-4o-mini to interpret user instructions and Appium to perform real-time UI operations based on the current screen structure (XML page source).

---

## Technology Stack

- **OpenAI GPT-4o-mini**: For parsing and interpreting natural language instructions.
- **Appium (UiAutomator2, WinAppDriver)**: For Android and Windows UI automation.
- **Python 3.x**: Core programming language for automation logic.
- **Jupyter Notebook**: Interface used during development and testing.
- **Android Emulator / Windows Desktop**: Target environments for automation.

---

## Setup Instructions

### Android Studio & Mobile Automation Setup

1. **Install Java JDK & Android Studio**
   - Download and install the latest Java Development Kit (JDK) from Oracle or AdoptOpenJDK.
   - Download and install Android Studio from the [official website](https://developer.android.com/studio).

2. **Create a New Empty Project**
   - Open Android Studio → “Start a new Android Studio project”.
   - Choose “Empty Activity” template and finish project creation.

3. **Configure Java SDK in Android Studio**
   - File → Project Structure → SDK Location → Ensure JDK location is set.

4. **Set Up Android Virtual Device (AVD)**
   - Tools → AVD Manager → Create Virtual Device.
   - Select a “Tablet” profile (e.g., Pixel C).
   - Choose System Image: Android API Level 33 (Android 13) or Android 16 as required.
   - Finish and launch the emulator.

5. **Install Appium Python Client & UiAutomator2 Driver**
   ```bash
   appium driver install uiautomator2
   pip install Appium-Python-Client
   
   ```
   - Use Appium Desktop to start the Appium server.
   - In Appium Settings, install the UiAutomator2 server on the emulator.

6. **Appium Inspector**
   - Launch Appium Inspector.
   - Connect to the running Appium server.
   - Provide desired capabilities (see below) to inspect UI elements.

#### Android Desired Capabilities Example
```json
{
  "platformName": "Android",
  "deviceName": "emulator-5554",
  "automationName": "UiAutomator2",
  "appPackage": "com.android.settings",
  "appActivity": ".Settings"
}
```

---

### Windows Desktop Automation Setup

1. **Install WinAppDriver**
   - Download WinAppDriver from the [official GitHub releases](https://github.com/microsoft/WinAppDriver/releases).
   - Enable Developer Mode on Windows: Settings → Update & Security → For developers → Enable “Developer mode”.

2. **Start WinAppDriver Server**
   ```bash
   "C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe"
   ```

3. **Install Python Libraries**
   ```bash
   pip install Appium-Python-Client openai selenium pyautogui
   ```

4. **Start Root Session for Multi-App Control**
   - Use the “Root” app capability to attach to any open window.

#### Windows Desired Capabilities Example
```json
{
  "platformName": "Windows",
  "deviceName": "WindowsPC",
  "app": "Root"
}
```

---

## Development Timeline & Milestones

### Phase 1: Android Mobile Automation

- **Initial Integration**:
  - Connected OpenAI GPT-4o-mini with Appium.
  - Extracted dynamic XML page source.
- **UI Operations**:
  - Implemented tap, scroll, and fallback mechanisms.
  - Handled multi-step navigation (e.g., Settings > Display > Brightness).
- **Testing & Validation**:
  - Created test cases: “Go to Wi-Fi”, “Check Battery”, “Enable Bluetooth”.

### Phase 2: Windows Desktop Automation

- **Launch & Attach**:
  - Implemented Start-menu launch logic via `pyautogui`.
  - Attached to new window handles automatically.
- **In-App Navigation**:
  - Used GPT-4o-mini to generate click/type steps.
  - Fallback to PyAutoGUI typing when necessary.
- **Examples**:
  - “Open Notepad and type ‘Hello World’”.
  - “Enable Bluetooth” via Settings search.

---

## Architecture Overview

![Appium_UI_Auto_windows drawio](https://github.com/user-attachments/assets/be09035b-220b-4943-ad92-f70beb741108)

---

## Example Prompts

- **Android**:
  - “Open Battery settings”
  - “Turn on Bluetooth”
- **Windows**:
  - “Enable Bluetooth”
  - “Type ‘Test’ in Notepad”
  - “Close Calculator”

---
