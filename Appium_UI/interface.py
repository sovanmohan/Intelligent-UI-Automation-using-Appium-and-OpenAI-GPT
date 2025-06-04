import streamlit as st
from ui_parser import extract_ui_elements, parse_actions
from llm_utils import get_llm_response

def run_ui(driver, selected_llm, gemini_model, perform_action_fn, get_source_fn):
    st.set_page_config(page_title="Android UI Automation AI")
    st.title("🤖 Android UI Automation with Gemini/OpenAI")
    st.markdown(f"Currently using: **{selected_llm.upper()}**")

    user_prompt = st.text_input("Enter a task (e.g., turn on Bluetooth)", "")
    if st.button("Execute") and user_prompt:
        xml = get_source_fn(driver)
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

        response_text = get_llm_response(full_prompt, selected_llm, gemini_model)
        st.subheader(" LLM Response")
        st.code(response_text)

        steps = parse_actions(response_text)
        st.subheader(" Execution Log")
        for step in steps:
            result = perform_action_fn(driver, step)
            st.write(result)
