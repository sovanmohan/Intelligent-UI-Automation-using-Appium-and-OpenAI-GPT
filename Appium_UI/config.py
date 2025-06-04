import streamlit as st
import google.generativeai as genai
import openai

OPENAI_KEY = ""  # Replace if available
GEMINI_KEY = "AIzaSyBJNIF6JBP8xqfSn8XNBQ2EuuYsW9c6XBI"
openai_available = False
selected_llm = None
gemini_model = None

def setup_llm():
    global openai_available, selected_llm, gemini_model

    if OPENAI_KEY:
        try:
            openai.api_key = OPENAI_KEY
            openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": "Ping"}]
            )
            openai_available = True
        except:
            st.warning("OpenAI API error, fallback to Gemini.")

    try:
        genai.configure(api_key=GEMINI_KEY)
        gemini_model = genai.GenerativeModel("gemini-2.0-flash")
        gemini_model.generate_content("Ping")
        selected_llm = "gemini"
    except:
        if openai_available:
            selected_llm = "openai"
        else:
            st.error("No available LLM (OpenAI/Gemini). Exiting.")
            st.stop()

    return selected_llm, gemini_model
