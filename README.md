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

## Development Timeline & Milestones

### Phase 1: Android Mobile Automation (Using Appium & GPT-4o-mini)

- **Setup Environment**:
  - Installed Python, pip, virtualenv
  - Installed Appium Python Client, OpenAI SDK
  - Configured Android Studio with emulator

- **Basic Functionalities**:
  - Connected OpenAI with prompt-response logic
  - Integrated Appium with Android emulator
  - Extracted real-time XML page source for prompt context
  - Used GPT-4o-mini to respond with UI navigation instructions

- **Enhancements**:
  - Introduced automatic element tapping using XPath
  - Implemented scroll-and-tap fallback logic
  - Handled multi-step UI navigation (e.g., navigating to Settings > Battery)
  - Created a detailed README and visual documentation
  - Generated presentation and project summary for clients

### Phase 2: Windows Desktop Automation (Using WinAppDriver & GPT-4o-mini)

- **Setup**:
  - Installed WinAppDriver and Windows SDK
  - Enabled Developer Mode on Windows
  - Validated device capability connection with Notepad and Calculator apps

- **Implementation**:
  - Created dynamic prompt handler to automate Notepad using natural language
  - Used GPT-4o-mini to return click/type/close instructions
  - Added element recognition by class name, name, and fallback methods

- **Challenges Addressed**:
  - Resolved driver session error by providing valid WinAppDriver-compatible capabilities
  - Used `pyautogui` as a fallback for typing into edit fields that failed with `send_keys`
  - Integrated logic to switch driver sessions for multiple app launches at runtime

---

## Current Roadblock

**Typing into desktop apps (e.g., Notepad) using Appium send_keys fails with an element not found error.**

- Attempted Solution:
  - Used standard Appium `send_keys()` — failed due to element detection issue
  - Switched to `pyautogui.write()` — successfully simulated typing in Notepad

- Next Steps:
  - Standardize input method fallback
  - Implement virtual key support using Appium's "keys" capability for advanced input
  - Refactor typing and click logic into a more modular class-based architecture

---

## Architecture Overview

### Functional Workflow

1. **User Input**: Entered as a natural language prompt
2. **OpenAI GPT-4o-mini**: Processes prompt and page context
3. **Instruction Response**: Returns action plan (e.g., Tap on 'Wi-Fi')
4. **Appium Driver**:
   - Android → Executes gesture or navigation
   - Windows → Launches and interacts with desktop applications
5. **Fallbacks**:
   - Scroll-to-view for off-screen elements
   - PyAutoGUI for keyboard input failures

---

## Example Prompts

- Android:
  - "Go to Battery Settings"
  - "Turn on Bluetooth"
  - "Scroll down and open About Phone"

- Windows:
  - "Type 'Hello World' in Notepad"
  - "Click on View menu"
  - "Close Notepad"

---

## File Structure

```
├── android_controller.py        # Android automation logic
├── windows_controller.py        # Windows automation logic
├── utils/
│   ├── element_parser.py        # XML extraction and parsing
│   ├── fallback_typing.py       # PyAutoGUI-based typing
├── assets/                      # Diagrams, flowcharts
├── Appium_OpenAI.ipynb          # Jupyter notebook interface
├── README.md                    # GitHub project overview
├── requirements.txt             # Python dependencies
```

---

## Future Enhancements

- [ ] Detect toggle switch state (e.g., Wi-Fi ON/OFF)
- [ ] Screenshot and logging after every step
- [ ] Voice command integration for both mobile and desktop
- [ ] Cross-platform support using `Root` driver for all open apps

---

## Maintainer

Sovan Mohanty  
Email: [msovan928@email.com]  
LinkedIn: [https://www.linkedin.com/in/sovan-mohanty-a32b64237/]

---

This document is updated to reflect the latest changes and development logs. Feel free to contribute or raise issues if using the open-source version on GitHub.
