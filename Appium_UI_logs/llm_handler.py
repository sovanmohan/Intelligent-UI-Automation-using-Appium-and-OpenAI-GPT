import openai
import google.generativeai as genai
from config import OPENAI_KEY, GEMINI_KEY
import streamlit as st

selected_llm = None
gemini_model = None
openai_available = False

def setup_llm():
    global selected_llm, gemini_model, openai_available

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

def get_llm_response(prompt_text):
    if selected_llm == "gemini":
        return gemini_model.generate_content(prompt_text).text.strip()
    elif selected_llm == "openai":
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt_text}]
        )
        return response.choices[0].message.content.strip()
    return ""
