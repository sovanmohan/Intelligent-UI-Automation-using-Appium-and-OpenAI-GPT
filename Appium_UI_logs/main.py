import streamlit as st
from llm_handler import setup_llm, get_llm_response
from driver_setup import initialize_driver
from ui_helpers import get_page_source, extract_ui_elements
from executor import parse_actions, perform_action
from utils import get_logcat_output

selected_llm, gemini_model = setup_llm()
driver, action = initialize_driver()

st.set_page_config(page_title="Android UI Automation AI")
st.title("🤖 Android UI Automation with Gemini/OpenAI")
st.markdown(f"Currently using: **{selected_llm.upper()}**")

user_prompt = st.text_input("Enter a task (e.g., turn on Bluetooth)", "")
if st.button("Execute") and user_prompt:
    xml = get_page_source(driver)
    ui_elements = extract_ui_elements(xml)
    context = "\n".join(
        [f"{el['text']} - {el['resource-id']} - {el['content-desc']}" for el in ui_elements]
    )

    if any(word in user_prompt.lower() for word in ["what", "which", "list", "visible", "present", "available"]):
        full_prompt = (
            "You are a mobile UI assistant. The user is asking to describe the visible screen elements.\n"
            "Please summarize or list the UI elements in a readable format.\n\n" + context
        )
    else:
        full_prompt = (
            "You are a mobile UI automation assistant. Based on the current screen and user request,\n"
            "list the steps needed to complete the task, one per line, like:\n"
            "Tap on 'Connected Devices'\nTap on 'Connection Preferences'\n\n"
            f"User Task: {user_prompt}\n\n{context}"
        )

    response_text = get_llm_response(full_prompt)
    st.subheader("🤖 LLM Response")
    st.code(response_text)

    steps = parse_actions(response_text)
    st.subheader("⚙️ Execution Log")
    for step in steps:
        result = perform_action(driver, step)
        st.write(result)

    st.subheader("📋 Logcat Logs")
    st.text(get_logcat_output())
