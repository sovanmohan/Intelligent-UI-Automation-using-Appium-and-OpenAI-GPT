# 🤖 Intelligent UI Automation with Appium & OpenAI GPT-4o-mini

This project enables **natural language-driven UI automation** on Android emulators using the power of **OpenAI GPT-4o-mini** and **Appium**. It allows users to type simple commands like "Turn on Bluetooth" or "Go to Battery settings", and the system will automatically interpret and execute these commands in the emulator environment.

---

## 📌 Features

- **Natural Language Input:** Users can give high-level instructions in plain English.
- **Real-Time Navigation:** UI actions are performed on the Android emulator via Appium.
- **Multi-Step Task Execution:** The system supports navigation through multiple screens.
- **Dynamic Page Source Refreshing:** Appium fetches the current XML source after every step.
- **Fallback Actions:** Automatically scrolls when elements are not visible on screen.

---

## 🔧 Tech Stack

| Component | Tool |
|----------|------|
| LLM Engine | OpenAI GPT-4o-mini |
| Automation Driver | Appium with UiAutomator2 |
| Programming Language | Python 3.x |
| Interface | Jupyter Notebook |
| Platform | Android Emulator (via Android Studio) |

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/llm-appium-ui-automation.git
cd llm-appium-ui-automation
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Configure OpenAI API
Create a `.env` file or set the API key in your script:
```python
openai.api_key = "your_openai_key"
```

### 4. Launch Android Emulator
Open Android Studio and start the emulator you’ve configured.

### 5. Start Appium Server
Use Appium Desktop or run via terminal:
```bash
appium
```

### 6. Run the Jupyter Notebook
```bash
jupyter notebook
```
Open the notebook and run the cell blocks to begin issuing commands.

---

## ✍️ Example Usage
```
> Enable Bluetooth
> Go to Battery settings
> Open Display preferences
```

GPT interprets the instructions and Appium performs:
1. Tapping on relevant buttons
2. Scrolling to find hidden items
3. Updating the current page source after each step

---

## 📂 Project Structure
```
├── llm_navigation.py           # Main controller script
├── appium_utils.py            # Swipe, tap, scroll handlers
├── screenshots/               # (Optional) UI screenshots
├── assets/                    # Flowcharts, diagrams
├── README.md                  # This file
```

---

## 🧠 AI Prompt Strategy
We used prompt templates like:
```
You are a UI automation assistant. Based on the user's task and the current screen, generate a list of steps to achieve it. Example: Tap on 'Bluetooth', Tap on 'Battery saver', etc.
```

---

## 📈 Roadmap
- [x] Multi-step command execution
- [x] GPT-4o-mini integration with real-time XML
- [ ] Toggle state detection (e.g. switch ON/OFF)
- [ ] Screenshot + log report after every task
- [ ] Voice assistant integration

---

## 📸 Demo Preview
Include screenshots or link to demo video here.

---

## 🙋‍♂️ Author
**Sovan Mohanty**  
Reach out via [LinkedIn](https://linkedin.com/in/yourprofile) or [Email](mailto:your@email.com)

---

## 📝 License
This project is licensed under the MIT License. Feel free to use, modify, and share with credits.

